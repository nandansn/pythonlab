'''
Everything is an object,

    Class can contain attributes - variables.
    Class can contain actions - methods.

    If a function declared inside a class -- Method.

    Structure of class:
        class keyword need to use.
            some description about the class
            variables
            methods

            example:
                class Student:
                    Document String
                    
                    def f1(self,name,age):
                        self.name = name
                        self.age = age

    Variables: instance variable, static variable and local variable.

        Instance variable:
            declared/defined inside constructor or method, using self. self is not a keyword in python.

            self means reference variable to current object.

            self should be first parameter in constructor or instance methods.

        Constructor:
            method __init__()
            default constructor will be called, if no constructor defined.
            it will be executed, whenever we are creating object.
            not required to call explicitly.
            per object, constructor will be executed only once.
            purpose to declare and initialize instance variables

'''