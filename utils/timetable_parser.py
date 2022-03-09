import io
import requests
import openpyxl

from db.timetable_operations import post_rasp

def get_new_timetable(url) -> True | False:
    try:
        resp = requests.get(url)
        bytes = io.BytesIO(resp.content)
        new_timatable = parse_rasp(bytes)
        post_rasp(nech=new_timatable[0], ch=new_timatable[1])
        return True
    except BaseException as e:
        print(e)
        return False


def parse_rasp(file):
    ps = openpyxl.reader.excel.load_workbook(file)
    sheet = ps['Лист1']

    pr_numbers = [3 * i for i in range(1, 31)]
    ch_array = []
    nech_array = []
    for number in pr_numbers:
        nech_array.append(sheet[f'C{number}'].value)
        ch_array.append(sheet[f'D{number}'].value)

    return [nech_array, ch_array]