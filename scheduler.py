import schedule, time

def get_time():
    return time.strftime("%H:%M:%S")
def task():
    print("Doing task...", get_time())
schedule.every(5).seconds.do(task)
while True:
    schedule.run_pending()
    time.sleep(1)



def task1():
    print("Running task 1 every 5 seconds")
def task2():
    print("Running task 2 every 10 minutes")
schedule.every(5).seconds.do(task1)
schedule.every(10).minutes.do(task2)
while True:
    schedule.run_pending()
    time.sleep(1)


def task():
    print("Running task every Monday at 8:00 AM")
schedule.every().monday.at("08:00").do(task)
while True:
    schedule.run_pending()
    time.sleep(1)


def task():
    print("Running task every 2 hours and 30 minutes")
schedule.every(2).hours.do(task)
schedule.every().minutes.do(task, minutes=30)
while True:
    schedule.run_pending()
    time.sleep(1)

# Stopping a task after a certain number of runs
def task():
    print("Running task")
    task.counter += 1
    if task.counter >= 5:
        schedule.clear('task')
task.counter = 0
schedule.every(5).seconds.do(task).tag('task')
while True:
    schedule.run_pending()
    time.sleep(1)


# Running a task at startup and then every 10 minutes
def task():
    print("Running task")
task()
schedule.every(10).minutes.do(task)
while True:
    schedule.run_pending()
    time.sleep(1)