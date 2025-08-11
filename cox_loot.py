from ge_prices import fetch_ge_prices, get_item_prices

fetch_ge_prices()

cox_loot = get_item_prices({
    "Dexterous prayer scroll",
    "Arcane prayer scroll",
    "Twisted buckler",
    "Dragon hunter crossbow",
    "Dinh's bulwark",
    "Ancestral hat",
    "Ancestral robe top",
    "Ancestral robe bottom",
    "Dragon claws",
    "Elder maul",
    "Kodai insignia",
    "Twisted bow",
    "Death rune",
    "Blood rune",
    "Soul rune",
    "Rune arrow",
    "Dragon arrow",
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
    "Silver ore",
    "Coal",
    "Gold ore",
    "Mithril ore",
    "Adamantite ore",
    "Runite ore",
    "Uncut sapphire",
    "Uncut emerald",
    "Uncut ruby",
    "Uncut diamond",
    "Lizardman fang",
    "Pure essence",
    "Saltpetre",
    "Teak plank",
    "Mahogany plank",
    "Dynamite",
    "Torn prayer scroll",
})

cox_loot_table = {
    "uniques": {
        "Dexterous prayer scroll": {
            "quantity": 1,
            "price": 1,
            "rate": 1/3.45
        },
        "Arcane prayer scroll": {
            "quantity": 1,
            "price": 1,
            "rate": 1/3.45
        },
        "Twisted buckler": {
            "quantity": 1,
            "price": 1,
            "rate": 1/17.25
        },
        "Dragon hunter crossbow": {
            "quantity": 1,
            "price": 1,
            "rate": 1/17.25
        },
        "Dinh's bulwark": {
            "quantity": 1,
            "price": 1,
            "rate": 1/23
        },
        "Ancestral hat": {
            "quantity": 1,
            "price": 1,
            "rate": 1/23
        },
        "Ancestral robe top": {
            "quantity": 1,
            "price": 1,
            "rate": 1/23
        },
        "Ancestral robe bottom": {
            "quantity": 1,
            "price": 1,
            "rate": 1/23
        },
        "Dragon claws": {
            "quantity": 1,
            "price": 1,
            "rate": 1/23
        },
        "Elder maul": {
            "quantity": 1,
            "price": 1,
            "rate": 1/34.5
        },
        "Kodai insignia": {
            "quantity": 1,
            "price": 1,
            "rate": 1/34.5
        },
        "Twisted bow": {
            "quantity": 1,
            "price": 1,
            "rate": 1/34.5
        },
    },
    "normal_loot": {
        "Death rune": {
            "quantity": 3640,
        },
        "Blood rune": {
            "quantity": 4095
        },
        "Soul rune": {
            "quantity": 6553
        },
        "Rune arrow": {
            "quantity": 9362
        },
        "Dragon arrow": {
            "quantity": 648
        },
        "Grimy cadantine": {
            "quantity": 394,
        },
        "Grimy avantoe": {
            "quantity": 404,
        },
        "Grimy toadflax": {
            "quantity": 248,
        },
        "Grimy ranarr weed": {
            "quantity": 163,
        },
        "Grimy kwuarm": {
            "quantity": 338,
        },  
        "Grimy irit leaf": {
            "quantity": 809,
        },
        "Grimy snapdragon": {
            "quantity": 100,
        },
        "Grimy lantadyme": {
            "quantity": 526,
        },
        "Grimy dwarf weed": {
            "quantity": 655,
        },
        "Grimy torstol": {
            "quantity": 161,
        },
        "Silver ore": {
            "quantity": 6553
        },
        "Coal": {
            "quantity": 6553
        },
        "Gold ore": {
            "quantity": 2978
        },
        "Mithril ore": {
            "quantity": 4095
        },
        "Adamantite ore": {
            "quantity": 789
        },
        "Runite ore": {
            "quantity": 65
        },
        "Uncut sapphire": {
            "quantity": 693
        },
        "Uncut emerald":{
            "quantity": 923
        },
        "Uncut ruby": {
            "quantity": 541
        },
        "Uncut diamond": {
            "quantity": 255
        },
        "Lizardman fang": {
            "quantity": 4681
        },
        "Pure essence": {
            "quantity": 65535
        },
        "Saltpetre": {
            "quantity": 5461
        },
        "Teak plank": {
            "quantity": 1365
        },
        "Mahogany plank": {
            "quantity": 548
        },
        "Dynamite": {
            "quantity": 2427
        },
        "Torn prayer scroll": {
            "quantity": 1,

        },
        "Dark relic": {
            "quantity": 1,
            "tradeable": False,
            "price": 1
        }
    }
}


for name, price_value in cox_loot.items():
    if name in cox_loot_table['uniques']:
        cox_loot_table['uniques'][name]['price'] = price_value
    elif name in cox_loot_table['normal_loot']:
        cox_loot_table["normal_loot"][name]['price'] = price_value
        
        
def get_cox_loot_table():
    return cox_loot_table