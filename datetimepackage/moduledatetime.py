from datetime import date, time, datetime

print(date.today())
yesterday = date(2025, 11, 13)
print(yesterday)

today = datetime.now()
print(today)

print("time now is ", datetime.now().time())  # Так можно узнать только время сейчас.

# Первые три параметра, представляющие год, месяц и день, являются обязательными. Остальные необязательные, и
# если мы не укажем для них значения, то по умолчанию они инициализируются нулем.
datetime1 = datetime(2025, 11, 15)
print(datetime1)

# Ниже преобразование нашей даты в виде текста в стандартную дату datetime.
new_format_today = datetime.strptime("14/11/2025 11:28", "%d/%m/%Y %H:%M")

print("----------------------------------")

# Вот как можно узнать только сколько сейчас часов.
time_hour_now = datetime.now().time().hour

print(f"time_hour_now -> {time_hour_now}")
full_time = datetime.now()
print(f"full_time -> {full_time}")
# Вот как можно узнать только сколько сейчас секунд.
time_seconds_now = datetime.now().second
print(f"time_seconds_now -> {time_seconds_now}")
print("#############################")
# Далее примеры преобразования записанной в определённом формате даты в стандартный формат datetime.
print(datetime.strptime("23", "%M"))  # 1900-01-01 00:23:00
print(datetime.strptime("11, 14, 2025 13:45:23", "%m, %d, %Y %H:%M:%S"))
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
print(datetime.now().date())  # А вот так можно узнать только дату на сегодня.
