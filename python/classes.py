class Cokkie:
    # The __init__ method is a special method in Python classes, known as the initializer or constructor.
    # It is automatically called when a new instance of the class is created.
    # It allows the class to initialize the attributes of the object.
    def __init__(self, color):
        # The 'self' parameter is a reference to the current instance of the class.
        # It is used to access variables and methods associated with the object.
        self.color = color  # This initializes the 'color' attribute of the object with the provided value.

    # This method returns the value of the 'color' attribute of the object.
    def get_color(self):
        return self.color
    
    # This method is supposed to set a new value for the 'color' attribute,
    # but there's a mistake in the implementation. 'color' is not defined in this method.
    def set_color(self, color):
        self.color = color  # This should assign the provided value to the 'color' attribute.

# Creating two instances of the Cokkie class with different colors.
cookie_one = Cokkie('green')
cookie_two = Cokkie('blue')

# Using the get_color method to retrieve and print the color of each cookie.
print('Cookie one is', cookie_one.get_color())  # Output: Cookie one is green
print('Cookie two is', cookie_two.get_color())  # Output: Cookie two is blue



"""
Why Use These Concepts?
Classes and Objects:

Classes provide a way to bundle data and functionality together. Creating objects (instances) from classes allows you to work with these bundles as separate entities.
In data structures and algorithms, classes can be used to represent complex data structures (e.g., linked lists, trees, graphs) and encapsulate related operations.
init Method:

The __init__ method initializes object attributes. This ensures that an object starts its life in a consistent state.
In DSA patterns, constructors can initialize the starting state of a data structure (e.g., initializing an empty list for a stack or queue).
self Keyword:

The self keyword is essential for accessing instance variables and methods. It differentiates between class-level variables and instance-level variables.
Understanding self is crucial for implementing methods that operate on specific instances of data structures.

"""
