import time
import threading

elapsed_time = 0

def timer(func):
    def wrapper(*args):
        global elapsed_time
        start_time = time.time()
        result = func(*args)
        end_time = time.time()
        elapsed_time += end_time - start_time
        return result
    return wrapper

@timer
def write_words(word_count, file_name):
    with open(file_name, 'a', encoding='UTF-8') as file:
        for number in range(1, word_count + 1):
            file.write(f'Какое-то слово № {str(number)}\n')
            time.sleep(0.1)
        print(f'Завершилась запись в файл {file_name}')


write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

print(f'Работа функций: {elapsed_time:.2f} секунд')

elapsed_time = 0

thread_1 = threading.Thread(target=write_words, args=(10, 'example5.txt'))
thread_2 = threading.Thread(target=write_words, args=(30, 'example6.txt'))
thread_3 = threading.Thread(target=write_words, args=(200, 'example7.txt'))
thread_4 = threading.Thread(target=write_words, args=(100, 'example8.txt'))

thread_1.start()
thread_2.start()
thread_3.start()
thread_4.start()

thread_1.join()
thread_2.join()
thread_3.join()
thread_4.join()

print(f'Работа потоков: {elapsed_time:.2f} секунд')
