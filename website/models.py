from django.db import models



#0 - Negative
#1 - Positive
RESULT = [
    (0,'Negative'),
    (1,'Positive')
]

# Create your models here.
class Info(models.Model):
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    location = models.CharField(max_length=20,default='India')
    sex = models.CharField(max_length=10)
    pregnancies = models.IntegerField(blank=True,default=None,null=True)
    glucose = models.FloatField()
    blood_pressure = models.FloatField()
    skin_thickness = models.FloatField()
    insulin = models.FloatField()
    bmi = models.FloatField()
    dpf = models.FloatField()
    age = models.IntegerField()
    result = models.FloatField()

    def __str__(self):
        return f'{self.first_name} {self.last_name} given {self.sex} is {self.result}'

