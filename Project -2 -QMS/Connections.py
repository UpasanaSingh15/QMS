import pymysql


class CONNECTIONS:

    def __init__(self):
        self.host = 'localhost'
        self.user = 'root'
        self.password = '1234'
        self.db = 'qms'

    def mysql_connection(self):
        conn = pymysql.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            db=self.db,
        )
        return conn

    def execute_query(self, query):
        conn, cur = None, None
        try:
            conn = self.mysql_connection()
            cur = conn.cursor()
            cur.execute(query)
            conn.commit()
        except Exception as e:
            print('Exception occurred!! %s'%str(e))
        finally:
            if cur is not None:
                cur.close()
            if conn is not None:
                conn.close()

    def fetch_data(self, query):
        conn, cur, rows = None, None, None
        try:
            conn = self.mysql_connection()
            cur = conn.cursor()
            cur.execute(query)
            rows = cur.fetchall()
        except Exception as e:
            print('Exception occurred!! %s'%str(e))
        finally:
            if cur is not None:
                cur.close()
            if conn is not None:
                conn.close()
        return rows