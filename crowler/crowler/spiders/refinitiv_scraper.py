from multiprocessing import Process

import scrapy
import json
import pandas as pd
from scrapy.crawler import CrawlerProcess


class DataScrapy(scrapy.Spider):
    name = 'ESG'
    start_urls = ['']
    def start_requests(self):
        df = pd.read_csv('D:\desktop\colab2\crowler\crowler\spiders\companyName\company_name.csv')
        for ric_code in df['ricCode'].values:

            yield scrapy.Request(f'https://www.refinitiv.com/bin/esg/esgsearchresult?ricCode={ric_code}',self.parse)



    def parse(self, response):

        filename = 'ESG.csv'
        f = open(filename,'wb')
        ric_code = response.request.url.split('=')[-1]

        df = pd.read_json(response.body)
        print(df)



class CompanyNameScrapy(scrapy.Spider):
    name = 'corps'
    start_urls = ['https://www.refinitiv.com/bin/esg/esgsearchsuggestions']

    def parse(self, response):

        self.filename = 'company.json'
        f = open(self.filename,'wb')
        f.write(response.body)












