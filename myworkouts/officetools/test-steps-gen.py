def prepareDataAPIFiletoFile():
    inputFileDetails = input("""Enter input file options:""")
    outputFileDetails = input("""Enter output file options:""")
    print ("""/**""")
    print(""" *Scenario: Test Case to validate the """,scenarioMap.get(scenarioOption),""" using Prepare Data api.""",)
    print(""" *\tPre-req:""")
    print(""" *\t\t1.Create source directory.""")
    print(""" *\t\t2.Create target directory.""" )
    if(len(inputFileDetails)>0):
        print(""" *\t\t3.Copy data file to source directory. File Options : """,inputFileDetails)
    else:
        print(""" *\t\t3.Copy data file to source directory. File Options : default""")
        print(""" *\t\t4.Create source file connection.""")
        print(""" *\t\t5.Create target file connection.""" )  
    print(""" *\t Steps:""")
    if(len(outputFileDetails)>0):
        outputFileDetails=  """Output File Options : """+outputFileDetails
    else:
        outputFileDetails=  """Output File Options : default"""
    if(len(inputFileDetails)>0):
        inputFileDetails ="""Input File Options : """+inputFileDetails
    else:
        inputFileDetails ="""Input File Options : default"""
    print(""" *\t\t1.Create data prep config.""")
    print(""" *\t\tConfig:""")
    print(""" *\t\t\t"""+inputFileDetails)
    print(""" *\t\t\t"""+outputFileDetails)
    print(""" *\t\t2.Submit the payload using prepare data api.""")
    print(""" *\t Expected Result:""")
    print(""" *\t\t1.Prepare Data API should return success.""")
    print(""" *\t\t2.File should be created in target directory.""")
    print(" */")

def executeAPIFiletoFile():
    inputFileDetails = input("""Enter input file options:""")
    outputFileDetails = input("""Enter output file options:""")
    transforms = input("""Enter trandform script details:""")
    print ("""/**""")
    print(""" *Scenario: Test Case to validate the """,scenarioMap.get(scenarioOption),""" using execute api.""",)
    print(""" *\tPre-req:""")
    print(""" *\t\t1.Create source directory.""")
    print(""" *\t\t2.Create target directory.""" )
    if(len(inputFileDetails)>0):
        print(""" *\t\t3.Copy data file to source directory. File Options : """,inputFileDetails)
    else:
        print(""" *\t\t3.Copy data file to source directory. File Options : default""")
        print(""" *\t\t4.Create source file connection.""")
        print(""" *\t\t5.Create target file connection.""" )  
    print(""" *\t Steps:""")
    if(len(outputFileDetails)>0):
        outputFileDetails=  """Output File Options : """+outputFileDetails
    else:
        outputFileDetails=  """Output File Options : default"""
    if(len(inputFileDetails)>0):
        inputFileDetails ="""Input File Options : """+inputFileDetails
    else:
        inputFileDetails ="""Input File Options : default"""
    print(""" *\t\t1.Create data prep config.""")
    print(""" *\t\tConfig:""")
    print(""" *\t\t\t"""+inputFileDetails)
    print(""" *\t\t\t"""+outputFileDetails)
    if (len(transforms) == 0):
	    print(""" *\t\t2.Submit the payload using execute api.""")
    else:
	    print(""" *\t\t2.Submit the payload with the transforms {0} using execute api.""".format(transforms))
    print(""" *\t Expected Result:""")
    print(""" *\t\t1.Execute API should return success.""")
    print(""" *\t\t2.File should be created in target directory.""")
    print(" */")


def prepareDataAPIOratoOra():
    sourceTableDetails = input("""Enter source db table details:""")
    print ("""/**""")
    print(""" *Scenario: Test Case to validate the """,scenarioMap.get(scenarioOption),""" using Prepare Data api.""",)
    print(""" *\tPre-req:""")
    print(""" *\t\t1.Create source db user schema.""")
    print(""" *\t\t2.Create target db user schema.""" )
    if(len(sourceTableDetails)>0):
        print(""" *\t\t3.Create source db table. Table details: """,sourceTableDetails)
    else:
        print(""" *\t\t3.Create source db table.""")
        print(""" *\t\t4.Create source db connection.""")
        print(""" *\t\t5.Create target db connection.""" )  
    print(""" *\t Steps:""")
    print(""" *\t\t1.Create data prep config.""")
    print(""" *\t\tConfig:""")
    print(""" *\t\t\tSource: DB Connection, DB Schema, Table""")
    print(""" *\t\t\tTarget: DB Connection, DB Schema, Table""")
    print(""" *\t\t2.Submit the payload using prepare data api.""")
    print(""" *\t Expected Result:""")
    print(""" *\t\t1.Prepare Data API should return success.""")
    print(""" *\t\t2.Target table should be created successfully.""")
    print(" */")

