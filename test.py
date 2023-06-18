from CubeEncrypt import CubeEncrypt

def testEncryptDecrypt():
    dec = CubeEncrypt.encrypt("Hello, world!")
    print(dec)