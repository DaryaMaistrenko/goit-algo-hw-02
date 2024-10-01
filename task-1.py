import queue
import random
import time

# Створюємо чергу для зберігання заявок
request_queue = queue.Queue()

# Функція для генерації нової заявки з унікальним номером
def generate_request(request_number):
    request = f"Request-{request_number}"  # Створюємо нову заявку
    print(f"Generated: {request}")
    request_queue.put(request)  # Додаємо заявку до черги

# Функція для обробки заявки
def process_request():
    if not request_queue.empty():  # Перевіряємо, чи є заявки у черзі
        request = request_queue.get()  # Видаляємо заявку з черги
        print(f"Processing: {request}")
        # Імітація часу обробки заявки
        time.sleep(random.uniform(0.5, 2))
        print(f"Completed: {request}")
    else:
        print("No requests to process. Waiting for new requests.")

# Головний цикл програми
def main():
    request_number = 1  # Лічильник для заявок
    try:
        while True:
            # Генеруємо нові заявки кожні 1-2 секунди
            generate_request(request_number)
            request_number += 1
            time.sleep(random.uniform(1, 2))

            # Одночасно обробляємо одну заявку
            process_request()

    except KeyboardInterrupt:
        print("\nProgram interrupted. Exiting...")

if __name__ == "__main__":
    main()
