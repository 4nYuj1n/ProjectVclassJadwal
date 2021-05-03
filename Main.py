import PythonScrapper
import toSql
import fromSQL
import TelegramBot
import time
def run():
    #fetch data from vclass
    PythonScrapper.run()
    #send data to mySQL from vclass
    toSql.run()
    #get data from mySQL
    fromSQL.run()
    #send list to bot
    TelegramBot.run()
if __name__=='__main__':
    run()