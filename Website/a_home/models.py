from django.db import models

class UserData(models.Model):
    text_input1 = models.CharField(max_length=100)
    text_input2 = models.CharField(max_length=100)
    dropdown_value1 = models.CharField(max_length=50)
    dropdown_value2 = models.CharField(max_length=50)

