import sqlite3

class DB:

    def q_new(self, query):
        try:
            conn = sqlite3.connect('FNS-MSP-2019-sg2.sqlite3')
            cur = conn.cursor()
            cur.execute(query)

            resources = cur.fetchall()
            return resources
        except Exception as e:
            print("qError", e)
        finally:
            cur.close()
            conn.close()