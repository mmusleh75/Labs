# initialize a generator
from faker import Faker

fake = Faker()

print(fake.profile())

colors = [fake.color_name() for x in range(400)]
print(colors)
