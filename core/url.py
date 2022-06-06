from django.contrib import admin
from django.urls import path

from core.views import GetCompanies, GetCompanyESG

urlpatterns = [
    path('corps/', GetCompanies.as_view()),
    path('esgscore/', GetCompanyESG.as_view()),
]
