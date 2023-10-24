import json

class json_schema:
    def carregar_json(self) -> None:
        schema_obj = open("schema.json")
        self.json_obj = json.load(schema_obj)

    def json_datatypes(self) -> dict:
        try:
            schema_datatypes = self.json_obj["properties"]
            columns_datatypes = {}
            for column, value in schema_datatypes.items():
                if column != "address":
                    columns_datatypes[column] = str(type(value["examples"][0])).split("'")[1]
                    continue
                coluna_address = value["properties"]
                for subcolumn, subvalue in coluna_address.items():
                    columns_datatypes[subcolumn] = str(type(subvalue["examples"][0])).split("'")[1]
            return columns_datatypes
        except Exception as e:
            raise RuntimeError("O arquivo JSON é invalido",str(e))
    

