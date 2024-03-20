#  Teste de Proficiência

Os quesitos deste teste são:  
  
- Já teve contato com a biblioteca beautifulsoup?
  Sim. Já fiz uso.

- Se sim, poderia explicar seu funcionamento aplicado?
  A lib disponibiliza classes e metódos para analisar e extrair dados
  de documentos com liguaguagem de marcação. Ex: HTML, XML 
  
- Já teve contato com a biblioteca scrapy?
  Sim. Trabalhei com ela algumas vezes.

- Se sim, poderia explicar seu funcionamento aplicado?
    A Scrapy fornece uma estrutura para criação de classes que executam a função de coletar dados de páginas, os spiders. 
    Partindo de uma página inicial definida essa classe toma pra si a responsabilidade de coletar os dados e de navegar para
    outras páginas, repetindo o ciclo até que todos os dados sejam coletados.
    Durante a execução da coleta a lib redireciona os dados coletados para serem tratados em pipelines, classes que permitem
    um processamento pós coleta, geralmente usados para tratamento, limpeza e destinação final dos dados, que pode ser
    um arquivo .csv, .xls, um banco de dados relacional ou não, um armazenamento em nuvem e etc.
  

Aplicação de Teste: WebCrawler
Site: https://www.melodybrazil.com

Campos:
	[x] URL da Postagem
	[x] Titulo da Postagem
	[x] Data da Postagem
	[x] Autor da Postagem
	[x] URL para Download do CD
	
Formato: .xls
