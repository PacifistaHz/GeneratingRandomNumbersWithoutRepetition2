start=input("Enter a start number: ")
end=input("Enter a end number: ")
generatingNumber=input("Enter a generating number: ")
start=int(start)
end=int(end)
generatingNumber=int(generatingNumber)

array=list(range(start,end+1))

import random
random.shuffle(array)

partOfArray=array[1:generatingNumber]
print(*partOfArray,sep='\n')