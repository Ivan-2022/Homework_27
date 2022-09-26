import csv
import json


def csv_to_json_ads(csvfilepath_ads, jsonfilepath_ads):
    json_ads = []
    with open(csvfilepath_ads, encoding='utf-8') as csvf:
        data = csv.DictReader(csvf)
        for row in data:
            json_ads.append({
                "model": "ads.ads",
                "pk": int(row["Id"]),
                "fields": {
                    "name": row["name"],
                    "author": row["author"],
                    "price": int(row["price"]),
                    "description": row["description"],
                    "address": row["address"],
                    "is_published": (True if row["is_published"] == 'TRUE' else False)
                }
            })

    with open(jsonfilepath_ads, 'w', encoding='utf-8') as jsonf:
        json_s = json.dumps(json_ads, ensure_ascii=False, indent=4)
        jsonf.write(json_s)


def csv_to_json_cat(csvfilepath_cat, jsonfilepath_cat):
    json_cat = []
    with open(csvfilepath_cat, encoding='utf-8') as csvf:
        data = csv.DictReader(csvf)
        for row in data:
            json_cat.append({
                "model": "ads.category",
                "pk": int(row["id"]),
                "fields": {"name": row["name"], }})

    with open(jsonfilepath_cat, 'w', encoding='utf-8') as jsonf:
        json_s = json.dumps(json_cat, ensure_ascii=False, indent=4)
        jsonf.write(json_s)


csvfilepath_ads = r'ads.csv'
jsonfilepath_ads = r'ads.json'

csvfilepath_cat = r'categories.csv'
jsonfilepath_cat = r'categories.json'


csv_to_json_ads(csvfilepath_ads, jsonfilepath_ads)

csv_to_json_cat(csvfilepath_cat, jsonfilepath_cat)
