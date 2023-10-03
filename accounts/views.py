from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
import accounts
import ticketSales
from accounts.forms import ProfileRegisterForm, ProfileEditForm, UserEditForm
from accounts.models import ProfileModel
from django_project import settings


# from ticketSales.views import timeView


# def loginViews(request):
#     # POST
#     if request.method == "POST":
#         username = request.POST.get("username")
#         password = request.POST.get("password")
#         user = authenticate(request, username=username, password=password)
#
#         if user is not None:
#             login(request, user)
#             return HttpResponseRedirect(reverse(ticketSales.views.timeView))
#         else:
#             context = {
#                 "username": username,
#                 "erorrMesage": "کاربری با این مشخصات یافت نشد"
#             }
#             return render(request, "accounts/login.html", context)
#     #GET
#     else:
#         return render(request, "accounts/login.html", {})


def loginView(request):
    # POST
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            if request.GET.get("next"):
            # return HttpResponseRedirect(reverse(ticketSales.views.timeView))
                return HttpResponseRedirect(request.GET.get("next"))
            else:
                return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)  # به انتهای settings مراجعه شود
        else:
            context = {
                "username": username,
                "erorrMesage": "کاربری با این مشخصات یافت نشد"
            }
            return render(request, "accounts/login.html", context)
    #GET
    else:
        return render(request, "accounts/login.html", {})


def logoutView(request):
    logout(request)
    return HttpResponseRedirect(reverse(ticketSales.views.concertListView))


@login_required
def profileView(request):
    profile = request.user.profile
    context = {
        "profile": profile
    }
    return render(request, "accounts/profile.html", context)


def profileRegisterView(request):
    if request.method == "POST":
        profileRegisterForm = ProfileRegisterForm(request.POST, request.FILES)
        if profileRegisterForm.is_valid():
            user = User.objects.create_user(username=profileRegisterForm.cleaned_data["username"],
                                            email=profileRegisterForm.cleaned_data["email"],
                                            password=profileRegisterForm.cleaned_data["password"],
                                            first_name=profileRegisterForm.cleaned_data["first_name"],
                                            last_name=profileRegisterForm.cleaned_data["last_name"])
            user.save()
            profileModel = ProfileModel(user=user, profileImage=profileRegisterForm.cleaned_data["profileImage"],
                                        gender=profileRegisterForm.cleaned_data["gender"],
                                        credit=profileRegisterForm.cleaned_data["credit"])
            profileModel.save()
            return HttpResponseRedirect(reverse(ticketSales.views.concertListView))
    else:
        profileRegisterForm = ProfileRegisterForm()
    context = {
        "formData": profileRegisterForm
    }
    return render(request, "accounts/profileRegister.html", context)


def profileEditView(request):
    if request.method == "POST":
        profileEditForm = ProfileEditForm(request.POST, request.FILES, instance=request.user.profile)
        userEditForm = UserEditForm(request.POST, instance=request.user)
        if profileEditForm.is_valid and userEditForm.is_valid:
            profileEditForm.save()
            userEditForm.save()
            return HttpResponseRedirect(reverse(accounts.views.profileView))
    else:
        profileEditForm = ProfileEditForm(instance=request.user.profile)
        userEditForm = UserEditForm(instance=request.user)
    context = {
        "profileEditForm": profileEditForm,
        "userEditForm": userEditForm,
        "profileImage": request.user.profile.profileImage,
    }
    return render(request, "accounts/profileEdit.html", context)






