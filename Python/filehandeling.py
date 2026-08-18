p = open('basic.py')
print(p.read())


r = open("superman.txt",'w')
r.write("Hello my name is nikhil ")
r.close()
w = open("superman.txt",'a')
w.write("heya")
w.close()