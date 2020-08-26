import yate
import cgitb
cgitb.enable()


print(yate.start_response())
print(yate.include_header("Coach Kelly's List of Athletes"))
print(yate.do_form('add_timing_data.py',['TimeValue'],text='Send'))
print(yate.include_footer({"HOME":"/index.html"}))