import asyncio
import random


def main3():
    num = 1_000_000
    b = random.randint(1, 100)
    class Gener:
        def task3(self):
            async def task3_func1():
                for i in range(1, num, b):
                    await asyncio.sleep(0.1)
                    yield i

            async def task3_func2():
                async for i in task3_func1():
                    print(i)

            async def task3_func3():
                try:    
                    await asyncio.wait_for(task3_func2(), timeout=15.0)
                except TimeoutError:
                    print("Время вышло")
                    
            return asyncio.run(task3_func3())
        
    task = Gener()
    return task.task3()

if __name__ == "__main__":
    main3()