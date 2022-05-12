def gcd(a, b):
    if(b == 0):
        return a
    else:
        return gcd(b, a % b)


# Two random prime numbers
p = 3
q = 7
n = p*q

# e stands for encrypt
e = 2
phi = (p-1)*(q-1)

while (e < phi):
    if (gcd(e, phi) == 1):
        break
    else:
        e = e+1

# Private key (d stands for decrypt)
k = 2  # A constant value
d = (1 + (k*phi))/e

# Encryption
msg = 10

print("Original Message : ", msg)
# Encryption c = (msg ^ e) % n
c = pow(msg, e)
c = c % n

print("Encrypted Text: ", c)

# decryption

m = pow(c, d)
m = m % n
print("Decrypted Text: ", m)
