from csv import writer, DictWriter, DictReader
import math
import os

dir_base = os.path.abspath(os.path.dirname(__file__))
dir_db = os.path.join(dir_base,'pokemon.csv')
header = ('#', 'Name', 'Type 1', 'Type 2', 'Total', 'HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed',
              'Generation', 'Legendary')

def reader():
    with open(dir_db) as db_file:
        csv_reader = DictReader(db_file)
        data = list(csv_reader)
    return data

def reader_id(id):
    with open(dir_db) as db_file:
        csv_reader = DictReader(db_file)
        data = list(csv_reader)
        for row in data:
            if row['#'] == str(id):
                break
    return row

def writer(data):
    with open(dir_db, 'a', newline='') as db_file:
        csv_writer = DictWriter(db_file,fieldnames=header)
        csv_writer.writeheader()
        csv_writer.writerow(data)

    return True

def updater(updData):
    data = reader()
    with open(dir_db, 'w') as db_file:

        csv_writer = DictWriter(db_file, fieldnames=header, lineterminator='\n')
        csv_writer.writeheader()
        for row in data:
            if row['#'] == updData['#']:
                row = updData
            csv_writer.writerow(row)
    return True

def delete(indexData):
    data = reader()
    with open(dir_db, 'w') as db_file:
        csv_writer = DictWriter(db_file, fieldnames=header, lineterminator='\n')
        csv_writer.writeheader()
        for row in data:
            if row['#'] == indexData:
                continue
            csv_writer.writerow(row)
    return True

def get_pages(per_page,total):
    if per_page == 0:
        pages = 0
    else:
        pages = int(math.ceil(total / float(per_page)))
    return pages

def data_pagination(per_page):
    data = reader()
    full_data = []
    total = len(data)
    if per_page>total or per_page<1:
        return None
    else:
        pages = get_pages(per_page,total)
        for i in range(1, pages + 1):
            start = (i - 1) * per_page
            end = (i * per_page)
            items_page = []
            for item in range(start, end):
                items_page.append(data[item])
            full_data.append(i)
            full_data.append(items_page)
        return full_data


def get_data_page(per_page,page):
    data = reader()
    total = len(data)
    start = (page - 1) * per_page
    end = (page * per_page)
    items_page = []
    pages = get_pages(per_page, total)
    if per_page>total or per_page<1:
        return None
    elif page > pages or page < 1:
        return None
    else:
        for item in range(start, end):
            items_page.append(data[item])

        return items_page