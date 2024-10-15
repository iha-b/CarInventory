class Car:
    def __init__(self, make, model, year, price):
        self.make = make.upper()
        self.model = model.upper()
        self.year = year
        self.price = price
    
    def __gt__(self, rhs):
        if self.make != rhs.make:
            return self.make > rhs.make
        if self.model != rhs.model:
            return self.model > rhs.model
        if self.year != rhs.year:
            return self.year > rhs.year
        return self.price > rhs.price

    def __lt__(self, rhs):
        return not (self > rhs or self == rhs)

    def __eq__(self, rhs):
        return (self.make == rhs.make and
                self.model == rhs.model and
                self.year == rhs.year and
                self.price == rhs.price)

    def __str__(self):
        return "Make: {}, Model: {}, Year: {}, Price: ${}".format(self.make, self.model, self.year, self.price)


