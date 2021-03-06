import athletemodel
import yate
import glob
import cgitb
cgitb.enable()


athletes = athletemodel.get_names_from_store()

print(yate.start_response())
print(yate.include_header("Coach Kelly's List of Athletes"))
print(yate.start_form('generate_timing_data.py'))
print(yate.para("Select an athlete from this list to work with:"))

for each_athlete in athletes:
    print(yate.radio_button("Which_athlete",each_athlete))
print(yate.end_form())
print(yate.include_footer({"HOME":"/index.html","Create athlete":"create_athlete.py"}))