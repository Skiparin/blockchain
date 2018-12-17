from flask import Flask
from hashing import mine_hash

app = Flask(__name__)

def get_chain():
	with open('blockchain.json', 'r') as fp:
		block_json = json.load(fp)
		return block_json

@app.route('/test', methods=['GET'])
def test():
    return "test"

@app.route('/post', methods=['POST'])
def mine_block():
	request_json = request.get_json()
	block_json = get_chain()
	blocknumber = int(block_json[-1]['blocknumber']) + 1
	old_hash = block_json[-1]['old_hash']
	data = request_json["data"]
	return mine_hash(blocknumber,data,old_hash)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)