from django.db import models
from django.core.validators import RegexValidator  

class ContactModel(models.Model):
    slno = models.AutoField(primary_key=True)  
    
    first_name = models.CharField(
        max_length=50, 
        validators=[RegexValidator(r'^[a-zA-Z ]{1,50}$', 'Enter a valid first name')]
    )
    
    last_name = models.CharField(
        max_length=50, 
        validators=[RegexValidator(r'^[a-zA-Z ]{1,50}$', 'Enter a valid last name')]
    )
    
    email = models.EmailField(unique=True,
        validators=[RegexValidator(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')])
    '''
    number = models.CharField(unique=True,
        max_length=10, 
        validators=[RegexValidator(r'^(\+\d{1,2}\s?)?1?\-?\.?\s?\(?\d{3}\)?[\s.-]?\d{3} [\s.-]?\d{4}$', 'Enter a valid 10-digit phone number')]
    )
    '''
    number = models.CharField(unique=True,
        max_length=10, 
        validators=[RegexValidator(r'^[6-9]\d{9}$', 'Enter a valid 10-digit phone number')]
    )
    address = models.TextField()
    
    gender = models.CharField(
        max_length=6, 
        choices=[('Male', 'Male'), ('Female', 'Female')]
    )

    def __str__(self):
        return f"{self.slno} - {self.first_name} {self.last_name}"
