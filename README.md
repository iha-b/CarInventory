# CarInventory

## Overview

This project implements a car management system for a used car dealership using a Binary Search Tree (BST) data structure. The system manages cars by their make, model, year, and price, allowing for efficient organization and retrieval of car information.

## Features

- **Car Class**: Represents individual cars with attributes for make, model, year, and price. 
- **BST Structure**: Utilizes a binary search tree to manage car inventory, organized first by make, then by model.
- **Car Inventory Node**: Each node in the BST contains a list of cars with the same make and model, maintaining their insertion order.
- **Traversal Methods**: Supports in-order, pre-order, and post-order traversal of the car inventory.
- **Car Search**: Methods to check if a car exists in the inventory, and to retrieve the best and worst cars based on year and price.

## Files

This project is organized into the following files:

1. **Car.py**: Contains the definition of the `Car` class with methods for comparison and string representation.
2. **CarInventoryNode.py**: Defines the `CarInventoryNode` class, representing a node in the BST.
3. **CarInventory.py**: Implements the `CarInventory` class, managing the BST and providing methods for car operations.
4. **testFile.py**: Contains pytest functions to validate the functionality of the classes and methods.

#### Usage
You can create a CarInventory instance and add cars to the inventory like this:

```python
from Car import Car
from CarInventory import CarInventory

inventory = CarInventory()

car1 = Car("Nissan", "Leaf", 2018, 18000)
car2 = Car("Tesla", "Model3", 2018, 50000)
inventory.addCar(car1)
inventory.addCar(car2)

# Check for a car
exists = inventory.doesCarExist(car1)

# Get the best car by make and model
best_car = inventory.getBestCar("Nissan", "Leaf")
```

#### Example Output
The system provides the following outputs for different traversal methods:
- In-Order Traversal
```python
Make: FORD, Model: RANGER, Year: 2021, Price: $25000
Make: MERCEDES, Model: SPRINTER, Year: 2022, Price: $40000
Make: MERCEDES, Model: SPRINTER, Year: 2014, Price: $25000
Make: NISSAN, Model: LEAF, Year: 2018, Price: $18000
Make: TESLA, Model: MODEL3, Year: 2018, Price: $50000
```
#### Contributing
Feel free to submit issues or pull requests to enhance the project.

