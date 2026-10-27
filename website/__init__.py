import mysql.connector
from dotenv import load_dotenv
import os

from flask import Flask, render_template

def create_app():
	load_dotenv()
	db_name = os.environ.get('DB_NAME')

	app = Flask(__name__) # as for template folder, it looks for "templates" by default

	@app.route('/')
	def home():
		cnx = None
		try:
			cnx = mysql.connector.connect(
				host="localhost",
				port=3306,
				user="root",
				database=db_name
			)
		except Exception as e:
			print(f"Error connecting to database: {e}")

		result = "0"
		if cnx is not None:
			cur = cnx.cursor()
			try:
				cur.execute("SELECT COUNT(*) FROM users")
				row = cur.fetchone()
				if isinstance(row, tuple):
					result = row[0]
			except Exception as e:
				print(e)
			cnx.close()

		return render_template('index.html', no_of_users=result)

	@app.route('/login')
	def login():
		return "login page"

	@app.route('/register')
	def register():
		return "register page"

	return app