from .views import *
from django.urls import path, include

app_name = 'main'

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('resume/', ResumePageView.as_view(), name='resume'),
    path('portfolio/', PortfolioPageView.as_view(), name='portfolio'),
    path('contacts/', ContactsPageView.as_view(), name='contacts'),
]

