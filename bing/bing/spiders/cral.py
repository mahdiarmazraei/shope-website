import scrapy


class CralSpider(scrapy.Spider):
    name = "cral"
    allowed_domains = ["bingx.com"]
    start_urls = ["https://bingx.pro/en-us/CopyTrading/1045507772875231240/?apiIdentity=0&rankStatisticDays=30&list_id=popular&from=1&accountEnum=BINGX_FEATURE"]
    custom_settings = {
        'DOWNLOAD_DELAY': 5 # 2 seconds of delay
        }

    def parse(self, response):
        yield (response.xpath('//*[@id="__layout"]/div/div[1]/div[2]/div/div[1]/div/div/div[1]/div[1]/div[1]/span').get())
        
        



        