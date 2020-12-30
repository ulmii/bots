from rasa.jupyter import chat
import nest_asyncio
import requests
# nest_asyncio.apply()

model_path = '/mnt/c/P/studia/skrypty/scripts-hw/retrievalbased/assistant/models/20201230-124237.tar.gz'
chat(model_path)