import random, time, datetime

#-------------------------------------------------------------
# Exemple programms list:
programms = [
    {
        'unique_id' : '771021f5-ab73-494c-8ffe-dc3b032f0724',
        'valve_number_link' : 1,
        'schedule_date' : None,
        'schedule_time' : None,
        'duration' : None,
        'frequency' : None,
        'frequency_comp' : None,
        'queue' : False
    },
    {
        'unique_id' : '954dfb31-2da3-4b31-a395-8a713acff492',
        'valve_number_link' : 2,
        'schedule_date' : None,
        'schedule_time' : None,
        'duration' : None,
        'frequency' : None,
        'frequency_comp' : None,
        'queue' : False
    },
    {
        'unique_id' : 'c85389b2-2e55-403a-86e6-a89f67dca3c7',
        'valve_number_link' : 3,
        'schedule_date' : None,
        'schedule_time' : None,
        'duration' : None,
        'frequency' : None,
        'frequency_comp' : None,
        'queue' : False
    },
    {
        'unique_id' : 'ff750ead-5568-4ee9-8df9-3fbf4473d59f',
        'valve_number_link' : 4,
        'schedule_date' : None,
        'schedule_time' : None,
        'duration' : None,
        'frequency' : None,
        'frequency_comp' : None,
        'queue' : False
    },
    {
        'unique_id' : '9a40066b-9976-49fb-8fdd-b34b7e8cea9c',
        'valve_number_link' : 2,
        'schedule_date' : None,
        'schedule_time' : None,
        'duration' : None,
        'frequency' : None,
        'frequency_comp' : None,
        'queue' : False
    },
]

#-------------------------------------------------------------
# Fill the example programms list with random data
def fill_date_and_time(this_programm):
    date_now = datetime.datetime.now()
    minutes_added = random.randrange(1, 6)
    date_futur = date_now + datetime.timedelta(minutes = minutes_added)
    date_futur = str(date_futur).split(" ")
    this_programm['schedule_date'] = date_futur[0]
    this_programm['schedule_time'] = date_futur[1]

def fill_duration(this_programm):
    new_duration = random.randrange(5, 31)
    this_programm['duration'] = new_duration

def fill_frequencies(this_programm):
    freq = ['schedule_every_x_days', 'even_day', 'odd_day', 'week_day']
    freq_rand = random.randrange(0, 4)
    new_freq = freq[freq_rand]
    new_freq_comp = None
    if new_freq == 'schedule_every_x_days':
        x_day = random.randrange(1, 7)
        new_freq_comp = x_day
    elif new_freq == 'week_day':
        days = []
        for day in range(0,7):
            choice = bool(random.getrandbits(1))
            if choice == True :
                days.append(day)
        new_freq_comp = days
    this_programm['frequency'] = new_freq
    this_programm['frequency_comp'] = new_freq_comp

# for programm in programms:
#     fill_date_and_time(programm)
#     fill_duration(programm)
#     fill_frequencies(programm)
# print(programms)

#-------------------------------------------------------------
# Mimic a timer with seconds instead of minutes:
def fake_timer(seconds):
    date_now = datetime.datetime.now()
    my_min = 1
    while True :
        date_now = date_now+datetime.timedelta(minutes = my_min)
        print(date_now)
        time.sleep(seconds)

# fake_timer(0.1)
