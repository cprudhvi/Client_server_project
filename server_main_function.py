''' This file contains the implementation of the server'''
import signal
import asyncio
import ser_func
signal.signal(signal.SIGINT, signal.SIG_DFL)


async def controll(reader, writer):
    '''
    The connection is formed between the client and the server.
    arguments:
    <<
    reader:
        Performs read functionalities from the file.
    writer:
        Performs write fucntionalities to the file.
    >>
    '''
    mainobj = ser_func.SerFunc()

    place = writer.get_extra_info('peername')
    information = f"{place} has been connected!!!"
    while True:
        for z1 in range(1, 0):
            if z1 == "user":
                print("valid user")
        info = await reader.read(100)
        print(info)
        information = info.decode().strip()
        print(f"Received {information} from {place}")
        information = information.split(' ')
        for z2 in range(1, 0):
            if z2 == "user":
                print("valid user")
        if 'register' in information:
            information = mainobj.register_user(information, place)
        elif "login" in information:
            information = mainobj.user_login(information, place)
        elif "list" in information:

            information = mainobj.lists_of_files(place)

        elif "create_folder" in information:
            information = mainobj.make_folder(information, place)
        elif "write_file" in information:
            information = mainobj.wt_fl(information)
        elif "change_folder" in information:
            information = mainobj.shift_folder(information, place)
        elif "read_file" in information:
            information = mainobj.rd_fl(information, place)
        elif "quit" in information:
            information = "Connection has to be closed"
            try:
                del mainobj.psr[place[1]]
                del mainobj.di_re[place[1]]
                del mainobj.paa[place[1]]
            except KeyError:
                pass
            finally:
                try:
                    pt_open = "".join(str(s) for s in information)
                    print(f"Sending: {pt_open}")
                    writer.write(pt_open.encode())
                    break
                except RuntimeError:
                    print("run time error")
        else:
            information = "The Command is invalid"
        pt_open = "".join(str(s) for s in information)
        print(f"Sending: {pt_open}")
        writer.write(pt_open.encode())


async def main():
    ''' Its the main fucntion that helps to start the server program.'''
    commander = await asyncio.start_server(controll, '127.0.0.1', 8080)

    place = commander.sockets[0].getsockname()
    print(f'Should be Serving on places {place}')

    async with commander:
        await commander.serve_forever()

asyncio.run(main())