def executeAPIOratoOra():
    sourceTableDetails = input("""Enter input source table data details:""")
    transforms = input("""Enter trandform script details:""")
    print ("""/**""")
    print(""" *Scenario: Test Case to validate the """,scenarioMap.get(scenarioOption),""" using execute api.""",)
    print(""" *\tPre-req:""")
    print(""" *\t\t1.Create source db schema, assign privileges.""")
    print(""" *\t\t2.Create target db schema, assign privileges.""" )
    if(len(sourceTableDetails)>0):
        print(""" *\t\t3.Create source db table. Table details: """,sourceTableDetails)
    else:
        print(""" *\t\t3.Create source db table.""")
        print(""" *\t\t4.Create source db connection.""")
        print(""" *\t\t5.Create target db connection.""" )  
    print(""" *\t Steps:""")
    print(""" *\t\t1.Create data prep config.""")
    print(""" *\t\tConfig:""")
    print(""" *\t\t\tSource: DB Connection, DB Schema, Table""")
    print(""" *\t\t\tTarget: DB Connection, DB Schema, Table""")
    if (len(transforms) == 0):
	    print(""" *\t\t2.Submit the payload using execute api.""")
    else:
	    print(""" *\t\t2.Submit the payload with the transforms {0} using execute api.""".format(transforms))
    print(""" *\t Expected Result:""")
    print(""" *\t\t1.Execute API should return success.""")
    print(""" *\t\t2.Target table should be created successfully.""")
    print(" */")

def prepareDataAPIFiletoOra():
    inputFileDetails = input("""Enter input file options:""")
    print ("""/**""")
    print(""" *Scenario: Test Case to validate the """,scenarioMap.get(scenarioOption),""" using Prepare Data api.""",)
    print(""" *\tPre-req:""")
    print(""" *\t\t1.Create source directory.""")
    print(""" *\t\t2.Create target db user schema.""" )
    if(len(inputFileDetails)>0):
        print(""" *\t\t3.Copy data file to source directory. File Options : """,inputFileDetails)
    else:
        print(""" *\t\t3.Copy data file to source directory. File Options : default""")
        print(""" *\t\t4.Create source file connection.""")
        print(""" *\t\t5.Create target db connection.""" )  
    print(""" *\t Steps:""")
    if(len(inputFileDetails)>0):
        inputFileDetails ="""Input File Options : """+inputFileDetails
    else:
        inputFileDetails ="""Input File Options : default"""
    print(""" *\t\t1.Create data prep config.""")
    print(""" *\t\tConfig:""")
    print(""" *\t\t\tSelect file connection, directory, file name and file option:"""+inputFileDetails)
    print(""" *\t\t\tSelect target db connection, schema, target table""")
    print(""" *\t\t2.Submit the payload using prepare data api.""")
    print(""" *\t Expected Result:""")
    print(""" *\t\t1.Prepare Data API should return success.""")
    print(""" *\t\t2.Target table should be created successfully.""")
    print(" */")

def executeAPIFiletoOra():
    inputFileDetails = input("""Enter input file options:""")
    transforms = input("""Enter trandform script details:""")
    print ("""/**""")
    print(""" *Scenario: Test Case to validate the """,scenarioMap.get(scenarioOption),""" using execute api.""",)
    print(""" *\tPre-req:""")
    print(""" *\t\t1.Create source directory.""")
    print(""" *\t\t2.Create target db user schema. Assign privileges""" )
    if(len(inputFileDetails)>0):
        print(""" *\t\t3.Copy data file to source directory. File Options : """,inputFileDetails)
    else:
        print(""" *\t\t3.Copy data file to source directory. File Options : default""")
        print(""" *\t\t4.Create source file connection.""")
        print(""" *\t\t5.Create target db connection.""" )  
    print(""" *\t Steps:""")
    if(len(inputFileDetails)>0):
        inputFileDetails ="""Input File Options : """+inputFileDetails
    else:
        inputFileDetails ="""Input File Options : default"""
    print(""" *\t\t1.Create data prep config.""")
    print(""" *\t\tConfig:""")
    print(""" *\t\t\t Select file connection, directory and file name."""+inputFileDetails)
    print(""" *\t\t\t Select db conneciton, db schema and target table.""")
    if (len(transforms) == 0):
	    print(""" *\t\t2.Submit the payload using execute api.""")
    else:
	    print(""" *\t\t2.Submit the payload with the transforms {0} using execute api.""".format(transforms))
    print(""" *\t Expected Result:""")
    print(""" *\t\t1.Execute API should return success.""")
    print(""" *\t\t2.Target table should be created successfully.""")
    print(" */")


