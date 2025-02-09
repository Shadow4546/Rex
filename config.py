# devgagan
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

# VPS --- FILL COOKIES 🍪 in """ ... """ 

INST_COOKIES = """
# wtite up here insta cookies
"""

YTUB_COOKIES = """
# write here yt cookies
"""

API_ID = int(getenv("API_ID", "28935416"))
API_HASH = getenv("API_HASH", "e18c05697d95edfe39d8957f6e110308")
BOT_TOKEN = getenv("BOT_TOKEN", "7823447094:AAFQIXNDKgLGe-JIaUDHvo0c9fbGv8JwQ8s")
OWNER_ID = list(map(int, getenv("OWNER_ID", "7170328188").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://kumarrajudrive:EsOA9GWnPLHPXF04@cluster0.mtn4u.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = getenv("LOG_GROUP", "-1002495769157")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002366085055"))
FREEMIUM_LIMIT = int(getenv("FREEMIUM_LIMIT", "50"))
PREMIUM_LIMIT = int(getenv("PREMIUM_LIMIT", "1000"))
WEBSITE_URL = getenv("WEBSITE_URL", "modijiurl.com")
AD_API = getenv("AD_API", "52b4a2cf4687d81e7d3f8f2b7bc2943f618e78cb")
STRING = getenv("STRING", None)
YT_COOKIES = getenv("YT_COOKIES", YTUB_COOKIES)
INSTA_COOKIES = getenv("INSTA_COOKIES", INST_COOKIES)
