import re
from os import environ,getenv
from Script import script

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default
#---------------------------------------------------------------
#---------------------------------------------------------------         ,
SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ.get('API_ID', '29171167'))
API_HASH = environ.get('API_HASH', '7ea2149629e445936619f06a3c0dc716')
BOT_TOKEN = environ.get('BOT_TOKEN', '')
#---------------------------------------------------------------
#---------------------------------------------------------------
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '1049173662 7251898668').split()]
USERNAME = environ.get('USERNAME', "https://t.me/AK_ownerbot") # ADMIN USERNAME
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1002241963214'))
MOVIE_GROUP_LINK = environ.get('MOVIE_GROUP_LINK', 'https://t.me/+2i0adOH6KRNlYWQ1')
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '-1002244361548 -1002432115506').split()]
#---------------------------------------------------------------
#---------------------------------------------------------------
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://ak:ak@cluster0.coguvzb.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DATABASE_NAME = environ.get('DATABASE_NAME', "Cluster0")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'techvjcollection')
#---------------------------------------------------------------
#---------------------------------------------------------------
#----------- There will be channel id add in all these ---------
LOG_API_CHANNEL = int(environ.get('LOG_API_CHANNEL', '-1002260577001'))  # set shortner log channel
DELETE_CHANNELS = int(environ.get('DELETE_CHANNELS','')) # The movie you upload in it will be deleted from the bot.
LOG_VR_CHANNEL = int(environ.get('LOG_VR_CHANNEL', '-1002374999695'))
auth_channel = environ.get('AUTH_CHANNEL', '-1002442422204')
SUPPORT_GROUP = int(environ.get('SUPPORT_GROUP', '-1002401879443'))
request_channel = environ.get('REQUEST_CHANNEL', '-1002258541880') # If anyone sends a request message to your bot, you will get it in this channel.
MOVIE_UPDATE_CHANNEL = int(environ.get('MOVIE_UPDATE_CHANNEL', '-1002456609565')) # 
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'https://t.me/+U9ABfC7hu1EyZjU1') #Support group link ( make sure bot is admin )
#---------------------------------------------------------------
#---------------------------------------------------------------
IS_VERIFY = is_enabled('IS_VERIFY', True)
#---------------------------------------------------------------
TUTORIAL = environ.get("TUTORIAL", "https://t.me/akhowtoopenlinks/32")
TUTORIAL_2 = environ.get("TUTORIAL_2", "https://t.me/akhowtoopenlinks/32")
TUTORIAL_3 = environ.get("TUTORIAL_3", "")
VERIFY_IMG = environ.get("VERIFY_IMG", "https://graph.org/file/1669ab9af68eaa62c3ca4.jpg")
SHORTENER_API = environ.get("SHORTENER_API", "95c90443f0324be097970c3f704e16eca7116c81")
SHORTENER_WEBSITE = environ.get("SHORTENER_WEBSITE", 'shortxlinks.com')
SHORTENER_API2 = environ.get("SHORTENER_API2", "95c90443f0324be097970c3f704e16eca7116c81")
SHORTENER_WEBSITE2 = environ.get("SHORTENER_WEBSITE2", 'shortxlinks.com')
SHORTENER_API3 = environ.get("SHORTENER_API3", "")
SHORTENER_WEBSITE3 = environ.get("SHORTENER_WEBSITE3", '')
TWO_VERIFY_GAP = int(environ.get('TWO_VERIFY_GAP', "43200"))
THREE_VERIFY_GAP = int(environ.get('THREE_VERIFY_GAP', "14400"))
#---------------------------------------------------------------
#---------------------------------------------------------------
LANGUAGES = ["hindi", "english", "telugu", "tamil", "kannada", "malayalam", "bengali", "marathi", "gujarati", "punjabi", "marathi"]
QUALITIES = ["HdRip","web-dl" ,"bluray", "hdr", "fhd" , "240p", "360p", "480p", "540p", "720p", "960p", "1080p", "1440p", "2K", "2160p", "4k", "5K", "8K"]
YEARS = [f'{i}' for i in range(2025, 2002,-1 )]
SEASONS = [f'season {i}'for i in range (1 , 23)]
REF_PREMIUM = 30
PREMIUM_POINT = 1500
#---------------------------------------------------------------
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
REQUEST_CHANNEL = int(request_channel) if request_channel and id_pattern.search(request_channel) else None
#---------------------------------------------------------------
#---------------------------------------------------------------
#---------------------------------------------------------------
START_IMG = (environ.get('START_IMG', 'https://envs.sh/EV5.jpg https://envs.sh/EVL.jpg')).split()
FORCESUB_IMG = environ.get('FORCESUB_IMG', 'https://i.ibb.co/ZNC1Hnb/ad3f2c88a8f2.jpg')
REFER_PICS = (environ.get("REFER_PICS", "https://envs.sh/PSI.jpg")).split() 
PAYPICS = (environ.get('PAYPICS', 'https://envs.sh/a_.jpg')).split()
SUBSCRIPTION = (environ.get('SUBSCRIPTION', 'https://envs.sh/a_.jpg'))
REACTIONS = ["👀", "😱", "🔥", "😍", "🎉", "🥰", "😇", "⚡"]
#---------------------------------------------------------------
#---------------------------------------------------------------
#---------------------------------------------------------------
FILE_AUTO_DEL_TIMER = int(environ.get('FILE_AUTO_DEL_TIMER', '1800'))
AUTO_FILTER = is_enabled('AUTO_FILTER', True)
IS_PM_SEARCH = is_enabled('IS_PM_SEARCH', True)
IS_SEND_MOVIE_UPDATE = is_enabled('IS_SEND_MOVIE_UPDATE', True) # Don't Change It ( If You Want To Turn It On Then Turn It On By Commands) We Suggest You To Make It Turn Off If You Are Indexing Files First Time.
PORT = environ.get('PORT', '5000')
MAX_BTN = int(environ.get('MAX_BTN', '8'))
AUTO_DELETE = is_enabled('AUTO_DELETE', True)
DELETE_TIME = int(environ.get('DELETE_TIME', 1200))
IMDB = is_enabled('IMDB', False)
FILE_CAPTION = environ.get('FILE_CAPTION', f'{script.FILE_CAPTION}')
IMDB_TEMPLATE = environ.get('IMDB_TEMPLATE', f'{script.IMDB_TEMPLATE_TXT}')
LONG_IMDB_DESCRIPTION = is_enabled('LONG_IMDB_DESCRIPTION', False)
PROTECT_CONTENT = is_enabled('PROTECT_CONTENT', False)
SPELL_CHECK = is_enabled('SPELL_CHECK', True)
LINK_MODE = is_enabled('LINK_MODE', False)

