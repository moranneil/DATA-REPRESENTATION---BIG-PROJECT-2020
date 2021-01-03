from vehicleDAO import vehicleDAO

vehicle = {
    'reg':'11 D 127205',
    'manu_code':'TOY',
    'mileage':'334000',
    'price':'7000.00',
    'colour':'Black',
    'fuel':'diesel'
}

vehicle2 = {
    'reg':'11 D 127205',
    'manu_code':'FOR',
    'mileage':'334000',
    'price':'5500.00',
    'colour':'White',
    'fuel':'petrol'
}

vehicle3 = {
    'reg':'10 D 127205',
    'manu_code':'FOR',
    'mileage':'134000',
    'price':'8500.00',
    'colour':'red',
    'fuel':'Diesel'
}
# print("This is the value of vehicle:",vehicle)
# returnValue = vehicleDAO.create(vehicle)
# print(returnvalue)

returnValue =  vehicleDAO.getAll()

# print("\n\n=========================================\n\n")

print(returnValue)

returnValue =  vehicleDAO.findByReg(vehicle3['reg'])
print("Find By Reg")
print(returnValue)

returnValue =  vehicleDAO.update(vehicle3)
print(returnValue)

returnValue =  vehicleDAO.findByReg(vehicle3['reg'])
print(returnValue)

returnValue =  vehicleDAO.delete(vehicle2['reg'])
print(returnValue)


returnValue =  vehicleDAO.getAll()
print(returnValue)