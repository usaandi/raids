import sqlite3
import requests
import time

LATEST_PRICES_URL = "https://prices.runescape.wiki/api/v1/osrs/latest"
MAPPING_URL = "https://prices.runescape.wiki/api/v1/osrs/mapping"
DB_FILE = "ge_prices.db"
EXPIRY_TIME = 10

HEADERS = {
    "User-Agent": "Item_prices/discord #us_ai"
}

def setup_database():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS ge_prices (
            item_id INTEGER PRIMARY KEY,
            item_name TEXT UNIQUE,
            price INTEGER,
            timestamp INTEGER
        )
    """)
    conn.commit()
    conn.close()

def fetch_ge_prices():
    """Fetches and stores GE prices in SQLite if outdated"""
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        # Check if data is fresh
        cursor.execute("SELECT MAX(timestamp) FROM ge_prices")
        last_update = cursor.fetchone()[0]

        if last_update and (time.time() - last_update) < EXPIRY_TIME:
            # Load from database
            cursor.execute("SELECT item_name, price FROM ge_prices")
            return dict(cursor.fetchall())

        # Fetch new data from OSRS Wiki API (with User-Agent)
        try:
            print('UPDATING PRICES')
            mapping_response = fetch_json(MAPPING_URL)
            prices_response = fetch_json(LATEST_PRICES_URL).get("data", {})
        except requests.RequestException as e:
            print(f"Error fetching OSRS Wiki API: {e}")
            return {}

        # Map item IDs to names
        ge_prices = {}
        for item in mapping_response:
            item_id = str(item["id"])
            item_name = item["name"]
            if item_id in prices_response:
                item_price = prices_response[item_id]["high"]  # Use "high" price as the most recent GE price
                ge_prices[item_name] = item_price

                # Insert or update database
                cursor.execute("""
                    INSERT INTO ge_prices (item_id, item_name, price, timestamp)
                    VALUES (?, ?, ?, ?)
                    ON CONFLICT(item_id) 
                    DO UPDATE SET price=excluded.price, timestamp=excluded.timestamp
                """, (item_id, item_name, item_price, int(time.time())))

        # Save to database
        conn.commit()

        return ge_prices

#get item prices
def get_item_prices(item_names):
    with sqlite3.connect(DB_FILE) as db:
        cursor = db.cursor()

        placeholders = ", ".join(["?"] * len(item_names))
        query = f"SELECT item_name, price FROM ge_prices WHERE item_name in ({placeholders})"
     
        cursor.execute(query, tuple(item_names))
        stored_prices = dict(cursor.fetchall())
    missing_items = set(item_names) - set(stored_prices)
    
    if missing_items:
        print(f"Fetching missing items: {missing_items}")
        fetch_ge_prices()
        return get_item_prices(item_names)
    
    return stored_prices

def fetch_json(url):
    try:
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return {}

setup_database()

fetch_ge_prices()