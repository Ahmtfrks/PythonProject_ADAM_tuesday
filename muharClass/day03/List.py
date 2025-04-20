items= ["Pen,", "Laptop", "Book"," Camera"]

print(len(items))
print(type(items))
print((items))

items.append("micro")
print((items))
items.pop(-2)
print((items))

items.remove("pen")
print((items))

items.extend(("egg", "apples", "water")) #nasil ya iterate ne deemk sor chate

print((items))

print("--------------------------------------")

languaes= ("Python", "Java", " c#" , "ruby", "javascript")

temp_list= list(languaes)

temp_list.pop(1)

temp_list.remove("ruby")

print(temp_list)

languaes= tuple(temp_list)

print(languaes)
