from datetime import date
from application.salary import calculate_salary
from db.people import get_employees


if __name__ == '__main__':
   date_now = date.today()
   print(date_now)
   calculate_salary()
   get_employees()