#------------------LIBRERIAS-------------------#
from conexion import db, app
from models import Productos
from flask import render_template, request, redirect, url_for

#--------------------RUTAS--------------------#

## RUTA PRINCIPAL ##
@app.route('/')
def index():
    return render_template('index.html')

## RUTA P/ CARGAR PRODUCTOS ##
@app.route('/cargar_productos', methods=['GET','POST'])
def cargar_productos():
    if request.method == 'POST':
        nombre = request.form['nombre']
        cantidad = request.form['cantidad']
        precio = request.form['precio']
        print(f"Nombre: {nombre}, Cantidad: {cantidad}, Precio: {precio}")

        datos_productos = Productos(nombre, cantidad, precio)

        db.session.add(datos_productos)
        db.session.commit()

        return render_template('cargar_productos.html')
    
    return render_template('cargar_productos.html')

## RUTA P/ MOSTRAR LA LISTA DE PRODUCTOS
@app.route('/mostrar_productos', methods=['GET','POST'])
def mostrar_productos():
    lista_productos = Productos.query.all()

    return render_template('mostrar_productos.html',lista_productos=lista_productos)

#RUTA P/ ACTUALIZAR LOS DATOS DE UN PRODUCTO
@app.route('/actualizar_productos/<int:producto_id>', methods=['GET','POST'])
def actualizar(producto_id):
    producto_actualizado = Productos.query.get(producto_id)
    
    if request.method == 'POST':
        nombre = request.form['nombre']
        cantidad = request.form['cantidad']
        precio = request.form['precio']

        producto_actualizado.nombre = nombre
        producto_actualizado.cantidad = cantidad
        producto_actualizado.precio = precio

        db.session.commit()

        return redirect(url_for('mostrar_productos'))
    
    return render_template('actualizar_productos.html', producto_actualizado=producto_actualizado)

@app.route('/eliminar', methods = ['GET','POST'])
def eliminar():
    if request.method == 'POST':
        id = request.form['producto_id']

        eliminar_producto = Productos.query.filter_by(id=id).first()

        db.session.delete(eliminar_producto)
        db.session.commit()

        return redirect(url_for('mostrar_productos'))

### BREAKPOINT ###
if __name__ == '__main__':
    app.run(debug=True)