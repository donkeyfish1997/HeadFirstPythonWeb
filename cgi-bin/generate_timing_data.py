import cgi
import yate
import athletemodel
import cgitb

cgitb.enable()

form_data = cgi.FieldStorage()
athlete_name = form_data['Which_athlete'].value
athlete_id = athletemodel.get_ID_from_name(athlete_name)


if 'time' in form_data:
    athlete_time = form_data['time'].value
    athletemodel.add_time_from_id(athlete_id,athlete_time)

athlete_data = athletemodel.get_athlete_from_id(athlete_id)
print(yate.start_response())
print(yate.include_header("Coach Kelly's Timing Data"))

print(yate.header("Athlete: " + athlete_data['Name'] +
                  ', DOB: ' + athlete_data['DOB']))
print(yate.para("the top times for this athlete are:"))
print(yate.u_list(athlete_data['top3']))
print(yate.para("The entire set of timing data is: " + str(athlete_data['data']) + "(duplicates removed)."))

print(yate.include_footer(
    {"HOME": "/index.html", "Select another athlete": "generate_list.py",
     "Add timing data": "add_timing_data.py?Name={}&Dob={}".format(athlete_data['Name'], athlete_data['DOB'])}))

# print(athletes)
