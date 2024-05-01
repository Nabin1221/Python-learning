#Indexing and Slicing


#Positive indexing
a = [1,2,3,4,5,'Hello']

b  =a[0]

print (a[0])

#Negative Indexing
a = [1,2,3,4,5,'Hello']

b = a[-1]
print (b)


#Slicing
a = [1,2,3,4,5,'Hello','Python']

b = a[-3:-1]

print (b)


#for loop
#iteration - The loop process of going from start to end of a iterable data

#Iterator - Iteration does iteration on iterable datas

#Iterable - Group data Types

a = [1,2,3,4,'Hello']

for i in a:
    if i == 2:
        break
        #continue
    print ('Hello World')

    