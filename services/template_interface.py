"""
    El módulo abc es el módulo de la biblioteca estándar de Python que proporciona soporte
    para la creación de clases abstractas.
"""
from abc import ABC, abstractmethod


class TemplateInterface(ABC):
    """
        Plantilla para realizar operaciones de consulta de SQL y Consumo de Store Procedure
    """

    def __init__(self, mongo_db_connection, COLLECTION_NAME, clientMongoDB):
        self.mongo_db_connection = mongo_db_connection
        self.clientMongoDB = clientMongoDB
        self.collection = mongo_db_connection[COLLECTION_NAME]

    @abstractmethod
    def query_table(app, host, user, password, database, query):
        """
            Realizar un query cobre una tabla de base de datos
        Params:
            app: App principal
            host: Ip Servidor
            user: Uusario DB
            password: Clave DB
            database: Nombre DB
            query: SQL a consultar
        Author: 
            wlopera
        Return:
            dict: Resultado del query
        """
        pass
