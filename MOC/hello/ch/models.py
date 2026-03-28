from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    dob = models.DateField(max_length=20)
    address = models.CharField(max_length=50)

    class Meta:
        db_table = 'hello_user'


