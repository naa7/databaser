import os, time, tabulate

try:
    class Database:

        def __init__(self, database={}):
            self.__database = database
            self.__username = ("admin1", "admin2", "admin3")
            self.__password = ("admin", "password", "abc123")


        def clear(self):
            if os.name == 'posix':
                _ = os.system('clear')
            else:
                _ = os.system('cls')


        def database(self):
            with open("usernames.txt",'r') as f:
                usernames_list = [i.strip() for i in f]
            with open("passwords.txt",'r') as g:
                passwords_list = [j.strip() for j in g]
            combined_list = list(zip(usernames_list, passwords_list))
            data = dict(zip(range(len(combined_list)), combined_list))
            return data


        def lookup(self):
            database = self.database()
            while True:
                option = input("Look up [U]sername or [P]assword | [R]eturn: ")
                
                if (option == 'U' or option == 'u') and (option != 'R' or option != 'r'):
                    password = input("Enter password: ")
                    flag = 0
                    for value in database.values():
                        if password == value[1]:
                            print("Username:", value[0])
                            flag = 0
                            break
                        else:
                            flag = 1
                            continue
                    if flag:
                        print("--- Not found ---")
                    time.sleep(2)
                    self.clear()

                elif (option == 'P' or option == 'p') and (option != 'R' or option != 'r'):
                    username = input("Enter username: ")
                    flag = 0
                    for value in database.values():
                        if username == value[0]:
                            print("Password:", value[1])
                            flag = 0
                            break
                        else:
                            flag = 1
                            continue
                    if flag:
                        print("--- Not found ---")
                    time.sleep(2)
                    self.clear()

                elif option == 'R' or option == 'r':
                    break

                else:
                    print("--- Error, wrong entry! ---")
                    time.sleep(1)
                    self.clear()
                    continue


        def authentication(self):
            print("+================+")
            print("|   Login Page   |")
            print("+================+")
            login_username = input(" Username: ")
            login_password = input(" Password: ")
            
            if login_username in self.__username:
                index = self.__username.index(login_username)
                if login_password == self.__password[index]:
                    return True
            else:
                return False

        def add(self):
           
            while True:
                username = input("Enter username | [R]eturn: ")
                if username == 'R' or username == 'r':
                    break
                password = input("Enter password: ")
                with open("usernames.txt", 'a') as f:
                    f.write("{}\n".format(username))
                with open("passwords.txt", 'a') as g:
                    g.write("{}\n".format(password))
                print("--- Added successfully ---")
                time.sleep(1)
                self.clear()

        def remove(self):
            database = self.database()
            while True:
                username = input("Enter username | [R]eturn: ")
                if username == 'R' or username == 'r':
                    break
                password = input("Enter Password: ")
                for value in database.values():
                        if username == value[0] and password == value[1]:
                            flag = 0
                            with open("usernames.txt", 'r') as f:
                                old_file = f.read()
                                new_file = old_file.replace("{}\n".format(username), '')
                                with open("usernames.txt", 'w') as f_out:
                                    f_out.write(new_file)
                            with open("passwords.txt", 'r') as g:
                                old_file = g.read()
                                new_file = old_file.replace("{}\n".format(password), '')
                                with open("passwords.txt", 'w') as g_out:
                                    g_out.write(new_file)
                            print("--- Removed successfully ---")
                            break
                        else:
                            flag = 1
                            continue
                if flag:
                    print("--- Not found ---")

                time.sleep(1)
                self.clear()
        

        def display(self):
            self.clear()
            database = self.database()
            header = ["#", "Username", "Password"]
            row = []
            for key, value in database.items():
                row.append([key, value[0], value[1]])
            print(tabulate.tabulate(row, header, tablefmt='grid'))



    def main():
        #data = dict(zip(database.Usernames[:-1], database.Passwords[:-1]))
        class_call = Database()
        class_call.clear()
        while True:
            try:
                if class_call.authentication():
                    class_call.clear()           
                    while True:
                        user_input = input("[A]dd | [R]emove | [L]ookup | [D]isplay | [Q]uit: ")
                        class_call.clear()
                        if user_input == 'A' or user_input == 'a':
                            class_call.add()
                            class_call.clear()
                        elif user_input == 'R' or user_input == 'r':
                            class_call.remove()
                            class_call.clear()
                        elif user_input == 'L' or user_input == 'l':
                            class_call.lookup()
                            class_call.clear()
                        elif user_input == 'D' or user_input == 'd':
                            class_call.display()
                            while True:
                                answer = input("[R]eturn: ")
                                if answer == 'R' or answer == 'r':
                                    class_call.clear()
                                    break
                                else:
                                    print("--- Error, wrong entry! ---")
                                    continue
                        elif user_input == 'Q' or user_input == 'q':
                            break
                        else:
                            print("--- Error, wrong entry! ---")
                            time.sleep(1)
                            class_call.clear()
                            continue
                    break

                else:
                    print("\n--- Unrecognized username/password ---")
                    time.sleep(1.5)
                    class_call.clear()
                    continue
            except KeyboardInterrupt:
                print("\n\nGoodbye")
                time.sleep(1)
                class_call.clear()

                break
except:
    print("Oops!", sys.exc_info()[0], "occurred.")

if __name__ == "__main__":
        main()