def prepareDataAPIOratoFile():
    sourceTableDetails = input("""Enter input source table data details:""")
    outputFileDetails = input("""Enter output file options:""")
    print ("""/**""")
    print(""" *Scenario: Test Case to validate the """,scenarioMap.get(scenarioOption),""" using Prepare Data api.""",)
    print(""" *\tPre-req:""")
    print(""" *\t\t1.Create source db. Assign privileges to the db""")
    print(""" *\t\t2.Create target directory.""" )
    if(len(sourceTableDetails)>0):
        print(""" *\t\t3.Create source db table. Data details : """,sourceTableDetails)
    else:
        print(""" *\t\t3.Create source db table.""")
        print(""" *\t\t4.Create source db connection.""")
        print(""" *\t\t5.Create target file connection.""" )  
    print(""" *\t Steps:""")
    if(len(outputFileDetails)>0):
        outputFileDetails=  """Output File Options : """+outputFileDetails
    else:
        outputFileDetails=  """Output File Options : default"""
    print(""" *\t\t1.Create data prep config.""")
    print(""" *\t\tConfig:""")
    print(""" *\t\t\tSelect db connection, db schema and db table.""")
    print(""" *\t\t\tSelect file connection, file directory and file name."""+outputFileDetails)
    print(""" *\t\t2.Submit the payload using prepare data api.""")
    print(""" *\t Expected Result:""")
    print(""" *\t\t1.Prepare Data API should return success.""")
    print(""" *\t\t2.File should be created in target directory.""")
    print(" */")

def executeAPIOratoFile():
    sourceTableDetails = input("""Enter input source table data details:""")
    outputFileDetails = input("""Enter output file options:""")
    transforms = input("""Enter trandform script details:""")
    print ("""/**""")
    print(""" *Scenario: Test Case to validate the """,scenarioMap.get(scenarioOption),""" using Prepare Data api.""",)
    print(""" *\tPre-req:""")
    print(""" *\t\t1.Create source db. Assign privileges to the db""")
    print(""" *\t\t2.Create target directory.""" )
    if(len(sourceTableDetails)>0):
        print(""" *\t\t3.Create source db table. Data details : """,sourceTableDetails)
    else:
        print(""" *\t\t3.Create source db table.""")
        print(""" *\t\t4.Create source db connection.""")
        print(""" *\t\t5.Create target file connection.""" )  
    print(""" *\t Steps:""")
    if(len(outputFileDetails)>0):
        outputFileDetails=  """Output File Options : """+outputFileDetails
    else:
        outputFileDetails=  """Output File Options : default"""
    print(""" *\t\t1.Create data prep config.""")
    print(""" *\t\tConfig:""")
    print(""" *\t\t\tSelect db connection, db schema and db table.""")
    print(""" *\t\t\tSelect file connection, file directory and file name."""+outputFileDetails)
    print(""" *\t\t2.Submit the payload with the transforms {0} using execute data api.""".format(transforms))
    print(""" *\t Expected Result:""")
    print(""" *\t\t1.Execute API should return success.""")
    print(""" *\t\t2.File should be created in target directory.""")
    print(" */")


#****************************************************************************************************************
print("""\t######################### Test Steps Generator #####################""")

scenarioMap ={1:'File To File',2:'Oracle to Oracle',3:"Oracle to File",4:"File to Oracle"}

for i in scenarioMap.keys():
    print("""\t""",i,""".""",scenarioMap.get(i))


scenarioOption = eval(input("""\n\tEnter the scenrio option:"""))

print("""\t\t Select API """)
print("""\t\t 1.Prepare Data""")
print("""\t\t 2.Execute Task""")

apiOptionValue = eval(input("Enter the api option:"))

if (scenarioOption == 1):
    if (apiOptionValue == 1):
        prepareDataAPIFiletoFile()
    elif(apiOptionValue == 2):
        executeAPIFiletoFile()
    else:
        print("API option number {0} is invalid. Please select right options".format(apiOptionValue))
elif (scenarioOption ==2):
    if (apiOptionValue == 1):
        prepareDataAPIOratoOra()
    elif(apiOptionValue == 2):
        executeAPIOratoOra()
    else:
        print("API option number {0} is invalid. Please select right options".format(apiOptionValue))
elif (scenarioOption ==3):
    if (apiOptionValue == 1):
        prepareDataAPIOratoFile()
    elif(apiOptionValue == 2):
        executeAPIOratoFile()
    else:
        print("API option number {0} is invalid. Please select right options".format(apiOptionValue))
elif(scenarioOption==4):
    if (apiOptionValue == 1):
        prepareDataAPIFiletoOra()
    elif(apiOptionValue == 2):
        executeAPIFiletoOra()
    else:
        print("API option number {0} is invalid. Please select right options".format(apiOptionValue))
else:
    pass

