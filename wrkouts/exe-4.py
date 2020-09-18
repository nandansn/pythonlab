message = "Hello {name},would you like to learn some Python today?"

name = input("Enter name:")

print(message.format(name=name))

print(message.format(name=name.lower()))

print(message.format(name=name.upper()))

print(message.format(name=name.title()))
