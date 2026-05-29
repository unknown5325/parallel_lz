import queue
import threading
import time

def main2():
    que = queue.Queue(maxsize=10)

    class Queue_task:
        def task2(self):
            def proizv():
                for i in range(0,100):
                    a = f'{i}'
                    que.put(a)
                    print(f'Процессор передал: {i}, время ожидания: {que.qsize()}')
                    time.sleep(1)

            def potreb():
                while True:
                    try:
                        it = que.get(timeout=2)
                        print(f'Пользователь получил: {it}, время ожидания: {que.qsize()}')
                        que.task_done()
                    except queue.Empty:
                        break
            
            proiz = threading.Thread(target=proizv)
            potr = threading.Thread(target=potreb)
            proiz.start()
            potr.start()
            proiz.join()
            potr.join()


    task = Queue_task()
    return task.task2()

if __name__ == "__main__":
    main2()