from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=200)
    address = models.TextField(max_length=200)
    address_two = models.TextField(max_length=200, blank=True, default='')
    town = models.CharField(max_length=200)
    zip_code = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def save_user(self, fname,lname,password,email, phone_number, address, address_two, town, zip_code, state):
        """Return a string representation of the model."""
        user = User.objects.create_user(username=fname + lname, first_name=fname, email=email, last_name=lname,
                                        password=password)
        user.save()
        userProfile = UserProfile(phone_number=phone_number, address=address, address_two=address_two, town=town,
                                  zip_code=zip_code, state=state, user_id_id=user.pk)
        userProfile.save()
        if userProfile.pk is not None:
            return "Success"
        else:
            return "Failed"

