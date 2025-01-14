# Imports
import time, random, requests, os

#const
REQ_URL = "https://api.parser.name/?api_key=6f1150c3c5eea24d192048403e801ce6&endpoint=generate&country_code=GB"

#functions
def format_leading(val,length,char="0"):
    val = str(val)
    if len(val) >= length: return val
    diff = length - len(val)
    return char*diff + val

def is_leap_year(year):
    if year%4 > 0: return False
    if year%100 == 0 and year%400 > 0: return False
    return True

def validate_date(date_string):
    try:
        spl = date_string.split("-")
        day, month, year = int(spl[0]), int(spl[1]), int(spl[2])
    except: return False

    #check month
    if month > 12 or month < 1: return False
    #check year
    if year < 0: return False
    #check day
    if day < 0: return False
    #variable month length
    if month == 2 and day > (29 if is_leap_year(year) else 28): return False
    elif day > (31 if month in [1,3,5,7,8,10,12] else 30): return False
    return date_string

#Splash
print('''
+==============================+
| STUDENT TABLE DATA GENERATOR |
|  Courtesy of ScottishPuffin  |
+==============================+
''')
input("Press <RETURN> to start")

#Input
num_students = 0
while num_students < 1:
    os.system('cls')
    print("TABLE DATA\n-------------")
    n = input("How many students should I generate: ")
    try: num_students = int(n)
    except:pass

num_classes = 0
while num_classes < 1:
    os.system('cls')
    print("TABLE DATA\n-------------\nHow many students should I generate: %s"%num_students)
    n = input("How many available classes are there: ")
    try: num_classes = int(n)
    except:pass

start_ID = -1
while start_ID < 0:
    os.system('cls')
    print("TABLE DATA\n-------------\nHow many students should I generate: %s\nHow many available classes are there: %s"%(num_students,num_classes))
    n = input("What ID do I use as starting point for the new students: ")
    try: start_ID = int(n)
    except:pass  


enroll_dates = []
act = ""
t=0
while n != "end":
    os.system('cls')
    print("TABLE DATA\n-------------\nHow many students should I generate: %s\nHow many available classes are there: %s\nWhat ID do I use as starting point for the new students: %s\n\nSTUDENT DATA\n-------------"%(num_students,num_classes,start_ID))
    n = input("Type in a date in DD-MM-YYYY format to add it to the list of possible enrollments dates. Type \'end\' to finish selection. (%s added): "%t)
    if validate_date(n):
        t+=1
        enroll_dates.append("%s 00:00:00"%n)

earliest_birthday_year = 0
earliest_birthday_month = 0
earliest_birthday_day = 0
while earliest_birthday_year < 1970:
    os.system('cls')
    print("TABLE DATA\n------------\nHow many students should I generate: %s\nHow many available classes are there: %s\nWhat ID do I use as starting point for the new students: %s\n\nSTUDENT DATA\n-------------\nEnrollment dates: %s specified"%(num_students,num_classes,start_ID,t))
    n = input("What is the birthday year of the oldest generatable student: ")
    try: earliest_birthday_year = int(n)
    except:pass

while earliest_birthday_month < 1 or earliest_birthday_month > 12:
    os.system('cls')
    print("TABLE DATA\n------------\nHow many students should I generate: %s\nHow many available classes are there: %s\nWhat ID do I use as starting point for the new students: %s\n\nSTUDENT DATA\n-------------\nEnrollment dates: %s specified\nEarliest DOB: ..-..-%s"%(num_students,num_classes,start_ID,t,earliest_birthday_year))
    n = input("What is the birthday month of the oldest generatable student: ")
    try: earliest_birthday_month = int(n)
    except:pass  

days_in_months = [31,28,31,30,31,30,31,31,30,31,30,31]
while earliest_birthday_day < 1 or earliest_birthday_day > days_in_months[earliest_birthday_month-1]:
    os.system('cls')
    print("TABLE DATA\n------------\nHow many students should I generate: %s\nHow many available classes are there: %s\nWhat ID do I use as starting point for the new students: %s\n\nSTUDENT DATA\n-------------\nEnrollment dates: %s specified\nEarliest DOB: ..-%s-%s"%(num_students,num_classes,start_ID,t,format_leading(earliest_birthday_month,2),earliest_birthday_year))
    n = input("What is the birthday day of the oldest generatable student: ")
    try: earliest_birthday_day = int(n)
    except:pass

latest_birthday_year = 0
latest_birthday_month = 0
latest_birthday_day = 0
while latest_birthday_year < earliest_birthday_year:
    os.system('cls')
    print("TABLE DATA\n------------\nHow many students should I generate: %s\nHow many available classes are there: %s\nWhat ID do I use as starting point for the new students: %s\n\nSTUDENT DATA\n-------------\nEnrollment dates: %s specified\nEarliest DOB: %s-%s-%s"%(num_students,num_classes,start_ID,t,format_leading(earliest_birthday_day,2),format_leading(earliest_birthday_month,2),earliest_birthday_year))
    n = input("What is the birthday year of the youngest generatable student: ")
    try: latest_birthday_year = int(n)
    except:pass

