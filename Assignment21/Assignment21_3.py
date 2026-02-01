"""
Docstring for Assignment21.Program_3

Question:3: Design a Python application where multiple threads update a shared variable.
• Use a Lock to avoid race conditions.
• Each thread should increment the shared counter multiple times.
• Display the final value of the counter after all threads complete execution.

"""

import threading

counter = 0
lock = threading.Lock()


def increment_counter():
    global counter
    for i in range(100000):
        with lock:
            counter += 1


def main():
    number_of_threads = int(input("Enter the number of threads: "))
    threads = []

    for i in range(number_of_threads):
        thread = threading.Thread(target=increment_counter)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print(f"Final counter value: {counter}")


if __name__ == "__main__":
    main()