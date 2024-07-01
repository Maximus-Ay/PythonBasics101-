'''
    DICTIONARY COMPREHENSIONS
    => They are very easy way to create a dictionary using an expression.
    => They can replace loops and certain lambda functions.

    => They follow the formula: 
    dictionary = {key: expression for (key,value) in iterable}

    => You could also add an if conditional at the end of the dictionary comprehension.

    dictionary = {key: expression for (key,value) in iterable if conditional}

    you can add an if/else in the expression
    dictionary = {key: (if/else) for (key,value) in iterable}

'''

# Let's say dictioanry for chords in the C Major Scale and their corresponding numbers

pianoKeys = {1:"CM", 2:"Dm", 3:"Em", 4:"FM", 5:"GM", 6:"Am", 7:"Bdi"}
print(f"Piano Keys chords in the scale of C Major Scale: {pianoKeys}")

# Let's create a dictionary of all major chords and a dictionary of all minor chords

majorChords = {key: value for (key,value) in pianoKeys.items() if value.find("M") >= 0}
print(f"The major chords in the scale are : {majorChords}")

minorChords = {key: value for (key,value) in pianoKeys.items() if value.find("m") >= 0}

print(f"The minor chords in the scale are : {minorChords}")


# Let's make use of the if else

citiesTemperature = {"New York": 28, "Boston":20, "Minnesota": 45, "Wisconsin": 35, "New Jersey": 78}

#Let's create a dictionary comprehension that has the cities and states w
# whether they are warm or cold, depending on the temperature.

citiesTemperatureDescription = {key: ("WARM" if value >= 30 else "COLD") for (key,value) in citiesTemperature.items()}

print(citiesTemperatureDescription)


# if we don't want only WARM and COLD, and other conditions, we cannot use an if else conditional expressions
# So if we have more expression we can create a function.

# Let's say we have warm, hot and cold.

def checkTemp(value):
    if value >=70:
        return "HOT"
    elif value >=30 and value <=50:
        return "WARM"
    else:
        return "COLD"
    
citiesTemperatureDescription = {key: checkTemp(value) for (key,value) in citiesTemperature.items()}

print(citiesTemperatureDescription)
