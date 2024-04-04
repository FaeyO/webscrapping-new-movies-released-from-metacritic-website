import scrapy
from scrapy_selenium import SeleniumRequest


class AgentSpider(scrapy.Spider):
    name = "new"
    
    def start_requests(self):
        yield SeleniumRequest(
            url = "https://www.metacritic.com/movie/",
            wait_time = 5,
            callback = self.parse
        )

    def parse(self, response):
        movies = response.xpath("(//div[contains(@class, 'c-globalCarousel_content ')])[1]/div")
        print(len(movies))
        for movie in movies:
            relative_link = movie.xpath(".//a[contains(@class, 'c-globalProductCard_container ')]/@href").get()
            absolute_url = response.urljoin(relative_link)
            yield response.follow(url=absolute_url, callback=self.parse_agents, cb_kwargs={'absolute_url': absolute_url})

    def parse_agents(self, response,absolute_url):
        title = response.xpath("normalize-space(//div[contains(@class, 'c-productHero_title ')]/div/text())").get()
        release_date = response.xpath("(//span[@class='g-outer-spacing-left-medium-fluid'])[2]/text()").get()
        description = response.xpath("(//span[contains(@class , 'c-productDetails_description ')])[2]/text()").get()
        meta_score = response.xpath("//div[contains(@class , 'c-siteReviewScore ')]/span/text()").get()
        #image_link = response.xpath("//picture[@class ='c-cmsImage c-cmsImage-loaded']/img/@src").get()
        image_link = response.css("div.c-productHero_playerContainer.g-container-rounded-medium > div > picture > img::attr(src)").get()

    

        yield{
            'title' : title,
            'release_date' : release_date,
            'description' : description,
            'meta_score' : meta_score,
            'image_link' : image_link
        }




