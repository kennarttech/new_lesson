from tkinter import *
from tkinter import messagebox

days_of_week = input('What day of the week is today: ').lower()


if days_of_week == 'monday':
    msg = messagebox.showinfo(f'Start the day with smile ):😀')

    # print(f'Start the day with smile {days_of_week} ):😀')

elif days_of_week == 'tuesday':
    print('its tuesday')

else:
    print('Today is not Monday ):😔')