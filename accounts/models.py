from django.contrib.auth.models import User
from django.db import models


class ProfileModel(models.Model):
    class Meta:
        verbose_name = "کاربر"
        verbose_name_plural = "کاربر"
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="کاربری", related_name="profile")
    # name = models.CharField(max_length=100, verbose_name="نام")
    # family = models.CharField(max_length=100, verbose_name="نام خانوادگی")
    man = 1
    woman = 2
    status_choices = (
        (man, "مرد"),
        (woman, "زن")
    )
    # gender = models.CharField(max_length=10, choices=status_choices)
    gender = models.IntegerField(choices=status_choices, verbose_name="جنسیت")
    profileImage = models.ImageField(upload_to="profileImages/", null=True, verbose_name="عکس")
    credit = models.IntegerField(verbose_name="اعتبار", default=0)

    # def __str__(self):
    #     # return f"Name: {self.name} Family: {self.family}"
    #     return "Fullname: {} {}".format(self.name, self.family)
