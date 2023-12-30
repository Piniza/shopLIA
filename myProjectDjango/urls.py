from django.contrib import admin
from django.urls import path,include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from client.views import user_login
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('admin/', admin.site.urls),
    path('', include('produit.urls')),
    path('', include('client.urls')),
    path('', include('home.urls')),
    path('', include('order.urls')),
    path('admin_tools_stats/', include('admin_tools_stats.urls')),
    path('accounts/login/',user_login,name='login')
]
urlpatterns += staticfiles_urlpatterns()

