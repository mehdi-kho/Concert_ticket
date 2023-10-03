from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from ticketSales.views import concertListView, locationListView, concertDetailsView, timeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ticketSales/', include("ticketSales.urls")),
    path('accounts/', include("accounts.urls")),
]

# برای نشان دادن عکسهای سیستم فایل(پوشه مدیا) اضافه شده و گرنه سرو کردن این عکسها با سرور است نه جنگو و جنگو فقط
# عکسهای پوشه استاتیک را سرو می کند پس با کد زیر عکسهای فایل سیستم(پوشه مدیا) هم توسط جنگو سرو و نشان داده می شود
# در ضمن کد زیر باعث می شود صفحه http://127.0.0.1:8000 دیده نشود و ارور بدهد ولی صفحه http//127.0.0.1:8000/admin دیده
# خواهد شد
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
