import scrapy
from scrapy.crawler import CrawlerProcess


stock = "TSLA"

class ResultItems(scrapy.Item):
    date = scrapy.Field()
    value = scrapy.Field()

class YChartScaper(scrapy.Spider):
    name = 'ycharts'

    def start_requests(self):
        stock = self.stock
        urls = [
            'https://ycharts.com/companies/'+ stock + '/stock_buyback'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):

        for row in response.xpath('//*[@id="dataTableBox"]/div[3]/div/div/table/tr'):
            item = ResultItems()
            item['date'] = row.css('td.col1::text').get()
            item['value'] = row.css('td.col2::text').re_first('[0-9A-Z.+-]+')
            yield item



def run_scraper(st,p):
    stock=st
    path=p
    process = CrawlerProcess(
        settings = {
        'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
        'FEED_FORMAT': 'csv',
        'FEED_URI': path + '/' + stock +'_buybacks.csv',
    })

    process.crawl(YChartScaper, stock=stock)
    process.start()


