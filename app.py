from datetime import datetime

class App:
    def __init__(self, dbCon):
        self.dbCon = dbCon
        print("Started app")
    def send(self, src, msg):
        now = datetime.now()
        date_time = now.strftime("%Y-%m-%dT%H:%M:%S")
        result = self.dbCon.send("""
            insert into messages (src, msg, ts_cre)
            values ('%s', '%s', '%s');
            """ % (src, msg, date_time)).status()
        print(result)
