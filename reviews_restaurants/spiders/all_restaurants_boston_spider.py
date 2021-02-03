import scrapy
import pandas as pd


class AllSpider(scrapy.Spider):
    name = "all"
    start_urls = [
        'https://www.tripadvisor.com/Restaurants-g60745-oa30-Boston_Massachusetts.html'
    ]

    def parse(self, response):
        pagination_links = response.css(
            "a[class*='next']::attr(href)")
        yield from response.follow_all(pagination_links, self.parse)

        restaurant_page_links = response.css(
            "div[data-test-target*='restaurants'] div[data-test*='item'] a[class*='_3tdrXOp7']::attr(href)")
        yield from response.follow_all(restaurant_page_links, self.parse_information)

    def parse_information(self, response):
        yield {
            'name_restaurant': response.css("h1[class*='header']::text").get(),
            'direction': response.css("a[href*='MAPVIEW']::text").get(),
            'amount_ratings': response.css("div[class*='title_text'] span[class*='count']::text").get(),
            'amount_ratings_excellent': response.css("div[class='choices']  div[data-value*='5']  span[class*='row_num']::text").get(),
            'amount_ratings_vgood': response.css("div[class='choices']  div[data-value*='4']  span[class*='row_num']::text").get(),
            'amount_ratings_average': response.css("div[class='choices']  div[data-value*='3']  span[class*='row_num']::text").get(),
            'amount_ratings_poor': response.css("div[class='choices']  div[data-value*='2']  span[class*='row_num']::text").get(),
            'amount_ratings_terrible': response.css("div[class='choices']  div[data-value*='1']  span[class*='row_num']::text").get(),
            'price_range': response.xpath("//span[contains(.//span, 'Restaurants in Boston')]/following-sibling::span/a[1]/text()").get(),
            'category_1': response.xpath("//span[contains(.//span, 'Restaurants in Boston')]/following-sibling::span/a[2]/text()").get(),
            'category_2': response.xpath("//span[contains(.//span, 'Restaurants in Boston')]/following-sibling::span/a[3]/text()").get(),
            'category_3': response.xpath("//span[contains(.//span, 'Restaurants in Boston')]/following-sibling::span/a[4]/text()").get()
        }
