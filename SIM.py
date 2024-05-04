import phonenumbers
from phonenumbers import geocoder, carrier
import tkinter as tk

def get_phone_info():
    number = phone_entry.get()
    parsed_number = phonenumbers.parse(number, None)
    country = geocoder.description_for_number(parsed_number, "en")
    company = carrier.name_for_number(parsed_number, "en")
    result_country.set("Country: " + country)
    result_company.set("Company: " + company)


root = tk.Tk()


root.title("Phone Number Info")


if root.tk.call('tk', 'windowingsystem') == 'win32':
    root.option_add('*Font', 'Arial 25 bold')  # Windows
elif root.tk.call('tk', 'windowingsystem') == 'aqua':
    root.option_add('*Font', '{Arial} 120')     # macOS
else:
    root.option_add('*Font', 'Arial 20 bold')  # Linux


phone_label = tk.Label(root, text="Enter the phone number:")
phone_label.pack()
phone_entry = tk.Entry(root)
phone_entry.pack()


get_info_button = tk.Button(root, text="Get Info", command=get_phone_info)
get_info_button.pack()


result_country = tk.StringVar()
result_company = tk.StringVar()
result_country_label = tk.Label(root, textvariable=result_country, font=("Arial", 30), width=40)
result_company_label = tk.Label(root, textvariable=result_company, font=("Arial", 30), width=40)
result_country_label.pack()
result_company_label.pack()

root.mainloop()