from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .models import Car, Loan
from django.utils.timezone import localtime, now
# Extra Imports for the Login and Logout Capabilities
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from rental.forms import UserForm
from django.views import generic
from django.contrib.auth.models import User

def index(request):
    try:
        current_user_auth = request.user.is_authenticated
    except:
        return HttpResponseRedirect(reverse('user_login'))
    else:
        if current_user_auth == False:
            return HttpResponseRedirect(reverse('user_login'))
        else:
            return HttpResponseRedirect(reverse('rental:cars_list'))

@login_required
def special(request):
    # Remember to also set login url in settings.py!
    # LOGIN_URL = '/rental/user_login/'
    return HttpResponse("You are logged in. Nice!")

@login_required
def user_logout(request):
    # Log out the user.
    logout(request)
    # Return to homepage.
    return HttpResponseRedirect(reverse('index'))

def register(request):

    registered = False

    if request.method == 'POST':

        # Get info from "both" forms
        # It appears as one form to the user on the .html page
        user_form = UserForm(data=request.POST)

        # Check to see both forms are valid
        if user_form.is_valid():

            # Save User Form to Database
            user = user_form.save()

            # Hash the password
            user.set_password(user.password)

            # Update with Hashed password
            user.save()

            # Now we deal with the extra info!

            # Can't commit yet because we still need to manipulate
            # profile = profile_form.save(commit=False)
            #
            # # Set One to One relationship between
            # # UserForm and UserProfileInfoForm
            # profile.user = user
            #
            # Check if they provided a profile picture
            # if 'profile_pic' in request.FILES:
            #     print('found it')
            #     # If yes, then grab it from the POST form reply
            #     profile.profile_pic = request.FILES['profile_pic']
            #
            # # Now save model
            # profile.save()
            #
            # # Registration Successful!
            registered = True

        else:
            # One of the forms was invalid if this else gets called.
            print(user_form.errors)

    else:
        # Was not an HTTP post so we just render the forms as blank.
        user_form = UserForm()
        # profile_form = UserProfileInfoForm()

    # This is the render and context dictionary to feed
    # back to the registration.html file page.
    return render(request,'rental/registration.html',
                          {'user_form':user_form,
                           # 'profile_form':profile_form,
                           'registered':registered})

def user_login(request):

    if request.method == 'POST':
        # First get the username and password supplied
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Django's built-in authentication function:
        user = authenticate(username=username, password=password)

        # If we have a user
        if user:
            #Check it the account is active
            if user.is_active:
                # Log the user in.
                login(request,user)
                # Send the user back to some page.
                # In this case their homepage.
                current_user_id = request.user.id
                loan_cars = Loans.objects.filter(loan_renter = current_user_id)
                if loan_cars == 0:
                    return HttpResponseRedirect(reverse('rental:client_Loan_Cars'))
                else:
                    return HttpResponseRedirect(reverse('rental:car_list'))
#                return render(request, 'rental/tasks.html', context)
            else:
                # If account is not active:
                return HttpResponse("Your account is not active.")
        else:
            return HttpResponse("Invalid login details supplied.")

    else:
        #Nothing has been provided for username or password.
        return render(request, 'rental/login.html', {})

def client_Loan_Cars(request):
    loan_cars = Loan.objects.filter(loan_renter = request.user.id)
    return render (request, 'rental/cars_list.html', context = {'cars_list': loan_cars})

def car_list(request):
    client_cars = Loan.objects.filter(loan_renter = request.user.id)
    if not client_cars:
        available_cars = Car.objects.filter(car_status = 'a')
        return render (request, 'rental/cars_list.html', context = {'cars_list': available_cars})
    else:
        return HttpResponseRedirect(reverse('rental:client_Loan_Cars'))


def User_info(request):

    User.objects.filter(pk = request.user.id)
