import sqlite3
import datetime


class DataBase:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()

    def _get_objects(self, table):
        try:
            self.__cur.execute(f'SELECT * FROM {table}')
            res = self.__cur.fetchall()
            if res:
                return res
        except IOError:
            print('Error while connecting to database')
        return []

    def get_menu(self):
        return self._get_objects('menu')

    def get_recipes(self):
        return self._get_objects('recipes')

    def get_recipe(self, recipe_title):
        try:
            self.__cur.execute(f'SELECT author, title, category, cooking_time, ingredients, instruction FROM recipes WHERE title == "{recipe_title}"')
            res = self.__cur.fetchone()
            if res:
                return res
        except IOError:
            print('Failed while searching for the recipe')
        return None, None, None, None, None, None

    def add_recipe(self, author, title, category, cooking_time, ingredients, instructions):
        try:
            self.__cur.execute(f'SELECT COUNT() as "count" FROM recipes WHERE title == "{title}"')
            res = self.__cur.fetchone()
            if res['count'] > 0:
                print('This recipe is already exists')
                return False
            dt_now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print(dt_now)
            self.__cur.execute(
                'INSERT INTO recipes VALUES (NULL, ?, ?, ?, ?, ?, ?, ?)',
                (author, title, category, cooking_time, ingredients, instructions, dt_now))
            self.__db.commit()
        except sqlite3.Error as e:
            print('Error while adding your recipe', e)
            return False
        return True