s = input("Enter string: ")
k = int(input("Enter key: "))

enc = [[" " for i in range(len(s))] for j in range(k)]

flag = 0
row = 0


for i in range(len(s)):
    enc[row][i] = s[i]
    if row == 0:
        flag = 0
    elif row == k-1:
        flag = 1
    if flag == 0:
        row += 1
    else:
        row -= 1


ct = []
for i in range(k):
    for j in range(len(s)):
        if enc[i][j] != ' ':
            ct.append(enc[i][j])


cipher = "".join(ct)
print("Cipher Text: ", cipher)


decrypted_text = ""
for i in range(0, len(enc[0])):
    if enc[0][i] != " ":
        decrypted_text += enc[0][i]
    else:
        decrypted_text += enc[1][i]

print("Decrypted Text: ", decrypted_text)
