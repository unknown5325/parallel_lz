import subprocess
import threading
import time

def main1():

    lis = []

    class Ping:
        def __init__(self, ip):
            self.ip = ip
        def with_potoks(self):
            def ping(ip):
                res = subprocess.run(['ping', '-n', '1', ip], capture_output=True)
                print(f"{ip} is {'up' if res.returncode ==  0 else 'down'} - with-potok")
            for i in self.ip:
                start = time.time()
                p = threading.Thread(target=ping, args=(i,))
                p.start()
                lis.append(p)
            for i in lis:
                i.join()
            end = time.time() - start
            return end

        def without_potoks(self):
            start = time.time()
            def ping(ip):
                res = subprocess.run(['ping', '-n', '1', ip], capture_output=True)
                print(f"{ip} is {'up' if res.returncode ==  0 else 'down'} - without-potok")

            for i in self.ip:
                ping(i)

            end = time.time() - start
            return end
        
 
        
    ip = [
        '68.6.136.145', '48.174.87.79', '64.254.211.52',
        '173.91.175.165', '192.191.98.140', '158.98.97.174',
        '4.5.11.193', '16.203.224.29', '117.52.0.100',
        '220.118.68.186',
    ]

    task = Ping(ip)
    func1 = task.with_potoks()
    func2 = task.without_potoks()
    diff = func2 - func1
    print(f"Время с потоками: {func1}, \nВремя без потоков: {func2}, \nРазница по времени: {diff}")


if __name__ == "__main__":
    main1()