f = open("no-spaces.txt", "r")

binary = f.read()

result = ""

for i in binary:
	if i == "1":
		result += "0"
	else:
		result += "1"

file = open("result.data", "w") 
file.write(result) 
file.close() 
f.close()