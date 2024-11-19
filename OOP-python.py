# OOP exercises in Python #
###########################

# Make a Class
class Flower:

    # Constructor
    def __init__(self, name, color, petals): # name, color and petals are considered internal states
        self.name = name
        self.color = color
        self.petals = petals
    
    # Create method 
    def printflower(self):
        print(f"This is a {self.name} in the color {self.color} and has {self.petals} petals.")

    # Create method with internal state and parameter: This can change the attributes of the object within the method
    def addpetals(self, addedpetals):
        self.petals += addedpetals
        print(f"This is a {self.name} in the color {self.color} and has {self.petals} petals.")

    # Create method with returntype
    def changecolor(self, newcolor):
        self.color = newcolor
        return f"The flower has changed its color to {self.color}."
    
    # To return string
    def __str__(self):
        return f"{self.name}, {self.color}, {self.petals}"
    
# Make another Class
class Tree:
    def __init__(self, height):
        self.height = height

    # Create method that uses a complex object (flower) as parameter
    def hybrid(self, flow):
        print(f"This is a {flow.name} with color {flow.color} and {flow.petals} petals and a height of {self.height}.")
    
    def hybridversion(self):
        return Flower("lily", "purple", 8)


# Make an Object
flower = Flower("rose", "white", 4)
flower.printflower()
flower.addpetals(6)
newcolorflower = flower.changecolor("green")
print(newcolorflower)

# Create new Object 
tree = Tree(150)

# Call the method 
tree.hybrid(flower)

# Returntype complex object
morphed = tree.hybridversion()
print(morphed)


#######

# Has-a relation

# Class Motor 
class Motor:
    def __init__(self, type_motor, hp):
        self.type_motor = type_motor 
        self.hp = hp      

    def __str__(self):
        return f"{self.type_motor} motor met {self.hp} pk"

# Class Auto 
class Auto:
    def __init__(self, brand, color, speed, motor):
        self.brand = brand       
        self.color = color      
        self.speed = speed 
        self.motor = motor      

    def start_auto(self):
        print(f"The {self.brand} auto with a {self.motor} is turned on.")

    def increase_speed(self, increasement):
        # Verhoog de snelheid van de auto
        self.speed += increasement
        print(f"The speed of {self.brand} is now {self.speed} km/u.")

# Make object of class Motor
my_motor = Motor("benzine", 150)

# Make object of class Car with motor as parameter
my_car = Auto("Toyota", "red", 50, my_motor)

# Call methods of Car
my_car.start_auto()  
my_car.increase_speed(30)  



# Is-a relation

# Superklasse Voertuig (de algemene klasse)
class Voertuig:
    def __init__(self, merk, snelheid):
        self.merk = merk      # Merk van het voertuig
        self.snelheid = snelheid  # Snelheid van het voertuig

    def rijd(self):
        # Algemene methode om te rijden, kan overschreven worden door subklassen
        print(f"Het {self.merk} voertuig rijdt met {self.snelheid} km/u.")

# Subklasse Auto (is een type van Voertuig)
class Auto(Voertuig):
    def __init__(self, merk, snelheid, brandstof):
        super().__init__(merk, snelheid)  # Roep de constructor van de superklasse aan
        self.brandstof = brandstof  # Extra eigenschap voor Auto

    def rijd(self):
        # Overschrijf de rijd methode voor de Auto
        print(f"De {self.merk} auto rijdt met {self.snelheid} km/u en gebruikt {self.brandstof} als brandstof.")

# Subklasse Fiets (is een type van Voertuig)
class Fiets(Voertuig):
    def __init__(self, merk, snelheid):
        super().__init__(merk, snelheid)  # Roep de constructor van de superklasse aan

    def rijd(self):
        # Overschrijf de rijd methode voor de Fiets
        print(f"De {self.merk} fiets rijdt met {self.snelheid} km/u zonder brandstof.")

# Maak objecten van de subklassen
mijn_auto = Auto("Toyota", 120, "benzine")
mijn_fiets = Fiets("Giant", 25)

# Roep de rijd methode aan voor beide objecten
mijn_auto.rijd()  # De Auto gebruikt de overschreven methode
mijn_fiets.rijd()  # De Fiets gebruikt zijn eigen overschreven method