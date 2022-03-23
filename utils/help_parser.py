import json

spaces = '&#12288;'

def parse_arg(d: dict) -> str:
    s = ''
    s += f"\t•cmd: {d['command']}"
    s += "".join([f" arg{i + 1} " for i in range(len(d['args']))]) + '\n'
    if d['args']:
        s += f"{spaces}args: {d['args']}\n"
    if d['description']:
        s += f"{spaces}desc: {d['description']}\n"
    return s

def get_full_help() -> str:
    with open('help.json') as json_file:
        data = json.load(json_file)
    text = 'Лови помощь, друк!\n'
    timetable = ''
    helpful = ''
    other = ''
    for d in data:
        match d['tag']:
            case 'timetable':
                timetable += parse_arg(d)
            case 'helpful':
                helpful += parse_arg(d)
            case 'other':
                other += parse_arg(d)
    text += f'--Расписание--\n{timetable}'
    text += f'--Полезное--\n{helpful}'
    return text

def get_cmd_help(cmd: str) -> str:
    with open('help.json') as json_file:
        data = json.load(json_file)
    key = "command"
    commands = [d[key] for d in data]
    if cmd in commands:
        idx = commands.index(cmd)
        text = 'Держи!\n'
        text += parse_arg(data[idx])
    else:
        text = 'не нашел такой команды :('
    return text
