import os
import sqlite3
from dotenv import dotenv_values


BASE_DIR = f"{os.getcwd()[:os.getcwd().index('fastapi_test_work04.2024')]}/fastapi_test_work04.2024"
env = dotenv_values(dotenv_path=os.path.join(BASE_DIR, "conf.env"))
DATABASE_URL = env["DATABASE_URL"]
connection = sqlite3.connect(os.path.abspath(DATABASE_URL))
connection.enable_load_extension(True)
connection.load_extension(os.path.normpath(f"{BASE_DIR}/{env['ENV_NAME']}/Lib/site-packages/sqlite_regex/regex0"))  # https://github.com/asg017/sqlite-regex?tab=readme-ov-file#as-a-loadable-extension


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
