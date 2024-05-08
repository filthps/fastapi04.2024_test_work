import os
import sqlite3
from dotenv import dotenv_values


ENV = dotenv_values(dotenv_path="../../conf.env")
DATABASE_URL = ENV["DATABASE_URL"]
connection = sqlite3.connect(os.path.abspath(DATABASE_URL))
connection.enable_load_extension(True)
connection.load_extension(f"../{ENV['ENV_NAME']}/Lib/site-packages/sqlite_regex/regex0")  # windows конфигурация https://github.com/asg017/sqlite-regex?tab=readme-ov-file#as-a-loadable-extension


def set_up():
    ddl_items = open(os.path.normpath(f"{os.path.abspath('init.sql')}"), mode="r", encoding="utf-8", newline="\r")
    sql_text = ddl_items.read()
    ddl_items.close()
    sqlite3.complete_statement(sql_text)
    cursor = connection.cursor()
    cursor.executescript(sql_text)
    connection.commit()
    cursor.close()
    connection.close()


if __name__ == "__main__":
    set_up()
