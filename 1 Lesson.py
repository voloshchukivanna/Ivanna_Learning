'''1 Task'''

#1
a = "Ivanna test"
a.isdigit()

#2
b = "f cffdf    ferf fdf 4 5 6"
b.count(" ")

#3
x = "n.e.l.l.y"
x.count(".")

#4
f = "Homework"
f.center(100)

#5
d = "ivanna voloshchuk"
d.title()

#6
"cdvjfding".endswith('ing')

#7
"sdsadsa".find('a')

#8
g = "a d d w w"
g.split()

'''3 Task'''
#1
cars = ['bmw', 'audi', 'ford', 'volvo', 'subaru']
print(cars[-3])

#2
cars = ['bmw', 'audi', 'ford', 'volvo', 'subaru']
print(cars[1][0])

#3
cars = ['bmw', 'audi', 'ford', 'volvo', 'subaru']
print(cars[-1][-1])

#4
cars = ['bmw', 'audi', 'ford', 'volvo', 'subaru']
cars.append('tesla')
print(cars)

#5
cars = ['bmw', 'audi', 'ford', 'volvo', 'subaru']
len(cars)
cars.insert(2, 'infiniti')
print(cars)

#6
cars = ['bmw', 'audi', 'ford', 'volvo', 'subaru']
del cars[0]
print(cars)

#7
cars = ['bmw', 'audi', 'ford', 'volvo', 'subaru']
cars.remove('subaru')
print(cars)

'''4 Task'''
#1
d = {"title": "female", "price": 3200, "ingredients": "suit"}
["description"] = "coton"
print(d)

#2
d = {"title": "female", "price": 3200, "ingredients": "suit"}
d["price"] += 100
print(d)

#3
d = {"title": "female", "price": 3100, "ingredients": "suit"}
d["ingredients"] += ", shirt"
print(d)

#4
d = {'title': 'female', 'price': 3100, 'ingredients': 'suit, shirt]'}
len(d["ingredients"].split())

#5
d = {'title': 'female', 'price': 200, 'ingredients': 'suit', 'description': 'coton'}
del d['description']
print(d)


