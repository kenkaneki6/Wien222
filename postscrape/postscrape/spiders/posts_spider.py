import scrapy

class PostsSpider(scrapy.Spider):
    name ="crypto"

#start_urls = [
    #'https://www.coingecko.com'
#]
#def parse(self, response):
    #page = response.url.split('/')[-1]
    #filename = 'posts-%s.html' % page
    #with open(filename, 'wb') as f:
        #f.write(response.body)

    def start_requests(self):
        list = [
            "https://www.coingecko.com/en/coins/bitcoin",
            "https://www.coingecko.com/en/coins/ethereum",
            "https://www.coingecko.com/en/coins/tether"]

        for i in list:
            yield scrapy.Request(i, callback=self.parse)
            sleep(random.randint(0, 5))


    def parse(self, response):
        product_name = response.css('#pd-h1-cartridge::text')[0].extract()
        product_price = response.css(
            '.product-price .is-current, .product-price_total .is-current, .product-price_total ins, .product-price ins').css(
            '::text')[3].extract()

        name = str(product_name).strip()
        price = str(product_price).replace('\n', "")


yield data = {name, price}
extracted_data = []
while i < len(data):
    extracted_data.append()
    sleep(5)
f = open('data.json', 'w')
json.dump(extracted_data, f, indent=4)