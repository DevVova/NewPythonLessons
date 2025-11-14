from datetime import datetime, timedelta

# Вот теперь если мы хотим преобразовать формат datetime в наш любой то вот:

# %a: аббревиатура дня недели. Например, Wed - от слова Wednesday (по умолчанию используются
# английские наименования)
# %A: день недели полностью, например, Wednesday
# %b: аббревиатура названия месяца. Например, Oct (сокращение от October)
# %B: название месяца полностью, например, October
# %d: день месяца, дополненный нулем, например, 01
# %m: номер месяца, дополненный нулем, например, 05
# %y: год в виде 2-х чисел
# %Y: год в виде 4-х чисел
# %H: час в 24-х часовом формате, например, 13
# %I: час в 12-ти часовом формате, например, 01
# %M: минута
# %S: секунда
# %f: микросекунда
# %p: указатель AM/PM
# %c: дата и время, отформатированные под текущую локаль
# %x: дата, отформатированная под текущую локаль
# %X: время, форматированное под текущую локаль

today = datetime.now()
my_today = datetime.strftime(today, "%y/%m %H:%M %A")
print(my_today)

# Сложение и вычитание дат и времени.

# Для определения промежутка времени можно использовать конструктор timedelta:
# timedelta([days], [seconds], [microseconds], [milliseconds], [minutes], [hours], [weeks])
yesterday = today + timedelta(1)
print(yesterday)
today_plus_two_hours = today + timedelta(hours=2)
print(f"Через два часа будет дата -> {today_plus_two_hours}")

#
period = today - timedelta(minutes=30)
print(period.minute)