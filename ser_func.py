'''This module contains all the functions of the server'''
import os
import time
import shutil


class SerFunc:
    def __init__(self):
        self.psr = {}
        self.di_re = {}
        self.fs = {}
        self.r_t = os.getcwd()
        self.paa = {}
        self.list = []
    #signal.signal(signal.SIGINT, signal.SIG_DFL)
        print(self.r_t)

    def register_user(self, cds, lable):
        '''
        register allows the new user to register on the server.

        Arguments:
        <<
        comands:
            It is the command given by the user to the server.
        address:
            It is a bundle of the ip address and the port of the client.
        >>
        '''
        lane = (f'{self.r_t}\\login_details.txt')
        fil_op = open(lane, "r")
        conts = fil_op.read()
        conts = conts.split(" ")
        print("contents in register_user: ", conts)
        fil_op.close()
        p_op = len(conts)
        try:
            for i in range(0, p_op):
                if i % 2 == False:
                    try:
                        if cds[1] == conts[i]:
                            msg_return = "Username already exists"
                            return msg_return
                        lane = (f'{self.r_t}\\login_details.txt')
                        fil_op = open(lane, "a+")
                        fil_op.write(cds[1])
                        fil_op.write(" ")
                        fil_op.write(cds[2])
                        fil_op.write(" ")
                        fil_op.close()
                        lane = (f'{self.r_t}\\root')
                        os.chdir(lane)
                        os.mkdir(cds[1])
                        os.chdir(cds[1])
                        self.di_re[lable[1]] = {cds[1]: str(os.getcwd())}
                        msg_return = "User has been Registered"
                        return msg_return
                    except SystemError:
                        print("error in the system")
        except IOError:
            print("the input is not valid")

    def user_login(self, cds, lable):
        '''Login allows a client to login to the server.
        Once logged in, the client will have the user's personal folder as starting point to work with.

        Arguments:
        <<
        commands:
            It is the command given by the user to the server.
        address:
            It is a bundle of the ip address and the port of the client.
        >>
        '''
        try:
            if cds[1] not in self.list:
                lane = (f'{self.r_t}\\login_details.txt')
                fil_op = open(lane, "r")
                content = fil_op.read()
                content = content.split(" ")
                fil_op.close()
                tem = len(content)
                for i in range(0, tem):
                    if i % 2 == False:
                        try:
                            if cds[1] == content[i]:
                                if cds[2] == content[i+1]:
                                    lane = (f'{self.r_t}\\root')
                                    os.chdir(lane)
                                    os.chdir(cds[1])
                                    msg_return = "Login succesful - User"
                                    self.list.append(cds[1])
                                    self.psr[lable[1]] = {cds[1]: "user"}
                                    self.di_re[lable[1]] = {
                                        cds[1]: str(os.getcwd())}
                                    return msg_return
                                msg_return = "Login is Unsuccesful - incorreect Pass"
                                return msg_return
                        except SystemError:
                            print("system error")
                        try:
                            if i == tem-True:
                                msg_return = "Username does not exist in the server"
                                return msg_return
                            else:
                                continue
                        except IOError:
                            print("input output error")
                msg_return = " User has already been logged in to the server"
                return msg_return
        except RuntimeError:
            print("run time error")

    def lists_of_files(self, lable):
        '''
        Lists displays all the files and folders in the working directory of the client application.

        Arguments:
        <<
        address:
            It is a group of the ip address and the port number of the client application.
        >>
        '''
        f_s_l = []
        try:
            for i in self.di_re[lable[1]].keys():
                shortterm = str(self.di_re[lable[1]][i])
            t_s = os.listdir(shortterm)
            f_s_l.append(
                ["Name_of_the_file", "size_of_file", "file_creation_time"])
            if len(t_s) == 0:
                pass_args = " No files are found "
                return pass_args
            try:
                for i in t_s:
                    j = os.stat(i)
                    f_s_l.append([i, j.st_size, time.ctime(j.st_mtime)])
                    pass_args = "\n".join(str(s) for s in f_s_l)
                return pass_args
            except SystemError:
                print("system error")
        except RuntimeError:
            print("run time error")

    def make_folder(self, cds, lable):
        '''
        create_folder creates a new folder in the working directory of the client application.

        Arguments:
        <<
        commands:
            It is the command given by the client to the server.
        address:
            It is a group of the ip address and the port numeber of the client application.
        >>
        '''
        try:
            if os.getcwd() == self.r_t:
                msg_return = " folder can't be created in root directory of the application"
                assert msg_return is not None
                return msg_return
            for i in self.di_re[lable[1]].keys():
                shortterm = str(self.di_re[lable[1]][i])
            try:
                t_s = os.listdir(shortterm)
                for i in range(0, len(t_s)):
                    if t_s[i] == cds[1]:
                        msg_return = "Folder is already exists"
                        assert msg_return is not None
                        return msg_return
                os.chdir(shortterm)
                os.mkdir(cds[1])
                msg_return = "Folder is to created"
                assert msg_return is not None
                return msg_return
            except SystemError:
                print("system error")
        except AssertionError:
            msg_return = 'No response to the given command'

    def wt_fl(self, cds):
        '''
        Write data to the file in current directory,starting on a new line.

        Parameters:
        <<
        commands:
            It is the command addressed by the user to the server.
        >>
        '''
        try:
            if cds[1] not in self.fs.keys():
                self.fs[cds[1]] = True
                try:
                    if len(cds) <= 2:
                        try:
                            fil_op = open(cds[1], "w")
                            fil_op.write("")
                            fil_op.close()
                            msg_return = " File has been created "
                        except PermissionError:
                            msg_return = " Denied to access to the requested file"
                    else:
                        try:
                            fil_op = open(cds[1], "a+")
                            fil_op.write("\n")
                            for i in range(2, len(cds)):
                                fil_op.write(cds[i])
                                fil_op.write(" ")
                            fil_op.close()
                            msg_return = " Writing the file complete "
                        except PermissionError:
                            msg_return = " Denied access to the reqeusted file"
                    del self.fs[cds[1]]
                    return msg_return
                except RuntimeError:
                    print("run time error")
            try:
                msg_return = " The file is use by the other user. "
                return msg_return
            except ValueError:
                print("the value entered is invalid")
        except AssertionError:
            msg_return = 'No response to the given command'

    def shift_folder(self, cds, lable):
        '''
        Move the present working directory to the specifised folder residing in the present folder.
        To go back to the before folder, a name of two dots <..> is used. 

        Arguments:
        <<
        commands:
            It is the command given by the user to the server.
        address:
            It is a group of the ip address and the port number of the user.
        >>
        '''
        for i in self.di_re[lable[1]].keys():
            shortterm = str(self.di_re[lable[1]][i])
        os.chdir(shortterm)
        enter = (f'{self.r_t}\\root')
        try:
            if os.getcwd() == enter:
                if cds[1] == "..":
                    msg_return = " Cannot move to previous folder from root folder "
                    return msg_return
                else:
                    for i in self.di_re[lable[1]].keys():
                        if i != cds[1]:
                            if self.psr[lable[1]][i] == "Admin":
                                if cds[1] == "Admin" or cds[1] == "User":
                                    os.chdir(cds[1])
                                    for i in self.di_re[lable[1]].keys():
                                        self.di_re[lable[1]] = {
                                            i: str(os.getcwd())}
                                    msg_return = "Present working directory has been changed!!"
                                    return msg_return
                                msg_return = "Denied to access the given file!!"
                                return msg_return
                            if cds[1] == "User":
                                os.chdir(cds[1])
                                for i in self.di_re[lable[1]].keys():
                                    self.di_re[lable[1]] = {
                                        i: str(os.getcwd())}
                                    msg_return = "Present working directory ahs been changed!!"
                                    return msg_return
                            msg_return = " Denied to access the given file!!"
                            return msg_return
                        os.chdir(cds[1])
                        for i in self.di_re[lable[1]].keys():
                            self.di_re[lable[1]] = {i: str(os.getcwd())}
                        msg_return = "Prensent working directory has been changed!!"
                        return msg_return
        except SystemError:
            print("System error")
        try:
            if cds[1] == "..":
                os.chdir("..")
                for i in self.di_re[lable[1]].keys():
                    self.di_re[lable[1]] = {i: str(os.getcwd())}
                msg_return = "Present working directory has been moved back to the previous folder!!"
                return msg_return
        except RuntimeError:
            print("runtime error")
        try:
            os.chdir(cds[1])
            for i in self.di_re[lable[1]].keys():
                self.di_re[lable[1]] = {i: str(os.getcwd())}
        except FileNotFoundError:
            msg_return = "folder is not found!!"
            return msg_return

        else:
            msg_return = "Present working directory has been changed!!"
            return msg_return

    def rd_fl(self, cds, lable):
        '''
        Read data from the file in Present working directory and return first 100 characters.
        Arguments:

        commands:
            It is the request passed by the user to the server.
        address:
            It is a group of the ip addresss and the port number of the user.
        '''
        try:
            for i in self.di_re[lable[1]].keys():
                end_user = str(self.di_re[lable[1]][i])
            try:
                for j in self.paa[end_user].keys():
                    self.list.append(str(j))
            except KeyError:
                self.paa[end_user] = {}
            finally:
                if len(cds) == True:
                    self.paa[end_user] = {}
                    msg_return = "command doesn't contain the file name!!"
                    return msg_return
                else:
                    if cds[1] in self.list:
                        zero = self.paa[end_user][cds[1]]
                        fil_op = open(cds[1], "r")
                        sample = str(fil_op.read())
                        why = list()
                        try:
                            if zero+100 <= len(sample):
                                try:
                                    for i in range(zero, zero+100):
                                        why.append(sample[i])
                                    pass_args = "".join(str(s) for s in why)
                                    self.paa[end_user] = {cds[1]: zero+100}
                                    return pass_args
                                except RuntimeError:
                                    print("runtime error")
                            else:
                                el = len(sample)
                                try:
                                    for i in range(zero, el):
                                        why.append(sample[i])
                                    pass_args = "".join(str(s) for s in why)
                                    self.paa[end_user] = {cds[1]: 0}
                                    return pass_args
                                except RuntimeError:
                                    print("run time error")
                        except RuntimeError:
                            print("runtime error")
                    else:
                        try:
                            file_list = os.listdir(os.getcwd())
                            if cds[1] in file_list:
                                why = list()
                                fil_op = open(cds[1], "r")
                                sample = str(fil_op.read())
                                if len(sample) > 100:
                                    for i in range(0, 100):
                                        why.append(sample[i])
                                    pass_args = "".join(str(s) for s in why)
                                    self.paa[end_user] = {cds[1]: 100}
                                    assert pass_args is not None
                                    return pass_args
                                elif len(sample) == False:
                                    msg_return = "The file is empty!!"
                                    assert msg_return is not None
                                    return msg_return
                                else:
                                    for i in range(0, len(sample)):
                                        why.append(sample[i])
                                    pass_args = "".join(str(s) for s in why)
                                    self.paa[end_user] = {cds[1]: len(sample)}
                                    return pass_args
                            elif cds[1] == '':
                                self.paa[end_user] = {}
                                msg_return = "The Present reading file is closed!!"
                                assert msg_return is not None
                                return msg_return
                            else:
                                msg_return = "The requested file doesn´t exist!!"
                                assert msg_return is not None
                                return msg_return
                        except PermissionError:
                            msg_return = " Denied to access the requested file!!"
                            return msg_return
                        except AssertionError:
                            msg_return = 'No respose to the given command!!'
        except RuntimeError:
            print("run time error")
