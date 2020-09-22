import athletemodel
import yate
import glob
import cgitb
cgitb.enable()


print(yate.start_response())
print(yate.include_header("Create new Athlete"))
print(yate.start_form('create_athlete2.py'))
print(yate.input_text("Name",""))
print(yate.input_text("Dob",""))
print(yate.para('(format: 1997-3-25)'))
print(yate.end_form())
print(yate.include_footer({"HOME":"/index.html"}))


