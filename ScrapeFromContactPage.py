import csv
import requests
import re

with open('links_scraped.csv', 'r') as links:
    reader = csv.reader(links)
    list_links = list(reader)

count = 0
total_arr = []
for i in range(20):
    website = ""
    website = website.join(list_links[i])
    if 'www.' not in website:
        website = 'https://www.' + website
    elif 'https' not in website:
        website = 'https://' + website
    try:
        page = requests.get(website)
    except:
        continue
    mail_list = list(dict.fromkeys(re.findall('\w+@\w+\.{1}\w+', page.text)))
    numbers = list(dict.fromkeys(re.findall('\+?\d[\d -]{8,12}\d', page.text)))
    # remove incorrect numbers
    for i in numbers:
        if len(i) > 10 and '+' not in i and '-' not in i and ' ' not in i:
            numbers.remove(i)
    arr = []
    arr.append(website)
    arr.append(mail_list)
    arr.append(numbers)
    total_arr.append(arr)
    count += 1
    if count == 10: break

with open("contact_info.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(total_arr)






