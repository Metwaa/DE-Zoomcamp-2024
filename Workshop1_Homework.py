#Question 1
def square_root_generator(limit):
    n = 1
    while n <= limit:
        yield n ** 0.5
        n += 1

# Example usage:
limit = 5
generator = square_root_generator(limit)

x=0
for sqrt_value in generator:
    x += sqrt_value
    print(sqrt_value)
    
print(x)
#########################################################
#Question 2
def square_root_generator(limit):
    n = 1
    while n <= limit:
        yield n ** 0.5
        n += 1

# Example usage:
limit = 13
generator = square_root_generator(limit)

x=0
for sqrt_value in generator:
    x += sqrt_value
    print(sqrt_value)
    
print(x)
#########################################################
#Question 3
list =[];
def people_1():
    for i in range(1, 6):
        yield {"ID": i, "Name": f"Person_{i}", "Age": 25 + i, "City": "City_A"}

for person in people_1():
    list.append(person.get("Age"))
    print(person)

def people_2():
    for i in range(3, 9):
        yield {"ID": i, "Name": f"Person_{i}", "Age": 30 + i, "City": "City_B", "Occupation": f"Job_{i}"}


for person in people_2():
    list.append(person.get("Age"))
    print(person)

print(list)
print(sum(list))
#########################################################
# to do: homework :)
list = []
def people_1():
    for i in range(1, 6):
        yield {"ID": i, "Name": f"Person_{i}", "Age": 25 + i, "City": "City_A"}

def people_2():
    for i in range(3, 9):
        yield {"ID": i, "Name": f"Person_{i}", "Age": 30 + i, "City": "City_B", "Occupation": f"Job_{i}"}

merged = {}
for person in people_1():
  merged[person['ID']] = person

for person in people_2():
  merged[person['ID']] = person

print(merged.values())

# show the outcome
for person in merged.values():
  list.append(person.get("Age"))

print(sum(list))
