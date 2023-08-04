from flask import Flask, request

from flask_cors import CORS

import traceback

from services.mysql_service import MySqlService
from flask import Flask, jsonify, make_response

try:

    app = Flask(__name__)
    app.secret_key = "wlopera_mysql_db"

    # --------------------------- Funciones de BD

    # Crea una instancia de la clase MySqlService
    service = MySqlService(app)

    @app.route('/api/mysql/getTableByQuery', methods=['POST'])
    def get_table_by_query():
        param = request.get_json()
        host = param['host']
        user = param['user']
        password = param['password']
        database = param['database']
        query = param['query']

        response = service.query_table(
            app, host, user, password, database, query)

        print("Response: ", response)

        #return make_response(jsonify({'error': 'Error interno del servidor'}), 500)
        return response

    CORS(app)

    if __name__ == '__main__':
        app.run(debug=True, port=5000)

except RuntimeError as e:
    print(f"Error en tiempo de ejecución: {e}")
    trace = traceback.format_exc()
    print(f"Error.........................: {trace}")
