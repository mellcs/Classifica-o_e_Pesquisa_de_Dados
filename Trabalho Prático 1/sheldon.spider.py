import scrapy #importação da biblioteca scrapy

class SheldonSpider(scrapy.Spider):#criação da classe da spider sheldon, que representa o crawler
    name = 'sheldon_spider' #define o nome pra ele poder ser localizado e utilizado
    start_urls = ['https://www.gog.com/en/games/indie'] #define a página que o spider vai visitar e escanear

    def parse(self, response):
    #chamado quando o spider acessa o link acima. cria a lista para armazenar a info e pega só o que é relevante do site-
    #através do elemento CSS.
        produtos = []

        for jogo in response.css('a.product-tile'):
            titulo = jogo.css('div.product-tile__title::attr(title)').get()
            preco_atual = jogo.css('span.final-value::text').get()
            preco_antigo = jogo.css('span.base-value::text').get()

            if preco_atual:
                preco_atual = self.limpar_preco(preco_atual)
            if preco_antigo:
                preco_antigo = self.limpar_preco(preco_antigo)

            if titulo and preco_atual:
                produtos.append({
                    'titulo': titulo,
                    'preco_atual': preco_atual,
                    'preco_antigo': preco_antigo
                })

        if produtos:
            self.selection_sort(produtos)

            for produto in produtos:
                self.log(f"Produto: {produto['titulo']} - Preço Atual: {produto['preco_atual']} - Preço Antigo: {produto.get('preco_antigo', 'N/A')}")
        else:
            self.log("Nenhum produto encontrado.")

        return produtos

    def limpar_preco(self, preco): #converte o preço de como ele aparece no site para float e trata uma possível exceção
        preco = preco.replace('R$', '').replace('$', '').replace(',', '.').strip()
        try:
            return float(preco)
        except ValueError:
            return None

    def selection_sort(self, lista): 
        #implementa o selection sort, pegando o tamanho da lista, realizando trocas entre o elemento atual e o menor elemento,-
        #garantindo a ordem crescente de elementos.
        n = len(lista)
        for i in range(n):
            min_idx = i
            for j in range(i + 1, n):
                if lista[j]['preco_atual'] < lista[min_idx]['preco_atual']:
                    min_idx = j

            lista[i], lista[min_idx] = lista[min_idx], lista[i] #aqui ocorre a troca

