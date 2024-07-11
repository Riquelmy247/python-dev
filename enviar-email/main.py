import win32com.client as win32

outlook = win32.Dispatch('outlook.application')

email = outlook.CreateItem(0)

email.To = "..."
email.Subject = "..."
email.HTMLBody = """<html></html>"""

email.Send()
print("Email enviado")