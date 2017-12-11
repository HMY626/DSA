import math
import gmpy
from Crypto.Hash import SHA 
p = 0x800000000000000089e1855218a0e7dac38136ffafa72eda7859f2171e25e65eac698c1702578b07dc2a1076da241c76c62d374d8389ea5aeffd3226a0530cc565f3bf6b50929139ebeac04f48c3c84afb796d61e5a4f9a8fda812ab59494232c7d2b4deb50aa18ee9e132bfa85ac4374d7f9091abc3d015efc871a584471bb1
q = 0xf4f47f05794b256174bba6e9b396a7707e563c5b
g = 0x5958c9d3898b224b12672c0b98e06c60df923cb8bc999d119458fef538b8fa4046c8db53039db620c094c9fa077ef389b5322a559946a71903f990f1f7e0e025e2d7f7cf494aff1a0470f5b64c36b625a097f1651fe775323556fe00b3608c887892878480e99041be601a62166ca6894bdd41a7054ec89f756ba9fc95302291
s = 857042759984254168557880549501802188789837994940
r = 548099063082341131477253921760299949438196259240
y = 0x84ad4719d044495496a3201c8ff484feb45b962e7302e56a392aee4abab3e4bdebf2955b4736012f21a08084056b19bcd7fee56048e004e44984e2f411788efdc837a0d2e5abb7b555039fd243ac01f0fb2ed1dec568280ce678e931868d23eb095fde9d3779191b8c0299d6e07bbb283e6633451e535c45513b2d33c99ea17

'''
#计算私钥
#x = ((s * k - H) // r ) % q

#计算公钥
#y = g^x % p

#计算s
#s = k^-1 * (H + x * r) % q
'''
#H(msg)
#H = 0x9b6d36a0678c9607c912d1a1547d3780834874e0


#r = ( g^k % p ) % q


def fastExpMod(c, d, n):
    result = 1
    while d != 0:
        if (d&1) == 1:
            # di = 1, then mul
            result = (result * c) % n
        d >>= 1
        # b, b^2, b^4, b^8, ... , b^(2^n)
        c = (c*c) % n
    return result

def Crack(g, p, q, r, s, H):
	for k in range(2, 65537):
		r0 = pow(g, k, p)
		if r0 % q == r:
			print("Key:%d" %(k))
			x = ((s * k - H) * gmpy.invert(r0, q)) % q
			print("Sercet key is:%s" % (x))

def Test():
	x = int(input("x:"))
	if fastExpMod(g, x, p) == y:
		print("True!")
	else:
		print("False!")

if __name__ == '__main__':
	h = input("message:")
	H = SHA.new()
	H.update(h.encode('utf-8'))
	print("The hash of message is:%s" % (H.hexdigest()))
	H = int(H.hexdigest(), 16)
	Crack(g, p, q, r, s, H)
	#Test()




