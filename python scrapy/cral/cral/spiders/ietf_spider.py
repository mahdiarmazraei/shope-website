import scrapy



class IetfSpider(scrapy.Spider):
    name = "ietf"
    allowed_domains = ["bingx.com"]
    start_urls = ["https://bingx.com/en-us/CopyTrading/1056101083344502790/?apiIdentity=1131592145044774916&rankStatisticDays=30&list_id=popular&from=1&accountEnum=BINGX_SWAP_FUTURES"]

    def parse(self, response):
        # title = response.css('span.title::text').get()
        title = response.xpath('/html/body/div[1]/div/div/div[1]/div[2]/div/div[3]/div/div[2]/div[2]/div/table/tbody/tr[1]/td[3]/div/div/span/text()').get()
        return {"title": title}
    

