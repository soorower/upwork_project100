# -*- coding: utf-8 -*-
import scrapy


class GlassesSpider(scrapy.Spider):
    name = 'glasses'
    allowed_domains = ['www.glassesshop.com']
    start_urls = ['https://www.glassesshop.com/bestsellers']

    def parse(self, response):
        products = response.xpath(
            "//div[@class='row pt-lg-5 product-list column-1']/div")
        for product in products:
            yield {
                'product_url': product.xpath(".//div[@class='product-img-outer']/a/@href").get(),
                'img_url': product.xpath(".//img[@class='lazy d-block w-100 product-img-default']/@data-src").get(),
                'name': product.xpath("normalize-space(.//div[@class='p-title']/a/text())").get(),
                'prices': product.xpath(".//div[@class='col-6 col-lg-6'][2]/div[@class='p-price']/div/span/text()").get()
            }
        pagination = response.xpath(
            "//ul[@class='pagination']/li[position() = last()]/a/@href").get()

        if pagination:
            yield scrapy.Request(url=pagination, callback=self.parse)
