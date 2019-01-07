# print("Hello World")


# message="hello world 1st"
# print(message)


##///traceback

# _message="hello world 1st"
# print(_message)

# world_message="test 1"
# print(world_message)
# world_message="test2"
# print(world_message)

# name="ada lovRlace"
# print(name.title())
# print(name.lower())
# print(name.upper())
# print(name)

# name="action 1"
# name2="action 2"
# print(name+" "+name2)

# name="Eric"
# print("Hello " + name +", would you learn some Python today")

# name=" eriC ";
# print(name.lower().strip());
# print(name.upper().rstrip());
# print(name.title().lstrip());

# famous_person="Albert Einstein"
# sentence=' once said, "A person who never made a mistake never tried anything new."'
# print(famous_person+sentence)

# famous_person="\tAlbert Einstein\n"
# print(famous_person)
# print(famous_person.rstrip())
# print(famous_person.lstrip())
# print(famous_person.strip())

# print(str(0.1)+ ' hello from other side')

# print(4+4)
# print(4*2)
# print(10.0-2)
# print(16/2)
# import this

# cars=['audi','bmw','mecerdes-benz']
# print(cars)
# print(cars[-1list])

# guests=['albert Einstein', 'Jack Ma', 'Nai Cha']
# print(guests)
# print(guests[0])
# guests[0]='Yao Ming'
# print(guests)
# guests.append('lily')
# guests.append('mumu')
# guests.insert(0,'testv')
# print(guests)
# name=guests.pop()
# print("sorry "+name+", you cannot go")
# name=guests.pop()
# print("sorry "+name+", you cannot go")
# name=guests.pop()
# print("sorry "+name+", you cannot go")
# name=guests.pop()
# print("sorry "+name+", you cannot go")
# print(guests)
# del guests[1]
# del guests[0]
# print(guests)


# guests=['Albert Einstein', 'Jack Ma', 'Nai Cha']
# guests.sort(reverse=True)
# print(guests)
# print(guests.sorted())

# places=['Hawaii', 'Alaska', 'Maldives', 'Bora-bora', 'Italy']
# print(places);
# print(sorted(places))
# print(places)
# print(sorted(places, reverse=True))
# print(places)

# places.reverse()
# print(places)
# places.reverse()
# print(places)
# places.sort()
# print(places)
# places.sort(reverse=True)
# print(places)

# magicians=['adam','bytrace'. 'charlie']

#4.1
# pizzas=['peperoni pizza', 'cheese pizza', 'fruit pizza']
# for pizza in pizzas:
# 	print("I like "+pizza)
# print('I like all pizzas')

# 4.2
# animals=['cat','dog', 'fish']
# for animal in animals:
# 	print('a '+animal+' is a great pet')
# print("I have all of them as pets")

# 4.3
# for value in range(1,21):
# 	print(value)

# 4.4
# numbers=list(range(1,1000001))
# for value in numbers:
# 	print(value)

# 4.5
# print(min(numbers))
# print(max(numbers))
# print(sum(numbers))

# 4.6
# odds=list(range(1,21,2))
# for odd in odds:
# 	print(odd)

# 4.7
# threes=list(range(3,31,3))
# for three in threes:
# 	print(three)

# 4.8
# numbers=[value**3 for value in range(1,11)]
# for number in numbers:
# 	print(number)

# 4.10
# items=[1,2,3,4,5,6,7,8,9,10]

# print("the first three items are:")
# for item in items[:3]:
# 	print(item)
# print("the middle three items are:")
# for item in items[4:7]:
# 	print(item)
# print("the last three items are:")
# for item in items[-3:]:
# 	print(item)

# 4.11
pizzas=['peperoni pizza', 'cheese pizza', 'fruit pizza']
friend_pizzas=pizzas[:]
pizzas.append('no more')
friend_pizzas.append('one more')
for pizza in pizzas:
	print(pizza)