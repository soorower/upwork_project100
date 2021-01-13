# -*- coding: utf-8 -*-
import scrapy
from scrapy_selenium import SeleniumRequest

class ComputerdealsSpider(scrapy.Spider):
    name = 'computerdeals' #name of the spider
    

    def start_requests(self): # sending request to the url, you want to scrape
        yield SeleniumRequest (
            url = 'https://slickdeals.net/computer-deals/',
            wait_time = 3, # waiting 3 seconds to run next codes.It reduces possibility of getting banned
            callback = self.parse # sending data to parse class

        )
    def parse(self, response): # parsing the data by selecting their xpath selectors. 
        products = response.xpath("//ul[@class='dealTiles categoryGridDeals']/li")
        for product in products:
            yield {
                'name': product.xpath(".//a[@class='itemTitle bp-p-dealLink bp-c-link']/text()").get(),
                'product_link': product.xpath(".//a[@class='itemTitle bp-p-dealLink bp-c-link']/@href").get(),
                'goods_provider': product.xpath("normalize-space(.//span[@class='blueprint']/button/text())").get(),
                'price': product.xpath("normalize-space(.//div[@class='itemPrice  wide ']/text())").get()
            }
        
        next_page = response.xpath("//a[@data-role='next-page']/@href").get() #checking , if there any next page exist
        if next_page: #  sending request to next page
            absoulute_url = f"https://slickdeals.net{next_page}"
            yield SeleniumRequest(
                url = absoulute_url,
                wait_time= 3,
                callback=self.parse # getting response to parse class.
            )