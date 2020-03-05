
from django.urls import path, include
import juhe.urls

# from django.conf.urls import handler403
urlpatterns = [
    path('jokes/', include(juhe.urls)),
]

