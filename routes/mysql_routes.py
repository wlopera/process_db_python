from flask import Blueprint, request, jsonify
from flaskext.mysql import MySQL

mysql_routes = Blueprint('mysql_routes', __name__)
mysql = MySQL()

# Ruta para realizar la consulta
@mysql_routes.route('/consulta', methods=['POST'])
def realizar_consulta():
    try:
        data = request.json  # Datos enviados desde el frontend
        host = data.get('host')
        user = data.get('user')
        password = data.get('password')
        db = data.get('db')
        
        # Configurar la base de datos
        app.config['MYSQL_DATABASE_HOST'] = host
        app.config['MYSQL_DATABASE_USER'] = user
        app.config['MYSQL_DATABASE_PASSWORD'] = password
        app.config['MYSQL_DATABASE_DB'] = db
        mysql.init_app(app)
        
        consulta = data.get('consulta')
        
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(consulta)
        result = cursor.fetchall()
        cursor.close()
        conn.close()
        
        return jsonify(result), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
