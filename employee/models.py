""""
This model is responsible for creating employee table
It contains methods for performing CRUD operations on the employee table

"""
from django.db import models


# Create your models here.
# Creating the employee model
class Employee(models.Model):
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    email = models.CharField(max_length=200, blank=True, default='')
    phone = models.CharField(max_length=200)
    address = models.TextField(max_length=200, blank=True, default='')
    worktype = models.CharField(max_length=200)
    hourly_rate = models.CharField(max_length=200)
    job_title = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    #Method to save employee details for new employess
    def save_employee(self, firstname, lastname, phone, worktype, hourly_rate, jtitle, email=None, address=None):
        emp = Employee(firstname=firstname, lastname=lastname, phone=phone, worktype=worktype, job_title=jtitle,
                       hourly_rate=hourly_rate, email=email, address=address)
        emp.save()
        #if the save process was successfull ;returns a primary key
        if emp.pk is not None:
            return "Success"
        else:
            return "Failed"
    #delete employe method
    def delete_employee(self, id):
        delete = Employee.objects.get(pk=id).delete()
        if delete is not None:
            return "Success"
        else:
            return "Failed"

    #get all the employees
    def get_employee(self):
        get_emp = Employee.objects.order_by('date_added')
        return get_emp
    #update employees
    def update_employee(self, id, firstname, lastname, phone, worktype, hourly_rate,jtitle, email=None, address=None):
        update = Employee.objects.get(pk=id)
        update.firstname=firstname
        update.lastname=lastname
        update.phone=phone
        update.worktype=worktype
        update.hourly_rate=hourly_rate
        update.job_title=jtitle
        update.email=email
        update.address=address
        update.save()
        if update is not None:
            return "Success"
        else:
            return "Failed"
    #get a single employee by ID
    def get_single_emp(self, id):
        single = Employee.objects.filter(id=id)
        return single
