from flask import Flask
from flask_mysqldb import MySQL
# codigo Para iniciar un servidor
app = Flask(__name__)
mysql = MySQL(app)

app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_DB'] = 'practica_flask'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/pepito")
def helloPepito():
    return "Hello, pepito!"

#respuesta para q lo vea el usuario tenga una respueta
@app.route('/usuarios')
def users():
    cur = mysql.connection.cursor()
    cur.execute('''SELECT usuarioscol FROM usuarios''')
    rv = cur.fetchall()
    return str(rv)

