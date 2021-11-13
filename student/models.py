from django.db import models
from django.utils import timezone


# Create your models here.
class StudyLevel(models.TextChoices):
    FirstYear=('1ST','First Year')
    SecondYear=('2ND','Second Year')
    ThirdYear=('3RD','Third Year')
class Student(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=70,null=True,blank=True)
    birthday=models.DateField(default=timezone.now)
    class Meta:
        ordering = ['name']
        abstract = True
        
class Terminal(Student):
    espMark=models.FloatField(verbose_name="End of Study Project Mark")
    class Meta:
        db_table = 'terminal_atb'

class Bechelor(Student):
    studyYear=models.CharField(max_length=3,choices=StudyLevel.choices,default=StudyLevel.FirstYear)
    class Meta:
        db_table='bechelor_tab'
