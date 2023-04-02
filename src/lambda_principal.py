import boto3
import json
from external_api import searchPlace
from decimal import Decimal
import logging 
logger = logging.getLogger()
logger.setLevel(logging.INFO)

#Associa a tabela 'Locais' do DynamoDB
dynamodbTableName = 'Locais'
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(dynamodbTableName)


getMethod = 'GET'
postMethod = 'POST'
""" postMethod = 'POST'
patchMethod = 'PATCH'
deleteMethod = 'DELETE' """
statusPath = '/status'
rootPath = '/'


def lambda_handler(event, contest):

    logger.info(event)
    httpMethod = event['httpMethod']
    path = event['path']

    if httpMethod == getMethod and path == statusPath:
        #response = buildResponse(200)
        response = buildResponse(200, 'A API está online')
    elif httpMethod == getMethod and path == rootPath:
        #response = buildResponse(200, 'Você está na raiz.')
        response = getLocalidade(event['queryStringParameters']['localidade'])
    else:
        response = buildResponse(404, 'Página não encontrada.')

    return response


def getLocalidade(localidade):
    try:
        #Pesquisa a localidade na tabela da banco de dados
        response = table.get_item(
            Key={
                'localidade': localidade.upper()
            }
        )
        
        #Se for encontrado no BD, retorna o registro salvo
        if 'Item' in response:
            
            Item = response['Item']
            Item['latitude'] = float(Item['latitude'])
            Item['longitude'] = float(Item['longitude'])
            
            print('Registro encontrado no banco de dados.')
            return buildResponse(200, Item)
        
        else:
            
            #Se não registro no BD, solicita uma pesquisa na API externa
            novo_local = searchPlace(localidade)
            
            if novo_local == None:
                return buildResponse(404, {'Message': 'Localidade NÃO ENCONTRADA. Especifique melhor a sua pesquisa e tente novamente.'})
            
            else:
                novo_Item = {
                    "localidade": localidade,
                    "endereco": novo_local[0],
                    "latitude": novo_local[1],
                    "longitude": novo_local[2]
                }
    
                print(novo_Item)

                #Formata o novo item no padrão exigido e salva na tabela
                formatted_new_Item = {
                    "localidade": localidade.upper(),
                    "endereco": novo_local[0],
                    "latitude": Decimal(str(novo_local[1])),
                    "longitude": Decimal(str(novo_local[2]))
                }

                table.put_item(Item = formatted_new_Item)
                
                return buildResponse(200, novo_Item)
                
    except:
        logger.exception('Log it here for now')



def buildResponse(statusCode, body=None):
    response = {
        'statusCode': statusCode,
        'headers': {
            'ContentType': 'application/json',
            'Access-Control-Allow-Origin': '*'
        }
    }
    if body is not None:
        response['body'] = json.dumps(body, ensure_ascii=False)

    return response
