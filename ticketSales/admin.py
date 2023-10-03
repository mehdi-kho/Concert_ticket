from django.contrib import admin
from ticketSales.models import ConcertModel, LocationModel, TimeModel, TicketModel  #, profileModel

admin.site.register(ConcertModel)
admin.site.register(LocationModel)
admin.site.register(TimeModel)
admin.site.register(TicketModel)
# admin.site.register(profileModel)


# class ReviewInline(admin.TabularInline):
#     model = Review
#
#
# class BookAdmin(admin.ModelAdmin):
#     inlines = [ReviewInline, ]
#     list_display = ("title", "author", "price",)
