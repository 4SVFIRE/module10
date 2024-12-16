from queue import Queue
import random
from threading import Thread
import threading
import time
from typing import Optional


class Table:
    def __init__(self, number: int):
        self.number = number
        self.guest: Optional[Guest] = None


class Guest(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        print(f"{self.name} начал(-а) кушать")
        time.sleep(random.randint(3, 10))
        print(f"{self.name} закончил(-а) кушать")


class Cafe:
    def __init__(self, *tables: Table):
        self.tables = tables
        self.queue = Queue()

    def guest_arrival(self, *guests):
        for guest in guests:
            is_free = False
            for table in self.tables:
                if not table.guest:
                    is_free = True
                    guest.start()
                    table.guest = guest
                    print(f"{guest.name} сел(-а) за стол номер {table.number}")
                    break
            if not is_free:
                self.queue.put(guest)
                print(f"{guest.name} в очереди")

    def discuss_guests(self):
        while not self.queue.empty() or any([table.guest for table in self.tables]):
            for table in self.tables:
                if table.guest and not table.guest.is_alive():
                    '''Освобождение стола'''
                    print(f"{table.guest.name} покушал(-а) и ушёл(ушла)\nСтол номер {table.number} свободен")
                    table.guest = None
                if not self.queue.empty() and not table.guest:
                    '''Из очереди за стол'''
                    table.guest = self.queue.get()
                    table.guest.start()
                    print(f"{table.guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}")

        time.sleep(1)


# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
    'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
    'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()
