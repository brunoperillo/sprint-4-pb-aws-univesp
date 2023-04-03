# Avaliação Sprint 4 - Programa de Bolsas Compass UOL / AWS e Univesp

Avaliação da quarta sprint do programa de bolsas Compass UOL para formação em machine learning para [AWS][aws].
A aplicação pode ser acessada clicando [aqui][aqui].
***

## Equipe
- **Irati Gonçalves Maffra**
- Adila Mota
- Marcos Zaparolli
- Viviane Alves

## Objetivo
Diponibilizar uma API própria que consome dados de uma API pública e retornar uma resposta ao usuário, sendo essa resposta armazenada no DynamoDB.

***

## Execução (Código Fonte)
##

**Criação da API**

Acesse o [CONSOLE][console] da AWS em serviços API Gateway, criar API e selecione a opção REST API para criar uma API pública. A API criada utilizando Python, consome os dados da API pública: https://api.pexels.com/v1/search
***

**Função Banco-Imagem**
Acesse o console da AWS em serviços Lambda, funções, criar função, defina um nome dentro da regra e selecione a linguagem Python.
https://github.com/Compass-pb-aws-2023-Univesp/sprint-4-pb-aws-univesp/tree/grupo-2/src/banco-imagem.py
Insira uma politica de permissão para acesso a S3.
```
https://us-east-1.console.aws.amazon.com/iam/home#/policies/arn:aws:iam::281498278862:policy/service-role/AWSLambdaLambdaFunctionDestinationExecutionRole-43571431-ac98-4ba6-b01d-73930fcb9ca2
```

**Função Sprint-4**
Acesse o console da AWS em serviços Lambda, funções, criar função, defina um nome dentro da regra e selecione a linguagem Python.
https://github.com/Compass-pb-aws-2023-Univesp/sprint-4-pb-aws-univesp/tree/grupo-2/src/Sprint-4.py
Insira uma politica de permissão para acesso a S3.
```
https://us-east-1.console.aws.amazon.com/iam/home#/policies/arn:aws:iam::281498278862:policy/service-role/AWSLambdaLambdaFunctionDestinationExecutionRole-0e5d10dc-9be1-415f-bca5-1950c020ab69
```

**Criação dos Buckets**
Acesse o console da AWS em serviços S3, Buckets, criar buckets, crie o nome de origem e seleciona a zona de disponibilidade utilizada no projeto. Repita os passos para criar o bucket de destino.
```
arn:aws:s3:::sprint-4-origem
arn:aws:s3:::sprint-4-destino
```
**Criação do Banco de Imagens**
Acesse o console da AWS em serviços DynamoDB, Tabelas, criar tabela, defina o nome e a chave de partição.
https://us-east-1.console.aws.amazon.com/dynamodbv2/home?region=us-east-1#tables

**Criação interação com usuário**
Utilizando JavaScript criado uma caixa de dialogo para busca de imagem, o usuário digita o nome da imagem e o código traz essa imagem da API pública do projeto e salva no banco de imagens criado no DynamoDB.



[aws]: <https://aws.amazon.com/pt/>
[aqui]: <http://127.0.0.1:5500/src/prompt.html>
[aws]: <https://aws.amazon.com/console>