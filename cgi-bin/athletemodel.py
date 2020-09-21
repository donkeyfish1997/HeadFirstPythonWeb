import sqlite3

def get_names_from_store():


    connection = sqlite3.connect('coachdata.sqlite')
    cursor = connection.cursor()

    cursor.execute("SELECT name FROM athletes")
    response = [row[0] for row in cursor.fetchall()]
    connection.close()
    return response

def get_ID_from_name(athlete_name):
    connection = sqlite3.connect('coachdata.sqlite')
    cursor = connection.cursor()

    cursor.execute("SELECT id FROM athletes WHERE name = ?",(athlete_name,))
    response = cursor.fetchone()[0]
    connection.close()
    return response

def get_athlete_from_id(athlete_id):
    connection = sqlite3.connect('coachdata.sqlite')
    cursor = connection.cursor()

    cursor.execute("SELECT name,dob FROM athletes WHERE id = ?",(athlete_id,))
    (name,dob) = cursor.fetchone()

    cursor.execute("SELECT value FROM timing WHERE athlete_id = ?", (athlete_id,))
    data = [row[0] for row in cursor.fetchall()]

    response = {
        'Name':name,
        'DOB':dob,
        'data':data,
        'top3':data[:3],
    }
    connection.close()
    return response

