import hashlib

class BlockChain:

	def __init__(self):
		first_block = {"blocknumber":0,
					   "hash":"0000e35b7ff1b88879dc3fad7fc7e85a5f354c806b7c17b684ab10cb53a817b5",
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


	def check_if_transaction_exists(self, transaction):
		for t in self.transactions:
			if str(t) == str(transaction):
				return True

		return False


	def validate_block(self, block):
		latest_block = self.chain[-1]
		return self.is_block_valid(block, latest_block)


	def mine(self):
		latest_block = self.chain[-1]
		data = self.transactions
		blocknumber = latest_block["blocknumber"] + 1
		hash_256_string = str(blocknumber) + str(data) + latest_block["hash"]
		nounce = 0
		while(True):
			nounce += 1
			sha256 = self.hash_256(hash_256_string + str(nounce))
			if "0000" in sha256[:4]:
				print(sha256)
				block = {}
				block['hash'] = sha256
				block['nounce'] = nounce
				block['data'] = data
				block['blocknumber'] = blocknumber
				block['old_hash'] = latest_block["hash"]

				self.add_block_to_chain(block)
				return block


	def is_block_valid(self, block, old_block):
		print("********************")
		print(str(block))
		print(str(old_block))
		if (block["blocknumber"] == (old_block["blocknumber"] + 1)
			and block["old_hash"] == old_block["hash"]):
			
			temp_hash_256_string = str(block["blocknumber"]) + str(block["data"]) + str(old_block["hash"])
			temp_hash = self.hash_256(hash_256_string + str(block['nounce']))
			print(temp_hash)
			if temp_hash == block["hash"]:
				return True
		return False


	def hash_256(self, string_to_hash):
		sha256string = hashlib.sha256(string_to_hash.encode()).hexdigest()
		return sha256string