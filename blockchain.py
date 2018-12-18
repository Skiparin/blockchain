

Class BlockChain()

	def __init__(self):
		first_block = {"blocknumber":"0",
					   "old_hash":"0000e35b7ff1b88879dc3fad7fc7e85a5f354c806b7c17b684ab10cb53a817b5",
					   "data":"first_block"}
		self.transactions = []
		self.chain = [first_block]
		

	def add_transaction(self, transaction):
		self.transactions.append(transaction)


	def set_transactions(self, transactions):
		self.transactions = transactions


	def get_transactions(self):
		return self.transactions


	def clear_transactions(self):
		self.transactions = []


	def add_block_to_chain(self, block):
		self.chain.append(block)


	def set_chain(self, chain):
		self.chain = chain


	def get_chain(self):
		return self.chain

	def mine(self):
		hash_256_string = str(blocknumber) + data
		nounce = 0
		while(True):
			nounce += 1
			print(nounce)
			sha256 = self.hash_256(hash_256_string + str(nounce))
			if "0000" in sha256[:4]:
				print(sha256)
				o = {}
				o['hash'] = sha256
				o['nounce'] = nounce
				o['data'] = data
				o['blocknumber'] = blocknumber
				o['old_hash'] = old_hash
				return o


	def hash_256(self, string_to_hash):
		sha256string = hashlib.sha256(string_to_hash.encode()).hexdigest()
		return sha256string