import asyncio
import discord
from discord.ext import commands
import sqlite3
import math
import time

serverDB = ''
def create_table(name):
    conn = sqlite3.connect('{}.db'.format(name))
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS classes(user TEXT, level REAL, role TEXT)')
    c.close()
    conn.close()
    serverDB= '{}.db'.format(name)



def read_from_db():
    conn = sqlite3.connect(serverDB)
    c = conn.cursor()
    c.execute('SELECT * FROM classes',)
    data = c.fetchall()
    if(data[0] == 'nyzzik'):
        print(data)
    else:
        print(data[0])
    c.close()
    conn.close()

def db_get_user(user: str):
    conn = sqlite3.connect(serverDB)
    c = conn.cursor()
    c.execute('SELECT * FROM classes WHERE user = (?)', (user,))
    data = c.fetchall()
    c.close()
    conn.close()
    return data

def get_user_level(user: str):
    conn = sqlite3.connect(serverDB)
    c = conn.cursor()
    c.execute('SELECT * FROM classes WHERE user = (?)', (user,))
    temp = c.fetchone()
    testlevel = temp[1]
    c.close()
    conn.close()

    return testlevel

def update_user_level(user: str, level: float):
    conn = sqlite3.connect(serverDB)
    c = conn.cursor()
    c.execute('UPDATE (?) SET level = classes WHERE user = (?)', (level, user))
    conn.commit()
    c.close()
    conn.close()

def user_level_up(user: str):
    conn = sqlite3.connect(serverDB)
    c = conn.cursor()
    keplevel = get_user_level(user)
    update_user_level(user, (keplevel + 0.2))
    c.close()
    conn.close()

def data_entry(user: str, level: float, role: str):
    conn = sqlite3.connect(serverDB)
    c = conn.cursor()
    c.execute("INSERT INTO classes(user, level, role) VALUES (?, ?, ?)",
                (user, level, role))
    conn.commit()
    c.close()
    conn.close()

def delete_user(user: str):
    conn = sqlite3.connect(serverDB)
    c = conn.cursor()
    c.execute("DELETE FROM classes WHERE user = (?))", (user,))
    conn.commit()
    c.close()
    conn.close()

def user_get_role(user: str):
    conn = sqlite3.connect(serverDB)
    c = conn.cursor()
    c.execute('SELECT * FROM classes WHERE user = (?)', (user,))
    temp = c.fetchone()
    role = temp[2]
    c.close()
    conn.close()
    return role 