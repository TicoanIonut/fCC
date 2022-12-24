import schedule
from schedule import every, repeat
import time as tm
from datetime import time, timedelta, datetime


# @repeat(every(5).seconds)
def job():
	print('ceva ceva ceva')
	
	
	
# schedule.every().day.at('10:45').do(job)
schedule.every().minute.at(':45').do(job)
# schedule.every().hour.until(timedelta(hours=1)).do(job)
# j = schedule.every(1).to(5).seconds.do(job)
# c = 0

while True:
	schedule.run_pending()
	tm.sleep(1)
	# c +=1
	# if c == 10:
	# 	schedule.cancel_job(j)