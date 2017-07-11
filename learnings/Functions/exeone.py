# Modify this function to return a list of strings as defined above
def list_benefits():
    strings =[]
    strings.append("More organized code")
    strings.append("More readable code")
    strings.append("Easier code reuse")
    strings.append("Allowing programmers to share and connect code together")
    return strings


# Modify this function to concatenate to each benefit - " is a benefit of functions!"
def build_sentence(benefit):
    return benefit+" is a benefit of functions!"

def name_the_benefits_of_functions():
    list_of_benefits = list_benefits()
    for benefit in list_of_benefits:
        print(build_sentence(benefit))

name_the_benefits_of_functions()
