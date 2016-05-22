# -*- coding: utf-8 -*-

import sqlite3
import csv

sql = 'INSERT INTO combobox values (?,?,?)'

conexao = sqlite3.connect('Database/gsm.db')
c = conexao.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS coordenador (ID integer not null, NOME varchar not null, ATIVO blob, primary key (ID))')
    c.execute('CREATE TABLE IF NOT EXISTS combobox (ID integer not null, NOME varchar not null, ATIVO blob, primary key (ID))')



def INTO():

    f = csv.reader(open('Database/coord.csv'), delimiter=';')

    for row in f:
        print(row)
        c.execute(sql, row)
        conexao.commit()

def cbCoordenadorPop():

    sql = 'SELECT * from coordenador'

    return c.execute(sql)





#create_table()
#INTO()