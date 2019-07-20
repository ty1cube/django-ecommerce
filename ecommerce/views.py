from django.http import HttpResponse
from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login, get_user_model
# from django.contrib.auth.models import User

from .forms import ContactForm, LoginForm, RegisterForm


def home_page(request):
    context = {
        "title": "Ecommerce Home Page",
        "welcome": "welcome to the Ecommerce Home Page",
        # "premium": "Take the username and password",
    }
    if request.user.is_authenticated:
        context["premium"] = "Username is 'azeez' and pass is 'akinsola'"

    return render(request, 'home_page.html', context)


def about_page(request):
    context = {
        "title": "About Us",
        "welcome": "Welcome to About us"
    }

    return render(request, 'home_page.html', context)


def service_page(request):
    context = {
        "title": "Service Page",
        "welcome": "Welcome to our service page"
    }

    return render(request, 'home_page.html', context)


def contact_page(request):

    contact_form = ContactForm(request.POST or None)
    context = {
        "title": "Contact us page",
        "content": "Contact us here for any questions",
        "form": contact_form
    }

    if contact_form.is_valid():
        print(contact_form.cleaned_data)
        context['form'] = ContactForm()

    return render(request, 'contact/view.html', context)


def login_page(request):
    login_form = LoginForm(request.POST or None)

    context = {
        "title": "Login Here",
        "form": login_form
    }
    if login_form.is_valid():

        print(login_form.cleaned_data)

        username = login_form.cleaned_data.get("username")
        password = login_form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)
        print(user)

        if user is not None:
            login(request, user)
            # Redirect to a success page.
            # context['form'] = LoginForm()
            return redirect("/")
        else:
            # Return an 'invalid login' error message.
            print("Error login")
    return render(request, "auth/login.html", context)


User = get_user_model()
def register_page(request):
    register_form = RegisterForm(request.POST or None)
    context = {
        "title": "Register Here",
        "form": register_form
    }

    if register_form.is_valid():
        print(register_form.cleaned_data)
        firstname = register_form.cleaned_data.get('firstname')
        lastname = register_form.cleaned_data.get('lastname')
        email = register_form.cleaned_data.get("email")
        username = register_form.cleaned_data.get('username')
        password = register_form.cleaned_data.get('password')

        new_user = User.objects.create_user(
            username, first_name=firstname, last_name=lastname, email=email,  password=password)
        print(new_user)

        context['form'] = RegisterForm()

    return render(request, "auth/register.html", context)


# def contact_page(request):

#     context = {
#         "title": "Contact us page",
#         "content": "Contact us here for any questions"
#     }
#     if request.method == "POST":
#         # print(request.POST)
#         print(request.POST.get('fullname'))
#         print(request.POST.get('email'))
#         print(request.POST.get('description'))
#     return render(request, 'contact/view.html', context)
