import socket

# サーバーのホスト名とポート番号を指定
HOST = '127.0.0.1'  # ローカルホスト
PORT = 65432        # 使用するポート

# ソケットを作成
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))  # ホストとポートにバインド
    s.listen()  # 接続を待つ

    print(f"サーバーは{HOST}:{PORT}で待機しています...")

    conn, addr = s.accept()  # クライアントからの接続を受け入れる
    with conn:
        print(f"接続されました: {addr}")
        while True:
            data = conn.recv(1024)  # データを受信（最大1024バイト）
            if not data:
                break
            print(f"受信: {data.decode()}")
            conn.sendall(data)  # クライアントにデータを送り返す（エコー）
