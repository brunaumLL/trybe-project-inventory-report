# Inventory Report

## Sobre o projeto:
- O projeto exige que seja implementado um gerador de relatórios que recebe arquivos com dados de um estoque e gera, de saída, um relatório acerca destes dados.
- Esses dados de estoque poderão ser obtidos de diversas formas, sendo elas: através da importação de um arquivo CSV, JSON ou XML.
- Além disso, o relatório final deverá ser gerável em duas versões: simples e completa.

## O que é de minha autoria:
- Os arquivos da pasta `inventory_report/`: `reports/simple_report.py`, `reports/complete_report.py`, `inventory/inventory.py`, todos os arquivos da pasta `importer/`, `inventory/inventory_iterator.py`, `inventory/inventory_refactor.py`, `main.py`
- Os arquivos de teste da pasta `tests/`: `product/test_product.py`, `product_report/test_product_report.py`, `product_report/test_product_report.py`, `report_decorator/test_report_decorator.py`

## Tecnologias utilizadas:
<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" /> <img src="https://img.shields.io/badge/-Pytest-fff?style=for-the-badge&logo=pytest" />

## Repositório original do projeto:
https://github.com/tryber/sd-019-b-inventory-report

<details>
  <summary>
    <strong>
      :newspaper_roll: Requisitos do projeto
    </strong>
  </summary>
 
*Nome* | *Avaliação*
--- | :---:
1 - Deve criar um teste para o novo produto com todos os atributos corretamente preenchidos | :heavy_check_mark:
2 - Criar um teste que garanta o retorno padrão de um objeto Product deve ser um relatório sobre ele | :heavy_check_mark:
3.1 - O método generate da classe SimpleReport deve retornar todas informações do relatório simples | :heavy_check_mark:
3.2 - O método generate da classe SimpleReport deve retornar o formato correto do relatório simples | :heavy_check_mark:
4 - O método generate da classe CompleteReport deve retornar todas informações do relatório completo | :heavy_check_mark:
5 - Ao importar um arquivo csv, deve retornar o relatórios simples ou o completo conforme solicitado | :heavy_check_mark:
6 - Ao importar um arquivo JSON, deve retornar o relatórios simples ou o completo conforme solicitado | :heavy_check_mark:
7 - Ao importar um arquivo XML, deve retornar o relatórios simples ou o completo conforme solicitado | :heavy_check_mark:
8 - As classes estratégicas CsvImporter, JsonImporter e CsvImporter devem retornar os dados dos produtos em uma lista | :heavy_check_mark:
9 - Deve criar um teste garantindo que retornar o relatório devidamente colorido | :heavy_check_mark:
10.1 - Será validado que a instancia de InventoryRefactor é iterável (Iterable) | :heavy_check_mark:
10.2 - Será validado que é possível iterar o primeiro item da lista usando csv | :heavy_check_mark:
10.3 - Será validado que é possível iterar o primeiro item da lista usando json | :heavy_check_mark:
10.4 - Será validado que é possível iterar o primeiro item da lista usando xml | :heavy_check_mark:
10.5 - Será validado que é possível receber duas fontes de dados sem sobrescrita | :heavy_check_mark:
10.6 - Será validado que não é possível enviar arquivo inválido | :heavy_check_mark:
11.1 - Será validado que o menu importa um arquivo csv e gera um report simples | :heavy_check_mark:
11.2 - Será validado que o menu importa um arquivo csv e gera um report completo | :heavy_check_mark:
11.3 - Será validado que o menu importa um arquivo json e gera um report simples | :heavy_check_mark:
11.4 - Será validado que o menu importa um arquivo json e gera um report completo | :heavy_check_mark:
11.5 - Será validado que o menu importa um arquivo xml e gera um report simples | :heavy_check_mark:
11.6 - Será validado que o menu importa um arquivo xml e gera um report completo | :heavy_check_mark:
11.7 - Será validado que enviar argumentos faltantes irá gerar um erro | :heavy_check_mark:
</details>
