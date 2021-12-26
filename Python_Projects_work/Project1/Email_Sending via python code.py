import yagmail
import os
import time
sender = 'harshwardhana00@gmail.com'
reciver = 'vkrj59@gmail.com'

Subject = "This the subject "

Contents = """
Hello vicky this is harsh from python.
"""
    yag = yagmail.SMTP(user = sender ,password=os.getenv('PASSWORD'))
    yag.send(to = reciver,subject=Subject,contents=Contents)
    print("Email send")