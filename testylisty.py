import sys

shop_list = []

while True:

    decision = input('Lets make a shopping list! Enter "shop" to create shopping list, type "exit" to exit application, or you can type "list" to check shopping list: ')

    if decision == 'shop':
        while True:
            shop = input('Enter goods that have to be purchased - Write "stop" to stop entering goods.')
            if shop.lower() == 'stop':
                break
            shop_list.append(shop)
        
    elif decision == 'exit':
        sys.exit
        
    elif decision == 'list':
        print('Here is your shopping list: ' + str(shop_list))    
    
        
    else:
        print('Wrong command')
        continue