age = "20"

print("My name is {}".format(age))

class Dog:
    dogInfo = "Hey dogs are so cool"

    def __init__(self, name="", age=0, furcolor=""):
        self.name = name
        self.age = age
        self.furcolor = furcolor

    def bark(self, str):
        print("Bark!!" + str)

mydog = Dog()
mydog = Dog("Fido","12","white")
mydog.bark("kawasaki")
print(mydog.name)
print(Dog.dogInfo)