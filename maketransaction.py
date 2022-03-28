from web3 import Web3

ganache_url = "HTTP://127.0.0.1:7545"                       # адрес из локального блокчейна 
web3 = Web3(Web3.HTTPProvider(ganache_url))                 # коннект с адресом

print(web3.isConnected())

# отправление криптовалюты на c 1 аккаунта на 2
account_1 = "0x94a9EEa52B805FaF3Ba728446B28541dd38507f6"    # 1 рандомный аккаунт 
account_2 = "0x40DfC0cdA8AF23fdf09A3bCDDBCe848E08Ed2De8"    # 2 рандомный аккаунт

private_key = "66c8a3cf2dd342b5654d6cfaba4e02abf743cfca6e923de3cdcbb6f1cefe5fc7"        # приватный ключ 1 аккаунта

# получение nonce у 1 аккаунта
nonce = web3.eth.getTransactionCount(account_1)

#создание самой транзакции 
tx = {
    'nonce': nonce,                            #nonce предотвращает отправку повторной транзакции 
    'to': account_2,
    'value': web3.toWei(1, 'ether'),
    'gas': 2000000,
    'gasPrice': web3.toWei('50', 'gwei')
}

# подписание транзакции 
tx_signed = web3.eth.account.signTransaction(tx, private_key)

# осуществление транзакции
tx_hash = web3.eth.sendRawTransaction(tx_signed.rawTransaction)
print(web3.toHex(tx_hash))