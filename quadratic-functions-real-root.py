import time
print("as a*x**2+b*x+c（a≠0） an example")
a=0
while float(a)==0:
	a=float(input("a"))
b=float(input("b"))
c=float(input("c"))
def  giao(a,b,c):
	d=b**2-4*a*c
	if d>=0:
		e=bool(1)
	else:
		e=bool(0)
	return e
f=giao(a,b,c)
print(f)
time.sleep(30)
