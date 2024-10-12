'''
Forage AIG Cybersecurity Program
Bruteforce starter template
'''

from zipfile import ZipFile

def attempt_extract(zf_handle, password):
    try:
        zf_handle.extractall(pwd=password)
        print("[+] Password Found")
        print("[+] Decrypting Files")
        print(f"[+] Password: {password}")
        return 1
    except:
        return 0


def main():
    print("[+] Beginning bruteforce ")
    with ZipFile('enc.zip') as zf:
        with open('rockyou.txt', 'rb') as f:
            for password in f:
                password = password.strip()
                found = attempt_extract(zf, password)
                if found:
                    return

    print("[+] Password not found in list")


if __name__ == "__main__":
    main()