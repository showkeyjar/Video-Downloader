# -*- coding: utf-8 -*-
import scrapy


class ToScrapeCSSSpider(scrapy.Spider):
    name = "videobot"
    start_urls = [
        'http://www.bilibili.com/',
    ]

    def parse(self, response):
        for quote in response.css("div.spread-module"):
            yield {
                'video': quote.css("a::attr(href)").extract()
            }
        next_page_url = response.css("ul.sub-nav > li > a::attr(href)").extract_first()
        if next_page_url is not None:
            yield scrapy.Request(response.urljoin(next_page_url))

