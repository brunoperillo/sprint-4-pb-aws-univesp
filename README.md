# Avaliação Sprint 4 - Programa de Bolsas Compass UOL / AWS e Univesp

Avaliação da quarta sprint do programa de bolsas Compass UOL para formação em machine learning para AWS.

***

# Grupo-3

- [Bernardo Lima](https://github.com/belima93)
- [Bruno Perillo](https://github.com/brunoperillo)
- [Diego Lopes](https://github.com/Diegox0301)
- [Luiz Renato Sassi](https://github.com/luizrsassi)

## Objetivo

Criar uma API para consultar um banco de dados, caso não haja informação no banco de dados, consultar uma API publica 

## Introdução

As APIs são um conjunto de padrões que fazem parte de uma interface. As APIs permitem a criação de plataformas de maneira mais simples e prática para desenvolvedores. A partir de APIs, é possível criar softwares, aplicativos, programas e plataformas diversas. Por exemplo, apps desenvolvidos para celulares Android e iPhone (iOS) são criados a partir de padrões definidos e disponibilizados pelas APIs de cada sistema operacional.

## Execução do Projeto

Foi criada uma API para consultar o banco de dados AWS DynamoDB em busca da cotação de moedas, caso não seja possível encontrar a informação no banco a API faz a requisição da cotação na API Forex (https://rapidapi.com/pt/principalapis/api/currency-conversion-and-exchange-rates/) e salva a informação no DynamoDB

## Técnicas e tecnologias utilizadas

*	Visual Studio
*	Python
*	AWS DynamoDB
*	AWS Lambda
*	Postman

## Dificuldades conhecidas

* A pouca familiaridade com o ambiente da AWS Lambda e compreendimento das especificações necessárias para o uso correto.

