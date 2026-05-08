print("Welcome to Smart Task Repetition System")
task_name = str(input("Task name:"))
time = int(input("Repeat this task today:"))

for x in range(1, time+1, 1):
    print("Task", x, task_name, "completed")

count = int(input("Countdown:"))

while count != 0:
    print(count)
    count -= 1

session = ["Morning", "Evening"]
for session in session:
    for task in range(1, 4, 1):
        print(session, "task:", task)
        
print("Final summary")
print(task_name)
print("Number of repitation completed:", time)
if count == 0:
    print("countdown finished")
