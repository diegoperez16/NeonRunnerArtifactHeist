"""
Leaderboard integration — submits scores to the workshop's Supabase backend.

Setup:
  1. Copy supabase_config.example.json → supabase_config.json
  2. Fill in your Supabase URL and anon key
  3. Run the SQL in the workshop docs to create the scores table
"""

import json
import os

_BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_CONFIG_FILE = os.path.join(_BASE, 'supabase_config.json')
_PLAYER_FILE = os.path.join(_BASE, 'player_config.json')


def _load_config():
    try:
        with open(_CONFIG_FILE) as f:
            return json.load(f)
    except FileNotFoundError:
        return None


def get_username():
    """Return saved username, or None if not configured yet."""
    try:
        with open(_PLAYER_FILE) as f:
            return json.load(f).get('username')
    except FileNotFoundError:
        return None


def save_username(username: str):
    with open(_PLAYER_FILE, 'w') as f:
        json.dump({'username': username}, f)


def submit_score(username: str, score: int, game_time: float) -> bool:
    """
    POST a score entry to Supabase. Returns True on success.
    Silently fails if supabase_config.json is missing or network is down.
    """
    config = _load_config()
    if not config:
        return False

    try:
        import requests
    except ImportError:
        return False

    url = config['supabase_url'].rstrip('/') + '/rest/v1/scores'
    headers = {
        'apikey': config['supabase_anon_key'],
        'Authorization': f"Bearer {config['supabase_anon_key']}",
        'Content-Type': 'application/json',
    }
    payload = {
        'username': username,
        'score': score,
        'game_time': round(game_time, 1),
    }

    try:
        resp = requests.post(url, json=payload, headers=headers, timeout=5)
        return resp.status_code in (200, 201)
    except Exception:
        return False
