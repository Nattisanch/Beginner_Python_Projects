import win32com.client as win32

outlook = win32.Dispatch('outlook.application')
user=input('Please enter a email to send to: ')
mail = outlook.CreateItem(0)
mail.To = user
mail.Subject = 'My emailing script for python'
mail.Body = 'Testing my automating skills with python'


# To attach a file to the email (optional):
#attachment  = "Path to the attachment"
#mail.Attachments.Add(attachment)

mail.Send()