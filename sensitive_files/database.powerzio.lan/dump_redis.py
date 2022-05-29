from lib2to3.pytree import convert
from matplotlib.pyplot import show
import redis

ip = "10.10.10.132"
port = 6379
connectRedis = redis.Redis(ip, port)
keys = connectRedis.keys("*")

def show_passwd(user_id):
    i = 0
    end = len(user_id)
    string = []
    while i < end:
       string.append(chr(ord(user_id[i]) - 9)) # ord() function converts a character into an integer that represents the Unicode code of the character, the chr() function converts a Unicode code character into the corresponding string
       i = i + 1
    return "".join(string)


def convert_name(key):
    name = connectRedis.get(key).decode("utf-8")
    return (name)

def convert_user_id(key):
    user_id = key.decode("utf-8")
    return (user_id)

def display_database(name, user_id):
    print("NAME " + name + " PASSWORD " + show_passwd(user_id) + " USER_ID " + user_id)

for key in keys:
    display_database(convert_name(key), convert_user_id(key))