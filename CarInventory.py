from Car import Car
from CarInventoryNode import CarInventoryNode

class CarInventory:
    def __init__(self):
        self.root = None

    def addCar(self, car):
        if self.root == None:
            self.root = CarInventoryNode(car)
        else:
            current = self.root
            parent = None
            while current is not None:
                parent = current
                if (car.make, car.model) < (current.getMake(), current.getModel()):
                    current = current.getLeft()
                elif (car.make, car.model) > (current.getMake(), current.getModel()):
                    current = current.getRight()
                else:
                    current.cars.append(car)
                    return
            
            newNode = CarInventoryNode(car)
            if (car.make, car.model) < (parent.getMake(), parent.getModel()):
                parent.setLeft(newNode)
            else:
                parent.setRight(newNode)
            newNode.setParent(parent)

    def doesCarExist(self, car):
        current = self.root
        while current != None:
            if (car.make, car.model) < (current.getMake(), current.getModel()):
                current = current.getLeft()
            elif (car.make, car.model) > (current.getMake(), current.getModel()):
                current = current.getRight()
            else:
                return car in current.cars
        return False

    def inOrder(self):
        output = ""
        stack = []
        current = self.root
        while current != None or stack:
            while current != None:
                stack.append(current)
                current = current.getLeft()
            current = stack.pop()
            for car in current.cars:
                output += "Make: {}, Model: {}, Year: {}, Price: ${}\n".format(car.make, car.model, car.year, car.price)
            current = current.getRight()
        return output

    def preOrder(self):
        output = ""
        stack = [self.root]
        while stack:
            current = stack.pop()
            for car in current.cars:
                output += "Make: {}, Model: {}, Year: {}, Price: ${}\n".format(car.make, car.model, car.year, car.price)
            if current.getRight() != None:
                stack.append(current.getRight())
            if current.getLeft() != None:
                stack.append(current.getLeft())
        return output

    def postOrder(self):
        output = ""
        stack = []
        current = self.root
        previous = None
        while stack or current != None:
            if current != None:
                stack.append(current)
                current = current.getLeft()
            else:
                peek_node = stack[-1]
                if peek_node.getRight() != None and previous != peek_node.getRight():
                    current = peek_node.getRight()
                else:
                    stack.pop()
                    for car in peek_node.cars:
                        output += "Make: {}, Model: {}, Year: {}, Price: ${}\n".format(car.make, car.model, car.year, car.price)
                    previous = peek_node
                    current = None
        return output

    def getBestCar(self, make, model):
        current = self.root
        while current is not None:
            if (make.upper(), model.upper()) < (current.getMake(), current.getModel()):
                current = current.getLeft()
            elif (make.upper(), model.upper()) > (current.getMake(), current.getModel()):
                current = current.getRight()
            else:
                if not current.cars:
                    return None
                best = current.cars[0]
                for car in current.cars[1:]:
                    if car.year > best.year or (car.year == best.year and car.price > best.price):
                        best = car
                return best
        return None

    def getWorstCar(self, make, model):
        current = self.root
        while current is not None:
            if (make.upper(), model.upper()) < (current.getMake(), current.getModel()):
                current = current.getLeft()
            elif (make.upper(), model.upper()) > (current.getMake(), current.getModel()):
                current = current.getRight()
            else:
                if not current.cars:
                    return None
                worst = current.cars[0]
                for car in current.cars[1:]:
                    if car.year < worst.year or (car.year == worst.year and car.price < worst.price):
                        worst = car
                return worst
        return None

    def getTotalInventoryPrice(self):
        total_price = 0
        stack = []
        current = self.root
        while current is not None or stack:
            while current is not None:
                stack.append(current)
                current = current.getLeft()
            current = stack.pop()
            total_price += sum(car.price for car in current.cars)
            current = current.getRight()
        return total_price



bst2 = CarInventory()
print(bst2.inOrder())
