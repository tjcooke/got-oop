# sssssssssh, these aren't "real" tests.

from character import Character
from character import Hero

# Characters can be instantiated with name and avatar.

arya = Character("Arya Stark", "arya.png")
jon_snow = Character("Jon Snow", "jon.png")

print(arya.name, arya.avatar)
print(jon_snow.name, jon_snow.avatar)


# After adding 2 items to inventory
# length of inventory should == 2

arya.inventory.append('needle')
arya.inventory.append('mask')


print(len(arya.inventory))


# arya should have a `greet` method.
# When I call it, with w`arya.greet(jon)`` it should return "Hello, Jon Snow, I am Arya Stark. I am awesome"

print(arya.greet(jon_snow))

# arya should have a `greet` method.
# When I call it, with  `arya.greet()`it should return "Hello, I am Arya Stark. I am awesome"

print(arya.greet())

# I should be able to create a Hero instance
bronn = Hero("Bronn of the Blackwater", "bron.png")