# Conexion y operaciones a la DB MySql
import mysql.connector
import json

from .template_interface import TemplateInterface
from util.service_utils import ServiceUtils


class MySqlService(TemplateInterface):

    def query_table(self, db_config, query):

        try:
            # Configuración de la conexión a MySQL
            connection = mysql.connector.connect(**db_config)

            cursor = connection.cursor(dictionary=True)

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
                value = {f"{columns[i]['key']}": record[valor] for i,
                         valor in enumerate(record)}
                records.append(value)

            response = {"columns": columns, "data": records}
            print("Response: ", response)

            cursor.close()
            connection.close()

            return ServiceUtils.success(response)
        except Exception as e:
            return ServiceUtils.error(e)

    def call_stored_procedure(self, db_config, procedure,  params):
        try:
            # Configuración de la conexión a MySQL
            connection = mysql.connector.connect(**db_config)

            # Crea un cursor para interactuar con la base de datos
            cursor = connection.cursor(dictionary=True)

            valores_key = [param['value'] for param in params]

            # Solo los valores de los parametros
            args = list(valores_key)

            # Llamar al procedimiento almacenado
            result = cursor.callproc(procedure, args)

            has_out = False

            for param in params:
                if param['type'] == 'OUT':
                    has_out = True
                    break

            result_data = None

            response = {}

            if has_out:
                values = list(result.values())
                print("Values:", values)
                data = values[len(values)-1]
                result_data = json.loads(data)

                columns = [{"key": col, "value": col}
                           for col, value in result_data.items()]

                response = {"columns": columns, "data": [result_data]}
                print("Response: ", response)
            else:
                for result in cursor.stored_results():
                    result_data = result.fetchall()


                keys_list = [list(item.keys()) for item in result_data]
                columns = [{"key": col, "value": col} for col in keys_list[0]]
                response = {"columns": columns, "data": result_data}
                print("Response: ", response)

            cursor.close()
            connection.close()

            return ServiceUtils.success(response)
        except Exception as e:
            return ServiceUtils.error(e)

# {
#     "host": "localhost",
#     "user": "root",
#     "password": "",
#     "database": "site",
#     "procedure": "getBookById",
#     "params": [
#         {
#             "key": "bookId",
#             "value": 21,
#             "type": "IN"
#         }
#     ]
# }

# {
#     "host": "localhost",
#     "user": "root",
#     "password": "",
#     "database": "site",
#     "procedure": "books_sp",
#     "params": [
#         {
#             "key": "book_id",
#             "value": 30,
#             "type": "IN"
#         },
# 		{
#             "key": "result_book",
#             "value": null,
#             "type": "OUT"
#         }
#     ]
# }
