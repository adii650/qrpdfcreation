from django.shortcuts import render,redirect
from client.models import*
import qrcode
import datetime
from io import BytesIO
from django.core.files import File
from client.utils import render_to_pdf
# Create your views here.
def index(request):
    return render(request,"index.html")
def base(request):
    return render(request,"base.html")
def signin(request):
    return render(request,"signin.html")
def clienthome(request):
    return render(request,"clienthome.html")
def signup(request):
    return render(request,"signup.html")
def register(request):
    if request.method=="POST":
        clientname=request.POST.get('clientname')
        email=request.POST.get('email')
        password=request.POST.get('password')
        photo=request.FILES['photo']
        Client_obj=Client(clientname=clientname,email=email,password=password,photo=photo)
        Client_obj.save()
        return redirect('admicheck')
    return render(request,"signup.html")
def admicheck(request):
    return render(request,'admicheck.html')
def clientlogin(request):
    if request.method=='POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        try:
            client_obj=Client.objects.get(email=email)
        except:
            error_message='client does not exist'
            return render(request,'signin.html',{'error':error_message})
        if client_obj and client_obj.status==1:
            if password==client_obj.password:
                request.session['id']=client_obj.id
                return render(request,'clienthome.html',{'client_obj':client_obj})
        

             

    return render(request,'signin.html')
def clienthome(request):
    return render(request,'clienthome.html')
def clientdataentry(request):
    if request.method=='POST':
        contactno=request.POST.get('Contactno')
        adhar=request.POST.get('adhar')
        adress=request.POST.get('adress')
        district=request.POST.get('district')
        place=request.POST.get('place')
        qualification=request.POST.get('qualification')
        print(contactno,adhar,adress,district,place,qualification)
        obj=clientinfo(contactno=contactno,adhar=adhar,adress=adress,district=district,place=place,qualification=qualification,client=Client(request.session['id']))
        obj.save()

        today_date=datetime.date.today()     
        clientobj=Client.objects.get(id=request.session['id'])   
        name=clientobj.clientname
        email=clientobj.email

        #qrcode
        img=qrcode.make("QR Code Created Date:%s \n\n Name:'%s' \n\n Email Address:'%s' \n\n Contact NO:'%s'  \n\n Address:'%s' \n\n District:'%s'  \n\n Education:'%s' \n\n Aadhar No:'%s'"%(str(today_date),str(name),str(email),str(contactno),str(adress),str(district),str(qualification),str(adhar)))
        imgfile="img%s.jpg"%(obj.id)
        img.save(imgfile)
        buffer=BytesIO()
        img.save(buffer,'PNG')
        document=clientdocument(client=clientinfo(obj.id))
        document.qrdata.save(imgfile,File(buffer))
        #pdfdata
        global pdf
        pdf= render_to_pdf(obj.id,'certificate.html',{'clientobj':clientobj,'obj':obj})

        #document=clientdocument(client=clientdataqrexe2(obj.id))
        global filename
        filename="test%s.pdf"%(obj.id)
        document.pdfdata.save(filename,File(BytesIO(pdf.content)))
        document.save()
        

        return render(request,'result.html',{'document':document})


    return render(request,'clientdataentry.html')
def logoutclient(request):
    request.session.clear()
    return redirect('/')

