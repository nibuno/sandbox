import socket

# サーバーのホスト名とポート番号を指定
HOST = '127.0.0.1'  # サーバーのホスト名
PORT = 65432        # サーバーのポート番号

# ソケットを作成
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))  # サーバーに接続
    s.sendall(b'Hello, server')  # サーバーにデータを送信
    data = s.recv(1024)  # サーバーからのデータを受信

print(f"サーバーからの返信: {data.decode()}")
