"""
    El módulo abc es el módulo de la biblioteca estándar de Python que proporciona soporte
    para la creación de clases abstractas.
"""
from abc import ABC, abstractmethod


class TemplateInterface(ABC):
    """
        Plantilla para realizar operaciones de consulta de SQL y Consumo de Store Procedure
    """

    @abstractmethod
    def query_table(db_config, query):
        """
            Realizar un query cobre una tabla de base de datos
        Params:
            db_config: Parametros de conexion a la base de datos
            query: SQL a consultar
        Author: 
            wlopera
        Return:
            dict: Resultado del query
        """
        pass

    @abstractmethod
    def call_stored_procedure(db_config):
        """
            Consumir un Store Procedure de base de datos
        Params:         
            db_config: Parametros de conexion a la base de datos
            query: SQL a consultar
        Author: 
            wlopera
        Return:
            dict: Resultado del SP
        """
        pass
