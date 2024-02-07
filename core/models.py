from django.db import models

# Create your models here.


dars = [

    ('Ona_tili', 'Ona_tili'),
    ('Matematika', 'Matematika'),
    ('Tarix', 'Tarix'),
    ('Adibiyot', 'Adabiyot'),

]

class Uqituvchi(models.Model):
    ismi = models.CharField(max_length = 250)
    famila = models.CharField(max_length = 255)
    yonalishi = models.CharField(max_length = 255)
    yoshi = models.IntegerField()
    Tugilgan_yili = models.DateTimeField()
    def __str__(self):
            return self.ismi





class name(models.Model):
    name = models.CharField(max_length = 250)
    def __str__(self):
        return self.name
    

class student(models.Model):
    dars_nomi = models.CharField(max_length = 250, choices = dars)
    uqituvchi = models.ForeignKey(Uqituvchi, on_delete = models.CASCADE)
    kirish_vaqti = models.DateTimeField(auto_now = False)
    chiqish_vaqti = models.DateTimeField(auto_now = False)
    student_name = models.ForeignKey(name, on_delete = models.CASCADE)

    def __str__(self) -> str:
        return self.dars_nomi