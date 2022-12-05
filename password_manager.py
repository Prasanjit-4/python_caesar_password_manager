import clipboard
import string
import random

def caesar_cipher(raw_text, key):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    shifted_alphabet = alphabet[26-key:]+alphabet[0:(26-key)]
    cipher_text = ""

    for i in range(len(raw_text)):
        char = raw_text[i]
        idx = alphabet.find(char.upper())
        if idx == -1:
            cipher_text = cipher_text + char
        elif char.islower():
            cipher_text = cipher_text + shifted_alphabet[idx].lower()
        else:
            cipher_text = cipher_text + shifted_alphabet[idx] 

    return cipher_text

def gen_passw():
    characters = string.ascii_letters + string.punctuation  + string.digits

    password = ""
    password_length = random.randint(8, 16)
    
    for x in range(password_length):
        char = random.choice(characters)
        password = password + char
        
    return password

def add_passw():
    f=open("key.txt",'r')
    key=f.read()
    print(key)
    u_key=input("Enter master key: ")
    print(u_key==key,len(u_key),len(key))
    if u_key==key:
        with open("passwords.txt","r+") as passf:
            lis=passf.readlines()
            passf.seek(0,2)
            site=input("Enter site: ")
            username=input("Enter username: ")
            passw=cnf_password=""
            passw_ch=input("Do you want to generate a password? [Y/N]\n")
            if passw_ch in "Yy":
                passw=cnf_password=gen_passw()
            else:
                passw=input("Enter password: ")    
                cnf_password=input("Confirm password: ")
            if cnf_password==passw:    
                row= site+" "+username+" "+caesar_cipher(passw,3)+"\n"
                passf.write(row)
            passf.close()

def get_passw():
    f=open("key.txt",'r')
    key=f.read()
    u_key=input("Enter master key: ")
    
    if u_key==key:
        with open("passwords.txt","r") as passf:
            lis=passf.readlines()
            k=1
            fetch_list=list()
            for i in lis:
                creds=i.split()
                print(k,creds[0],creds[1])
                fetch_list.append(creds[2])
                k=k+1
            index=int(input("Enter password no. to be fetched: "))-1
            clipboard.copy(caesar_cipher(fetch_list[index],26-3))
            print("PASSWORD COPIED TO CLIPBOARD!")
        passf.close()
    
def set_new_key():
    prev_key=input("Enter previous key: ")
    key_file=open("key.txt",'r+')
    key=key_file.read()
    if prev_key==key:
        new_key=input("Enter new master key: ")
        key_file.seek(0)
        key_file.write(new_key)

def modify_password():
    f=open("key.txt",'r')
    key=f.read()
    u_key=input("Enter master key: ")
    
    if u_key==key:
        with open("passwords.txt","r+") as passf:
            lis=passf.readlines()
            k=1
            fetch_list=list()
            for i in lis:
                creds=i.split()
                print(k,creds[0],creds[1])
                fetch_list.append(creds[2])
                k=k+1
            index=int(input("Enter password no. to be modified: "))-1
            passw_ch=input("Do you want to generate a password? [Y/N]\n")
            if passw_ch in "Yy":
                passw=cnf_password=gen_passw()
            else:
                passw=input("Enter password: ")    
                cnf_password=input("Confirm password: ")
            if cnf_password==passw:    
                lis[index]= lis[index].split()[0]+" "+lis[index].split()[1]+" "+caesar_cipher(passw,3)+"\n"
                passf.seek(0)
                passf.writelines(lis)
            passf.close()
            
            
def main():
    print("Add new password[Aa]\nFetch password[Gg]\nModify password[Mm]\nSet new master key[Kk]")
    choice=input("Enter choice: ")
    print("\n\n")
    if choice in "Aa":
        add_passw()
    elif choice in "Gg":
        get_passw()
    elif choice in "Mm":
        modify_password()
    elif choice in "Kk":
        set_new_key()
    else:
        ch=input("Invalid choice! Do you wish to continue?[Y/N]")
        if ch in "Yy":
            main()
        else:
            print("Exiting Password Manager")
            
    ch=input("Do you wish to continue?[Y/N]")
    if ch in "Yy":
        print("\n\n")
        main()
    else:
        print("Exiting Password Manager....")

if __name__=='__main__':
    main()


