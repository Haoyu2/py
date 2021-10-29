import sqlalchemy
print(sqlalchemy.__version__)
from sqlalchemy import create_engine, Column, Integer, String, MetaData, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///../db/foo.db', echo=True, connect_args={"check_same_thread":False})
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
Base = declarative_base()

class Blog(Base):
    __tablename__ = 'blogs'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    body = Column(String)

Base.metadata.create_all(engine)

metadata = MetaData(engine)
schema = list(range(5))
def createTable(schema:list, name:str)->Table :
        return Table(name, metadata, *[Column(str(i), String) for i in schema])
table = createTable(schema, 'DynamicExample')
metadata.create_all()

