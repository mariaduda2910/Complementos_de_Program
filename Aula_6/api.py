from flask import Flask, jsonify, request, abort
import os
import sqlite3

app = Flask(__name__)


# Função para criar a tabela 'sensors' se ela não existir
def CriarTabela():
    conn = AbrirConexao()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS sensors (
            id_sensor INTEGER PRIMARY KEY AUTOINCREMENT,
            id_location INTEGER NOT NULL,
            name TEXT NOT NULL,
            unit TEXT NOT NULL
        )
    ''')
    conn.commit()
    cursor.close()
    conn.close()


# Função para abrir a conexão com o banco de dados
def AbrirConexao():
    base_de_dados = sqlite3.connect('sensors.db')
    base_de_dados.row_factory = sqlite3.Row
    return base_de_dados


# Função para conectar e buscar dados de sensores
def ConectarCursor():
    base_de_dados = AbrirConexao()
    cursor = base_de_dados.cursor()
    cursor.execute("SELECT * FROM sensors")
    tabelas = cursor.fetchall()

    table_data = [dict(tabela) for tabela in tabelas]

    cursor.close()
    base_de_dados.close()
    return table_data


# Função para manipular erros 404
@app.errorhandler(404)
def not_found(error):
    return jsonify({'Erro': 'Não encontrada'}), 404


# Rota para obter todos os sensores
@app.route('/iot/api/v1.0/bd/', methods=['GET'])
def get_data_base():
    table_data = ConectarCursor()
    return jsonify(table_data)


# Rota para obter um sensor específico pelo id
@app.route('/iot/api/v1.0/bd/<int:sensor_id>', methods=['GET'])
def get_id_data_base(sensor_id):
    conn = AbrirConexao()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM sensors WHERE id_sensor = ?", (sensor_id,))
    sensor = cursor.fetchone()

    if sensor is None:
        abort(404, description="Esse Sensor ID não existe na tabela.")

    sensor_data = dict(sensor)
    cursor.close()
    conn.close()

    return jsonify(sensor_data)


# Rota para adicionar um novo sensor
@app.route('/iot/api/v1.0/bd/', methods=['POST'])
def create_thing():
    if not request.json or 'name' not in request.json or 'unit' not in request.json:
        abort(400, description="Dados inválidos")

    # Adicionando um novo sensor
    sensor_data = {
        "id_location": request.json.get('id_location', 1),  # Exemplo: valor padrão para id_location
        "name": request.json['name'],
        "unit": request.json['unit']
    }

    conn = AbrirConexao()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO sensors (id_location, name, unit) VALUES (?, ?, ?)",
            (sensor_data["id_location"], sensor_data["name"], sensor_data["unit"])
        )
        conn.commit()

        sensor_data["id_sensor"] = cursor.lastrowid  # Obtém o último id inserido
    except sqlite3.Error as e:
        conn.rollback()
        return jsonify({"Erro no Banco de Dados": str(e)}), 500
    finally:
        cursor.close()
        conn.close()

    return jsonify(sensor_data), 201


# Rota para atualizar um sensor existente
@app.route('/iot/api/v1.0/bd/<int:sensor_id>', methods=['PUT'])
def update_sensor(sensor_id):
    if not request.json:
        abort(400, description="Requisição inválida - formato JSON esperado.")

    conn = AbrirConexao()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM sensors WHERE id_sensor = ?", (sensor_id,))
    sensor = cursor.fetchone()

    if sensor is None:
        abort(404, description="Sensor não encontrado.")

    # Atualizar os campos com os valores recebidos, mantendo os antigos se não forem fornecidos
    id_location = request.json.get('id_location', sensor['id_location'])
    name = request.json.get('name', sensor['name'])
    unit = request.json.get('unit', sensor['unit'])

    try:
        cursor.execute(
            "UPDATE sensors SET id_location = ?, name = ?, unit = ? WHERE id_sensor = ?",
            (id_location, name, unit, sensor_id)
        )
        conn.commit()
    except sqlite3.Error as e:
        conn.rollback()
        return jsonify({"Erro no Banco de Dados": str(e)}), 500
    finally:
        cursor.close()
        conn.close()

    updated_sensor = {
        "id_sensor": sensor_id,
        "id_location": id_location,
        "name": name,
        "unit": unit
    }

    return jsonify(updated_sensor), 200


@app.route('/iot/api/v1.0/bd/<int:sensor_id>', methods=['DELETE'])
def delete_sensor(sensor_id):

    conn = AbrirConexao()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM sensors WHERE id_sensor = ?", (sensor_id,))
    sensor = cursor.fetchone()

    if sensor is None:
        abort(404, description="sensor não encontrado")
    try:
        cursor.execute("DELETE FROM sensors WHERE id_sensor = ?",(sensor_id,))
        conn.commit()
    except sqlite3.Error as e:
        conn.rollback()
        return jsonify({"Erro no Banco de Dados": str(e)}), 500
    finally:
        cursor.close()
        conn.close()

    return "apagado com sucesso"


# Configurações de inicialização do servidor
if __name__ == '__main__':
    CriarTabela()
    app.debug = True
    host = os.environ.get('IP', '0.0.0.0')
    port = int(os.environ.get('PORT', 8080))
    app.run(host=host, port=port, debug=True)
