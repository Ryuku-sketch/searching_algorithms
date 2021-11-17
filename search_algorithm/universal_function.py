
def getPassword():
    password = str(input("Enter a password"))
    return password
    

def listToString(lis):  
    convertToString = ""
    for lisComponent in lis:
        convertToString += lisComponent
    return convertToString
