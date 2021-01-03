from flask import Flask, url_for, request, redirect, abort, jsonify
from vehicleDAO import vehicleDAO

app = Flask(__name__, static_url_path='', static_folder='staticpages')


@app.route('/')
def index():
    return "hello"
#get all

@app.route('/vehicle')
def getAll():
    return jsonify([vehicleDAO.getAll()])

# find By Reg
@app.route('/vehicle/<string:reg>')
def findByReg(reg):
    return jsonify(vehicleDAO.findByReg(reg))

# create
# curl -X POST -d "{\"reg\":\"08MO1234\", \"manu_code\":\"FOR\", \"mileage\":23000, \"price\":1250.00, \"colour\":\"pink\", \"fuel\":\"petrol\"}" -H Content-Type:application/json http://127.0.0.1:5000/vehicle
@app.route('/vehicle', methods=['POST'])
def create():
    if not request.json:
        abort(400)
    
    vehicle = {
        "reg": request.json["reg"],
        "manu_code": request.json["manu_code"],
        "mileage": request.json["mileage"],
        "price": request.json["price"],
        "colour": request.json["colour"],
        "fuel": request.json["fuel"]
    }
    return jsonify(vehicleDAO.create(vehicle))


    # return "served by Create "

#update
# curl -X PUT -d "{\"Title\":\"new Title\", \"Price\":999}" -H "content-type:application/json" http://127.0.0.1:5000/books/1
@app.route('/vehicle/<string:reg>', methods=['PUT'])
def update(reg):
    foundVehicle = vehicleDAO.findByReg(reg)
    if len(foundVehicle) == {}:
        return jsonify({}), 404
    currentVehicle = foundVehicle
    # print("The vehicle found is :", currentVehicle)
    if 'reg' in request.json:
        currentVehicle['reg'] = request.json['reg']
    if 'manu_code' in request.json:
        currentVehicle['manu_code'] = request.json['manu_code']
    if 'mileage' in request.json:
        currentVehicle['mileage'] = request.json['mileage']
    if 'price' in request.json:
        currentVehicle['price'] = request.json['price']
    if 'colour' in request.json:
        currentVehicle['colour'] = request.json['colour']
    if 'fuel' in request.json:
        currentVehicle['fuel'] = request.json['fuel']
    
    vehicleDAO.update(currentVehicle)
    return jsonify(currentVehicle)

#delete
# curl -X DELETE http://127.0.0.1:5000/books/1
@app.route('/vehicle/<string:reg>', methods=['DELETE'])
def delete(reg):
    vehicleDAO.delete(reg)
    return jsonify({"done":True})


if __name__ == "__main__":
    app.run(debug=True)

