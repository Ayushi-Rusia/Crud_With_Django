from django.urls import path  
from. import views 
urlpatterns = [
    path("",views.home),
    path("reg",views.reg),
    path("log",views.log),
    path("logout",views.logout),
    path("home",views.home),
    path("test",views.test),
    path("delete",views.delte),
    path("update",views.update),
    path("search",views.search)
]
