import socket, ssl
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(10)
wrapped = ssl.wrap_socket(sock, ssl_version=ssl.PROTOCOL_TLSv1_2)
wrapped.connect('172.17.0.3', 61613)
# openssl s_client -connect 172.17.0.3:61613