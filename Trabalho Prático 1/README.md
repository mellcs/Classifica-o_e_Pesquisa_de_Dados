<h1>Sheldon Spider - Scrapy Crawler para GOG</h1>

<p>Este projeto é um <strong>web scraper</strong> desenvolvido com <strong>Scrapy</strong> para coletar dados de jogos da página de <strong>jogos indie</strong> da GOG. Ele coleta informações como título e preço dos jogos e implementa uma ordenação:</p>

<ul>
  <li><strong>Ordenação Interna (na memória)</strong>, utilizando <strong>Selection Sort</strong>.</li>
</ul>

<h2>Funcionalidades</h2>

<ul>
  <li><strong>Coleta de Dados:</strong> Extrai títulos e preços de jogos da seção de jogos indie da GOG.</li>
  <li><strong>Ordenação Interna:</strong> Ordena os jogos pelo preço em ordem crescente, usando o algoritmo <strong>Selection Sort</strong>.</li>
</ul>

<h2>Pré-requisitos</h2>

<ul>
  <li><strong>Python 3.7+</strong></li>
  <li><strong>Scrapy</strong></li>
</ul>

<h2>Estrutura do Projeto</h2>

<pre><code>sheldon_spider/
├── projeto_segunda/
│   ├── __init__.py
│   ├── spiders/
│   │   └── sheldon_spider.py  # Spider principal
├── requirements.txt
└── README.md
</code></pre>

<h2>Como executar o projeto</h2>

<h3>Rodando o Spider e coletando dados</h3>

<ol>
  <li>Para rodar o spider e coletar os dados de jogos da GOG:
    <pre><code>scrapy crawl sheldon_spider -o produtos.json
    </code></pre>
    Isso irá coletar os jogos e salvar os dados em um arquivo <code>produtos.json</code>.
  </li>
</ol>

<h2>Explicação do Algoritmo de Ordenação</h2>

<h3>Ordenação Interna</h3>

<p>O spider utiliza <strong>Selection Sort</strong>, um algoritmo simples de ordenação. Cada vez que ele coleta um conjunto de produtos, ordena os dados diretamente na memória.</p>
