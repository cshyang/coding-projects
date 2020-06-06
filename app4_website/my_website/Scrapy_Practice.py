import scrapy


class ShopcluesSpider(scrapy.Spider):
    # name of the spider
    name = 'shopclues'

    # list of allowed domain
    allowed_domains = [
        'https://www.shopclues.com/mobiles-feature-phones.html?facet_brand%5b%5d=Rocktel&fsrc=facet_brand']
    # starting_url
    start_urls = [
        'https://www.shopclues.com/mobiles-feature-phones.html?facet_brand%5b%5d=Rocktel&fsrc=facet_brand']
    # location of csv file
    custom_settings = {
        'FEED_FORMAT': 'csv',                         # Used for pipeline 2
        'FEED_URI': 'quoteresult.csv'                 # Used for pipeline 2
    }

    def parse(self, response):
        # Extract product information
        titles = response.css('img::attr(title)').extract()
        prices = response.css('.p_price::text').extract()
        images = response.css('img::attr(data-img)').extract()
        discounts = response.css('.prd_discount::text').extract()

        for item in zip(titles, prices, images, discounts):
            scraped_info = {
                'title': item[0],
                'price': item[1],
                'image_urls': item[2],
                'discount': item[3]

            }
            yield scraped_info
