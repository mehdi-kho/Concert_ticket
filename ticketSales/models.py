from django.db import models
from jalali_date import date2jalali, datetime2jalali
from accounts.models import ProfileModel


class ConcertModel(models.Model):
    class Meta:
        verbose_name = "کنسرت"
        verbose_name_plural = "کنسرت"
    name = models.CharField(max_length=100, verbose_name="نام کنسرت")
    singer_name = models.CharField(max_length=100, verbose_name="نام خواننده")
    length = models.IntegerField(verbose_name="مدت زمان کنسرت")
    poster = models.ImageField(upload_to="concertImages/", null=True, verbose_name="عکس پوستر کنسرت")

    def __str__(self):
        return self.singer_name


class LocationModel(models.Model):
    # idNumber = models.IntegerField(primary_key=True, )
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=500, default="تهران - برج میلاد", unique=False)
    phone = models.CharField(max_length=11, null=True)
    capacity = models.IntegerField()

    def __str__(self):
        return self.name


class TimeModel(models.Model):
    concertModel = models.ForeignKey("ConcertModel", on_delete=models.CASCADE)
    locationModel = models.ForeignKey(to=LocationModel, on_delete=models.CASCADE)
    startDateTime = models.DateTimeField()
    seats = models.IntegerField()

    start = 1
    end = 2
    cansel = 3
    sale = 4
    status_choices = (
        (start, "فروش بلیط شروع شده است"),
        (end, "فروش بلیط تمام شده است"),
        (cansel, "فروش بلیط کنسل شده است"),
        (sale, "در حال فروش بلیط"),
    )
    status = models.IntegerField(choices=status_choices)

    def __str__(self):
        return "Time:{} ConcertName:{} location:{}".format(self.startDateTime, self.concertModel.name,
                                                           self.locationModel.name)

    def get_jalali_date(self):
        return datetime2jalali(self.startDateTime)



# کد زیر تایم مدلی است که من نوشتم و درست کار کرد و بالایی برای خانم شادلو است
# class TimeModel(models.Model):
#     concertModel = models.ForeignKey("ConcertModel", on_delete=models.CASCADE)
#     locationModel = models.ForeignKey(to=LocationModel, on_delete=models.CASCADE)
#     startDateTime = models.DateTimeField()
#     seats = models.IntegerField()
#     status_choices = (
#         ("فروش بلیط شروع شده است", "start"),
#         ("فروش بلیط تمام شده است", "end"),
#         ("فروش بلیط کنسل شده است", "cansel"),
#         ("در حال فروش بلیط", "sale"),
#     )
#     status = models.CharField(choices=status_choices, max_length=50)
#
#     def __str__(self):
#         return "Time:{} ConcertName:{} location:{}".format(self.startDateTime, self.concertModel.name,
#                                                            self.locationModel.name)


# class profileModel(models.Model):
#     name = models.CharField(max_length=100)
#     family = models.CharField(max_length=100)
#     # man = 1
#     # woman = 2
#     status_choices = (
#         ("man", "مرد"),
#         ("woman", "زن")
#     )
#     gender = models.CharField(max_length=10, choices=status_choices)
#     profileImage = models.ImageField(upload_to="profileImages/", null=True)
#
#     def __str__(self):
#         return f"Name: {self.name} Family: {self.family}"
#         # return "Fullname: {} {}".format(name, family)


class TicketModel(models.Model):
    # concertModel = models.ForeignKey("ConcertModel", on_delete=models.CASCADE, null=True)
    profileModel = models.ForeignKey(ProfileModel, on_delete=models.CASCADE, null=True)
    timeModel = models.ForeignKey("TimeModel", on_delete=models.CASCADE, null=True)
    ticketName = models.CharField(max_length=100, null=True)  # بلیط طلایی و بلیط نقره ای
    price = models.IntegerField(null=True)
    ticketImage = models.ImageField(upload_to="ticketImages/", null=True)

    def __str__(self):
        return "TicketInfo:  profile {} TimeModel {}".format(self.profileModel, self.timeModel)
        # return (f"TicketInfo: profile: {self.profileModel} concert: {self.concertModel}"
        #         f" Time: {self.timeModel}")
        # return "TicketInfo: profile: {} ConcertInfo: {} {} {}".format(self.profileModel, self.concertModel,
        #                                                            self.LocationModel, TimeModel.startDateTime)
        # return "TicketInfo:  profile {} cocertinfo: {}".format(TimeModel.__str__())
        # return "TicketInfo:  profile {}{} ConcertInfo: {} TimeModel {} {} {}".format(self.profileModel,
        #                                                                              self.concertModel, self.timeModel)