# steam-library-lister

A lightweight Python script that fetches your Steam game library with playtime via the Steam Web API and exports it to a text file.

## Requirements

- Python 3.6+
- `requests` library (`pip install requests`)

## Setup

1. Get a Steam API key from [https://steamcommunity.com/dev/apikey](https://steamcommunity.com/dev/apikey)
2. Find your Steam ID (17-digit numeric ID)
3. Set environment variables:

```powershell
$env:STEAM_API_KEY = "your_api_key"
$env:STEAM_ID = "your_steam_id"
```

Or on Linux/macOS:

```bash
export STEAM_API_KEY="your_api_key"
export STEAM_ID="your_steam_id"
```

## Usage

```bash
python main.py
```

Output is saved to `steam_games.txt`.
