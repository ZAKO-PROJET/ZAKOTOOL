import os

os.system("sudo apt install nmap")
os.system("sudo apt-get -y install gobuster")
os.system("sudo apt install ruby")
os.system("sudo apt install build-essential libcurl4-openssl-dev libxml2 libxml2-dev libxslt1-dev ruby-dev  libgmp-dev zlib1g-dev")
os.system("sudo gem install wpscan")
os.system("sudo apt-get install hydra-gtk")
os.system("sudo mv common.txt /usr/share")
os.system("sudo mv bigone.txt /usr/share")
os.system("sudo apt install john")
os.system("sudo mv zako /bin/")
os.system("sudo wget https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt")
os.system("sudo mv rockyou.txt /usr/share")
os.system("sudo mv zakotools.py /usr/share")
os.system("chmod +x /bin/zako")
