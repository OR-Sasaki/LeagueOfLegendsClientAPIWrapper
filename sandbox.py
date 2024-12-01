import lol_game_client_api_wrapper as lw

if lw.life_check():
    print("ゲームを確認しました. life_check ok")
else:
    print("ゲームが起動していません. life_check failed")

result = lw.all_game_data()

# 取得したゲームデータ
print(result.data)

# サモナーネームなどを取得できる
print("summoner_name: " + result.active_player.summoner_name)
