import sqlite3

connection = sqlite3.connect('../coachdata.sqlite')
cursor = connection.cursor()

import glob
import athletemodel

data_files = glob.glob("../data/*.txt")
athletes = athletemodel.put_to_store(data_files)
for each_athlete in athletes:
    name = athletes[each_athlete].name
    dob = athletes[each_athlete].dob
    cursor.execute("INSERT INTO athletes (name,dob) VALUES (?,?)", (name, dob))
    # print(name,dob,athletes[each_athlete])
    cursor.execute("SELECT id FROM athletes WHERE name = ? AND dob = ?", (name, dob))
    the_current_id = cursor.fetchone()[0]
    # print(the_current_id)
    # print(athletes[each_athlete].clean_data)
    for each_time in athletes[each_athlete].clean_data:
        cursor.execute("INSERT INTO timing (athlete_id,value) VALUES (?,?)", (the_current_id, each_time))



connection.commit()
connection.close()
