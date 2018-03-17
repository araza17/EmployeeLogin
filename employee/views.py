""""
THis view file contains all our views functions to handle individual routes as specified in the url file
"""

from django.shortcuts import render, redirect
from .models import Employee
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
# Index page; or land page to handle employee/
def index(request):
    """The home page for Employee
    This will contain forms"""
    resp = request.GET.get('error')
    employees = Employee().get_employee()
    return render(request, 'employee/index.html', {'message': employees, 'error': resp})


#add new employee page to handle employee/add employee /
def add_emp_page(request, id=None):

    #get any error message passed to this page
    resp = request.GET.get('error')
    if id is not None:
        single = Employee().get_single_emp(id)
        return render(request, 'employee/create_emp.html',
                      {'single': single, 'error': resp, 'title': 'Update Employee', 'url': 'update employee'})

    else:
        return render(request, 'employee/create_emp.html',
                      {'error': resp, 'title': 'Create New Employee', 'url': 'create employee'})

#this is used to create a new employee, this is a logic function
@csrf_exempt
def create_emp(request):
    # Check for required Fields
    if request.POST['fname'] != '' and request.POST['lname'] != '' and request.POST['phone'] != '' and request.POST[
        'hrlyrate'] != '':
        create = Employee().save_employee(request.POST['fname'],
                                          request.POST['lname'],
                                          request.POST['phone'],
                                          request.POST['worktype'],
                                          request.POST['hrlyrate'],
                                          request.POST['jtitle'],
                                          request.POST['email'],
                                          request.POST['address'],

                                          )
        if create == 'Success':
            return render(request, 'employee/confirmation.html',
                          {'message': 'The Employee has been created, click the All employee page,'
                                      'to view all employees'})
        else:
            return redirect('/employee/add employee/?error=%s' % create)
    else:
        error = 'Some of the required Fields are missing'
        return redirect('/employee/add employee/?error=%s' % error)


def delete_emp(request, id):
    delete = Employee().delete_employee(id)
    if delete == 'Success':
        return redirect('/employee/')
    else:
        error = "Could not delete employee"
        return redirect('/employee/?error=%s' % error)

#used to udate the employee details
@csrf_exempt
def update_emp(request):
    if request.POST['fname'] != '' and request.POST['lname'] != '' and request.POST['phone'] != '' and request.POST[
        'hrlyrate'] != '':
        create = Employee().update_employee(request.POST['id'], request.POST['fname'],
                                            request.POST['lname'],
                                            request.POST['phone'],
                                            request.POST['worktype'],
                                            request.POST['hrlyrate'],
                                            request.POST['jtitle'],
                                            request.POST['email'],
                                            request.POST['address'],

                                            )
        if create == 'Success':
            message = request.POST['fname'] + '  ' + request.POST['lname'] + '   employee has been updated'
            return render(request, 'employee/confirmation.html',
                          {'message': message})
        else:
            return redirect('/employee/add employee/?error=%s' % create)
    else:
        error = 'Some of the required Fields are missing'
        return redirect('/employee/add employee/?error=%s' % error)
