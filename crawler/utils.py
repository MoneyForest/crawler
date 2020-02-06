import os

def is_development():
    return os.environ['ENV'] == 'development'

