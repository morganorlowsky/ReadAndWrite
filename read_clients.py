def main():
    clients_file = open('clients.txt','r')

    clientNo = 1

    for client in clients_file:
        client = client.rstrip('\n')
        print(f"{clientNo}. {client}")
        clientNo += 1
 
        

main()