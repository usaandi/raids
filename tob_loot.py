import random
from ge_prices import fetch_ge_prices, get_item_prices


prices = fetch_ge_prices()

tob_loot = get_item_prices({
    "Scythe of vitur (uncharged)",
    "Sanguinesti staff (uncharged)",
    "Ghrazi rapier",
    "Avernic defender hilt",
    "Justiciar faceguard",
    "Justiciar chestguard",
    "Justiciar legguards",
    "Vial of blood", 
    "Death rune", 
    "Blood rune", 
    "Swamp tar", 
    "Coal",
    "Gold ore", 
    "Molten glass", 
    "Adamantite ore", 
    "Runite ore",
    "Wine of zamorak", 
    "Potato cactus", 
    "Grimy cadantine", 
    "Grimy avantoe",
    "Grimy toadflax", 
    "Grimy ranarr weed", 
    "Grimy kwuarm", 
    "Grimy irit leaf",
    "Grimy snapdragon", 
    "Grimy lantadyme", 
    "Grimy dwarf weed", 
    "Grimy torstol",
    "Battlestaff", 
    "Rune battleaxe", 
    "Rune platebody", 
    "Rune chainbody",
    "Palm tree seed", 
    "Yew seed", 
    "Magic seed", 
    "Mahogany seed"
})


tob_loot_table = {
    "uniques": {
        "Scythe of vitur (uncharged)": {
            "quantity": 1,
            "price": 1,
            "rate": 1/19
        },
        "Sanguinesti staff (uncharged)": {
            "quantity": 1,
            "price": 1,
            "rate": 2/19
        },
        "Ghrazi rapier": {
            "quantity": 1,
            "price": 1,
            "rate": 2/19
        },
        "Avernic defender hilt": {
            "quantity": 1,
            "price": 1,
            "rate": 8/19
        },
        "Justiciar faceguard": {
            "quantity": 1,
            "price": 1,
            "rate": 2/19
        },
        "Justiciar chestguard": {
            "quantity": 1,
            "price": 1,
            "rate": 2/19
        },
        "Justiciar legguards": {
            "quantity": 1,
            "price": 1,
            "rate": 2/19
        },
    },
    "normal_loot": {
        "Vial of blood": {
            "quantity": random.randint(45, 60),
            "price": 14_300,
            "rate": 1/15  # Special rate
        },
        "Death rune": {
            "quantity": random.randint(500, 600),
            "price": 170,
            "rate": 1/30
        },
        "Blood rune": {
            "quantity": random.randint(500, 600),
            "price": 299,
            "rate": 1/30
        },
        "Swamp tar": {
            "quantity": random.randint(500, 600),
            "price": 3,
            "rate": 1/30
        },
        "Coal": {
            "quantity": random.randint(500, 600),
            "price": 167,
            "rate": 1/30
        },
        "Gold ore": {
            "quantity": random.randint(300, 360),
            "price": 154,
            "rate": 1/30
        },
        "Molten glass": {
            "quantity": random.randint(200, 240),
            "price": 94,
            "rate": 1/30
        },
        "Adamantite ore": {
            "quantity": random.randint(130, 156),
            "price": 995,
            "rate": 1/30
        },
        "Runite ore": {
            "quantity": random.randint(60, 72),
            "price": 10_941,
            "rate": 1/30
        },
        "Wine of zamorak": {
            "quantity": random.randint(50, 60),
            "price": 950,
            "rate": 1/30
        },
        "Potato cactus": {
            "quantity": random.randint(50, 60),
            "price": 53,
            "rate": 1/30
        },
        "Grimy cadantine": {
            "quantity": random.randint(50, 60),
            "price": 3_190,
            "rate": 1/30
        },
        "Grimy avantoe": {
            "quantity": random.randint(40, 48),
            "price": 2_496,
            "rate": 1/30
        },
        "Grimy toadflax": {
            "quantity": random.randint(37, 44),
            "price": 2_865,
            "rate": 1/30
        },
        "Grimy ranarr weed": {
            "quantity": random.randint(30, 36),
            "price": 5_873,
            "rate": 1/30
        },
        "Grimy kwuarm": {
            "quantity": random.randint(36, 43),
            "price": 2_987,
            "rate": 1/30
        },  
        "Grimy irit leaf": {
            "quantity": random.randint(34, 40),
            "price": 1_175,
            "rate": 1/30
        },
        "Grimy snapdragon": {
            "quantity": random.randint(27, 32),
            "price": 7_917,
            "rate": 1/30
        },
        "Grimy lantadyme": {
            "quantity": random.randint(26, 31),
            "price": 1_701,
            "rate": 1/30
        },
        "Grimy dwarf weed": {
            "quantity": random.randint(24, 28),
            "price": 1_885,
            "rate": 1/30
        },
        "Grimy torstol": {
            "quantity": random.randint(20, 24),
            "price": 3_445,
            "rate": 1/30
        },
        "Battlestaff": {
            "quantity": random.randint(15, 18),
            "price": 8_178,
            "rate": 1/30
        },
        "Rune battleaxe": {
            "quantity": 4,
            "price": 24_227,
            "rate": 1/30
        },
        "Rune platebody": {
            "quantity": 4,
            "price": 38_378,
            "rate": 1/30
        },
        "Rune chainbody": {
            "quantity": 4,
            "price": 29_410,
            "rate": 1/30
        },
        "Palm tree seed": {
            "quantity": 3,
            "price": 17_842,
            "rate": 1/30
        },
        "Yew seed": {
            "quantity": 3,
            "price": 27_846,
            "rate": 1/30
        },
        "Magic seed": {
            "quantity": 3,
            "price": 105_649,
            "rate": 1/30
        },
        "Mahogany seed": {
            "quantity": random.randint(10, 12),
            "price": 803,
            "rate": 1/30
        }
    },
    "tertiary_rewards": {
        "clue_scroll (elite)": {
            "quantity": 1,
            "price": None,
            "rate": 1/20
        },
        "Holy ornament kit": {
            "quantity": 1,
            "price": None,
            "rate": 1/100,
            "hardmode": True
        },
        "Sanguine ornament kit": {
            "quantity": 1,
            "price": None,
            "rate": 1/150,
            "hardmode": True
        },
        "Sanguine dust": {
            "quantity": 1,
            "price": None,
            "rate": 1/275,
            "hardmode": True
        },
        "lil' zik": {
            "quantity": 1,
            "price": None,
            "rate": {
                1/650,
                1/500
            },   
        },
    }
}


for name, price_value in tob_loot.items():
    if name in tob_loot_table['uniques']:
        tob_loot_table['uniques'][name]['price'] = price_value
    elif name in tob_loot_table['normal_loot']:
        tob_loot_table["normal_loot"][name]['price'] = price_value


def get_tob_loot_table():
    return tob_loot_table