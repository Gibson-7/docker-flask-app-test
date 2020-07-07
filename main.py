from flask import Flask, jsonify, request

app = Flask(__name__)

from products import products

# Ruta de Prueba
@app.route('/ping')
def ping():
    return jsonify({"message": "Pong!"})

# GET: Solicitar todos los productos
@app.route('/products', methods=['GET'])
def getProducts():
    return jsonify({"products": products, "message": "Product's List"})

# GET: Solicitar un solo producto
@app.route('/products/<string:product_name>')
def getProduct(product_name):
    productsFound = [product for product in products if product['name'] == product_name]
    if (len(productsFound) > 0):
        return jsonify({"product": productsFound[0]})
    else:
        return jsonify({"message": "Product not found"})

# POST: Registrar un producto
@app.route("/products", methods=['POST'])
def addProduct():
    # print(request.json)
    newProduct = {
        "name" : request.json['name'],
        "price": request.json['price'],
        "stock": request.json['stock']
    }
    products.append(newProduct)
    return jsonify({"message": "Product Added Succesfully", "products": products})

# PUT: Actualizar una propiedad del producto
@app.route('/products/<string:product_name>', methods=['PUT'])
def editProduct(product_name):
    productsFound = [product for product in products if product['name'] == product_name] 
    if (len(productsFound) > 0):
        productsFound[0]['name']  = request.json['name']
        productsFound[0]['price'] = request.json['price']
        productsFound[0]['stock'] = request.json['stock']

        return jsonify({
            "message": "Product Update",
            "product": productsFound[0]
        })
    else:
        return jsonify({"message": "Product not found"})

# DELETE: Eliminar un producto
@app.route('/products/<string:product_name>', methods=['DELETE'])
def deleteProduct(product_name):
    productsFound = [product for product in products if product['name'] == product_name] 
    if (len(productsFound) > 0):
        products.remove(productsFound[0])
        return jsonify({
            "message": "Product Deleted",
            "products": products
        })
    else:
        return jsonify({"message": "Product not found"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)