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
conn.execute("DROP TABLE IF EXISTS locations")
conn.execute("CREATE TABLE IF NOT EXISTS locations (id INTEGER PRIMARY KEY, placeid TEXT NOT NULL, name TEXT NOT NULL, lat REAL NOT NULL, lon REAL NOT NULL, address TEXT NOT NULL, sights REAL NOT NULL, nightlife REAL NOT NULL, casual REAL NOT NULL, shopping REAL NOT NULL)")

conn.execute("DROP TABLE IF EXISTS users")
conn.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT NOT NULL, lat REAL NOT NULL, lon REAL NOT NULL)")

conn.execute("DROP TABLE IF EXISTS rankings")
conn.execute("CREATE TABLE IF NOT EXISTS rankings (id INTEGER PRIMARY KEY, userid INTEGER NOT NULL, locationid INTEGER NOT NULL, enjoyment REAL NOT NULL, FOREIGN KEY(userid) REFERENCES users(id), FOREIGN KEY(locationid) REFERENCES locations(id))")

conn.commit()
conn.close()