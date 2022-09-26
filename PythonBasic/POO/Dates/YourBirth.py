from datetime import datetime
import datetime as d


today = d.datetime.today()

birth = "17/12/2001"


convertBirth = datetime.strptime(birth, "%d/%M/%Y")
print(convertBirth)
print("Your have {} years old".format(today.year-convertBirth.year))