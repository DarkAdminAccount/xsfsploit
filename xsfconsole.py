import socket
import os, sys

host=''
port=''
session=''

def exploit():
       print('exploiting .........')
       if host!='' and port!='':
              print()
              print('creating the tcp/ip4 socket ........')
              tcp4=socket.socket(socket.AF_INET, socket.SOCK_STREAM, 6)
              print('created the tcp/ip4 socket ........')
              print('binding the tcp/ip4 socket from host and port options ......')
              tcp4.bind((host, port))
              print('bindet the tcp/ip4 socket from host and port options .....')
              tcp4.listen()
              print('hosting on '+host+' : '+port+' ...........')
              print('waiting the client connection .......')
              c, addr=tcp4.accept()
              print()
              print('connection sucsess with '+add[0]+' : '+str(addr[1]))
              print('client socket is : '+c)
              print()
              print('starting the meterpreter .....')
              print('started the meterpreter .....')
              print()
              while True:
                     meterpreter=input('meterpreter ('+addr[0]+' : '+str(addr[1])+') > ')
                     if meterpreter!='exit':
                            print('sending the command .........')
                            c.send(meterpreter.encode('utf32'))
                            print('sented the meterpreter ........')
                            print('recving the output .....')
                            output=c.recv(1024).decode('utf32')
                            print('recvied output ........')
                            print('output: \n'+output)
                     else:
                            c.close()
                            print('closed session ........')
       else:
              pass
def copy_file(file, name):os.system('copy '+file+' '+name if os.name == 'nt' else 'cp '+file+' '+name)
def clear():os.system('cls' if os.name == 'nt' else 'clear')

def main():
       clear()
       global host, port, session
       print('started the xsfconsole .......')
       print('start .....')
       print()
       print('starting time is: '+time.ctime())
       print()
       while True:
              xsf=input('console > ')
              if xsf=='help':
                     print('help: ')
                     print()
                     print('exploit')
                     print('set <option> <valule>')
                     print('show options')
                     print('use <module>')
                     print('mkfile <module> <name>')
#                    print('banner')
                     print('time')
                     print('<console system command>')
                     print('exit')
                     print()
                     continue
              elif xsf=='exploit' or xsf=='run' or xsf=='launch':
                     exploit()
                     continue
              elif 'set ' in xsf:
                     option=xsf.split()[-2]
                     if option=='host':
                            valule=xsf.split()[-1]
                            host=valule
                            print('host => '+host)
                            continue
                     elif option=='port':
                            valule=xsf.split()[-1]
                            port=valule
                            print('port => '+port)
                            continue
                     elif option=='session':
                            valule=xsf.split()[-1]
                            session=valule
                            print('session => '+valule)
                            continue
                     else:
                            continue
              elif 'use ' in xsf:
                     print('importing the module ........')
                     _module=xsf.split()[-1]
                     module.replace('modules','')
                     __import__(module)
                     __main__()
                     continue
              elif 'mkfile ' in xsf:
                     _path=xsf.split()[-1]
                     _module=xsf.split()[-2]
                     module.replace('modules','')
                     copy_file(module, path)
                     print('copied the file ....')
                     continue
              elif xsf=='time':
                     print('time is: '+time.ctime())
                     continue
              elif xsf=='ecit' or xsf=='break' or xsf=='quit':
                     print('exiting ......')
                     exit()
              else:
                     print('command not found please try again .....')
                     pass
def controle():
       try:
              import time
              import request, requests
              import subprocess as sp, numpy as np
              import console, tkinter
              import socketserver, http.server
              import __future__
              from xsf.tools import *
              from xsf.tools.core import *
              main()                      #main function
       except KeyboardInterrupt:
              pass
       except EOFError:
              pass
       except OSError:
              print('OSError: not supported error .........')
              pass
       except OverflowError:
              print('overflow valule .......')
              pass
       except ConnectionRefusedError:
              print('connection refused error .........')
              pass
       except IndexError:
              print("the command are with args \ntype: 'help' for more info")
              pass
       except ImportError:
              print('please install the current modules')
