from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

@app.route('/testdb')
def testdb():
    try:
        cnx = mysql.connector.connect(user='pocmysql',
                                      password='P0c@mysql123',
                                      host='azure-to-gcp-poc-mysql.mysql.database.azure.com',
                                      database='azure-to-gcp-poc-db')
        if cnx.is_connected():
            return jsonify(message='Connection to database successful')
        else:
            return jsonify(message='Connection to database failed'), 500
    except mysql.connector.Error as err:
        return jsonify(message='Error: {}'.format(err)), 500
    finally:
        cnx.close()

if __name__ == '__main__':
    app.run()

