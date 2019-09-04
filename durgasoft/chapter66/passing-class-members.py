'''
passing memebers of once class to another class:
    1. refer:example -1
    2. Inner classes/Nested classes
        a class inside another class.
        when to go for inner class? 
            without existing one type of object, if there is no chance of existing another type of object.
                example, 
                    without engine object, car object can't exist.
                    refere example 2
            outer class memebers by default not available to inner class members

            Object creation methods:
                o= Outer()
                i=o.Inner()
                i.innerClassMethod()
                ----------------------
                i=Outer().Inner()
                i.innerClassMethod()
                ----------------------
                Outer().inner().innerClassMethod()


'''