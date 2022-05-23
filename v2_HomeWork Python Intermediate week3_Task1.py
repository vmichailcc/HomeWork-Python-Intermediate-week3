from contextlib import contextmanager

read_file_name = input("Введите имя файла для чтения: ")
write_file_name = input("Введите имя файла для записи: ")
count = 1


@contextmanager
def file_open(path, mode):
    try:
        file_obj = open(path, mode, encoding="UTF-8")
        yield file_obj
    except OSError:
        print("Неправильно указано название файла или путь к нему!")
    finally:
        file_obj.close()


with file_open(read_file_name, "r") as read_file:
    with file_open(write_file_name, "x") as write_file:
        for line in read_file:
            line_w = f"{count}: {line}"
            count += 1
            write_file.write(line_w)
