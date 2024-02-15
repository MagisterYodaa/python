
import logging
import threading
import time
import random

LOG_FORMAT = '%(asctime)s %(threadName)-17s %(levelname)-8s %(message)s'
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)

# Создаем семафор
semaphore = threading.Semaphore(0)
item = 0

def consumer():
    logging.info('Privet vlad')
    # Поток потребителя ждет, пока семафор не будет разблокирован
    semaphore.acquire()
    logging.info('Poka vlad {}'.format(item))
    # Для демонстрации эффекта потоки потребителей могут работать сразу после получения уведомления
    # Здесь можно добавить обработку элемента item

def producer():
    global item
    time.sleep(3)
    item = random.randint(0, 1000)
    logging.info('Dosvidanie vlad {}'.format(item))
    # После создания элемента производитель разблокирует семафор, чтобы разблокировать потоки потребителей
    semaphore.release()

# Основная программа
def main():
    start_time = time.time()  # Запускаем отсчет времени

    threads = []
    for _ in range(15):  # Создаем 15 потоков
        t1 = threading.Thread(target=consumer)
        t2 = threading.Thread(target=producer)
        threads.extend([t1, t2])

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    end_time = time.time()  # Завершаем отсчет времени
    total_time = end_time - start_time
    logging.info(f"Время выполнения программы: {total_time} секунд")

if __name__ == "__main__":
    main()
