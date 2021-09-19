blockchain = []


def get_last_blockchain_item():
    """Returns value of last block in block chain"""
    if len(blockchain) < 1:
        return None
    return blockchain[-1]


def add_transaction(transaction_amount, last_transaction=[1]):
    if last_transaction == None:
        last_transaction = [1]
    blockchain.append([last_transaction, transaction_amount])
    print(blockchain)

def verify_chain():
    # block_index = 0
    is_valid = True

    for block_index in range(len(blockchain)):
        if block_index == 0:
            continue
        elif blockchain[block_index][0] == blockchain[block_index - 1]:
            is_valid = True
        else: 
            is_valid = False
            break
    return is_valid       

def get_transaction_value():
    return float(input('your transaction amount: '))


def get_user_choice():
    user_input = input("Your Choice: ")
    return user_input


def print_blockchain_elements():
    for block in blockchain:
        print('Outputting Block')
        print(block)
    else:
        print('-' * 20)

# tx_amount = get_transaction_value()
# add_transaction(tx_amount)

# add_value(0.3,get_last_blockchain_item())
# add_value(0.5,get_last_blockchain_item())

# for i in range(2,10):
#     add_value(i)

waiting_for_input = True;

while waiting_for_input:
    print("please Choose: ")

    print("1: Add a new Transaction Value")
    print("2: Output the blockchain blocks")
    print("h: Manipulate blockchain blocks")
    print("q: quit")
    user_choice = get_user_choice()
    if user_choice == '1':
        tx_amount = get_transaction_value()
        add_transaction(tx_amount, get_last_blockchain_item())
    elif user_choice == '2':
        print_blockchain_elements()
    elif user_choice == 'h':
        if len(blockchain) >= 1:
            blockchain[0] = [2]

    elif user_choice == 'q':
        waiting_for_input = False;
    else:
        print('Input was invalid . Please pick a value from the list')
    if not verify_chain():
        print("invalid blockchain")
        break

print('Done')
