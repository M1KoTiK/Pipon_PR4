import argparse
import pathlib
import datetime
import os
import traceback
import multiprocessing
FOLDER = ""

def addition(comp_int) -> int:
    total_summ : int = 0
    for i in range(comp_int + 1):
        total_summ : int = total_summ + i 
    return total_summ

def compose(base_int, exp_int) ->int:
     comp_int = base_int**exp_int
     return comp_int

def task1(queue_inp):
    while True:
        try:
            if queue_inp.empty():
                continue
            base_int, exp_int = queue_inp.get() 
            directory = pathlib.Path(FOLDER, get_date_ymdhmm())
            comp_int = compose(base_int, exp_int)
            total_summ = addition(comp_int) 
            total_str = str(base_int) + ";" + str(exp_int) + ";" + str(comp_int) + ";" + str(total_summ) + ";" + get_date_ymdhm()
            with open(directory, 'w') as file:
                file.write(total_str)
        except Exception:
            traceback.print_exc()
            print("Произошла ошибка")



def get_date_ymdhmm() -> str:
    now = datetime.datetime.now()
    total_str = str(now.day) + "." + str(now.month) + "." + str(now.year) + " " + str(now.hour) + "." + str(now.minute) + "." + str(now.second) + "." + str(now.microsecond)
    return total_str

def get_date_ymdhm() -> str:
    now = datetime.datetime.now()
    total_str = str(now.day) + "." + str(now.month) + "." + str(now.year) + " " + str(now.hour) + "." + str(now.minute) + "." + str(now.second) 
    return total_str

def main():
    # использование библиотеки pathlib для создания стандартного пути к редактируемому файлу
    path_to_file :str = pathlib.Path(pathlib.Path.cwd(), )
    # использование библиотеки agrparse для обработки аргументов начальной настройки программы (задание пути)
    set_up = argparse.ArgumentParser()
    # Аргументы строки (один аргумент, имеюющий стандартное относительное значение пути для редактируемого файла)
    set_up.add_argument('path', type=str, nargs='?', help=' path to file', default = str(path_to_file) )
    arguments = set_up.parse_args()
    FOLDER = arguments.path
    queue = multiprocessing.Queue()
    process = multiprocessing.Process(target = task1, args = (queue,))
    process.start()
    while True:
        try:
            os.system('cls||clear')
            print("Введите число и степень")
            inp_str :str = input().split()
            base_int = int(inp_str[0])
            exp_int = int(inp_str[1])
            queue.put((base_int, exp_int))
        except Exception:
            traceback.print_exc()
            print("Ошибкус. Повторите ввод")
            continue
     
      


if __name__ == "__main__":
    main()