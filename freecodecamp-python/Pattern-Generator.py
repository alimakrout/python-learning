def number_pattern(n) :
    if not isinstance(n,int) : 
        return "Argument must be an integer value."
    if n < 1 : 
        return "Argument must be an integer greater than 0."
    result = ""
    for n in range (1, n+1) : 
        result += str(n) + " "
        # strip() pour supp espaces en trop
    return result.strip() 
print (number_pattern(5))