#Prompt the user for a number.
ncount= int(input("How many numbers? "))

#Define the variables to use in your code.
n1,n2 = 0 , 1
count = 0

#Print zero if the users input is equal to one.
if ncount == 1:
  print("Fibonnaci sequence" , ncount, ":")
  print (n1)

#Print out the fibonacci sequence to match the numerical length of the users input.
else:
  print("Fibonacci sequence: ")
  while count < ncount:
    print(n1)
    nth = n1 + n2

#Reassign your variables to one another and reassign the number one to your count variable.
    n1 = n2
    n2 = nth
    count += 1