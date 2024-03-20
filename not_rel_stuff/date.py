from datetime import datetime

today = datetime.now()
print(datetime.strftime(today, '%a %b %H:%M:%S %Y'))
