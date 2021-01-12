# -*- coding: utf-8 -*-
import scrapy
from scrapy_selenium import SeleniumRequest

class ComputerdealsSpider(scrapy.Spider):
    name = 'computerdeals'
    

    def start_requests(self):
        yield SeleniumRequest (
            url = 'https://slickdeals.net/computer-deals/',
            wait_time = 3,
            callback = self.parse

        )
    def parse(self, response):
        products = response.xpath("//ul[@class='dealTiles categoryGridDeals']/li")
        for product in products:
            yield {
                'name': product.xpath(".//a[@class='itemTitle bp-p-dealLink bp-c-link']/text()").get(),
                'product_link': product.xpath(".//a[@class='itemTitle bp-p-dealLink bp-c-link']/@href").get(),
                'goods_provider': product.xpath("normalize-space(.//span[@class='blueprint']/button/text())").get(),
                'price': product.xpath("normalize-space(.//div[@class='itemPrice  wide ']/text())").get()
            }
        
        next_page = response.xpath("//a[@data-role='next-page']/@href").get()
        if next_page:
            absoulute_url = f"https://slickdeals.net{next_page}"
            yield SeleniumRequest(
                url = absoulute_url,
                wait_time= 3,
                callback=self.parse
            )