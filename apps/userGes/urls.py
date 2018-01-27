from django.urls import path

from apps.userGes.views import indexView

urlpatterns = [
    path(r'', indexView.as_view(), name='index'),

]
