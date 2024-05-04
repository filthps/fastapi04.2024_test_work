import os
import sqlite3
from dotenv import dotenv_values


ENV = dotenv_values(dotenv_path="../conf.env")
DATABASE_URL = ENV["DATABASE_URL"]
connection = sqlite3.connect(os.path.abspath(DATABASE_URL))


if __name__ == "__main__":
    ddl_items = open(os.path.normpath(f"{os.path.abspath('init.sql')}"), mode="r", encoding="utf-8", newline="\r")
    sql_text = ddl_items.read()
    ddl_items.close()
    sqlite3.complete_statement(sql_text)
    cursor = connection.cursor()
    cursor.executescript(sql_text)
    connection.commit()
    cursor.close()
    connection.close()
