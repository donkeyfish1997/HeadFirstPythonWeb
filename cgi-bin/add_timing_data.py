import cgi, cgitb
import yate
cgitb.enable()


form_data = cgi.FieldStorage()

print(yate.start_response())

print(yate.include_header("Athlete: " + form_data['Name'].value +
                  ', DOB: ' + form_data['Dob'].value))

print(yate.start_form('generate_timing_data.py?Which_athlete={}'.format(form_data['Name'].value)))
print(yate.input_text("time",""))

print(yate.para('(format: 2.11)'))
print(yate.end_form())

print(yate.include_footer(
    {"HOME": "/index.html", "Select another athlete": "generate_list.py"}))



