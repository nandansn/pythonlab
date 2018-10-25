class Parent:
    def __init__(self):
        self.asset ="nanda"
        print("parent")

    def parentAsset(self):
        print(self.asset)
    
class Child(Parent):
    def __init__(self):
        Parent.__init__(self)
        self.new_asset="child"

c1 = Child()

print(c1.parentAsset())
print(c1.new_asset)