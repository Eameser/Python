import socket

sock = socket.socket()
sock.bind(('', 9090))
sock.listen(1)
conn, addr = sock.accept()
while True:
    data = conn.recv(1024).decode()
    if not data:
        break
    s = data
    s_list = s.split()
    reversred_list = []
    for i in s_list:
        reversred_list.append(i[::-1])
    m = ' '.join(reversred_list)
    print(m)
    conn.send(m.encode())
conn.close()