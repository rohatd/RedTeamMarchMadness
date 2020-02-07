import dataScraper
import json

#dataScraper.getStats(["Rensselaer", "Army West Point", "Utah"])
dataScraper.getPlayerStats(["Rensselaer", "Army West Point", "Utah"])

with open('scrapeData.json', 'r') as f:
    IDs = json.load(f)
