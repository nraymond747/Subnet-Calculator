# IPv4 Subnet calculator

from ipaddress import *

print(""" __  .______   ____    ____  _  _            _______. __    __  .______   .__   __.  _______ .___________.     ______     ___       __        ______  __    __       ___       __      .___________. ______   .______      
|  | |   _  \  \   \  /   / | || |          /       ||  |  |  | |   _  \  |  \ |  | |   ____||           |    /      |   /   \     |  |      /      ||  |  |  |     /   \     |  |     |           |/  __  \  |   _  \     
|  | |  |_)  |  \   \/   /  | || |_        |   (----`|  |  |  | |  |_)  | |   \|  | |  |__   `---|  |----`   |  ,----'  /  ^  \    |  |     |  ,----'|  |  |  |    /  ^  \    |  |     `---|  |----|  |  |  | |  |_)  |    
|  | |   ___/    \      /   |__   _|        \   \    |  |  |  | |   _  <  |  . `  | |   __|      |  |        |  |      /  /_\  \   |  |     |  |     |  |  |  |   /  /_\  \   |  |         |  |    |  |  |  | |      /     
|  | |  |         \    /       | |      .----)   |   |  `--'  | |  |_)  | |  |\   | |  |____     |  |        |  `----./  _____  \  |  `----.|  `----.|  `--'  |  /  _____  \  |  `----.    |  |    |  `--'  | |  |\  \----.
|__| | _|          \__/        |_|      |_______/     \______/  |______/  |__| \__| |_______|    |__|         \______/__/     \__\ |_______| \______| \______/  /__/     \__\ |_______|    |__|     \______/  | _| `._____|)
By: Nolan Raymond
""")

print("""Subnet mask key:
/30 ---> 255.255.255.252
/29 ---> 255.255.255.248
/28 ---> 255.255.255.240
/27 ---> 255.255.255.224
/26 ---> 255.255.255.192
/25 ---> 255.255.255.128
/24 ---> 255.255.255.0
/23 ---> 255.255.254.0
/22 ---> 255.255.252.0
/21 ---> 255.255.248.0
/20 ---> 255.255.240.0
/19 ---> 255.255.224.0
/18 ---> 255.255.192.0
/17 ---> 255.255.128.0
/16 ---> 255.255.0.0
/15 ---> 255.254.0.0
/14 ---> 255.252.0.0
/13 ---> 255.248.0.0
/12 ---> 255.240.0.0
/11 ---> 255.224.0.0
/10 ---> 255.192.0.0
/9  ---> 255.128.0.0
/8  ---> 255.0.0.0
""")

masks = [255, 254, 252, 248, 240, 224, 192, 128, 0]

addr = input("Enter your ip address: ")
addr = addr.split('.')

# Display all results.
def display():
    print("-------------------------------------------------")
    print("IP Address: {0}.{1}.{2}.{3}".format(*addr))
    print("Subnet Mask: {0}.{1}.{2}.{3}".format(*mask))
    print("Network Address:",CIDR_addr.network_address)
    print("Usable Host IP Range:",str(CIDR_addr.network_address+1) + " - " + str(CIDR_addr.broadcast_address-1))
    print("Broadcast Address:",CIDR_addr.broadcast_address)
    print("Total Number of Hosts:","{:,}".format(CIDR_addr.num_addresses))
    print("Number of Usable Hosts:","{:,}".format(CIDR_addr.num_addresses-2))
    print("CIDR Notation: {0}.{1}.{2}.{3}".format(*addr) + "/" + str(CIDR_mask))
    print("Wildcard Mask:",CIDR_addr.hostmask)
    print("Binary IP Address: {0}.{1}.{2}.{3}".format(*addr_bin))
    print("Binary Subnet Mask: {0}.{1}.{2}.{3}".format(*mask_bin))

# Calculate binary and CIDR before displaying.
def calculate():
    global addr_bin, mask_bin, CIDR_addr, CIDR_mask

    addr_bin = []
    for i in range(4):
        num1 = bin(int(addr[i]))[2:]
        addr_bin.append(int(num1))

    mask_bin = []
    for i in range(4):
        num2 = bin(int(mask[i]))[2:]
        mask_bin.append(int(num2))

    CIDR_mask = sum(bin(int(i)).count('1') for i in mask)
    
    net_addr = [int(addr[i]) & int(mask[i]) for i in range(4)]
    net_addr = "{0}.{1}.{2}.{3}".format(*net_addr)

    CIDR_addr = str(net_addr) + "/" + str(CIDR_mask)
    CIDR_addr = IPv4Network(CIDR_addr)

    display()

# Checks validity of the entered subnet mask ("mask").
def mask_check():
    global mask
    mask = input("Enter your subnet mask (ex.'255.255.255.252'): ")
    mask = mask.split('.')
    
    if (len(mask) == 4) and (int(mask[0]) == 255) and (int(mask[1]) in masks) and (int(mask[2]) in masks and (int(mask[2])<= int(mask[1]))) and (int(mask[3]) in masks and (int(mask[3])<= int(mask[2]))):
        calculate()
    else:
        print("You need to enter a valid subnet mask.")
        exit()

# Checks validity of the entered ip address ("addr").
if (len(addr) == 4) and (0 <= int(addr[0]) <= 255) and (0 <= int(addr[1]) <= 255) and (0 <= int(addr[2]) <= 255) and (0 <= int(addr[3]) <= 255):
    mask_check()
else:
    print("You need to enter a valid ip address.")
    exit()