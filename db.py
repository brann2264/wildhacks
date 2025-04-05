import sqlite3

"""
LOCATIONS TABLE:
CREATE TABLE IF NOT EXISTS locations (
    id INTEGER PRIMARY KEY, 
    placeid TEXT NOT NULL, 
    name TEXT NOT NULL, 
    lat REAL NOT NULL, 
    lon REAL NOT NULL, 
    address TEXT NOT NULL, 
    sights REAL NOT NULL, 
    nightlife REAL NOT NULL, 
    casual REAL NOT NULL, 
    shopping REAL NOT NULL)

USERS TABLE:
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY, 
    name TEXT NOT NULL, 
    lat REAL NOT NULL, 
    lon REAL NOT NULL, 
    FOREIGN KEY(rankingid) REFERENCES rankings(userid)))

RANKINGS TABLE:
CREATE TABLE IF NOT EXISTS rankings (
    userid INTEGER PRIMARY KEY, 
    FOREIGN KEY(locationid) REFERENCES locations(id), 
    enjoyment REAL NOT NULL)
"""

conn = sqlite3.connect("tables.db")
conn.execute("CREATE TABLE IF NOT EXISTS locations (id INTEGER PRIMARY KEY, placeid TEXT NOT NULL, name TEXT NOT NULL, lat REAL NOT NULL, lon REAL NOT NULL, address TEXT NOT NULL, sights REAL NOT NULL, nightlife REAL NOT NULL, casual REAL NOT NULL, shopping REAL NOT NULL)")
conn.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT NOT NULL, lat REAL NOT NULL, lon REAL NOT NULL, FOREIGN KEY(rankingid) REFERENCES rankings(userid)))")
conn.execute("CREATE TABLE IF NOT EXISTS rankings (userid INTEGER PRIMARY KEY, FOREIGN KEY(locationid) REFERENCES locations(id), enjoyment REAL NOT NULL)")

conn.commit()
conn.close()