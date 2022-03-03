1.

class Towers:
    def _init_(self, disks=3):
        self.disks = disks
        self.towers = [[]]*3
        self.towers[0] = [i for i in range(self.disks, 0, -1)]
        self.towers[1] = []
        self.towers[2] = []
    def _str_(self):
        output = ""
        for i in range(self.disks, -1, -1):
            for j in range(3):
                if len(self.towers[j]) > i:
                    output += " " + str(self.towers[j][i])
                else:
                    output += "  "
            output += "\n"
        return output + "-------"
    def move(self, from_tower, dest_tower):
        disk = self.towers[from_tower].pop()
        self.towers[dest_tower].append(disk)

def solve_tower_of_hanoi(towers, n, start_tower, dest_tower, aux_tower):
    # Base case - do nothing
    if n == 0:
        return
    # Move subproblem of n - 1 disks from start_tower to aux_tower.
    solve_tower_of_hanoi(towers, n - 1, start_tower, aux_tower, dest_tower)
    # Move disk n to dest_tower.
    towers.move(start_tower, dest_tower)
    print(towers)
    # Move subproblem of n - 1 disk from aux_tower to dest_tower.
    solve_tower_of_hanoi(towers, n - 1, aux_tower, dest_tower, start_tower)

t = Towers()
print(t)
solve_tower_of_hanoi(t, len(t.towers), 0, 2, 1)

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

2.

# Print Pascal's Triangle in Python
from math import factorial

# input n
n = int(input("Enter Number of rows : "))
for i in range(n):
	for j in range(n-i+1):

		# for left spacing
		print(end=" ")

	for j in range(i+1):

		# nCr = n!/((n-r)!*r!)
		print(factorial(i)//(factorial(j)*factorial(i-j)), end=" ")

	# for new line
	print()

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------=

3.

n1=float(input("Enter First Number : "))
n2=float(input("Enter Second Number : "))
q=n1//n2
r=n1%n2
print("The quotient is ",q)
print("The remainder is ",r)

.......
3 (a).

def calc(n1,n2):
    q=n1//n2
    r=n1%n2
n1=float(input("Enter first number : "))
n2=float(input("Enter second number : "))
print(callable(n1))
print(callable(n2))

.......
3(b).

def calc(n1,n2):
    if n1!=0 and n2!=0:
        print("The values are non zeroes")
    else:
        print("The values contains zero")

n1=float(input("Enter first number : "))
n2=float(input("Enter second number : "))
calc(n1,n2)

.......
3(d).

def calc(n1,n2):
    q=n1//n2
    r=n1%n2
    s1={q,r}
    print(s1)
n1=float(input("Enter first number : "))
n2=float(input("Enter second number : "))
calc(n1,n2)

........
3(e).

def calc(n1,n2):
    q=n1//n2
    r=n1%n2
    s1={q,r}
    f=frozenset(s1)
    print("The immutable set ",f)
n1=float(input("Enter first number : "))
n2=float(input("Enter second number : "))
calc(n1,n2)

........
3(f).

def calc(n1,n2):
    q=n1/n2
    r=n1%n2
    s1={q,r}
    m=max(s1)
    h=hash(m)
    print("The max value from set ",m)
    print("The hash value is ",h)
n1=float(input("Enter first number : "))
n2=float(input("Enter second number : "))
calc(n1,n2)

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

4.

class Student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll
p1 = Student("John", 36)
p2 =  Student("Harry", 21)
print("Name of the first student is : ",p1.name)
print("Roll no of the first student is : ",p1.roll)
print("Name of the second student is : ",p2.name)
print("Roll no of the second student is : ",p2.roll)
del Student

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
.........
5(a).

class Employee:
        count=0
        def __init__(self, name, salary):
            self.name=name
            self.salary=salary
            Employee.count+=1
        def displayCount(self):
            print("There are %d employees" % Employee.count)
        def displayDetails(self):
            print("Name:", self.name, ", Salary:", self.salary)
        def update(self):
            self.salary+=30000
e1=Employee("Mehak", 40000)
e2=Employee("Ashok", 50000)
e3=Employee("Viren", 60000)
e3.displayCount()
print("Details of all employee:")
e1.update()
e1.displayDetails()
e2.displayDetails()
e3.displayDetails()

.........
5(b).

class Employee:
        count=0
        def __init__(self, name, salary):
            self.name=name
            self.salary=salary
            Employee.count+=1
        def displayCount(self):
            print("There are %d employees" % Employee.count)
        def displayDetails(self):
            print("Name:", self.name, ", Salary:", self.salary)
        def update(self):
            self.salary+=30000
e1=Employee("Mehak", 40000)
e2=Employee("Ashok", 50000)
e3=Employee("Viren", 60000)
e3.displayCount()
del e3
print("Details of all employee:")
e1.update()
e1.displayDetails()
e2.displayDetails()
e3.displayDetails()


---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


6.

from itertools import permutations
import enchant
d=enchant.Dict("en_US")
op=set()

inp="extreme"
lettr = [x.lower() for x in inp]

for n in range (3,len(inp)) :
    for y in list(permutations(lettr, n)) :
        z="".join(y)
        if d.check(z) :
                op.add(z)
print(op)
