import base64
import argparse
import binascii
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

def decrypt_b64_password(b64_ciphertext):
    #the json blobs will have nested encrypted contents, just run the script again with that blob as the ciphertext
    key = "jCviWBweShAarI0/ukCN4CVVQ05vn5hcwDB4NExsU7Y="
    iv = "AT2NyUgw5dI7b/H2eJ2lGw=="
    key_bytes = base64.b64decode(key)
    iv_bytes = base64.b64decode(iv)

    ciphertext = base64.b64decode(b64_ciphertext)
    cipher = AES.new(key_bytes, AES.MODE_CBC, iv_bytes)

    try:
        decrypted = cipher.decrypt(ciphertext)
        decrypted = unpad(decrypted, AES.block_size)
        return decrypted.decode('utf-8', errors='replace')
    except Exception as e:
        return f"Decryption error: {str(e)}"

def decrypt_hex_password(hex_ciphertext):
    key_str = "8BEE8F53EDD48b3z"
    key_bytes = key_str.encode('utf-8')
    ciphertext = binascii.unhexlify(hex_ciphertext)
    cipher = AES.new(key_bytes, AES.MODE_ECB)
    
    try:
        decrypted = cipher.decrypt(ciphertext)
        if b'\x00' in decrypted:
            decrypted = decrypted.split(b'\x00')[0]
        return decrypted.decode('utf-8', errors='replace')
    except Exception as e:
        return f"Decryption error: {str(e)}"

def arg_parse():
    parser = argparse.ArgumentParser(description="Decrypt SmartDeploy encrypted creds prior to 3.0.2046")
    parser.add_argument("ciphertext", help="")
    parser.add_argument('-f', '--format', choices=['hex', 'base64'], help='Data format (hex or base64)')
    
    args = parser.parse_args()
    
    return args


def main():
    print("v0.0.1 by @unsigned_sh0rt")
    args = arg_parse()
    if args.format == "base64":
        result = decrypt_b64_password(args.ciphertext)
    else:
        result = decrypt_hex_password(args.ciphertext)

    print(f"Decrypted password: {result}")

if __name__ == "__main__":
    main()

