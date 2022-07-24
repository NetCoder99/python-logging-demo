import logging

def get_file_handler(name, file_name, formatter, level=logging.INFO, file_mode="a"):
  tmp_handler = logging.FileHandler(file_name, mode=file_mode)
  tmp_handler.setLevel(level)
  tmp_handler.setFormatter(formatter)
  tmp_handler.set_name(name)
  return tmp_handler

def get_db_handler(name, file_name, formatter, level=logging.INFO, file_mode="a"):
  tmp_handler = logging.FileHandler(file_name, mode=file_mode)
  tmp_handler.setLevel(level)
  tmp_handler.setFormatter(formatter)
  tmp_handler.set_name(name)
  return tmp_handler

