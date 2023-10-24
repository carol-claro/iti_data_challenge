from json_schema import json_schema

_ATHENA_CLIENT = None

def create_hive_table_with_athena(query):
    '''
    Função necessária para criação da tabela HIVE na AWS
    :param query: Script SQL de Create Table (str)
    :return: None
    '''
    
    print(f"Query: {query}")
    _ATHENA_CLIENT.start_query_execution(
        QueryString=query,
        ResultConfiguration={
            'OutputLocation': f's3://iti-query-results/'
        }
    )

def handler():
    '''
    #  Função principal
    Aqui você deve começar a implementar o seu código
    Você pode criar funções/classes à vontade
    Utilize a função create_hive_table_with_athena para te auxiliar
        na criação da tabela HIVE, não é necessário alterá-la
    '''
    try:
        table_name = "tabela_teste"
        schema = json_schema()
        schema.carregar_json()
        field_types = schema.json_datatypes()  
        columns = []
        for field, data_type in field_types.items():
            columns.append(f"`{field}` {data_type}")

        query = f"""
        CREATE EXTERNAL TABLE IF NOT EXISTS {table_name} (
            {', '.join(columns)}
        )
        ROW FORMAT SERDE 'org.openx.data.jsonserde.JsonSerDe'
        LOCATION 's3://iti-query-results/'
        """
        create_hive_table_with_athena(query)
    except Exception as e:
        raise RuntimeError("O arquivo JSON é inválido", str(e))
