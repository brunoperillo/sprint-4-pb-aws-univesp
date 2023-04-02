import boto3
import json
import os
import urllib3
from boto3.dynamodb.conditions import Key

# Variáveis de ambiente
tableName = os.environ["TABLE_NAME"]
KEY1 = os.environ["KEY1"]
VALUE1 = os.environ["VALUE1"]
KEY2 = os.environ["KEY2"]
VALUE2 = os.environ["VALUE2"]
API_URL = os.environ["API_URL"]

headers = {KEY1: VALUE1, KEY2: VALUE2}

# create the DynamoDB resource
dynamo = boto3.resource('dynamodb').Table(tableName)

# Insere os novos valores de cotação no banco
def inserir_cotacao(id, emMoeda, paraMoeda, cotacao, data):
    Item={
            'id': id,
            'emMoeda': emMoeda,
            'paraMoeda': paraMoeda,
            'cotacao': cotacao,
            'data': data
        }
    dynamo.put_item(Item=Item)
    return Item

# Consulta a cotaçao das moedas
def consultar_api(emMoeda, paraMoeda):
    http = urllib3.PoolManager()
    response = http.request("GET", API_URL, fields={"from": emMoeda,"to": paraMoeda, "amount":"1"}, headers=headers)
    resp_dict = json.loads(response.data.decode('utf-8'))
    data = resp_dict["date"]
    total = resp_dict["query"]["amount"]
    cotDolar = str(resp_dict["info"]["rate"])
    # id => <from><to><date>
    id = emMoeda + paraMoeda +  data
    # return id
    return inserir_cotacao(id, emMoeda, paraMoeda, cotDolar, data)

def handler(event, context):

    # Verifica se a cotação está no banco, se não irá buscá-la na api externa
    def ddb_read(x):
        id = x["Key"]["id"]
        temNoBanco = dynamo.query(KeyConditionExpression=Key('id').eq(id))
        if temNoBanco["Count"] > 0:
            return dynamo.get_item(**x)["Item"]
        else:
            emMoeda = id[:3]
            paraMoeda = id[3:6]
            return consultar_api(emMoeda, paraMoeda)
    
    # Apaga a cotação informada
    def ddb_delete(x):
        dynamo.delete_item(**x)
    
    # listar os dados dados armazenados no banco de dados
    def listar_dados(x):
        response = dynamo.scan()
        return response['Items']

    operation = event['operation']

    operations = {
        'read': ddb_read,
        'delete': ddb_delete,
        'list': listar_dados,
    }

    if operation in operations:
        return operations[operation](event.get('payload'))
    else:
        raise ValueError('Unrecognized operation "{}"'.format(operation))
