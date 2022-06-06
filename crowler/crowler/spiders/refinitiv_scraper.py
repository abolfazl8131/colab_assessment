from multiprocessing import Process

import scrapy
import json
import pandas as pd
from scrapy.crawler import CrawlerProcess



class DataScrapy(scrapy.Spider):
    name = 'ESG'
    df = pd.DataFrame()
    user_agent = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"

    def start_requests(self):
        df = pd.read_csv('D:\desktop\colab2\crowler\crowler\spiders\companyName\company_name.csv')
        for ric_code in df['ricCode'].values:

            yield scrapy.Request(f'https://www.refinitiv.com/bin/esg/esgsearchresult?ricCode={ric_code}',self.parse)



    def parse(self, response):

        filename = 'ESG.csv'

        ric_code = response.request.url.split('=')[-1]
        json_ = json.loads(response.text)

        data_dict = {'code': ric_code,
                     'goverance':json_["esgScore"]['TR.GovernancePillar']['score'],
                     'social':json_["esgScore"]['TR.SocialPillar']['score'],
                     'enviromnent':json_["esgScore"]['TR.EnvironmentPillar']['score'],
                     'rank':json_["industryComparison"]['rank']}

        self.df = self.df.append(data_dict,ignore_index=True)
        yield self.df.to_csv(filename,index=False)




class CompanyNameScrapy(scrapy.Spider):
    name = 'corps'
    start_urls = ['https://www.refinitiv.com/bin/esg/esgsearchsuggestions']

    def parse(self, response):

        self.filename = 'company.json'
        f = open(self.filename,'wb')
        f.write(response.body)












