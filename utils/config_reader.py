import configparser

config=configparser.ConfigParser()
config.read("Config/config.ini")
#print(files)

BASE_URL=config["API"]["BASE_URL"]
USERNAME=config["AUTH"]["USERNAME"]
PASSWORD=config["AUTH"]["PASSWORD"]


