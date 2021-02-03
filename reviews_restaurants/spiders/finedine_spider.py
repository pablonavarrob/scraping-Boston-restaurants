import scrapy
import pandas as pd


class FastFoodSpider(scrapy.Spider):
    name = "finedine"
    start_urls = [
        'https://www.tripadvisor.com/Restaurants-g60745-zfp10954-Boston_Massachusetts.html'
    ]

    def parse(self, response):
        pagination_links = response.css(
            "a[class*='next']::attr(href)")
        yield from response.follow_all(pagination_links, self.parse)

        restaurant_page_links = response.xpath(
            "//a[contains(@href, 'Review') and not(.//*[contains(@button, '')])]/@href")
        yield from response.follow_all(restaurant_page_links, self.parse_information)

    def parse_information(self, response):
        yield {
            'name_restaurant': response.css("h1[class*='header']::text").get(),
            'direction': response.css("a[href*='MAPVIEW']::text").get(),
            'amount_ratings': response.css("div[class*='title_text'] span[class*='count']::text").get(),
            # 'average_rating': response.css("div[class='ui_columns'] h2 ~ div span::text").get(),
            'amount_ratings_excellent': response.css("div[class='choices']  div[data-value*='5']  span[class*='row_num']::text").get(),
            'amount_ratings_vgood': response.css("div[class='choices']  div[data-value*='4']  span[class*='row_num']::text").get(),
            'amount_ratings_average': response.css("div[class='choices']  div[data-value*='3']  span[class*='row_num']::text").get(),
            'amount_ratings_poor': response.css("div[class='choices']  div[data-value*='2']  span[class*='row_num']::text").get(),
            'amount_ratings_terrible': response.css("div[class='choices']  div[data-value*='1']  span[class*='row_num']::text").get()
        }
