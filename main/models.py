from django.db import models


class Feedback(models.Model):
    name = models.CharField('Никнейм', max_length=20)
    feedback = models.TextField('Отзыв')

    def __str__(self):
        return self.name


class User(models.Model):
    id = models.AutoField(primary_key=True)
    login = models.CharField(max_length=255, verbose_name=u"login")
    password = models.CharField(max_length=255, verbose_name=u"password")
    is_staff = models.BooleanField(default=0)

    def __str__(self):
        return self.login

class Hospital(models.Model):
    id = models.AutoField(primary_key=True)
    address = models.CharField(max_length=255, verbose_name=u"address")
    name = models.CharField(max_length=255, verbose_name=u"name")
    phone = models.CharField(max_length=255, verbose_name=u"phone number")

    def __str__(self):
        return self.name


class Profession(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, verbose_name=u"Имя")

    def __str__(self):
        return self.name


class Doctor(models.Model):
    id = models.AutoField(primary_key=True)
    models.ForeignKey(Hospital, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, verbose_name=u"Имя")
    room = models.IntegerField(verbose_name=u"Имя")
    profession_id = models.ForeignKey(Profession, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class MedicalCard(models.Model):
    id = models.AutoField(primary_key=True)
    app_date = models.DateTimeField(max_length=255, verbose_name=u"Имя")
    diagnosis = models.EmailField(null=True, blank=True)
    doctor_id = models.ForeignKey(Doctor, on_delete=models.CASCADE)

    def __str__(self):
        return self.app_date


class Patient(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, verbose_name=u"Имя")
    passport = models.CharField(max_length=255, verbose_name=u"Имя")
    phone_number = models.CharField(max_length=255, verbose_name=u"Мобильный номер", null=True, blank=True)
    birth = models.CharField(max_length=255, verbose_name=u"Имя")
    card_id = models.ForeignKey(MedicalCard, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name



class Appointment(models.Model):
    id = models.AutoField(primary_key=True)
    patient_id = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor_id = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    time = models.DateTimeField()

    def __str__(self):
        return self.id



class Vacation(models.Model):
    id = models.AutoField(primary_key=True)
    doctor_id = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    start_date = models.DateTimeField(max_length=255, verbose_name=u"Имя")
    end_date = models.DateTimeField(max_length=255, verbose_name=u"Мобильный номер", null=True, blank=True)

    def __str__(self):
        return self.id


class Schedule(models.Model):
    id = models.AutoField(primary_key=True)
    doctor_id = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    mon = models.CharField(max_length=255)
    tue = models.CharField(max_length=255)
    wed = models.CharField(max_length=255)
    thu = models.CharField(max_length=255)
    fri = models.CharField(max_length=255)
    sat = models.CharField(max_length=255)
    sun = models.CharField(max_length=255)

    def __str__(self):
        return self.id

