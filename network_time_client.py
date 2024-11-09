from socket import socket, AF_INET, SOCK_STREAM

HOST = "google.com"
PORT = 80

HTTP_REQUEST = f"""HEAD / HTTP/1.1
Host: {HOST}:{PORT}
User-Agent: Links (2.20.2; Linux 5.15.153.1-microsoft-standard-WSL2 x86_64; GNU C 9.2.1; text)
Accept: */*
Accept-Language: en,*;q=0.1
Accept-Encoding: gzip, deflate, br, zstd, bzip2, lzma, lzma2, lzip
Accept-Charset: us-ascii,ISO-8859-1,ISO-8859-2,ISO-8859-3,ISO-8859-4,ISO-8859-5,ISO-8859-6,ISO-8859-7,ISO-8859-8,ISO-8859-9,ISO-8859-10,ISO-8859-13,ISO-8859-14,ISO-8859-15,ISO-8859-16,windows-1250,windows-1251,windows-1252,windows-1256,windows-1257,cp437,cp737,cp850,cp852,cp866,x-cp866-u,x-mac,x-mac-ce,x-kam-cs,koi8-r,koi8-u,koi8-ru,TCVN-5712,VISCII,utf-8
Connection: close

"""

sock = socket(AF_INET, SOCK_STREAM) # AF_INET indicates -> use TCP/IP network protocol (IPv4).
                                    # SOCK_STREAM indicates -> use TCP (stream socket)
sock.connect((HOST, PORT))

ins, outs = sock.makefile("r"), sock.makefile("w")
# input_stream, output_stream

outs.write(HTTP_REQUEST)
outs.flush()

for line in ins:
    if line.startswith("Date:"):
        print(line)

outs.close()
ins.close()
sock.close()

