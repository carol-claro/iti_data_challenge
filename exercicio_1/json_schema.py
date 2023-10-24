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
                    columns_datatypes[column] = type(value["examples"][0])
                    continue
                coluna_address = value["properties"]
                for subcolumn, subvalue in coluna_address.items():
                    columns_datatypes[subcolumn] = type(subvalue["examples"][0])
            json_columns_datatype = dict(sorted(columns_datatypes.items()))
            return json_columns_datatype
        except Exception as e:
            raise RuntimeError("O arquivo JSON é invalido",str(e))
