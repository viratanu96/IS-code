inputString = "Hello World"
string2 = ""

for i in range(0, len(inputString)):
    string2 += chr(ord(inputString[i]) & 127)
print(string2)