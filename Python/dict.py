dc = {2: "HELLO", 1:"HI ",3:0}
print(dc)
print(dc[2])
dc[2] =  "NIKHIL"
print(len(dc))
dc["x"] = 5
print(dc)
dc.update({2:"nik"})
print(dc)
print(dc.get(2))
print(dc.get(4))
print(dc.keys())
print(dc.values())
dc.pop(2)
print(dc)
dc.popitem()
print(dc)
dc.setdefault(2,"nikhil")
print(dc)