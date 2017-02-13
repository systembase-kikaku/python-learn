s = "This is a pen"
print(s.split())

s_date = "2020/01/02"
print(s_date.split("/"))

print(s_date.split("/", maxsplit = 1))

print("-".join(s.split()))
