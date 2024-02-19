"""
Bot Token Configs
"""

from environs import Env

env = Env()
env.read_env()

BOT_TOKEN = env("BOT_TOKEN")
