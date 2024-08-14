import win32com.client as win32

outlook = win32.Dispatch('outlook.application')
user=input('Please enter a email to send to: ')
email = outlook.CreateItem(0)
email.To = user
email.Subject = 'My emailing script for python'
email.Body = 'Testing my automating skills with python'
email.Send()