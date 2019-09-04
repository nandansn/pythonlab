'''
static variable - same across the objects


class_name.__dict__ to print the static variables

various places to declare static variable:
1. inside class, outside methid
2. inside constuctor, with class name, like class.static_var_name. it will be initiated, when the constructor is called.
3. inside instance method, with class name, like class.static_var_name
4. inside classmethod @classmethod, by using cls variable or class name.
5. inside static method, static method, without args or by using @staicmethod, using classname.
6. Outside the class, using class name.

accessing static variable,
1. inside constructor, using classname or self.
2. inside instance method , using classname or self.
3. inside class method, using classname or cls.
4. inside static method, using classname .
5. outside class, using classname or reference variable.

To modify statsi variable, you need to use class name, you cant user reference or self.



'''