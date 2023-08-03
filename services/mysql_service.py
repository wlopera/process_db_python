# Conexion y operaciones a la DB MySql
from flaskext.mysql import MySQL

from .template_interface import TemplateInterface


class MySqlService(TemplateInterface):

    def __init__(self, app):
        self.mysql = MySQL()
        self.mysql.init_app(app)

    def query_table(self, app, host, user, password, database, query):
        app.config['MYSQL_DATABASE_HOST'] = host
        app.config['MYSQL_DATABASE_USER'] = user
        app.config['MYSQL_DATABASE_PASSWORD'] = password
        app.config['MYSQL_DATABASE_DB'] = database
        
        connection = self.mysql.connect()
        cursor = connection.cursor()

        # Ejecuta la consulta con los parámetros proporcionados
        cursor.execute(query)

        # Resultado de la consulta
        cursor_data = cursor.fetchall()

        # Nombres de los campos
        column_names = [desc[0] for desc in cursor.description]

        # Crear una lista de diccionarios con el formato deseado (key, value)
        columns = [{"key": col, "value": col} for col in column_names]

        records = []
        # Convertir la lista de tuplas en una lista de diccionarios
        for record in cursor_data:
            value = {f"{columns[i]['key']}": valor for i,
                     valor in enumerate(record)}
            records.append(value)

        response = {"columns": columns, "data": records}
        print("Response: ", response)

        cursor.close()
        connection.close()

        return response
