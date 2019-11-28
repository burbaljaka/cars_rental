from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .models import Car
from django.utils.timezone import localtime, now
# Extra Imports for the Login and Logout Capabilities
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from rental.forms import UserForm
from django.views import generic
from django.contrib.auth.models import User
from django.views.generic.edit import UpdateView, FormView
from .forms import CarRent
from django.utils import timezone
from django.core.mail import send_mail

def index(request):
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
                return HttpResponseRedirect(reverse('rental:cars_list'))
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
    loan_cars = Car.objects.filter(car_renter = request.user.id, car_status = 'o')
    return render (request, 'rental/client_cars.html', context = {'cars_list': loan_cars})

def car_list(request):
    available_cars = Car.objects.filter(car_status = 'a')
    return render (request, 'rental/cars_list.html', context = {'cars_list': available_cars})


# def User_info(request):
#
#     User.objects.filter(pk = request.user.id)

# class CarDetailView(generic.DetailView):
#     model = Car

def car_detail(request, pk):
    car_info = Car.objects.filter(pk = pk)[0]
    current_user_id = request.user.id
    if request.method == 'POST' and 'rent_button' in request.POST:
        form = CarRent(request.POST)
        if form.is_valid():
            user = User.objects.get(pk = current_user_id)
            car_info.car_renter = user
            car_info.car_rent_date = timezone.now()
            car_info.car_status = 'o'
            car_info.save()
            # send_email_to_rent('rent', user, car_info)
            return HttpResponseRedirect(reverse('rental:client_cars'))
        else:
            print(form)
    elif request.method == 'POST' and 'return_button' in request.POST:
        form = CarRent(request.POST)
        if form.is_valid():
            user = User.objects.get(pk = current_user_id)
            car_info.car_renter = None
            car_info.car_rent_date = None
            car_info.car_status = 'a'
            car_info.save()
            # send_email_to_rent('rent', user, car_info)
            return HttpResponseRedirect(reverse('rental:client_cars'))
        else:
            print(form)
    else:
        car_info = Car.objects.filter(pk = pk)[0]
        return render (request, 'rental/car_detail.html', context = {'car':car_info})

# def send_email_to_rent(type, user, car):
#     if type == 'rent':
#         send_mail(
#         'You have rented a car',
#         'Hi!You have rented a car {} {} at {}'.format(car.car_mark, car.car_model, car.car_rent_date),
#         'from@example.com',
#         [user.email],
#         fail_silently=False,
#         )
#     elif type == 'return':
#         send_mail(
#         'You have returned a car',
#         'Hi! You have returned a car {} {} at {}'.format(car.car_mark, car.car_model, car.car_return_date),
#         'from@example.com',
#         [user.email],
#         fail_silently=False,
#         )
