from django.shortcuts import render

# Create your views here.
from rest_framework.generics import *
from rest_framework.response import Response
from rest_framework.views import APIView
import pandas as pd
import os
class GetCompanies(APIView):
    def get(self, format = None):

        df = pd.read_csv("core/data/company_name.csv")
        return Response(df['companyName'])



class GetCompanyESG(APIView):
    def get(self,format = None):
        ric_code = self.request.GET.get('ric_code')
        df = pd.read_csv("core/data/company_name.csv")
        my_df = None
        if ric_code not in df['ricCode'].values:

            return Response('not found')
        c_name = df[df.ricCode == ric_code].companyName

