# import scrapy
# import pandas as pd
# import time
#
# class LookFantasticSpider(scrapy.Spider):
#     name = "look"
#     allowed_domains = ["www.lookfantastic.com"]
#     start_urls = ['https://www.lookfantastic.com/health-beauty/face/skincare-products.list']
#
#     def parse(self, response):
#         for page_num in range(1, 100):
#             yield scrapy.Request(url=response.urljoin(f'?pageNumber={page_num}'), callback=self.parse_page)
#
#     def parse_page(self, response):
#         products = response.css('li.productListProducts_product')
#
#         for product in products:
#             product_link = product.css('a.productBlock_link::attr(href)').extract_first()
#             yield scrapy.Request(url=response.urljoin(product_link), callback=self.parse_product)
#
#         time.sleep(10)
#
#     def parse_product(self, response):
#         name = response.css('h1.productName_title::text').get()
#         price = response.css('p.productPrice_price::text').get()
#         ingredients = response.css('div#product-description-content-lg-7 div div p::text').get()
#
#         data = {'Name': [name], 'Price': [price], 'Ingredients': [ingredients]}
#         self.save_to_csv(data)
#
#     def save_to_csv(self, data):
#         csv_file_path = 'products_dt.csv'
#
#         try:
#             existing_df = pd.read_csv(csv_file_path)
#         except FileNotFoundError:
#             existing_df = pd.DataFrame(columns=['Name', 'Price', 'Ingredients'])
#
#         updated_df = pd.concat([existing_df, pd.DataFrame(data)], ignore_index=True)
#
#         updated_df.to_csv(csv_file_path, index=False)
#         self.log(f'Data successfully written to {csv_file_path}')




import scrapy
import pandas as pd
import time

class LookFantasticSpider(scrapy.Spider):
    name = "look"
    allowed_domains = ["www.lookfantastic.com"]
    start_urls = ['https://www.lookfantastic.com/health-beauty/face/skincare-products.list']

    def parse(self, response):
        for page_num in range(1, 115):
            yield scrapy.Request(url=response.urljoin(f'?pageNumber={page_num}'), callback=self.parse_page)

    def parse_page(self, response):
        products = response.css('li.productListProducts_product')

        for product in products:
            product_link = product.css('a.productBlock_link::attr(href)').extract_first()
            yield scrapy.Request(url=response.urljoin(product_link), callback=self.parse_product, meta={'product_link': product_link})

        time.sleep(10)

    def parse_product(self, response):
        name = response.css('h1.productName_title::text').get()
        price = response.css('p.productPrice_price::text').get().replace('\n',
                                                                         '').strip()  # remove newline characters and leading/trailing whitespaces
        ingredients = response.css('div#product-description-content-lg-7 div div p::text').get()
        product_link = response.meta.get('product_link')
        full_product_link = "https://www.lookfantastic.com" + product_link  # prepend the base url to the product link

        data = {'Name': name, 'Price': price, 'Ingredients': ingredients, 'Product_Link': full_product_link}
        self.save_to_csv(data)

    def save_to_csv(self, data):
        csv_file_path = 'product_dt.csv'

        try:
            existing_df = pd.read_csv(csv_file_path)
        except FileNotFoundError:
            existing_df = pd.DataFrame(columns=['Name', 'Price', 'Ingredients', 'Product_Link'])

        updated_df = pd.concat([existing_df, pd.DataFrame([data])], ignore_index=True)

        updated_df.to_csv(csv_file_path, index=False)
        self.log(f'Data successfully written to {csv_file_path}')