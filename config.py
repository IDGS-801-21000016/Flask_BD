import os
from sqlalchemy import create_engine
import urllib
from dataclasses import dataclass


@dataclass
class Config():
  SECRET_KEY: str = 'secret'
  SECRET_COOKIE: str = 'secret'


@dataclass
class DevConfig(Config):
  DEBUG: bool = True
  SQLALCHEMY_DATABASE_URI: str = 'mysql+pymysql://jonarro:Ganondorf09#@127.0.0.1:3306/bdidgs801'
  SQLALCHEMY_TRACK_MODIFICATIONS: bool = False