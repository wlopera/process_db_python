# Conexion y operaciones a la DB Oracle
import cx_Oracle
import json

from .template_interface import TemplateInterface
from util.service_utils import ServiceUtils


class OracleService(TemplateInterface):

    def query_table(self, db_config, query):

        try:
            # Establecer la conexión con la base de datos
            connection = cx_Oracle.connect(
                db_config['user'], db_config['password'], db_config['host'] + "/"+db_config['database'])

            print("Version[conectado]", connection.version)

            # Crear un cursor para ejecutar consultas
            cursor = connection.cursor()

            resp = cursor.execute(query)

            # con_wlopera@credicorpbank.com
            resp = cursor.fetchall()

            # # Nombres de los campos
            column_names = [desc[0] for desc in cursor.description]

            # # Crear una lista de diccionarios con el formato deseado (key, value)
            columns = [{"key": col, "value": col} for col in column_names]

            records = []
            # Convertir la lista de tuplas en una lista de diccionarios
            for record in resp:
                value = {f"{columns[index]['key']}": value
                         for index, value in enumerate(record)}
                records.append(value)

            response = {"columns": columns, "data": records}
            print("Response: ", response)

            cursor.close()
            connection.close()

            return ServiceUtils.success(response)
        except Exception as e:
            return ServiceUtils.error(e)

    def call_stored_procedure(self, db_config, procedure,  params):
        pass
        # try:
        #     # Configuración de la conexión a MySQL
        #     connection = mysql.connector.connect(**db_config)

        #     # Crea un cursor para interactuar con la base de datos
        #     cursor = connection.cursor(dictionary=True)

        #     valores_key = [param['value'] for param in params]

        #     # Solo los valores de los parametros
        #     args = list(valores_key)

        #     # Llamar al procedimiento almacenado
        #     result = cursor.callproc(procedure, args)

        #     has_out = False

        #     for param in params:
        #         if param['type'] == 'OUT':
        #             has_out = True
        #             break

        #     result_data = None

        #     response = {}

        #     if has_out:
        #         values = list(result.values())
        #         print("Values:", values)
        #         data = values[len(values)-1]
        #         result_data = json.loads(data)

        #         columns = [{"key": col, "value": col}
        #                    for col, value in result_data.items()]

        #         response = {"columns": columns, "data": [result_data]}
        #         print("Response: ", response)
        #     else:
        #         for result in cursor.stored_results():
        #             result_data = result.fetchall()

        #         keys_list = [list(item.keys()) for item in result_data]
        #         columns = [{"key": col, "value": col} for col in keys_list[0]]
        #         response = {"columns": columns, "data": result_data}
        #         print("Response: ", response)

        #     cursor.close()
        #     connection.close()

        #     return ServiceUtils.success(response)
        # except Exception as e:
        #     return ServiceUtils.error(e)
