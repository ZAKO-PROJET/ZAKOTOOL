import os

os.system("clear")

print("Zako tool penetrassion testing for ctf and pentesting.\n")

os.system("toilet ZAKO")

print("  LISTE DES CHOIX                            LISTE DES CHOIX ")
print("                                                                              ")
print("    (1)Nmap                                    (4)Hydra")
print("    (2)Gobuster                                (5)John")
print("    (3)Wpscan                                       \n")

choice = input("Quelle est votre choix: ")

def nmapp():
    ipp = input("\nQuelle est l'ip a scanner: ")
    os.system("nmap -vv -sV -sC " + ipp + " -A -T4")


def enum():
    ipp = input("\nQuelle est l'ip a scanner: ")
    print("\nWORDLIST")
    print("(1)common.txt")
    print("(2)bigone.txt")
    print("(3)wordlist personaliser")
    wrd = input("Quelle wordlist souaiter vous utiliser ?: ")
    if wrd == ("1"):
        chemmm = ("/usr/share/common.txt")
        os.system("gobuster -e -u " + ipp +" -w " + chemmm)
    if wrd == ("2"):
        chemmm = ("/usr/share/bigone.txt")
        os.system("gobuster -e -u " + ipp +" -w " + chemmm)
    if wrd == ("3"):
        chemmm = input("Chemin de la wordlist: ")
        os.system("gobuster -e -u " + ipp +" -w " + chemmm)

def wp():
    chemm = input("\nEntrer l'url: ")
    os.system("wpscan --url " + chemm +" --enumerate")
    brute = input("\nVoulez vous bruteforcer ?:(Y/N) ")
    if brute == ("Y"):
        usr = input("Quelle user souaiter vous bruteforcer ?: ") 
        print("\nWORDLIST")
        print("(1)rockyou.txt")
        print("(2)wordlist personaliser")
        wrd = input("Quelle wordlist souaiter vous utiliser ?: ")
        if wrd == ("1"):
            chemmm = ("/usr/share/rockyou.txt")
            os.system("wpscan --url " + chemm + " -P " + chemmm + " -U " + usr)
        else:
            chemmm = input("Chemin de la wordlist: ")
            os.system("wpscan --url " + chemm + " -P " + chemmm + " -U " + usr)


def nik():
    print("BRUTEFORCE")
    print("(1)WEB")
    print("(2)SSH")
    choice = input("Quelle service souaiter vous bruteforcer ?: ")
    if choice == ("1"):
        ipp = input("\nQuelle est l'ip a bruteforce ?: ")
        usr = input("Quelle est l'utilisateur a bruteforce ?: ")
        page = input("Entrer L'url: ")
        print("\nWORDLIST")
        print("(1)rockyou.txt")
        print("(2)wordlist personaliser")
        wrd = input("Quelle wordlist souaiter vous utiliser ?: ")
        if wrd == ("1"):
            wrd = ("/usr/share/rockyou.txt")
            os.system("hydra -l " + usr + " -P " + wrd + " " + ipp + " http-post-form " + '"' + page +':username=^USER^&password=^PASS^:F=incorrect" -V')
        else: 
            wrd == ("2")
            wrd = input("Chemin de la wordlist: ")
            os.system("hydra -l " + usr + " -P " + wrd + " " + ipp + " http-post-form " + '"' + page +':username=^USER^&password=^PASS^:F=incorrect" -V')

    if choice == ("2"):
        ipp = input("\nQuelle est l'ip a bruteforce ?: ")
        usr = input("Quelle est l'utilisateur a bruteforce ?: ")
        print("\nWORDLIST")
        print("(1)rockyou.txt")
        print("(2)wordlist personaliser")
        wrd = input("Quelle wordlist souaiter vous utiliser ?: ")
        if wrd == ("1"):
            wrd = ("/usr/share/rockyou.txt")
            os.system("hydra -l " + usr + " -P " + wrd + " " + ipp + " -t 4 ssh")
        else:
            wrd == ("2")
            wrd = input("Chemin de la wordlist: ")
            os.system("hydra -l " + usr + " -P " + wrd + " " + ipp + " -t 4 ssh")


def jhn():
    file = input("\nQuelle est le chemin du fichier contenant le hash ?: ")
    print("\nWORDLIST")
    print("(1)rockyou.txt")
    print("(2)wordlist personaliser")
    wrd = input("Quelle wordlist souaiter vous utiliser ?: ")
    if wrd == ("1"):
        wrd = ("/usr/share/rockyou.txt")
        os.system("john --wordlist=" + wrd + " " + file)
    else:
        wrd = input("Chemin de la wordlist: ")
        os.system("john --wordlist=" + wrd + " " + file)


if choice == ("1"):
    nmapp()        

if choice == ("2"):
    enum()

if choice == ("3"):
    wp()

if choice == ("4"):
    nik()

if choice == ("5"):
    jhn()