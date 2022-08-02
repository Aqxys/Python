import csv
import pathlib

path = pathlib.Path.cwd()/'Programming_lessons'/'Project_1'/'data.csv'

def show():
    with open(path, "r", encoding='utf-8') as file:
        reader = csv.reader(file, delimiter=";")
        print("\nФамилия Имя | Телефон")
        for row in reader:
            print(row)
        

def add_contact():
    line = []
    surname = input('Фамилия: ')
    line.append(surname)
    name = input('Имя: ')
    line.append(name)
    telephone = input('Телефон: ')
    line.append(telephone)
    with open(path, mode="a", encoding='utf-8') as csvfile:
        file_writer = csv.writer(csvfile, delimiter = ";", lineterminator="\r")
        file_writer.writerow(line)
