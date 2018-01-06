import base64
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256
from Crypto.Util.number import bytes_to_long, long_to_bytes
from gmpy import invert

def import_pk():
    with open('pub.pem', 'r') as f:
        return RSA.importKey(f.read())

if __name__ == '__main__':
    pubkey = import_pk()

    n = pubkey.n
    e = pubkey.e

    c1 = bytes_to_long(base64.b64decode('k6kExKZavwGKtbSyXHN6zJxg2sKcKLOYY9UhKtYnPEqekLt2zFtGcbIxdbrYjv1Mn+j4pbcU7zICVa4b2raT7zsM7RWpCAQR3exKSvIejAbI7DRicBf2y8Eu2PorQ4ErA2ikg6lvj05jNtJWLVCqh4W9g+5hURanJt9lHxq50T/dSOHjGalxSccYiRoiYWdFDXjF0sOOT4qkWfLjFYwiU54s1J7mt1Q7zHzdWXrFpyhV9cEG/XBpfi4bVeUE6qAL0x/OumzaE8TGOY8qaargu+qMlWnGFxpzXS3xjzCGU1Z9Qg52td4Zd4PIku//l4PR9aiWxCZL3/dz/+ObXz/2RA=='))
    c2 = bytes_to_long(base64.b64decode('l9QL7wZLynSGE4Sw0g2xbYQ39h4ow10/ZvRm6ERmbClZsSBnd7Us76eXdajUdNulat98kYsgsr8MUzvzgrHtSX5bW/c7f9peLWYbeFE+v/uJYj5VmBdxDzL1tr+EhgaRd3ageyc0/aUO4V337lL7R16Go4+//gXuXYoH+Et8N8BzWRyyljdI0AQzLIZCjQUYZn/75kuKyYq9MsxVKpu2AZdAOEwRfn2jb/DE7gY2DRJrkbuj4jKPZDB9LD3pWq+hjahfzpT+hI+aOAhmoDb8SsK3DhV1NgQCm8X3lCYS61TXP0SpUMUuvKI+YY4+Mot6Ewj0SJVGjX9PkptOGqiJAw=='))

    a = 1
    b = 1

    assert e == 3

    frac = b * (c2 + 2*pow(a,3)*c1 - pow(b,3))
    denom = a * (c2 - pow(a,3)*c1 + 2*pow(b,3))
    m = (frac * invert(denom, n)) % n


    for i in range(22):
        key = long_to_bytes(m+i)
        key = SHA256.new(key).digest()
        key = base64.b64encode(key)

        print key
