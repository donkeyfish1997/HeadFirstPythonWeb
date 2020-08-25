import cgi
import yate
import athletemodel
import cgitb

cgitb.enable()

athletes = athletemodel.get_from_store()

form_data = cgi.FieldStorage()
athlete_name = form_data['Which_athlete'].value
athlete_data = athletes[athlete_name]

print(yate.start_response())
print(yate.include_header("Coach Kelly's Timing Data"))

print(yate.header("Athlete: " + athlete_name +
                  ', DOB: ' + athlete_data.dob))
print(yate.para("the top times for this athlete are:"))
print(yate.u_list(athlete_data.top3))

print(yate.include_footer({"HOME": "/index.html", "Select another athlete": "generate_list.py"}))

# print(athletes)
