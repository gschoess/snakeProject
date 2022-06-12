#! /usr/bin/env python
# -*- coding: utf-8 -*
import sqlite3


class HighscoreDB:
    def __init__(self):
        self.location = 'db/highscore_db'
        self.connection = sqlite3.connect(self.location)
        self.cursor = self.connection.cursor()
        self.create_table()
        self.get_highscores()

    def create_table(self):
        """Function to create the table in the SQLite database
        for the highscore.
        """
        self.cursor.execute('''
            SELECT name FROM sqlite_master 
                WHERE type='table' 
                AND name='highscore_db';
        ''')
        if self.cursor.fetchone():
            print('Datenbank vorhanden')
        else:
            self.cursor.execute('''
                  CREATE TABLE highscore_db(
                     id INTEGER PRIMARY KEY,
                     name text,
                     score int
                  );
            ''')
            self.connection.commit()
            print('Datenbank erstellt')

    def add_to_highscore(self, name, score):
        sql = '''INSERT INTO highscore_db(name, score) VALUES(?, ?)'''
        self.cursor.execute(sql, (name, score))
        self.connection.commit()

    def get_highscores(self):
        sql = '''SELECT name, score FROM highscore_db ORDER BY score DESC 
        LIMIT 10'''
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def get_tenth_highscore(self):
        highscores = self.get_highscores()
        if len(highscores) == 10:
            return highscores[-1][1]
        else:
            return 0

    # TODO close connection!?
