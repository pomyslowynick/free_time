print( "Hey %s there" % "you")
my_name = "Rafi R"
my_age = 23 #not a lie
my_height = 184
my_eyes = "Blue"
text = "Let's talk about {}."
"My name is {my_age}"
print(text.format(my_name))

print("Mary had a little lamb") # prints string
print("It's fleece was white as {}.".format("snow")) # prints tring and formats brackets inside
print("." * 10) #prints string of 10 dots

print(""" Type as smuch as
I want
boy it never
ends really""")
print("my name is ", my_name)
persian_cat = "I'm split\non \v line"
print(persian_cat)

#print("Your age?", end=' ')
#age = input()
#print("your height?", end=' ')
#height = input()
#print("Yer name?")
#name = input()

#from sys import argv

#script, first, third = argv
#print("The script is called:", input())
#print("Your first variable is:", first)
#print("Your third variable is:", third)

from sys import argv
script, user_name = argv
prompt = '>'

print("Hi {}, I'm the {} script".format(user_name, script))
