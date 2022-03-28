from calendar import c
from web3 import Web3

# web3 instance 
infura_url = "https://mainnet.infura.io/v3/ef0e860f921a488fa3d889927970f4a9"    # ссылка на endpoint проекта на infura
web3 = Web3(Web3.HTTPProvider(infura_url))                                      # установление взаимодейтсвия проекта и сервера 

account = web3.eth.account.create()
print(account)
print(account.address)
print(account.privateKey)

keystore = account.encrypt('12345')
print(keystore)

decrypt = web3.eth.account.decrypt(keystore, '12345')
print(decrypt)