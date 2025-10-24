from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
    host="database-1.czi4uwuyaevt.eu-north-1.rds.amazonaws.com",
    user="admin",
    password="abcd1234",
    database="Mydatabase"
)
cursor = db.cursor()

@app.route('/')
def index():
    cursor.execute("SELECT * FROM contacts")
    users = cursor.fetchall()
    return render_template('index.html', users=users)

@app.route('/add', methods=['POST'])
def add():
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    cursor.execute("INSERT INTO contacts (name, email, phone) VALUES (%s, %s, %s)", (name, email, phone))
    db.commit()
    return redirect('/')

@app.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    cursor.execute("DELETE FROM contacts WHERE id = %s", (id,))
    db.commit()
    return redirect('/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

