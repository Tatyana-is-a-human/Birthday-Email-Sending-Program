import pandas
import datetime
import smtplib
from random import choice

with open("birthdays.csv") as bdFile:
    bdCSV=pandas.read_csv(bdFile)

bdDict={(row.month, row.day):[row.givenname, row.email] for (index, row) in bdCSV.iterrows()}

today=datetime.datetime.now()

myEmail="tatyana.automated@yahoo.com"

if (today.month, today.day) in bdDict:

    with open("quotes.txt") as quoteFile:
        quotesList=quoteFile.readlines()
        quote=choice(quotesList)

    recipientName = bdDict[(today.month, today.day)][0]
    recipientEmail=bdDict[(today.month, today.day)][1]

    with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
        connection.starttls()
        connection.login(user=myEmail, password="numombdpagreuhyh")
        connection.sendmail(from_addr=myEmail, to_addrs=recipientEmail,
                            msg=f"Subject: Happy birthday ya big old oaf!\n\n"+
                                f"Congrats on staying alive, {recipientName}!\n"+
                                f"I hope you're feeling like a valued member of society.\n\n"+
                                f"XOXO, \nTatyana\n \n{quote}")

