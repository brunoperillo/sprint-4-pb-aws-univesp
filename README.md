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

![REPRESENTAÇÃO-SPRINT4](https://user-images.githubusercontent.com/81330043/229531860-500b4683-d830-4da6-9745-8604361e63ab.png)



## Introdução

As APIs são um conjunto de padrões que fazem parte de uma interface. As APIs permitem a criação de plataformas de maneira mais simples e prática para desenvolvedores. A partir de APIs, é possível criar softwares, aplicativos, programas e plataformas diversas. Por exemplo, apps desenvolvidos para celulares Android e iPhone (iOS) são criados a partir de padrões definidos e disponibilizados pelas APIs de cada sistema operacional.



## Execução do Projeto

Foi criada uma API (https://tvi6zcivij.execute-api.us-east-1.amazonaws.com/prod/dolarreal) para consultar o banco de dados AWS DynamoDB em busca da cotação de moedas, caso não seja possível encontrar a informação no banco a API faz a requisição da cotação na API Forex (https://rapidapi.com/pt/principalapis/api/currency-conversion-and-exchange-rates/) e salva a informação no DynamoDB, para futuras requisições sem a necessidade de consultar a API novamente

#### Resultado Teste

![REPRESENTAÇÃO2-SPRINT4](https://user-images.githubusercontent.com/81330043/229535163-c8d04fb4-1716-4873-a472-6c5c35cecca4.png)

## Técnicas e tecnologias utilizadas

*	Visual Studio
*	Python
*	AWS DynamoDB
*	AWS Lambda
*	Postman

## Dificuldades conhecidas

* A pouca familiaridade com o ambiente da AWS Lambda e compreendimento das especificações necessárias para o uso correto.

