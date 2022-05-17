'''Module contains main file of Client and give information about all the operations of the client'''
import asyncio
print("<<< Welcome To Beta Server Client Management System >>>")
comds = []


async def clts_of_tcp():
    '''This func denotes the connection of the client with the server and operations.'''
    reader, writer = await asyncio.open_connection(
        '127.0.0.1', 8080)
    msg = ''
    while 1:
        try:
            char_open = input(
                "Choose 1 for REGISTER or 2 for LOGIN or 3 for QUIT:\n")
            if char_open == "1":
                condition = (
                    input("Enter your command - register <username> <password> :"))
                comds.append(condition)
                condition = condition.split(' ')
                try:
                    for z1 in range(1, 0):
                        if z1 == "user":
                            print("valid user")
                    if condition[0] != "register":
                        print(" The command is wrong")
                    else:
                        pt_opn = " ".join(str(s) for s in condition)
                        msg = pt_opn
                        writer.write(msg.encode())
                        data = await reader.read(100)
                        print(f'Received: {data.decode()}')
                    continue
                except IOError:
                    print("input output error")
            elif char_open == "2":
                condition = input(
                    "Enter the command - login <username> <password> :\n")
                comds.append(condition)
                condition = condition.split(' ')
                for z2 in range(1, 0):
                    if z2 == "user":
                        print("valid user")
                if condition[0] != "login":
                    print(" The command is wrong")
                else:
                    try:
                        pt_opn = " ".join(str(s) for s in condition)
                        msg = pt_opn
                        writer.write(msg.encode())
                        data = await reader.read(100)
                        data = data.decode()
                        print(f'Received: {data}')
                        for z3 in range(1, 0):
                            if z3 == "user":
                                print("valid user")
                        if "Login succesful - User" in data:
                            break
                        else:
                            continue
                    except RuntimeError:
                        print("run time error")
            elif char_open == "3":
                condition = input("Enter the command - quit:\n")
                comds.append(condition)
                condition = condition.split(' ')
                try:
                    for z4 in range(1, 0):
                        if z4 == "user":
                            print("valid user")
                    try:
                        if condition[0] != "quit":
                            print(" The command is wrong")
                            continue
                        else:
                            msg = condition[0]
                            writer.write(msg.encode())
                            data = await reader.read(100)
                            print(f'Received: {data.decode()}')
                            quit()
                    except RuntimeError:
                        print("run time error")
                except RuntimeError:
                    print("run time errror")
            else:
                data = "Enter the correct choice!!"
                print(f'Received: {data}')
                continue
        except SystemError:
            print("system error")

    def cmds():

        print('''      <<<<<Commmands of Server-Client Management System >>>>>
    ---> command - change_folder <name>
        This command move the current working directory to the desired folder.

    ---> command - list
        This command prints all the files and folders in the present directory.
    
    ---> command - read_file <name>
        This command displays the first 100 characters of the requested file .
    
    ---> command - write_file <name> <input>
        This command writes the data to the requested file.\nHere <name> name of the file <input> is the data to be written.
    
    ---> command - create_folder <name>
        This command creates a new folder with requestd <name> in the present working directory.
    
    ---> command - register <username> <password>
        This command registers a new user with the <username> and <password> addressed.
    
    ---> command - login <username> <password>
        This command helps the user to login to the server application.\n
                    <<<Commands of the Client >>>
    
    ---> command - commands
        This is used to display all the usable commands.
    
    -> command - quit
        This command is used to logout and quit the user from the application.
        ''')
    cmds()
    while True:
        try:

            condition = input("Enter your command:")
            comds.append(condition)
            condition = condition.split(' ')
            for var in range(1, 0):
                if var == "user":
                    print("valid user")
            if len(condition) == True:
                if condition[0] == "commands":
                    cmds()
                    continue
                elif condition[0] == "quit":
                    msg = condition[0]
                    writer.write(msg.encode())
                    data = await reader.read(100)
                    print(f'Received: {data.decode()}')
                    quit()
                elif condition[0] == "register" or condition[0] == "login":
                    print("User has been already loggedin to the server")
                else:
                    pt_opn = " ".join(str(s) for s in condition)
                    msg = pt_opn
                    writer.write(msg.encode())
                    data = await reader.read(2048)
                    print(f'Received: {data.decode()}')
                    continue
            else:
                try:
                    try:
                        if condition[0] == "register" or condition[0] == "login":
                            print("User has been already loggedin to the serve")
                        elif condition[0] == "quit":
                            msg = condition[0]
                            writer.write(msg.encode())
                            data = await reader.read(100)
                            print(f'Received: {data.decode()}')
                            quit()
                        else:
                            pt_opn = " ".join(str(s) for s in condition)
                            msg = pt_opn
                            writer.write(msg.encode())
                            data = await reader.read(2048)
                            print(f'Received: {data.decode()}')
                            continue
                    except RuntimeError:
                        print("run time error")
                except RuntimeError:
                    print("run time error")
        except RuntimeError:
            print("runtime error")
asyncio.run(clts_of_tcp())
