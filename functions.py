file_path = "data.txt"

"""Get to do list from txt file"""

def get_todos(Filepath=file_path):
    with open(file_path,'r') as file:
        data = file.readlines()
        return (data)

"""write to do list to txt file"""
def write_todos(todos, Filepath=file_path):
    with open(file_path,'w') as file:
        file.writelines(todos)

if __name__=="__main__":
    print("Hello")
    print(get_todos())