userInput = input("Enter Class:")

classNames=str(userInput).split(',')

for className in classNames:
    output = "echo \"<class name=\"\'\"" + className + "\"\'\"/>\" >> ${OUTPUT_FILE}"
    print(output)



