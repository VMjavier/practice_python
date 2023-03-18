"""
print("hola mundo")
print(type(5))


# Variables en una sola linea
name, surname, age = "Javier", "Velasco", 35
print(name, surname, age)

#inputs
age = input("Cuál es tu edad? \n")
print(age)

#operators
x1 = float(input("Enter the first number: "))
x2 = float(input("Enter the second number: "))

print("the sum of the two numbers is: ", x1+x2)
print("the rest of the two number is: ", x1-x2)
print(x1*x2)
print(x1**x2)
print(x1/x2)
print(x1//x2)
print(x1%x2)
"""

"""
#operators compart
x1 = float(input("Enter the first number: "))
x2 = float(input("Enter the second number: "))
print(x1>x2)
print(x1<x2)
print(x1==x2)
print(x1>=x2)
print(x1<=x2)
print(x1!=x2)
"""

"""
#formateo
name, surname, age = "Javier", "Velasco", 35
print("My name is {} {}. I'm {} year old".format(name,surname, age))
print("My name is %s %s. I'm %d year old" %(name, surname, age))
print("My name is "+name+" "+surname+". I'm "+ str(age)+" year old")
print(f"My name is {name} {surname}. I'm {age} year old")



#string, optional "
multiline_string = '''I am a teacher math.
I'm from Pamplona - Colombia.'''
print(multiline_string)

#Concatenated
animal = ["Cat", "Dog", "Cow", "Donkey", "Alpaca"]
result = ' '.join(animal)
print(result)
result = ' - '.join(animal)
print(result)


#strip(): Removes all given characters starting from the beginning and end of the string
animal = "loscamareroslocos"
result = animal.strip("sol")
print(result)

#desempacar 
palabra = "key"
a1, a2, a3 = palabra
print(a1)
print(a3)
"""

#metodos con string
animal = "cabAllo"
print(animal)
print(animal.upper())
print(animal.capitalize())
print(animal.count("l"))
print(animal.lower())
print(animal.lower().isupper())

