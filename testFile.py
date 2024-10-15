from Car import Car
from CarInventoryNode import CarInventoryNode
from CarInventory import CarInventory


def test_Car():
    c1 = Car("bmw", "x1 suv", 2025, 41000)
    assert str(c1) == "Make: BMW, Model: X1 SUV, Year: 2025, Price: $41000"
    c2 = Car("Mercedes-Benz", "eqs Sedan", 2022, 100000)
    assert str(c2) == "Make: MERCEDES-BENZ, Model: EQS SEDAN, Year: 2022, Price: $100000"

def test_CarInventoryNode():
    car1 = Car("tesla", "model 3", 2017, 25000)
    car2 = Car("tesla", "model s", 2017, 75000)
    carNode = CarInventoryNode(car1)
    carNode.cars.append(car2)
    assert str(carNode) ==  ("Make: TESLA, Model: MODEL 3, Year: 2017, Price: $25000\n"
                            "Make: TESLA, Model: MODEL S, Year: 2017, Price: $75000\n")
    assert carNode.getLeft() == None
    assert carNode.getRight() == None

def test_CarInventory():
    bst = CarInventory()

    car1 = Car("Cadillac", "Escalade", 2024, 85000)
    car2 = Car("Cadillac", "Escalade", 2020, 60000)
    car3 = Car("Porsche", "Cayenne", 2019, 70000)
    car4 = Car("Rolls-Royce", "Phantom", 2020, 350000)
    car5 = Car("Bentley", "Flying Spur", 2024, 230000)
    car6 = Car("Bentley", "Flying Spur", 2024, 215000)
    car7 = Car("Maserati", "MC20", 2024, 240000)

    bst.addCar(car1)
    bst.addCar(car2)
    bst.addCar(car3)
    bst.addCar(car4)
    bst.addCar(car5)
    bst.addCar(car6)
    bst.addCar(car7)

    assert bst.getBestCar("Cadillac", "Escalade") == car1
    assert bst.getBestCar("Bentley", "Flying Spur") == car5
    assert bst.getBestCar("Bugatti", "Divo") == None
    assert bst.getWorstCar("Maserati", "MC20") == car7
    assert bst.getBestCar("Maserati", "MC20") == car7
    assert bst.getTotalInventoryPrice() == 1250000
    assert bst.doesCarExist(car5) == True

    assert bst.inOrder() == ("Make: BENTLEY, Model: FLYING SPUR, Year: 2024, Price: $230000\n"
                             "Make: BENTLEY, Model: FLYING SPUR, Year: 2024, Price: $215000\n"
                             "Make: CADILLAC, Model: ESCALADE, Year: 2024, Price: $85000\n"
                             "Make: CADILLAC, Model: ESCALADE, Year: 2020, Price: $60000\n"
                             "Make: MASERATI, Model: MC20, Year: 2024, Price: $240000\n"
                             "Make: PORSCHE, Model: CAYENNE, Year: 2019, Price: $70000\n"
                             "Make: ROLLS-ROYCE, Model: PHANTOM, Year: 2020, Price: $350000\n")
    assert bst.preOrder() == ("Make: CADILLAC, Model: ESCALADE, Year: 2024, Price: $85000\n"
                              "Make: CADILLAC, Model: ESCALADE, Year: 2020, Price: $60000\n"
                              "Make: BENTLEY, Model: FLYING SPUR, Year: 2024, Price: $230000\n"
                              "Make: BENTLEY, Model: FLYING SPUR, Year: 2024, Price: $215000\n"
                              "Make: PORSCHE, Model: CAYENNE, Year: 2019, Price: $70000\n"
                              "Make: MASERATI, Model: MC20, Year: 2024, Price: $240000\n"
                              "Make: ROLLS-ROYCE, Model: PHANTOM, Year: 2020, Price: $350000\n")
    assert bst.postOrder() == ("Make: BENTLEY, Model: FLYING SPUR, Year: 2024, Price: $230000\n"
                               "Make: BENTLEY, Model: FLYING SPUR, Year: 2024, Price: $215000\n"
                               "Make: MASERATI, Model: MC20, Year: 2024, Price: $240000\n"
                               "Make: ROLLS-ROYCE, Model: PHANTOM, Year: 2020, Price: $350000\n"
                               "Make: PORSCHE, Model: CAYENNE, Year: 2019, Price: $70000\n"
                               "Make: CADILLAC, Model: ESCALADE, Year: 2024, Price: $85000\n"
                               "Make: CADILLAC, Model: ESCALADE, Year: 2020, Price: $60000\n")
    bst2 = CarInventory()
    
