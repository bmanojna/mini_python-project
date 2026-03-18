# todolist by using conditions

tasks = []
while True:
   print("1.enter your task")
   print("2.view your task")
   print("3.delete your task")
   print("4.exit")

   choice = (int(input("enter choice: ")))
   if choice == 1:
       task = (input("enter task"))
       tasks.append(task)
       print("task added!")
   elif choice == 2:
       if len(tasks) == 0:
           print("no tasks avaliable")
       else:
           print("\nyour tasks")
           for i in range(len(tasks)):
               print(f"{i+1}. {tasks[i]}")
   elif choice == 3:
       if len(tasks)==0: 
           print("there is no task to delete")
       else:
           for i in range(len(tasks)):
               print(f"{i+1}.{tasks[i]}")
           num = int(input("enter your task number to delete: "))
           if 1 <= num <= len(tasks):
               tasks.pop(num-1)
               print("tasks deleted!")
           else:
               print("invalid task")
   elif choice == 4:
       print("good bye!")
       break
   else:
       print("invalid choice")

