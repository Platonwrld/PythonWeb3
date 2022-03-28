from calendar import c
from web3 import Web3

# web3 instance 
infura_url = ""    
web3 = Web3(Web3.HTTPProvider(infura_url))                                

account = web3.eth.account.create()
print(account)
print(account.address)
print(account.privateKey)

keystore = account.encrypt('12345')
print(keystore)

decrypt = web3.eth.account.decrypt(keystore, '12345')
print(decrypt)
