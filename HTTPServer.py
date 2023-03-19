import ctypes
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
from optparse import OptionParser
import netifaces
import os
import http.server
import socketserver


class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        return  # 禁用日志输出
    def do_GET(self):
        if shell_cmd in self.path:
            cmd = self.path.replace('/?','').replace('%20',' ').replace('=',' ').replace(shell_cmd,'').replace('shell','')
            cmd = os.popen(cmd).read()
            self.wfile.write(cmd.encode())
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

#显示所有网络接口
def get_local_ipv4_addresses():
    ipv4_addresses = []
    # 获取当前计算机的所有网络接口
    interfaces = netifaces.interfaces()
    for interface in interfaces:
        addresses = netifaces.ifaddresses(interface)
        # 获取当前网络接口的 IPv4 地址
        if netifaces.AF_INET in addresses:
            ipv4_info = addresses[netifaces.AF_INET]
            for info in ipv4_info:
                ip = info['addr']
                # 排除本地回环地址和 IPv6 地址
                if ip.startswith('127.') or ':' in ip:
                    continue
                ipv4_addresses.append(ip)
    return ipv4_addresses

def Banner():
    print("""      _    _ _______ _______ _____   _____                          
     | |  | |__   __|__   __|  __ \ / ____|                         
     | |__| |  | |     | |  | |__) | (___   ___ _ ____   _____ _ __ 
     |  __  |  | |     | |  |  ___/ \___ \ / _ \ '__\ \ / / _ \ '__|
     | |  | |  | |     | |  | |     ____) |  __/ |   \ V /  __/ |   
     |_|  |_|  |_|     |_|  |_|    |_____/ \___|_|    \_/ \___|_|   

                https://github.com/Axx8/HTTPServer   \n                """)
    print("""   Options:
         -h,        --help           show this help message and exit
         -p PORT,   --port=PORT      自定义端口（默认：8080）
         -d DIR,    --dir=DIR        自定义目录（默认：当前目录）
         -s SHELL,  --shell=SHELL    自定义Shell路径（默认：/?shell=）\n""")
    # 当前共享目录
    print(f' in directory {os.getcwd()}\n')
    for ip in ipv4_addresses:
        print(f' Starting HTTP server http://{ip}:{port}')
    print(f'\n Get Shell  http://ip:{port}/?{shell_cmd}=whoami')


ctypes.windll.kernel32.SetConsoleTitleW("HTTPServer    Axx8   HTTP文件浏览服务   ")

if __name__ == '__main__':
    ipv4_addresses = get_local_ipv4_addresses()
    if not ipv4_addresses:
        print('No non-loopback IPv4 address found.')
    else:
        try:
            parser = OptionParser()
            parser.add_option("-p", "--port", dest="port", default=8080, help="自定义端口（默认：8080）")
            parser.add_option("-d", "--dir", dest="dir", default=os.getcwd(), help="自定义目录（默认：当前目录）")
            parser.add_option("-s", "--shell", dest="shell", default='shell', help="自定义Shell路径（默认：/?shell=）")
            (options, args) = parser.parse_args()
            port = int(options.port)
            server_address = ('', port)
            os.chdir(options.dir)
            shell_cmd = options.shell

            httpd = socketserver.TCPServer(("", port), MyHTTPRequestHandler)
            Banner()
            httpd.serve_forever()
        except OSError as e:
            print("""                  _    _ _______ _______ _____   _____                          
                 | |  | |__   __|__   __|  __ \ / ____|                         
                 | |__| |  | |     | |  | |__) | (___   ___ _ ____   _____ _ __ 
                 |  __  |  | |     | |  |  ___/ \___ \ / _ \ '__\ \ / / _ \ '__|
                 | |  | |  | |     | |  | |     ____) |  __/ |   \ V /  __/ |   
                 |_|  |_|  |_|     |_|  |_|    |_____/ \___|_|    \_/ \___|_|   

                            https://github.com/Axx8/HTTPServer   \n                """)
            print("""   Options:
        -h,        --help           show this help message and exit
        -p PORT,   --port=PORT      自定义端口（默认：8080）
        -d DIR,    --dir=DIR        自定义目录（默认：当前目录）
        -s SHELL,  --shell=SHELL    自定义Shell路径（默认：/?shell=）\n""")
            print(e)
            print(e)
            print(e)
            os.system('pause')
        except Exception as ee:
            print(ee)
            os.system('pause')
