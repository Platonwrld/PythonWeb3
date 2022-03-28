from web3 import Web3

ganache_url = "HTTP://127.0.0.1:7545"                       # local blockchain
web3 = Web3(Web3.HTTPProvider(ganache_url))                 # connect

print(web3.isConnected())

# sending cryptocurrency from 1 account to 2 
account_1 = "0x94a9EEa52B805FaF3Ba728446B28541dd38507f6"    # 1 random account
account_2 = "0x40DfC0cdA8AF23fdf09A3bCDDBCe848E08Ed2De8"    # 2 random account

private_key = ""        # private key from 1 account

# getting nonce from 1 account
nonce = web3.eth.getTransactionCount(account_1)

# creating transaction
tx = {
    'nonce': nonce,                            
    'to': account_2,
    'value': web3.toWei(1, 'ether'),
    'gas': 2000000,
    'gasPrice': web3.toWei('50', 'gwei')
}

# transaction signing 
tx_signed = web3.eth.account.signTransaction(tx, private_key)

# instantiation transaction
tx_hash = web3.eth.sendRawTransaction(tx_signed.rawTransaction)
print(web3.toHex(tx_hash))
