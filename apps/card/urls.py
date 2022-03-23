from django.urls import path
from .views import Home,Update
app_name = "card"
urlpatterns =[
    path("",Home.as_view(),name="home"),
    path("update/",Update.as_view(),name="update")
]