from django.urls import path
from .views import Home,Update,History,HistoryDetail
app_name = "card"
urlpatterns =[
    path("", Home.as_view(), name="home"),
    path("update/", Update.as_view(), name="update"),
    path('history/', History.as_view(), name="history"),
    path("history/<int:id>/<str:token>/", HistoryDetail.as_view(), name="detail")
]