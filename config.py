import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "27026389")

API_HASH = os.environ.get("API_HASH", "158b014213c39d3b342a8792e495a5dc")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6139931468:AAEInK7S9neJ5Z_IlJx3bWE8s7JWDvamFfU") 

FORCE_SUB = os.environ.get("FORCE_SUB", "-1001857528168") 

DB_NAME = os.environ.get("DB_NAME","Cluster0")     

DB_URL = os.environ.get("DB_URL","mongodb+srv://Hunterbots:Hunterbots@cluster0.il15reh.mongodb.net/?retryWrites=true&w=majority&appName=AtlasApp")

FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://graph.org/file/5fc119c05326d2595965f.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN','1601545124').split()]

PORT = os.environ.get("PORT", "8080")
