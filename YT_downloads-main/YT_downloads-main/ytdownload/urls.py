from django.urls import path
from ytdownload import views

urlpatterns = [
    path("home",views.home, name =  'home'),
    path("",views.en50, name =  'en50'),
    path("",views.aboutusv4, name =  'about-us-v4'),

    path("youtubemp3",views.youtubemp3, name =  'youtube-mp3'),
    path("linksubmit",views.submit, name ="submit"),
    path("<str:pixel>",views.download, name = "list"),
    path("",views.final, name = "final"),
]