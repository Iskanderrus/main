##################### Extra Hard Starting Project ######################
import datetime as dt
import pandas as pd

today = dt.datetime.today()

df = pd.read_csv('dates.csv', index_col="name")
birthday_list = []
for index, row in df.iterrows():
    bd = dt.datetime(year=row["year"], month=row["month"], day=row["day"])
    if bd.month == today.month and bd.month == today.month:
        pass
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.



