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
    connection.commit()
connection.close()
