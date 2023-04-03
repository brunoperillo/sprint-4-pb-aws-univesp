# Avaliação [Sprint 4](https://github.com/Compass-pb-aws-2023-Univesp/sprint-4-pb-aws-univesp) - Programa de Bolsas Compass UOL / AWS e Univesp 

![](readme-images/logo1.png)

## Informações
<p align ="justify">Este projeto foi realizador por um grupo com quatro componentes, que desenvolveram o trabalho completo, mas tiveram responsabilidades específicas.</p>
##### Organização da equipe
|*Componentes* | *Responsabilidades específicas* |
|---|  ---|
|Luciene|API Gateway|
|Márcio|Código Python|
|Marcos|Código Python|
|O'Dhara|DynamoDB|


## Descrição do projeto proposto
<p align ="justify"> A proposta do projeto era a construção de uma API, que utilizasse uma API pública, usando uma função lambda em AWS Lambda para fazer consultas em uma API pública ou em um banco de dados e que fosse configurado uma AWS API GATEWAY para chamar as funções no Lambda e armazenar as consultas realizadas em DynamoDB.</p>


[![AWS](https://img.shields.io/badge/AWS-%23FF9900.svg?style=for-the-badge&logo=amazon-aws&logoColor=white)](https://aws.amazon.com/)



[![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&black&logo=python&logoColor=ffdd54&)](https://www.python.org/)

   
  

## Desenvolvimento do Projeto
O Projeto foi desenvolvido na plataforma da [AWS](https://aws.amazon.com/) com a linguagem [Python](https://www.python.org/), com a qual foi criada uma função que consulta uma API pública, a [viacep]('https://viacep.com.br/ws/{cep}/json/), ou o banco de dados, tabela do DynamoDB, que retorna informações relacionadas ao CEP, e uma API Gateway com o método GET, para conexão com a função Lambda.
  
- ### Arquitetura 
![](readme-images/arquitetura.png)

- #### Função Lambda
    * ###### Criar politica
      * Entre na página [IAM políticas](https://aws.amazon.com/pt/iam/?nc2=type_a) escolha ```Criar política``` e na aba ```JSON``` escreva o código JSON.

      ```json
        {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Sid": "VisualEditor0",
                "Effect": "Allow",
                "Action": "dynamodb:*",
                "Resource": "*"
            }
        ]
        }
      ```
      * Escolha ```Próximo: Tags``` e ```Próximo: Revisar```; 
      * Escolha o nome da política e coloque sua lambda;
      * Escolha ```Criar política```.
    * ###### Criar perfil
        * Entre na página IAM Funções;
        * Selecione ```Criar Funções``` selecione ```Serviço da AWS ``` , ```Lambda ``` e na caixa de pesquisa insira o nome da sua função e escolha ```próximo```;
        * Em detalhes do perfil para nome do perfil coloque o nome do seu perfil e escolha ```Criar perfil```.

    * ###### Criar função em Python
        * Crie a sua função em Pyhon na sua IDE e compacte a pasta (.zip);
        ```python
        
        
        
        ```
        *Encontre sua função Lambda AWS e faça upload do arquivo que contém a função.
    * ###### Testar funcionamento
    * Vá na aba ```Testar``` da sua função Python e crie um código JSON para testar o funcionamento da sua função.


 - #### REST API usando a API Gateway
    * ###### criar API
        * Entre na página da API Gateway e clique em ```Criar API```;
        * Entre as APIs escolha ```API REST``` e clique em construir; 
        * Em configurações, escreva o nome da API e escolha o Endpoint Type e clique em ```Criar API``` 

    * ###### criar recurso
        * Abra a sua API e clique e na aba recursos, selecione no diretório ```/consultacep``` e no botão ```Ações  ```  escolha o método GET e salve (✔ ).
     
    * ###### Método de criação
        * Clique no método GET e em tipo de integração escolha ``` Lambda Function```, região ```******```, o nome da sua função ``` Lambada****``` e clique em ```salvar```;
        * No botão ```Ações ``` escolha ```Deploy API```.

- #### Banco de Dados DynamoDB
    * ###### Criar tabela 
        * Abra a página [DynamoDB](https://aws.amazon.com/pt/dynamodb/) em tabelas e escolha ```Criar tabela``` em detalhes da tabela:
            * Em nome da tabela escolha sua tabela;
            * Para a  **Chave de partição**, insira  ```id``` e ```String```.
        * Escolha a configurações da sua tabela ou mantenha os padrões, e clique em ```Criar tabela```.

    * ###### Testar com API Gateway
        * Localize a sua API Gateway e na coluna Recursos, escolha o método ```GET ``` e no painel de execução, na caixa cliente e escolha ```Testar```;
        * No painel método de teste, escreva o JSON e escolha ```testar```, depois vá até sua tabela do DynomoDB e veja se estar funcionando;
        
              
               
- #### Deploy e Testes da API
    * ###### Deploy da API
        * Vá até a página da [API Gateway](https://aws.amazon.com/pt/api-gateway/);
        * Entre na sua API e clique em ```Ações``` e em ```Deploy API```;
        * Para Deployment stage,  escolha  ```Novo estágio``` e clique em ```Deploy```.

    * ###### Testar HTTP
        * No painel Stage Editor do estágio anterior clique na ```URL``` e veja se a saída era o esperado.

- ## Dificuldades apresentadas
    * Utilização da plataforma AWS (pouco intuitiva);
    * Relacionamento entre API Gateway, Função Lambda e DynamoDB.

---
- ## Conclusão
    * No final nossa API ficou assim 👉 [Nossa api]().