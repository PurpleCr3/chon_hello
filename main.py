import json 
from linebot import LineBotApi
from linebot.models import TextSendMessage

file = open('info.json','r')
info = json.load(file)

CHNNNEL_ACCESS_TOKEN = info['CHNNNEL_ACCESS_TOKEN']
line_bot_api = LineBotApi(CHNNNEL_ACCESS_TOKEN)

def main():
    USER_ID = info['USER_ID']
    messages = TextSendMessage(text='ますみさん！\n おはようございます！')
    line_bot_api.push_message(USER_ID, messages = messages)

if __name__=="__main__":
    main()

