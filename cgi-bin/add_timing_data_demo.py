import os
import time
import sys
import cgi
import yate
import cgitb

cgitb.enable()

print(yate.start_response('text/plain'))
# 純文字送回正在等待的web瀏覽器

addr = os.environ['REMOTE_ADDR']
host = os.environ['REMOTE_HOST']
method = os.environ['REQUEST_METHOD']

cur_time = time.asctime(time.localtime())  # 取得當前時間

print(host + ", " + addr + ", " + cur_time + ": " + method,end=' ', file=sys.stderr)

form = cgi.FieldStorage()
for each_form_item in form.keys():
    print(each_form_item + '->' + form[each_form_item].value, end=' ', file=sys.stderr)
print(file=sys.stderr)  #在標準作物使用換列字符

print('ok.')
