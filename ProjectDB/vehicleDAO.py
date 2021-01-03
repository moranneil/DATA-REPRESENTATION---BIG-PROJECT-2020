import mysql.connector

class VehicleDAO:
    db = ""
    def __init__(self):
        self.db = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = 'root',
            auth_plugin="mysql_native_password",
            database="garage"
        )
    
    print("connection made")

    def create(self, vehicle):
        cursor = self.db.cursor()
        sql = "insert into vehicle (reg, manu_code, mileage, price, colour, fuel) values (%s,%s,%s,%s,%s,%s)"
        values = [
            vehicle['reg'],
            vehicle['manu_code'],
            vehicle['mileage'],
            vehicle['price'],
            vehicle['colour'],
            vehicle['fuel']          
        ]
        # print("The values are",values)
        cursor.execute(sql, values)
        self.db.commit()
        return cursor.lastrowid


    def getAll(self):
        cursor = self.db.cursor()
        sql = 'select * from vehicle'
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        # print("This is the RAW data",results)
        for result in results:
            resultAsDict = self.converttoDict(result)
            returnArray.append(resultAsDict)

        return returnArray
    
    def findByReg(self,reg):
        cursor = self.db.cursor()
        sql = 'select * from vehicle where reg = %s'
        values = [ reg ]
        cursor.execute(sql, values)
        result = cursor.fetchone()
        return self.converttoDict(result)

    def update(self, vehicle):
        cursor = self.db.cursor()
        sql = "update vehicle set manu_code = %s, mileage = %s, price = %s, colour = %s, fuel = %s where reg = %s"
        values = [
            vehicle['manu_code'],
            vehicle['mileage'],
            vehicle['price'],
            vehicle['colour'],
            vehicle['fuel'],          
            vehicle['reg']
        ]
        # print("The values are",values)
        cursor.execute(sql, values)
        self.db.commit()
        return vehicle

    def delete(self, reg):
        cursor = self.db.cursor()
        sql = 'delete from vehicle where reg = %s'
        values = [ reg ]
        print("The value of reg is :",values)
        cursor.execute(sql, values)
        self.db.commit()
        return {}



    def converttoDict(self, result):
        colnames = ['reg', 'manu_code', 'mileage', 'price', 'colour', 'fuel']
        vehicle = {}

        if result:
            for i , colName in enumerate(colnames):
                value = result[i]
                vehicle[colName] = value
        return vehicle

vehicleDAO = VehicleDAO()

