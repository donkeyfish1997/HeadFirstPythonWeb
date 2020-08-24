import athletemodel
import yate
import glob



data_files = glob.glob("data/*.txt")
# glob 模組讓你得以要求你的作業系統列出所指定的檔案名稱
athletes = athletemodel.put_to_store(data_files)
print(athletes)

print(yate.start_response())
print(yate.include_header("Coach Kelly's List of Athletes"))
print(yate.start_form('generate_timing_data.py'))
print(yate.para("Select an athlete from this list to work with:"))

for each_athlete in athletes:
    print(yate.radio_button(each_athlete,each_athlete))
print(yate.end_form())
print(yate.include_footer({"HOME":"/index.html"}))