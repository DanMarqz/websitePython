# Importar librerias
from flask import Flask
from flask import render_template

# Archivo principal
app = Flask (__name__)

# Creamos las rutas
@app.route('/')
def home():
  return render_template('home.html')

@app.route('/about')
def about():
  return render_template('about.html')

@app.route('/contact')
def contact():
  return render_template('contact.html')

# Activamos el servidor
if __name__ == '__main__':
  app.run(debug=True)

