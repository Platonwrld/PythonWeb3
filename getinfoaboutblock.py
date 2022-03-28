from web3 import Web3


# read information from the blockchain
infura_url = ""                                                                 # reference on endpoint from infura
web3 = Web3(Web3.HTTPProvider(infura_url))                                      
                                        

hash = '0x25433d44ebf7dfca8d82597a782d94e51ace4d6c5635cb4d55f470d97b32d8de'     # hash by block
print(web3.eth.getTransactionByBlock(hash, 2))                                  # 2 - transaction that i wanna see
