import logging
import sqlite3

logger = logging.getLogger("app_logger")

def get_db_version():
  try:
      sqliteConnection = sqlite3.connect('fastapi_logging_demo.db')
      cursor = sqliteConnection.cursor()
      logger.info("Database created and Successfully Connected to SQLite")
      sqlite_select_Query = "select sqlite_version();"
      cursor.execute(sqlite_select_Query)
      record = cursor.fetchall()
      logger.info("SQLite Database Version is: ".format(record))
      cursor.close()
      return record

  except sqlite3.Error as error:
      logger.error("Error while connecting to sqlite".format(error))
      print("Error while connecting to sqlite", error)
      raise

  except Exception as error:
      logger.error("Error while getting db version".format(error))
      print("Error while getting db version", error)
      raise

  finally:
      if sqliteConnection:
          sqliteConnection.close()
          print("The SQLite connection is closed")