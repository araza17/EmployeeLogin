from django.shortcuts import render
from .models import UserProfile


# Create your views here.
def index(request):
    """The home page for Learning Log"""
    return render(request, 'user/index.html')

# Create your views here.
def order(request):
    """The home page for Learning Log"""
    return render(request, 'user/confirmation.html',
                  {'message': 'Your Order was successfull'})
    
# Create your views here.
def register(request):
    # Check for required Fields
    if request.POST['fname'] != '' and request.POST['lname'] != '' and request.POST['pnumber'] != '' and request.POST[
        'address'] != '':
        create = UserProfile().save_user(request.POST['fname'],
                                          request.POST['lname'],
                                          request.POST['password'],
                                          request.POST['email'],
                                          request.POST['pnumber'],
                                          request.POST['address'],
                                          request.POST['address2'],
                                          request.POST['town'],
                                          request.POST['zip'],
                                          request.POST['state'],

                                          )
        if create == 'Success':
            return render(request, 'user/confirmation.html',
                          {'message': 'The user has been created'})
        else:
            return render(request, 'user/confirmation.html',
                          {'message': 'There was an error'})

    
