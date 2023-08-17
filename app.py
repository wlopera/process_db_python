from flask import Flask, request

from flask_cors import CORS

import traceback

from services.mysql_service import MySqlService
from services.oracle_service import OracleService

try:

    app = Flask(__name__)
    app.secret_key = "wlopera_db"

    # Crea una instancia de la clase MySqlService
    mysql_service = MySqlService()
    oracle_service = OracleService()

    @app.route('/api/mysql/getTableByQuery', methods=['POST'])
    def get_mysql_table_by_query():
        global mysql_service

        param = request.get_json()

        query = param['query']

        db_config = {
            'host': param['host'],
            'user': param['user'],
            'password': param['password'],
            'database': param['database']
        }
        response = mysql_service.query_table(db_config, query)
        print("Response: ", response)

        # return make_response(jsonify({'error': 'Error interno del servidor'}), 500)
        return response

    @app.route('/api/oracle/getTableByQuery', methods=['POST'])
    def get_oracle_table_by_query():
        global oracle_service
        
        param = request.get_json()

        query = param['query']

        db_config = {
            'host': param['host'],
            'user': param['user'],
            'password': param['password'],
            'database': param['database']
        }
        response = oracle_service.query_table(db_config, query)
        print("Response: ", response)

        # return make_response(jsonify({'error': 'Error interno del servidor'}), 500)
        return response

    @app.route('/api/mysql/callSP', methods=['POST'])
    def call_mysql_sp():
        global mysql_service

        param = request.get_json()

        db_config = {
            'host': param['host'],
            'user': param['user'],
            'password': param['password'],
            'database': param['database']
        }
        procedure = param['procedure']
        params = param['params']

        response = mysql_service.call_stored_procedure(
            db_config, procedure, params)

        print("Response: ", response)

        # return make_response(jsonify({'error': 'Error interno del servidor'}), 500)
        return response

    CORS(app)

    if __name__ == '__main__':
        app.run(debug=True, port=5000)

except RuntimeError as e:
    print(f"Error en tiempo de ejecución: {e}")
    trace = traceback.format_exc()
    print(f"Error.........................: {trace}")
