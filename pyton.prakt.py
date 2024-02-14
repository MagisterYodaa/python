import threading
import time

# Функция, которую будет выполнять каждый поток
def thread_function(thread_id):
    print(f"Поток {thread_id} начал работу")
    # Имитация некоторой работы потока
    time.sleep(2)
    print(f"Поток {thread_id} закончил работу")

# Создание и запуск 20 потоков
threads = []
for i in range(20):
    thread = threading.Thread(target=thread_function, args=(i,))
    threads.append(thread)
    thread.start()

# Ожидание завершения всех потоков
for thread in threads:
    thread.join()

print("Все потоки завершили работу")
