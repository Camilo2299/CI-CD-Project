from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Lista para almacenar los gastos
gastos = []

# Lógica de negocio
def agregar_gasto_logic(gastos, descripcion, monto):
    gastos.append({'descripcion': descripcion, 'monto': monto})

def eliminar_gasto_logic(gastos, index):
    if 0 <= index < len(gastos):
        del gastos[index]

def obtener_lista_de_gastos():
    return gastos

# Rutas de Flask
@app.route('/')
def index():
    gastos = obtener_lista_de_gastos()
    return render_template('index.html', gastos=gastos)

@app.route('/agregar_gasto', methods=['GET', 'POST'])
def agregar_gasto():
    if request.method == 'POST':
        descripcion = request.form['descripcion']
        monto = float(request.form['monto'])
        agregar_gasto_logic(gastos, descripcion, monto)
        return redirect(url_for('index'))
    return render_template('agregar_gasto.html')

@app.route('/eliminar_gasto', methods=['POST'])
def eliminar_gasto():
    if request.method == 'POST':
        gasto_index = int(request.form['gasto_index'])
        eliminar_gasto_logic(gastos, gasto_index)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)