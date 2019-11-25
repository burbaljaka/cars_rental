from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone


# Create your models here.
class Cars(models.Model):
    car_mark = models.CharField(max_length = 50)
    car_model = models.CharField(max_length = 50)
    car_issue_year = models.IntegerField()
    car_adding_date = models.DateField(default = timezone.now())
    car_renter = models.CharField(blank = True)

    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

    car_status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default='m',
        help_text='Car availability',
    )

    class Meta:
        ordering = ['car_mark', 'car_model']

    def __str__(self):
        return self.car_mark, self.car_model

    def get_auto_absolute_url(self):
        return reverse('car_detail', args=[str(self.id)])

class Loans(models.Model):
<<<<<<< HEAD
    loan_renter = models.ForeignKey(User, on_delete=models.SET_NULL, null = True, blank = True)
    loan_date_of_loan = models.DateField(default = timezone.now())
    loan_date_of_return = models.DateField()
    loan_car = models.ForeignKey(Car, on_delete=models.SET_NULL, null = True, blank = True)

    def __str__(self):
        return self.loan_car.car_mark, self.loan_car.car_model, self.loan_date_of_loan
=======
    renter = models.ForeignKey(User, on_delete = DO_Nothing, null = True, blank = True)
    date_of_loan = models.DateField(default = timezone.now())
    date_of_return = models.DateField()
>>>>>>> master
