import json
import boto3
from event_schema import event_schema
from json_schema  import json_schema

_SQS_CLIENT = None

def send_event_to_queue(event, queue_name):
    '''
     Responsável pelo envio do evento para uma fila
    :param event: Evento  (dict)
    :param queue_name: Nome da fila (str)
    :return: None
    '''
    
    sqs_client = boto3.client("sqs", region_name="us-east-1")
    response = sqs_client.get_queue_url(
        QueueName=queue_name
    )
    queue_url = response['QueueUrl']
    response = sqs_client.send_message(
        QueueUrl=queue_url,
        MessageBody=json.dumps(event)
    )
    print(f"Response status code: [{response['ResponseMetadata']['HTTPStatusCode']}]")



def handler(event):
    '''
    #  Função principal que é sensibilizada para cada evento
    Aqui você deve começar a implementar o seu código
    Você pode criar funções/classes à vontade
    Utilize a função send_event_to_queue para envio do evento para a fila,
        não é necessário alterá-la
    '''
    schema = json_schema()
    schema.carregar_json()
    raw_schema = schema.json_datatypes()

    
    raw_event = event_schema()
    schema_event = raw_event.evento_datatypes(event)


    if schema_event == raw_schema:
        send_event_to_queue(event,'valid-events-queue')
        print("O evento foi enviado para a fila.")
    else:
        print("O evento nao corresponde ao padrao do JSON schema.")


