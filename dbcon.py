import psycopg2
class DbCon:
    def __init__(self):
        try:
            self.connection = psycopg2.connect(user = "oejdfpyizarfhm",
                                               password = "fb4b18b8a9ba59b6720ab50bb230175466630d71aafa1f7a9463ed47e8e69d5a",
                                               host = "ec2-54-197-254-189.compute-1.amazonaws.com",
                                               port = "5432",
                                               database = "d4vvkr2us65lvp")
            self.cursor = self.connection.cursor()
            print("Connected to DB:",
                  self.send("Select version();").result())
        except (Exception, psycopg2.Error) as error :
            print ("error:", error)
            self.close()
    def send(self, sql='Select version();'):
            print('sql> ', sql)
            self.cursor.execute(sql)
            self.connection.commit()
            return self
    def status(self):
        return self.cursor.statusmessage
    def result(self):
        return self.cursor.fetchone()
    def results(self):
        return self.cursor.fetchall()
    def close(self):
        if(self.connection):
            self.cursor.close()
            self.connection.close()
            print("connection closed")
