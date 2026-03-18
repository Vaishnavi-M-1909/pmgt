import mysql.connector


def run_query(sql):

    if sql is None:
        return None

    try:

        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="pmgt"
        )

        cursor = conn.cursor()

        cursor.execute(sql)

        rows = cursor.fetchall()

        cursor.close()
        conn.close()

        return rows

    except Exception as e:

        print("SQL Error:", e)

        return None
