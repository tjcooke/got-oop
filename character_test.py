# sssssssssh, these aren't "real" tests.

from character import Character

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
# When I calle it, it should return "Hello, I am Arya Stark. I am awesome"

print(arya.greet())