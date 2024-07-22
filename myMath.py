### This will hold my math functions for this program

# rounds float type to integer
def round(floatType):
    numberString = str(floatType).split(".")
    integer = int(numberString[0])
    if int(numberString[1][0]) >= 5:
        integer += 1
    
    return integer