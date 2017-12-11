import gmpy
from Crypto.Hash import SHA

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


def Crack(g, p, q, r, s, Ha, k):
	x = ((s * k - Ha) * gmpy.invert(r, q)) % q
	print("Sercet key is:%s" % (x))
	Test(x)



m1 = "Listen for me, you better listen for me now. "
m2 = "Yeah me shoes a an tear up an' now me toes is a show a "
s1 = 0x518c6992460db2b20759fb15cfc2a7f58d6ff8b
s2 = 506591325247687166499867321330657300306462367256
p = 0x800000000000000089e1855218a0e7dac38136ffafa72eda7859f2171e25e65eac698c1702578b07dc2a1076da241c76c62d374d8389ea5aeffd3226a0530cc565f3bf6b50929139ebeac04f48c3c84afb796d61e5a4f9a8fda812ab59494232c7d2b4deb50aa18ee9e132bfa85ac4374d7f9091abc3d015efc871a584471bb1
q = 0xf4f47f05794b256174bba6e9b396a7707e563c5b
g = 0x5958c9d3898b224b12672c0b98e06c60df923cb8bc999d119458fef538b8fa4046c8db53039db620c094c9fa077ef389b5322a559946a71903f990f1f7e0e025e2d7f7cf494aff1a0470f5b64c36b625a097f1651fe775323556fe00b3608c887892878480e99041be601a62166ca6894bdd41a7054ec89f756ba9fc95302291
r = 51241962016175933742870323080382366896234169532
Ha = 0xa4db3de27e2db3e5ef085ced2bced91b82e0df19
Hb = 0xbc7ec371d951977cba10381da08fe934dea80314

def CalculateK(m1, m2):
	H1 = SHA.new()
	H2 = SHA.new()
	H1.update(m1.encode('utf-8'))
	H2.update(m2.encode('utf-8'))
	m1 = H1.hexdigest()
	m2 = H2.hexdigest()
	print("SHA1 of m1:%s\nSHA1 of m2:%s" % (m1, m2))

	k = ((int(m1, 16) - int(m2, 16)) * gmpy.invert(s1 - s2, q)) % q
	print("k is:%d" % (k))
	return k

def Test(x):
	k_hash = 0xca8f6f7c66fa362d40760d135b763eb8527d3d52
	x = hex(x)[2:]
	secret_key_hash = SHA.new()
	secret_key_hash.update(x.encode("utf-8"))
	secret_key_value = secret_key_hash.hexdigest()
	if int(secret_key_value, 16) == k_hash:
		print("Correct!")
	else:
		print("Wrong!")



if __name__ == '__main__':
	k = CalculateK(m1, m2)
	#h = input("message:")
	#H = SHA.new()
	#H.update(h.encode('utf-8'))
	#print("The hash of message is:%s" % (H.hexdigest()))
	#H = int(H.hexdigest(), 16)
	Crack(g, p, q, r, s1, Ha, k)

