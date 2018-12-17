import hashlib
import json

def hash_256(string_to_hash):
	sha256string = hashlib.sha256(string_to_hash.encode()).hexdigest()
	return sha256string


def mine_hash(blocknumber, data, old_hash):	
	hash_256_string = str(blocknumber) + data
	nounce = 0
	while(True):
		nounce += 1
		print(nounce)
		sha256 = hash_256(hash_256_string+str(nounce))
		if "0000" in sha256[:4]:
			print(sha256)
			o = {}
			o['hash'] = sha256
			o['nounce'] = nounce
			o['data'] = data
			o['blocknumber'] = blocknumber
			o['old_hash'] = old_hash
			return o


if __name__ == '__main__':
	try:
		#block_json = '[{"blocknumber":"0","old_hash":"0000e35b7ff1b88879dc3fad7fc7e85a5f354c806b7c17b684ab10cb53a817b5","data":"a"}]'
		#block_json = json.loads(block_json)
		with open('blockchain.json', 'r') as fp:
			block_json = json.load(fp)
		for x in range(1,10):
			blocknumber = int(block_json[-1]['blocknumber'])+1
			old_hash = block_json[-1]['old_hash']
			data = "Hej"
			block_json.append(mine_hash(blocknumber,data,old_hash))
		with open('blockchain.json', 'w') as fp:
			json.dump(block_json, fp)
	except Exception as e:
		with open('blockchain.json', 'w') as fp:
			json.dump(block_json, fp)
	


