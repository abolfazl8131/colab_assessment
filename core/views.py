import json

from django.http import JsonResponse
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

        df = pd.read_csv("core/data/ESG.csv")

        if ric_code not in df['code'].values:

            return Response({'error':'not found'}, 404)

        company_scores = pd.DataFrame(df[df.code == ric_code])

        data_dict = {'code':company_scores['code'],
                 'env':company_scores['enviromnent'],
                 'goverance':company_scores['goverance'],
                 'rank':company_scores['rank'],
                 'social':company_scores['social']}

        print(data_dict)
        return Response(data_dict, status=200)


