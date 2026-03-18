import mysql.connector


user_state = {
    "name": None,
    "phone": None,
    "email": None
}


def save_user(name, phone, email):

    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="pmgt"
    )

    cursor = conn.cursor()

    query = """
    INSERT INTO users(name, phone, email)
    VALUES(%s,%s,%s)
    """

    cursor.execute(query, (name, phone, email))

    conn.commit()

    cursor.close()
    conn.close()
