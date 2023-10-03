from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
import ticketSales
from ticketSales.models import ConcertModel, LocationModel, TicketModel, TimeModel
from django.urls import reverse
import accounts
from ticketSales.forms import SearchForm, ConcertForm


def concertListView(request):
    searchForm = SearchForm(request.GET)
    if searchForm.is_valid():
        searchText1 = searchForm.cleaned_data["searchText"]
        concerts = ConcertModel.objects.filter(name__contains=searchText1)
    else:
        concerts = ConcertModel.objects.all()
    context = {
        "concertlist": concerts,
        "concertcount": concerts.count(),
        "searchForm1": searchForm,
    }
    return render(request, "ticketSales/concertlist.html", context)


@login_required
def locationListView(request):
    locations = LocationModel.objects.all()
    context = {
        "locationlist": locations,
    }
    return render(request, "ticketSales/locationList.html", context)


def concertDetailsView(request, concert_id):
    concert = ConcertModel.objects.get(pk=concert_id)
    context = {
        "concertdetail": concert,
    }
    return render(request, "ticketSales/concertDetails.html", context)


@login_required
def timeView(request):
    # if request.user.is_authenticated and request.user.is_active:
        times = TimeModel.objects.all()
        context = {
            "timelist": times,
        }
        return render(request, "ticketSales/timeList.html", context)
    # else:
    #     return HttpResponseRedirect(reverse(accounts.views.loginViews))


# @login_required
def concertEditView(request, concert_id):
    concert = ConcertModel.objects.get(pk=concert_id)
    if request.method == "POST":
        concertForm = ConcertForm(request.POST, request.FILES, instance=concert)
        if concertForm.is_valid:
            concertForm.save()
            return HttpResponseRedirect(reverse(ticketSales.views.concertListView))
            # return HttpResponseRedirect(reverse(ticketSales.views.timeView)) # اینطور هم می شود نوشت ولی خط فوق بهتره
    else:
        concertForm = ConcertForm(instance=concert)

    context = {
        "concertForm": concertForm,
        "PosterImage": concert.poster,
    }

    return render(request, "ticketSales/concertEdit.html", context)



# def concertListView(request):
#     concerts = ConcertModel.objects.all()
#     text = """
#     <!DOCTYPE html>
#     <html lang="en">
#     <head>
#         <meta charset="UTF-8">
#         <title>Title</title>
#     </head>
#     <body>
#         <h1>لیست کنسرت ها</h1>
#         <ul>
#             {}
#         </ul>
#     </body>
#     </html>
#     """.format('\n'.join('<li>{}</li>'.format(concert) for concert in concerts))
#     return HttpResponse(text)
