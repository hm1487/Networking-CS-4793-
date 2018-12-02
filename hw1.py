import socket

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

sock.bind(("127.0.0.1",8080))

sock.listen()
request = 0
print("Serving up smiles on 8080")
while True:
	(conn, (ip, port)) = sock.accept()
	response = conn.recv(8080)
	if (response):
		request+=1
	#print(response)
	response = response.decode('ascii')
	response = response.split(" ")
	request_type = response[0]
	response = response[1]
	if (response[0] == 'GET'):
		if (response == "/page2"):
			html = """<HTML><HEAD><TITLE>HTTP Homework</TITLE></HEAD><BODY><H3><CENTER>HTTP Homework</CENTER></H3>This is page 2<P>You can go <A HREF='/'>back</A> <P><CENTER>This server has been used""" + str(request) + """ times</CENTER></BODY></HTML>"""
			conn.send(b'HTTP/1.0 200 OK\r\n')
			conn.send(b'Server: hm1487\r\n')
			conn.send(b"Content Length: " + bytes(str(len(html)),encoding='ascii'))
			conn.send(b'Content-Type: text/html\r\n')
			conn.send(b'Connection: Closed\r\n')
			conn.send(b'\r\n')
			conn.send(bytes(html,encoding='ascii'))
		elif (response == "/page3"):
			html = """<HTML><HEAD><TITLE>HTTP Homework</TITLE></HEAD><BODY><H3><CENTER>HTTP Homework</CENTER></H3>This is page 3<P>You can go <A HREF='/'>back</A> <P><CENTER>This server has been used""" + str(request) + """ times</CENTER></BODY></HTML>"""
			conn.send(b'HTTP/1.0 200 OK\r\n')
			conn.send(b'Server: hm1487\r\n')
			conn.send(b"Content Length: " + bytes(str(len(html)),encoding='ascii'))
			conn.send(b'Content-Type: text/html\r\n')
			conn.send(b'Connection: Closed\r\n')
			conn.send(b'\r\n')
			conn.send(bytes(html,encoding='ascii'))
		elif (response == "/"):
			html = """<HTML><HEAD><TITLE>HTTP Homework</TITLE></HEAD><BODY><H3><CENTER>HTTP Homework</CENTER></H3>This is the main page<P>You can click on <A HREF='/page2'>page2</A> or <A HREF='/page3'>or Page 3</A><P><CENTER>This server has been used """ + str(request) + """ times</CENTER></BODY></HTML>"""
			conn.send(b'HTTP/1.0 200 OK\r\n')
			conn.send(b'Server: hm1487\r\n')
			conn.send(b"Content Length: " + bytes(str(len(html)),encoding='ascii'))
			conn.send(b'Content-Type: text/html\r\n')
			conn.send(b'Connection: Closed\r\n')
			conn.send(b'\r\n')
			conn.send(bytes(html,encoding='ascii'))
		else:
			html = """<h3>Wow! You've found a way to mess everything up! Great Job! :'  )</h3><br><h3>This server has been used """ + str(request) + """ times"""
			conn.send(b'HTTP/1.0 404 NOT FOUND\r\n')
			conn.send(b'hm1487\r\n')
			conn.send(b"Content Length: " + bytes(str(len(html)),encoding='ascii'))
			conn.send(b'Content-Type: text/html\r\n')
			conn.send(b'Connection: Closed\r\n')
			conn.send(b'\r\n')
			conn.send(bytes(html,encoding='ascii'))
	else:
		html = """<h3>Wow! You've found a way to mess everything up! Great Job! :'  )</h3><br><h3>This server has been used """ + str(request) + """ times"""
		conn.send(b'HTTP/1.0 404 NOT FOUND\r\n')
		conn.send(b'hm1487\r\n')
		conn.send(b"Content Length: " + bytes(str(len(html)),encoding='ascii'))
		conn.send(b'Content-Type: text/html\r\n')
		conn.send(b'Connection: Closed\r\n')
		conn.send(b'\r\n')
		conn.send(bytes(html,encoding='ascii'))
	conn.close()


