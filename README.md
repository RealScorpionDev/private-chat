# Python TCP Chat Server

A simple multi-client TCP chat server built with Python sockets and threading.

This project demonstrates how a basic server can accept multiple client connections, receive messages, and broadcast them to other connected clients in real time.

---

## Features

- Multi-client support
- Real-time message broadcasting
- Uses Python's built-in `socket` module
- Uses `threading` to handle multiple clients at the same time
- Lightweight and beginner-friendly networking project

---

## How It Works

The server listens on port `9999` and waits for clients to connect.

When a client connects:

1. The client is added to the active clients list.
2. A new thread is created for that client.
3. The server listens for messages from that client.
4. When a message is received, it is sent to all other connected clients.

---

## Code Overview

```python
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("0.0.0.0", 9999))
server.listen(5)
