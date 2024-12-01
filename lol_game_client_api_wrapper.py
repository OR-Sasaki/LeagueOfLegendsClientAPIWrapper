import socket
import requests
from data_types.all_game_data import AllGameData

HOST = "127.0.0.1"
PORT = 2999

def life_check() -> bool:
    # ゲームクライアントが立ち上がると127.0.0.1:2999が使われるため、それを検知するためのメソッド

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((HOST, PORT))
        s.close()

        return True
    except socket.error as e:
        return False

def base_url() -> str:
    return f"""https://{HOST}:{PORT}"""

def all_game_data() -> AllGameData:
    # TODO: SSLのルート証明書と通して検証する必要がある
    # Game Client API >  Root Certificate/SSL Errors を参照
    # https://developer.riotgames.com/docs/lol#game-client-api
    result = requests.get(f"""{base_url()}/liveclientdata/allgamedata""", verify=False)

    return AllGameData(result.json())

# TODO: 他のAPIも実装する
