# Avaliação Sprint 4 - Programa de Bolsas Compass UOL / AWS e Univesp

Avaliação da quarta Sprint do programa de bolsas Compass UOL para formação em machine learning para AWS.

***

## Grupo-4:

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

Assim elimina as tarefas de gerenciamento de servidores e transferi as responsabilidades operacionais à AWS, através da Lambda. 

<div>

 </div>

![eventoLambda](https://user-images.githubusercontent.com/88354075/229350680-7f873fa7-7057-4286-90f1-4a49c75580aa.png)



<div> 

</div>


*O que é Lambda?*

É um serviço de computação que permite executar código sem o provisonamento ou gerenciamento de servidores. 
O Lambda executa o código em uma infraestrutura de computação de alta disponibilidade e executa toda a administração dos recursos computacionais, incluindo manutenção do servidor e do sistema operacional, provisionamento e escalabilidade automática da capacidade e resgrito em log do código para praticamente qualquer tipo de aplicação ou serviço de backend. 
É necessário fornencer o código em uma das linguagens compatíveis com o Lambda.

***
## Descrição 

O projeto desenvolvindo iniciou com o arquivo em html para disponibilizar a consulta na API. 

Na sequência, o upload do código para AWS através da Lambda para executamos a partir de outros serviços. 

E para compartilhar entre o grupo foi criado subcontas para que todos pudessem acessar a funçao em Lambda. 

E para otimizar o tempo de execução do código foi escolhido o tamanho de mémoria ideal para a função.Também foi habilitado a simultaniedade provionada para manter as funções inicializadas e prontas para responder em questões de poucos milissegundos. 

***

## Passos para execução do projeto

1. Faça ulpdoad do código para o AWS Lambda ou escreva no editor de código do Lambda. 


2. Configure o código para ser executado a partir de outros serviços da AWS, como S3. 

3. Execute o código apenas quando acionado, usando apenas os recursos de computação necessários



### Ferramentas e Tecnologias Utilizadas

*[Visual Studio Code](https://code.visualstudio.com/)

*[AWS - Lambda](https://aws.amazon.com/pt/lambda/)

*[Python](https://python.org).

***

### Dificuldades conhecidas:

* Familiadade com AWS - Lambda


*******

Referências:

[Gustavo Pinoti - Desenvolvimento AWS 2020 com foco em Serverless](https://www.udemy.com/course/serverless-aws/)

***






























