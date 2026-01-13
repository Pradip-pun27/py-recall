'''
zip() = Combines multiple iterables (lists, tuples, sets, dict) into a single iterator
           It makes managing multiple indices easier.
'''
names = ['Ram','Shyam','Anu']
ages = [19,20,21]
jobs = ['Doctor', 'Professor','Nurse']

data = (zip(names, ages, jobs)) # We can run loop over data variable. (it's iterable)

for name, age, job in data:
    print(f"{name} is {age} years old {job}")

r = range(1,11)
for num in r:
    print(num)
print(type(r))



