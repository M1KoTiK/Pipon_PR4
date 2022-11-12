import argparse
import pathlib
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler, FileCreatedEvent
from datetime import datetime
import os
import time
FOLDER = ""

class MyHandler(FileSystemEventHandler):
    def on_created(self, event):
        base = None
        exp = None
        comp = None
        total_summ = None
        time_modif : str = None
        try:
            with open(event.src_path) as file:
                file_str = file.read().split(";")
                base = file_str[0]
                exp = file_str[1]
                comp = file_str[2]
                total_summ = file_str[3]
                time_modif : str = file_str[4]
                print(time_modif + " >> " + base + "^" + exp + " = " + comp)
        except Exception:
            print("Ошибка")
def main():
    # использование библиотеки pathlib для создания стандартного пути к редактируемому файлу
    path_to_file :str = pathlib.Path(pathlib.Path.cwd(), )
    # использование библиотеки agrparse для обработки аргументов начальной настройки программы (задание пути)
    set_up = argparse.ArgumentParser()
    # Аргументы строки (один аргумент, имеюющий стандартное относительное значение пути для редактируемого файла)
    set_up.add_argument('path', type=str, nargs='?', help=' path to file', default = str(path_to_file) )
    arguments = set_up.parse_args()
    FOLDER = arguments.path
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, FOLDER, recursive=False)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except Exception:
        observer.stop()
        observer.join()   

if __name__ == "__main__":
    main()