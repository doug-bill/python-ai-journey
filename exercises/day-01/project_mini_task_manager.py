#CLI Task Manager system

tasks = []

def add_tasks():
		task = input("What's your task? ")
		tasks.append({"name": task, "completed": False})
		print("Task added succefully!")

def list_tasks():
	if len(tasks) == 0:
		print("No tasks found!")
	else:
		for i, task in enumerate(tasks,1):
			status = "✅" if task["completed"] else " "
			print(f"{i}. [{status}] {task['name']}") # use double" (" ") to encapsulate 
			
def complete_task():
		list_tasks()
		index = int(input("Completed task number: ")) - 1	
		
		if 0 <= index < len(tasks):
				tasks[index]["completed"] = True
				print("Task completed!")
		else:
				print("Invalid number.")
				

while True:
  
  print("Welcome to your Task Maganger \nHere are the avaliable options:")
  
  print("\n1. Add a task")
  print("2. List tasks")
  print("3. Complete a task")
  print("4. Exit")
   
  option = input("\nChoose an option:")
  #Options for valid user input   

  if option == "1":
      add_tasks()
  elif option == "2":
      list_tasks()
  elif option == "3":
      complete_task()
  elif option =="4":
      print("Exiting the program now. \nSee you soon!")
      break
  else:
      print("Invalid Option")
      
      
#add_tasks()		