while latest_birthday_month < 1 or latest_birthday_month > 12 or (earliest_birthday_year == latest_birthday_year and latest_birthday_month < earliest_birthday_month):
    os.system('cls')
    print("TABLE DATA\n------------\nHow many students should I generate: %s\nHow many available classes are there: %s\nWhat ID do I use as starting point for the new students: %s\n\nSTUDENT DATA\n-------------\nEnrollment dates: %s specified\nEarliest DOB: %s-%s-%s\nLatest DOB: ..-..-%s"%(num_students,num_classes,start_ID,t,format_leading(earliest_birthday_day,2),format_leading(earliest_birthday_month,2),earliest_birthday_year,latest_birthday_year))
    n = input("What is the birthday month of the oldest generatable student: ")
    try: latest_birthday_month = int(n)
    except:pass  

days_in_months = [31,28,31,30,31,30,31,31,30,31,30,31]
while latest_birthday_day < 1 or latest_birthday_day > days_in_months[earliest_birthday_month-1] or (earliest_birthday_month == latest_birthday_month and earliest_birthday_year == latest_birthday_year and latest_birthday_day <= earliest_birthday_day):
    os.system('cls')
    print("TABLE DATA\n------------\nHow many students should I generate: %s\nHow many available classes are there: %s\nWhat ID do I use as starting point for the new students: %s\n\nSTUDENT DATA\n-------------\nEnrollment dates: %s specified\nEarliest DOB: %s-%s-%s\nLatest DOB: ..-%s-%s"%(num_students,num_classes,start_ID,t,format_leading(earliest_birthday_day,2),format_leading(earliest_birthday_month,2),earliest_birthday_year,format_leading(latest_birthday_month,2),latest_birthday_year))
    n = input("What is the birthday day of the oldest generatable student: ")
    try: latest_birthday_day = int(n)
    except:pass

print("TABLE DATA\n------------\nHow many students should I generate: %s\nHow many available classes are there: %s\nWhat ID do I use as starting point for the new students: %s\n\nSTUDENT DATA\n-------------\nEnrollment dates: %s specified\nEarliest DOB: %s-%s-%s\nLatest DOB: %s-%s-%s"%(num_students,num_classes,start_ID,t,format_leading(earliest_birthday_day,2),format_leading(earliest_birthday_month,2),earliest_birthday_year,format_leading(latest_birthday_day,2),format_leading(latest_birthday_month,2),latest_birthday_year))
input("Thats all I need! Press <RETURN> to generate file!")
os.system('cls')
names = []
students = []
print("Calculating name generator API request data size (max=25)")
full_reqs = num_students // 25
last_req_len = num_students - full_reqs * 25
print("Sending requests to name generator API")    
generated = 0
for x in range(full_reqs):
    name_req = requests.get(REQ_URL+"&results=25")
    names_json = name_req.json()
    for data_item in names_json['data']:
        generated += 1
        names.append((data_item['name']['firstname']['name'],
                    ''.join(data_item['name']['middlenames']) +
                    data_item['name']['lastname']['name']))
    print("\r\rGenerated: %s/%s"%(generated,num_students),end="")
if last_req_len > 0:
    name_req = requests.get(REQ_URL+"&results=%s"%last_req_len)
    names_json = name_req.json()
    for data_item in names_json['data']:
        generated += 1
        names.append((data_item['name']['firstname']['name'],
                    ''.join(data_item['name']['middlenames']) +
                    data_item['name']['lastname']['name']))
    print("Generated: %s/%s"%(generated,num_students),end="")
print("\nGenerated Names!")
print("Formatting data for students")
for x in range(num_students):
    print("\r\rFormatting student: %s/%s"%(x,num_students),end="")
    curr_id = str(start_ID + x)
    FName, LName = names[x]
    dob_epoch = time.gmtime(random.randint(1104537600, 1167609599))
    dob = "%s-%s-%s 00:00:00"%(dob_epoch[2],dob_epoch[1],dob_epoch[0])
    doe = random.choice(enroll_dates)
    classnum = str(random.randint(1,num_classes))
    students.append("%s;\"%s\";\"%s\";%s;%s;%s\n"%(curr_id,FName,LName,dob,doe,classnum))

print("\r\rFormatting students: DONE!  ")
print("Writing to file")
print(students)
with open("./student_data_in.txt","w+") as wfile:
    wfile.writelines(students)
print("Done!\n That\'s all done, please come again!")
