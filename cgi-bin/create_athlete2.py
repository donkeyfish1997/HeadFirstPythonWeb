import athletemodel
import yate
import sqlite3
import cgitb
import cgi
cgitb.enable()


print(yate.start_response())
print(yate.include_header("Create new Athlete"))
form_data = cgi.FieldStorage()


if 'Name' in form_data and 'Dob' in form_data:
    athlete_name = form_data['Name'].value
    athlete_dob = form_data['Dob'].value

    connection = sqlite3.connect('coachdata.sqlite')
    cursor = connection.cursor()
    cursor.execute("INSERT INTO athletes (name,dob) VALUES (?,?)", (athlete_name, athlete_dob))
    connection.commit()
    connection.close()

    print(yate.header("輸入完成", 6))

else :
    print(yate.header("值不能為空",6))

print(yate.include_footer({"HOME":"/index.html","Create athlete":"create_athlete.py"}))


