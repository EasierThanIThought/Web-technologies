from django.db import models
from django.contrib.auth.models import User


# class User(models.Model):
#     #id = models.AutoField(primary_key=True)
#     login = models.CharField(max_length=255, verbose_name=u"login")
#     password = models.CharField(max_length=255, verbose_name=u"password")
#     is_staff = models.BooleanField(default=0)
#
#     def __str__(self):
#         return self.login


class Hospital(models.Model):
    #id = models.AutoField(primary_key=True)
    address = models.CharField(max_length=255, verbose_name=u"address")
    name = models.CharField(max_length=255, verbose_name=u"name")
    phone = models.CharField(max_length=255, verbose_name=u"phone number")

    def __str__(self):
        return self.name


class Profession(models.Model):
    #id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, verbose_name=u"profession")

    def __str__(self):
        return self.name


class Doctor(models.Model):
   # id = models.AutoField(primary_key=True)
    models.ForeignKey(Hospital, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, verbose_name=u"name")
    room = models.IntegerField(verbose_name=u"room")
    profession_id = models.ForeignKey(Profession, on_delete=models.CASCADE)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)

    def __str__(self):
        return self.name




class Patient(User):
    #id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, verbose_name=u"name", blank=True)
    surname = models.CharField(max_length=255, verbose_name=u"surname", blank=True)
    passport = models.CharField(max_length=255, verbose_name=u"passport",blank=True, unique=True)
    phone_number = models.CharField(max_length=255, verbose_name=u"mobile", null=True, blank=True)
    birth = models.DateField(max_length=255, verbose_name=u"bithday", blank=True, null=True)
    #user_id = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)

    def __str__(self):
        return self.name

    # def getbyuserid(id):
    #     return self.name



class MedicalCard(models.Model):
    #id = models.AutoField(primary_key=True)
    app_date = models.DateTimeField(max_length=255, verbose_name=u"date")
    diagnosis = models.CharField(max_length=255, verbose_name=u"diagnosis")
    doctor_id = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)


    def __str__(self):
        return self.diagnosis

class Appointment(models.Model):
    #id = models.AutoField(primary_key=True)
    patient_id = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor_id = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    time = models.DateTimeField()

    def __int__(self):
        return self.id


class Vacation(models.Model):
    #id = models.AutoField(primary_key=True)
    doctor_id = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    start_date = models.DateTimeField(max_length=255, verbose_name=u"start date")
    end_date = models.DateTimeField(max_length=255, verbose_name=u"end date", null=True, blank=True)

    def __int__(self):
        return self.id


class Schedule(models.Model):
   # id = models.AutoField(primary_key=True)
    doctor_id = models.ForeignKey(Doctor, on_delete=models.CASCADE, primary_key=True)
    mon = models.CharField(max_length=255)
    tue = models.CharField(max_length=255)
    wed = models.CharField(max_length=255)
    thu = models.CharField(max_length=255)
    fri = models.CharField(max_length=255)
    sat = models.CharField(max_length=255)
    sun = models.CharField(max_length=255)

    def __int__(self):
        return self.id

