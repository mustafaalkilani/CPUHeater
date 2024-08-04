import os, multiprocessing, time, psutil

def cpu_load():
    while True:
        pass

def monitor_cpu_tem(interval=0):
    print('Starting CPU monitor')
    while True:
        temp = psutil.sensors_temperatures().get('coretemp', [])[0].current
        print(temp)
        print(f'Current temperature: {temp}°C')
        time.sleep(interval)


if __name__ == '__main__':
    cpu_count = os.cpu_count()
    processes = []

    for _ in range(cpu_count):
        p = multiprocessing.Process(target=cpu_load)
        processes.append(p)
        p.start()

    # Start monitoring
    while True:
        try:
            monitor_cpu_tem()
        except KeyboardInterrupt:
            print('Keyboard interrupt caught, but continuing execution.')
            monitor_cpu_tem()
        except Exception as e:
            print(f'An error occurred: {e}')
            break

print('CPU load test finished.')