# Avaliação Sprint 4 - Programa de Bolsas Compass UOL / AWS e Univesp

Avaliação da quarta Sprint do programa de bolsas Compass UOL para formação em machine learning para AWS.

***

## Grupo 4

[Ana Vitoria Louro Navili ](https://github.com/anaVitoriaLouro)

[Barbara Haydee Presente](https://github.com/Barbarahayd)

[Carlos Roberto de Souza Camilo ](https://github.com/crobertocamilo)

[Kelly Patricia Lopes Silva](https://github.com/KellyPLSilva)

*****
### Objetivo 

Criar uma API em Python com acesso a banco de dados para otimizar o acesso a outra API pública.
******

## Introdução 

Disponibilizar uma arquitetura nativa em nuvem orientada a eventos e que permita criar e executar o serviço para rodar sem servidor.

Não existe um servidor online "ouvindo" nossas requisições, quando chega uma requisição, a AWS sobe uma máquina para processá-la e depois a encerra. 

O API Gateway fornece ferramentas para criar e documentar APIs da Web que roteiam solicitações HTTP para funções do Lambda. 

Assim elimina as tarefas de gerenciamento de servidores e transfere as responsabilidades operacionais à AWS, através da Lambda. 

<div>

 </div>

![funcaoLambda](https://user-images.githubusercontent.com/88354075/229517193-52064606-d7ef-4699-b984-de8bc4490bfc.png)

<div> 

</div>


*O que é Lambda?*

É um serviço de computação que permite executar código sem o provisonamento ou gerenciamento de servidores. 
O Lambda executa o código em uma infraestrutura de computação de alta disponibilidade e executa toda a administração dos recursos computacionais, incluindo manutenção do servidor e do sistema operacional, provisionamento e escalabilidade automática da capacidade e resgrito em log do código para praticamente qualquer tipo de aplicação ou serviço de backend. 
É necessário fornencer o código em uma das linguagens compatíveis com o Lambda.

*O que é S3?*

É um serviço de armazenamento de objetos que oferece escabilidade, disponibilidade de dados, segurança e performance. Como ele podemos armazenar e proteger qualquer quantidade de dados, aplicações nativas da nuvem e aplicações móveis. 


***
## Descrição 

O projeto desenvolvido iniciou com o arquivo em HTML para disponibilizar a consulta na API. 

Utilizamos a [API- Places](https://developers.google.com/maps/documentation/places/web-service?hl=pt-br) para fazer chamadas de API HTTP. 

O AWS API Gateway hospeda as solicitações e as respostas aos clientes.

Como a função Lambda contém a lógica de negócios para processar as chamadas de API recebida, e usa o S3 como um armazenamento. 


Na sequência, o upload do código para AWS através da Lambda para invocação síncrona, no qual a função processa o evento e retorna uma resposta no caso uma localidade.  

E para compartilhar entre o grupo foi criado subcontas para que todos pudessem acessar a funçao em Lambda. 

E para otimizar o tempo de execução do código foi escolhido o tamanho de mémoria ideal para a função.
Também foi habilitado a simultaniedade provicionada para manter as funções inicializadas e prontas para responder em questões de poucos milissegundos. 

Prototipo versão  1.0
<div>

 </div>


![image (2)](https://user-images.githubusercontent.com/88354075/229509227-265d4429-ffa1-421e-87d8-89617e557eb3.png)

<div> 

</div>



***

## Passos para execução do projeto

1. Faça upload do código para o AWS Lambda ou escreva no editor de código do Lambda. 

2. Configure o código para ser executado a partir de outros serviços da AWS, como S3. 

3. Execute o código apenas quando acionado, usando apenas os recursos de computação necessários



### Ferramentas e Tecnologias Utilizadas

*[Visual Studio Code](https://code.visualstudio.com/)

*[AWS - Lambda](https://aws.amazon.com/pt/lambda/)

*[Python](https://python.org).

***

### Dificuldades conhecidas:

* Familiadade com AWS - Lambda

* Dificuldade para conectar o HTML ao S3. 


*******

Referências:

[Aprofundamento na Categoria - sem servidor](https://aws.amazon.com/pt/getting-started/deep-dive-serverless/)

[Amazon S3](https://aws.amazon.com/pt/s3/)



[Gustavo Pinoti - Desenvolvimento AWS 2020 com foco em Serverless](https://www.udemy.com/course/serverless-aws/)

***






























