blockchain = []


def get_last_blockchain_item():
    return blockchain[-1]


def add_value(transaction_amount, last_transaction=[1]):
    blockchain.append([last_transaction, transaction_amount])
    print(blockchain)


def get_user_input():
    return float(input('your transaction amount: '))


tx_amount = get_user_input()
add_value(tx_amount)

# add_value(0.3,get_last_blockchain_item())
# add_value(0.5,get_last_blockchain_item())

# for i in range(2,10):
#     add_value(i)

while True:
    tx_amount = get_user_input()
    add_value(tx_amount)
    for block in blockchain:
        print(block)


    print('Done')
