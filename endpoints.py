from flask import Flask
from flask import request
from flask import jsonify
import json
import os.path
import requests
from hashing import mine_hash
from blockchain import BlockChain

app = Flask(__name__)

connections = []

blockchain = BlockChain()


@app.route('/test', methods=['GET'])
def test():
    return "test"


@app.route('/transactions/new', methods=['POST'])
def new_transaction():
    request_json = request.get_json()
    blockchain.add_transaction(request_json)
    return jsonify(request_json), 201


@app.route('/transactions/get', methods=['GET'])
def get_transactions():
    transactions = blockchain.get_transactions()
    return jsonify(transactions), 201


@app.route('/mine', methods=['POST'])
def mine_block():
	latest_block = blockchain.mine()
	return jsonify(latest_block), 201


@app.route('/chain/get', methods=['GET'])
def get_chain():
	block_json = blockchain.get_chain()
	return jsonify(block_json)


@app.route('/block/latest', methods=['GET'])
def last_block():
	block_json = blockchain.get_chain()
	return jsonify(block_json[-1])


@app.route('/get_info', methods=['GET'])
def get_info():
	blockchain_json = blockchain.get_chain()
	transactions = blockchain.get_transactions()

	chain = {}
	chain["chain"] = blockchain_json
	chain["connections"] = connections
	chain["transactions"] = transactions
	return jsonify(chain)


@app.route('/join_network', methods=['GET'])
def join_network():
	global connections
	request_json = request.get_json()
	conn = request_json["connection"]
	chain = requests.get(conn + "/get_info")

	connections = chain["connections"]
	blockchain.set_chain(chain["chain"])
	blockchain.set_transactions(chain["transactions"])
	return "Success!"



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)