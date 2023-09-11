from django.shortcuts import render
from . models import *
from django.shortcuts import redirect,get_object_or_404,reverse,HttpResponse
from django.contrib import messages
import random
from django.contrib.sessions.models import Session
from django.contrib.auth import authenticate , login
import pyotp
from django.contrib.auth.decorators import login_required
from .forms import CustomPasswordChangeForm
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.views import PasswordResetView
from django.utils.html import strip_tags
from django.core.mail import send_mail, EmailMessage
from django.template.loader import render_to_string
from django.contrib.auth import logout

def home(request):
    return render(request, 'user_app/index.html')


def register(request):
    if request.method == 'POST':

        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        mobno = request.POST['mobno']
        address = request.POST['address']
        gender = request.POST['gender']

        # Basic validation
        if password == confirm_password:
          user = User(username=username, email=email, password=password, mobno=mobno, address=address, gender=gender, is_registered=True)
          user.save()
          messages.success(request, f'{user.username} Registration successful. You can now log in.')

         # Redirect to success page
        
        return render(request, 'regsuccess.html', {'user': user})

    return render(request, 'register_form.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            user.save()
        return redirect('login_success',user)
    
    return render(request, 'login_form.html')

# @login_required
def login_success(request):

    if request.method == 'POST':
        
        username = request.POST['username']
        password = request.POST['password']
    
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
        messages.success(request, f'{username} Logged in successfully')  # Display success message
        

    return render(request, 'login_success.html')


# def logout(request):
    
#     username = User.username  # Initialize username to None
#     if request.user.is_authenticated:
#         username = request.user.username  # Get the username of the logged-out user
#         logout(request)
        
#     return render(request, 'logout_success.html', {'username': username})

from django.contrib.auth import logout as auth_logout  # Import Django's logout function

def custom_logout(request):
    username = None  # Initialize username to None
    if request.user.is_authenticated:
        username = request.user.username  # Get the username of the logged-out user
        auth_logout(request)  # Use Django's logout function from authentication module
        
    return render(request, 'logout_success.html', {'username': username})


   

def forget_password(request):
    
     return render(request,'forget_password.html')


def email_template(request):
    return render(request,'emailtemplate.html')


def password_reset_sent(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            
            # Send the password reset email
            form.save(request=request)
            
            # Print the email in the terminal
            print("Password reset email sent to:", email)
       
            
            # Render the template with a success message
            return render(request, 'password_reset_sent.html', {'email': email})
    else:
        form = PasswordResetForm()
    return render(request, 'password_reset_form.html', {'form': form})



# @login_required
def change_password(request):
    if request.method == 'POST':
        form = CustomPasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('password_change_success')
    else:
        form = CustomPasswordChangeForm(user=request.user)
    return render(request, 'change_password.html', {'form': form})

def password_change_success(request):
    return render(request, 'password_change_success.html')

def dashboard(request):
    registered_users = User.objects.filter(is_registered=True)
    context = {'registered_users': registered_users}
    return render(request, 'dashboard.html', context)

def delete_user(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    user.delete()
    return redirect('dashboard')


def get_user_data(user):
    user_data = {
        'userid': user.id,
        'username': user.username,
        'email': user.email,
        'mobno': user.mobno,
        'gender': user.get_gender_display(),
        'address': user.address,
    }
    return user_data

def profile_view(request,user_id):
   # person = get_object_or_404(Person, pk=person_id)
    user_data = User.objects.get(id=user_id)
    print(type(user_data),user_data)
    # print(type(person),person)
    return render(request, 'profile.html', {'user': user_data})


def send_email_two(request):
    subject = 'Your Old Password Details'  
      # message = "This is your old password " + for_password + " You can use this old password or Enter your new password for your login" # Body of the email
    sender = "mr.santhoshkumar3005@gmail.com"
    receipent_email = "mr.santhoshkumar3005@gmail.com" 
      
      # send_mail(subject, message, sender, [receipent_email])
      # print("mail sended>>>>>>>")

      #django email function:
      # Load the HTML template file
    template_name = '../templates/send_email.html'
      # template_name = loader.get_template('send_email.html')
    context = {'old_password': 'Santhu@7595937'}  # Optional context variables for the template
      # Render the template as a string
    html_message = render_to_string(template_name, context)
      # Convert HTML content to plain text
    plain_message = strip_tags(html_message)
      # subject = 'Your Subject'
      # from_email = 'your-email@example.com'
    to_email = 'recipient-email@example.com'
    email = EmailMessage(subject,  html_message, sender, [receipent_email])
    email.content_subtype = 'html'
      # email.attach_alternative(html_message, "text/html")
    email.send()
    return HttpResponse("Email sent check your inbox")


