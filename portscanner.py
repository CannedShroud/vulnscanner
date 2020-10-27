from IPy import IP
import socket


class PortScan:
    banner_list = []
    ports_list = []

    def __init__(self, target, port_num):
        self.target = target
        self.port_num = port_num

    def chek_ip(self):
        try:
            IP(self.target)
            return self.target
        except ValueError:
            return socket.gethostbyname(self.target)

    def scan_port(self, prt):
        try:
            converted_ip = self.chek_ip()
            s = socket.socket()
            s.settimeout(0.5)
            s.connect((converted_ip, int(prt)))
            self.ports_list.append(prt)
            try:
                banner = s.recv(1024).decode().strip("\n").strip("\r")
                self.banner_list.append(banner)
            except:
                self.banner_list.append(" ")
            s.close()
        except:
            pass

    def scan(self):
        for port in range(1, int(self.port_num)):
            self.scan_port(port)