#---------------------------------------------------------------
#---------------------------------------------------------------
#---------------------------------------------------------------
STREAM_MODE = bool(environ.get('STREAM_MODE', True)) # Set True or Flase
# Online Stream and Download

MULTI_CLIENT = False
SLEEP_THRESHOLD = int(environ.get('SLEEP_THRESHOLD', '60'))
PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
if 'DYNO' in environ:
    ON_HEROKU = True
else:
    ON_HEROKU = False
URL = environ.get("FQDN", "")

#---------------------------------------------------------------
#---------------------------------------------------------------
SETTINGS = {
            'spell_check': SPELL_CHECK,
            'auto_filter': AUTO_FILTER,
            'file_secure': PROTECT_CONTENT,
            'auto_delete': AUTO_DELETE,
            'template': IMDB_TEMPLATE,
            'caption': FILE_CAPTION,
            'tutorial': TUTORIAL,
            'tutorial_2': TUTORIAL_2,
            'tutorial_3': TUTORIAL_3,
            'shortner': SHORTENER_WEBSITE,
            'api': SHORTENER_API,
            'shortner_two': SHORTENER_WEBSITE2,
            'api_two': SHORTENER_API2,
            'log': LOG_VR_CHANNEL,
            'imdb': IMDB,
            'link': LINK_MODE, 
            'is_verify': IS_VERIFY, 
            'verify_time': TWO_VERIFY_GAP,
            'shortner_three': SHORTENER_WEBSITE3,
            'api_three': SHORTENER_API3,
            'third_verify_time': THREE_VERIFY_GAP
}

admin_cmds = [
    "/add_premium", "/premium_users", "/remove_premium", "/add_redeem",
    "/refresh", "/set_muc", "/pm_search_on", "/pm_search_off",
    "/set_ads", "/del_ads", "/setlist", "/clearlist",
    "/verify_id", "/index", "/send", "/leave",
    "/ban", "/unban", "/broadcast", "/grp_broadcast",
    "/delreq", "/channel", "/del_file", "/delete",
    "/deletefiles", "/deleteall", 
    "All These Commands Can Be Used Only By Admins.", 
    "⚡ powered by @AKMOVIEBOTZ"
]

cmds = [
    {"start": "Start The Bot"},
    {"most": "Get Most Searches Button List"},
    {"trend": "Get Top Trending Button List"},
    {"mostlist": "Show Most Searches List"},
    {"trendlist": "𝖦𝖾𝗍 𝖳𝗈𝗉 𝖳𝗋𝖾𝗇𝖽𝗂𝗇𝗀 𝖡𝗎𝗍𝗍𝗈𝗇 𝖫𝗂𝗌t"},
    {"plan": "Check Available Premium Membership Plans"},
    {"myplan": "Check Your Currunt Plan"},
    {"refer": "To Refer Your Friend And Get Premium"},
    {"stats": "Check My Database"},
    {"id": "Get Telegram Id"},
    {"font": "To Generate Cool Fonts"},
    {"details": "Check Group Details"},
    {"settings": "Change Bot Setting"},
    {"grp_cmds": "Check Group Commands"},
    {"admin_cmds": "Bot Admin Commands"}
]
