import json
import os

CACHE_FILE = "/home/p-tech-fusion/BilalR./LnkdnBot/app/utils/data/cache.json"

cache = []

def load_cache():
    global cache
    if os.path.exists(CACHE_FILE):
        try:
            with open(CACHE_FILE, "r") as file:
                content = file.read().strip()
                if content:
                    cache = json.loads(content)
                    print("Cache loaded from file")
                else:
                    print("Cache file is empty, starting with an empty cache")
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}, starting with an empty cache")
            cache = []
    else:
        print("Cache file not found, starting with an empty cache")

def save_cache():
    with open(CACHE_FILE, "w") as file:
        json.dump(cache, file)
        print("Cache saved to file")

def insert_element(value):
    if value not in cache:
        cache.append(value)
        save_cache()
        print(f"Inserted: {value}")
    else:
        print(f"Value {value} already in cache")

def get_element(index):
    if 0 <= index < len(cache):
        return cache[index]
    else:
        print(f"Index {index} out of range")
        return None

def delete_element(value):
    if value in cache:
        cache.remove(value)
        save_cache()
        print(f"Deleted: {value}")
    else:
        print(f"Value {value} not found in cache")

def display_cache():
    print("Current Cache:", cache)

load_cache()

import atexit
atexit.register(save_cache)

