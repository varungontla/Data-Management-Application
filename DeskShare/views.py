from django.core.mail import send_mail, EmailMessage
from django.shortcuts import render, redirect
from CNproject.forms import UploadForm, CreateUserForm,EmailForm
from .models import Upload,User
from django.contrib.auth import authenticate, logout, login
from django.contrib import messages
from django.contrib.auth.models import User
from django.db.models import Q
import smtplib

def register_page(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    context = {
        'form': form,
    }
    return render(request, 'register.html', context)


def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('DeskShare')
        else:
            messages.info(request, 'Username or Password is incorrect')
    context = {}
    return render(request, 'login.html', context)


def logout_user(request):
    logout(request)
    return redirect('login')


def deskSharePage(request):
    files_qs = Upload.objects.filter(user=request.user)
    context = {
        'items': files_qs
    }
    return render(request, 'DeskShare.html', context)


#def pdf_list(request):
 #   files_qs = Upload.objects.filter(user=request.user)

  #  context = {
   #     'items': files_qs
    #}
   # return render(request, 'pdf_list.html', context)


def upload_pdf(request, null=None):
    if request.method == 'POST':
        form = Upload(request.POST, request.FILES)
        if form != null:
            instance = Upload(user=request.user, Filename=request.POST.get('title'), File=request.FILES['pdf'])
            messages.success(request,"Done Uploading")
            instance.save()
            return redirect('DeskShare')
    form = UploadForm()
    return render(request, 'upload_pdf.html', {"form": form})

#def shared_view(request):
 #   usernames = ""
  #  if 'search' in request.GET:
   #     search_term = request.GET['search']
    #    usernames = User.objects.filter(username=search_term)



#    files = Upload.objects.filter(user = request.user)

   # context = {
    #   'items':usernames
   # }

    #return render(request,'share.html',context)

def email_view(request):
    if request.method == 'GET':
        form = EmailForm()

    else:
        form = EmailForm(request.POST,request.FILES)
        subject = request.POST.get('subject')
        from_email = request.POST.get('from_email')
        to_email   = request.POST.get('to_email')
        message    = request.POST.get('message')
        file = request.FILES['attachment']

        email = EmailMessage(
            subject,
            message,
            [from_email],
            [''],
            [to_email]
        )
        email.attach(file.name,file.read(),file.content_type)
        email.send()


        #server = smtplib.SMTP('smtp.gmail.com:587')
        #server.ehlo()
        #server.starttls()
        #server.login(from_email,passw)
        #server.sendmail(from_email,[to_email],message)
        #server.quit()

    return render(request,'share.html',{'form':form})


