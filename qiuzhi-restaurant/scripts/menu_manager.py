#!/usr/bin/env python3
import json
import sys
import os

MENU_FILE = "../assets/menu.json"

def load_menu():
    if not os.path.exists(MENU_FILE):
        return {"items": []}
    with open(MENU_FILE, 'r') as f:
        return json.load(f)

def save_menu(menu):
    os.makedirs(os.path.dirname(MENU_FILE), exist_ok=True)
    with open(MENU_FILE, 'w') as f:
        json.dump(menu, f, indent=2, ensure_ascii=False)

def add_item(name, price):
    menu = load_menu()
    menu["items"].append({"name": name, "price": float(price)})
    save_menu(menu)
    print(f"✅ Added: {name} - ${price}")

def list_menu():
    menu = load_menu()
    print("📋 Current Menu:")
    for item in menu["items"]:
        print(f"- {item['name']}: ${item['price']}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 menu_manager.py [add <name> <price> | list]")
        sys.exit(1)
    
    cmd = sys.argv[1]
    if cmd == "add":
        add_item(sys.argv[2], sys.argv[3])
    elif cmd == "list":
        list_menu()
