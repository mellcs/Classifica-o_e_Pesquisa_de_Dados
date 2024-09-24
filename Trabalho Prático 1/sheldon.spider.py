import scrapy #importação da biblioteca scrapy

class SheldonSpider(scrapy.Spider):#criação da classe da spider sheldon, que representa o crawler
    name = 'sheldon_spider' #define o nome pra ele poder ser localizado e utilizado
    start_urls = ['https://www.gog.com/en/games/indie'] #define a página que o spider vai visitar e escanear
