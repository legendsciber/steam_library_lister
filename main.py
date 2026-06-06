import os
import requests
import json

def list_games():
    url = "http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/"

    api_key = os.getenv("STEAM_API_KEY")
    steam_id = os.getenv("STEAM_ID")

    if not api_key or not steam_id:
        print("Missing STEAM_API_KEY or STEAM_ID environment variables.")
        return

    params = {
        'key': api_key,
        'steamid': steam_id,
        'include_appinfo': True,
        'format': 'json'
    }

    print("Fetching game list from Steam...")
    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        games = data.get('response', {}).get('games', [])

        if not games:
            print("No games found or profile is private! Check your privacy settings.")
            return

        games.sort(key=lambda x: x.get('name', '').lower())

        with open("steam_games.txt", "w", encoding="utf-8") as file:
            file.write(f"Total Games: {len(games)}\n")
            file.write("-" * 40 + "\n")

            for index, game in enumerate(games, 1):
                game_name = game.get('name')
                play_hours = round(game.get('playtime_forever', 0) / 60, 1)

                line = f"{index}. {game_name} ({play_hours} hrs)"
                print(line)
                file.write(line + "\n")

        print("\n" + "=" * 40)
        print(f"Success! {len(games)} games listed.")
        print("Saved to 'steam_games.txt'.")
    else:
        print(f"Error! Status Code: {response.status_code}")
        print("Check your API key or Steam ID.")

if __name__ == "__main__":
    try:
        list_games()
    except requests.exceptions.RequestException as e:
        print("Connection error:", e)