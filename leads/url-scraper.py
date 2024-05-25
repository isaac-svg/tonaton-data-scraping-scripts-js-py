import requests

page = 1


def get_file_data(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        file_data = file.read().strip().split('\n')
    return file_data


all_links = get_file_data('tonaton_links.txt')
while True:
    res = requests.get(f'https://tonaton.com/api_web/v1/listing?page={page}&init_page=true&slug=vehicles&webp=true')
    data = res.json()['adverts_list']['adverts']
    if not data:
        break
    for single_row in data:
        guid = single_row['guid']
        slug = single_row['slug']

        url = f"https://tonaton.com/a_{slug}-{guid}.html"
        if url not in all_links:
            with open('tonaton_links.txt', 'a') as f:
                f.write(url + '\n')



    print(page, " page done")
    total_links = get_file_data('tonaton_links.txt')
    print(len(list(set(total_links))), " links saved in file")
    page += 1





