from django.db import models

class approval(models.Model):
    GENDER_CHOICES={
        ('Male','Male'),
        ('Female','Female')
    }
    MARRIED_CHOICES={
        ('Yes','Yes'),
        ('No','No')
    }
    GRADUATE_CHOICES={
        ('Graduate','Graduate'),
        ('Not_Graduate','Not_Graduate')
    }
    SELFEMPLOYED_CHOICES={
        ('Yes','Yes'),
        ('No','No')
    }
    PROPERTY_CHOICES={
        ('Rural','Rural'),
        ('Semiurban','Semiurban'),
        ('Urban','Urban')
    }
    firstname=models.CharField(max_length=15)
    lastname=models.CharField(max_length=15)
    dependants=models.IntegerField()
    applicantincome=models.IntegerField()
    coapplicantincome=models.IntegerField()
    loanamt=models.IntegerField()
    loanterm=models.IntegerField()
    credithistory=models.IntegerField()
    gender=models.CharField(max_length=15,choices=GENDER_CHOICES)
    married=models.CharField(max_length=15,choices=MARRIED_CHOICES)
    graduatededucation=models.CharField(max_length=15,choices=GRADUATE_CHOICES)
    selfemployed=models.CharField(max_length=15,choices=SELFEMPLOYED_CHOICES)
    area=models.CharField(max_length=15,choices=PROPERTY_CHOICES)

    def __str__(self):
        return self.firstname,self.lastname
