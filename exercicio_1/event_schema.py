import json

class event_schema:
    def evento_datatypes(self, event):
        try:
            coluna_evento_datatypes = {}
            for column, value in event.items():
                if column != "address":
                    coluna_evento_datatypes[column] = type(value)
                    continue
                for subcolumn, subvalue in value.items():
                    coluna_evento_datatypes[subcolumn] = type(subvalue)
            evento_datatype_dict = dict(sorted(coluna_evento_datatypes.items()))
            return evento_datatype_dict
        except Exception as e:
            raise RuntimeError("Erro ao ler o schema do arquivo.", str(e))
   