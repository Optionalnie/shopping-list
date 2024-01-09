import sys

shop_list = []

while True:

    decision = input('No elo, robimy zakupową listę? Wpisz "zakupy" aby zacząć tworzyć listę albo "exit" aby wyjsc z apki ew. wpisz "lista" aby wyswietlic aktualna liste zakupów: ')

    if decision == 'zakupy':
        while True:
            zakupy = input('Wpisz listę zakupów - Napisz "stop" aby zakończyć dodaniwe zakupów ')
            if zakupy.lower() == 'stop':
                break
            shop_list.append(zakupy)
        
    elif decision == 'exit':
        sys.exit
        
    elif decision == 'lista':
        print('Oto Twoja lista zakupów: ' + str(shop_list))    
        
        
    else:
        print('Zła komenda')
        continue