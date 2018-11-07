"""sieres of exersices for labs sessions week six problem solving with python"""

#statments ex 1 a 
sports =  ["football", "rugby", "hockey", "tenis"]
#list of sports 
print(sports)
#prints sports 
sports.append("cycling")
#adds cycling

for sport in sports: 
	#ittorates sports and prints first and last letter,
	#of each item in sports 
	print(sport[0],sport[len(sport)-1])

print("the length of list sports is %s" % (len(sports)))

sports.remove("football")
#removes football from list 
print(sports)
sports_slice = sports[1:3]
print(sports_slice)

a = [2, -6, -5, 3, 9]
print("sorted" + str(sorted(a)))

print(sorted(a, key=lambda x : x))
print(sorted(a, key=lambda x : abs(x)))
print(sorted(a, key=lambda x : x ** 2))
print(sorted(a, key=lambda x : (x % 2, x)))

names = ["tim", "bob", "trevor", "susan","anna"]
print(lambda x : (x[1] for i in names), names)
