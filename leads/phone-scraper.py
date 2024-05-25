import grequests
from xextract import String
import re
import csv

# pip install grequests xextract requests

def get_file_data(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        data = file.read().strip().split('\n')
    return data


headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-language": "en-US,en;q=0.9",
    "cache-control": "max-age=0",
    "cookie": "uid=65fca3b94dc4435f525ddcd8003b230df74cac9c; _gcl_au=1.1.352579030.1711055803; first_visit=1711055801; rid=tonaton.com; app=1ee79de71a744b95b0fca0fe381a58e5",
    "if-none-match": 'W/"5beb-j7HA+NTniMpjK04+k8LqTBaaOHI"',

    "sec-ch-ua-mobile": "?0",

    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
}


def list_in_chunks(l, n):
    for i in range(0, len(l), n):
        yield l[i:i + n]


all_links = get_file_data('tonaton_links.txt')
all_links = list(list_in_chunks(all_links, 100))

# print(all_links)
print("started work")

for chunk_index, links in enumerate(all_links):
    print(f"Processing chunk {chunk_index + 1} of {len(all_links)}")

    reqs = (grequests.get(link, headers=headers) for link in links)
    responses = grequests.map(reqs)
    for res in responses:
        if res:
            page_source = str(res.text)
            # ,phone:"([^"]+)"
            phone_number = re.findall(r',phone:"([^"]+)"', page_source)
            if phone_number:
                phone_number = phone_number[0].strip()
                try:
                    category = String(xpath='//ol/li[@itemprop="itemListElement"][2]//span').parse_html(page_source)[0]
                except:
                    category = "NA"
                try:
                    address = String(xpath='//div[@class="location"]/div/span').parse_html(page_source)[0]
                except:
                    address = "NA"
                try:
                    name = String(xpath='//div[@class="details__feedback flex items-center"]/div/p').parse_html(page_source)[0]
                    print(name)
                except:
                    name = "NA"
                record = [name,phone_number, category, address, name]
                print(record)
                with open('tonaton_phone2_numbers.csv', 'a', newline='', encoding='utf-8') as file:
                    writer = csv.writer(file)
                    writer.writerow(record)



            else:
                print("Phone number not found")


