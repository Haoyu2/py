from sqlalchemy import MetaData, Table
from sqlalchemy.types import TypeEngine





# Schema Config Type

def create_table_from_config(metadata:MetaData, config:dict) ->None:
    pass


def create_table(name:str, metadata: MetaData, columns:list[TypeEngine]) -> None:
    return Table(name, metadata, *columns)
