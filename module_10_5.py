import time
from multiprocessing import Pool

def read_info(name):
    all_data = []
    with open(name, 'r', encoding='utf-8') as file:
        while True:
            content = file.readline().rstrip()
            if content:
                all_data.append(content)
            else:
                break


def linear_read(filenames):
    start_time = time.time()
    for file in filenames:
        read_info(file)
    end_time = time.time()
    print(f"Линейный вызов занял: {end_time - start_time:.6f} секунд")


def parallel_read(filenames):
    start_time = time.time()
    with Pool() as pool:
        pool.map(read_info, filenames)
    end_time = time.time()
    print(f"Многопроцессный вызов занял: {end_time - start_time:.6f} секунд")

if __name__ == '__main__':
    filenames = [f'./file {number}.txt' for number in range(1, 5)]

    print("Запуск линейного вызова:")
    linear_read(filenames)

    print("Запуск многопроцессного вызова:")
    parallel_read(filenames)
