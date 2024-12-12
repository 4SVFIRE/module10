
import time
from threading import Thread


class Knight(Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power
        self.enemy = 100
        self.timer = 0

    def fight(self):
        while self.enemy > 0:
            time.sleep(1)
            self.timer += 1
            self.enemy -= self.power
            self.enemy = max(0, self.enemy)
            print(f'{self.name} сражается {self.timer} день(дня)..., осталось {self.enemy} воинов.')

    def run(self):
        print(f'{self.name}, на нас напали!')
        self.fight()
        print(f'{self.name} одержал победу спустя {self.timer} дней(дня)!')



first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print('Все битвы закончились')