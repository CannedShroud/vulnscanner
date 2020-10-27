import portscanner

target_ip = input("Enter the target to scan for vulnerable ports: ")
port_num = int(input("Enter the amount of ports you want to scan: (500 -> First 500 ports) "))
vul_file = input("Enter path to file with vulnerable software: ")
print("\n")

target = portscanner.PortScan(target=target_ip, port_num=port_num)
target.scan()

with open(vul_file, "r") as file:
    count = 0
    for banner in target.banner_list:
        file.seek(0)
        for line in file.readlines():
            if line.strip() in banner:
                print(f"!!!  VULNERABLE BANNER  !!! {banner} ON PORT {str(target.ports_list[count])}")
        count += 1
    print("\n")
    print(f"Scan ended, all banners -> {target.banner_list}")
