from flask import Flask
from flask import request
from flask import jsonify
import json
import os.path
import requests
from hashing import mine_hash
from blockchain import BlockChain

app = Flask(__name__)

connections = ["http://192.168.0.1:5001",
			   "http://192.168.0.1:5002",
			   "http://192.168.0.1:5003",
			   "http://192.168.0.1:5004"]

blockchain = BlockChain()


@app.route('/test', methods=['GET'])
def test():
    return "test"


def send_transactions_to_network(transaction):
		for conn in connections:
			requests.post(conn + "/transactions/new", json=transaction)


def send_block_to_be_validated(block):
	for conn in connections:
		requests.post(conn + "/validate_block", json=block)


@app.route('/validate_block', methods=['POST'])
def validate_block():
	request_json = request.get_json()
	if blockchain.validate_block(request_json):
		blockchain.add_block_to_chain(request_json)
		blockchain.clear_transactions()
		send_block_to_be_validated(request_json)


@app.route('/transactions/new', methods=['POST'])
def new_transaction():
	request_json = request.get_json()
	if not blockchain.check_if_transaction_exists(request_json):
		blockchain.add_transaction(request_json)
		send_transactions_to_network(request_json)
		return jsonify(request_json), 201
	else:
		return "Transaction already exists", 400


@app.route('/transactions/get', methods=['GET'])
def get_transactions():
    transactions = blockchain.get_transactions()
    return jsonify(transactions), 201


@app.route('/mine', methods=['POST'])
def mine_block():
	block = blockchain.mine()
	send_block_to_be_validated(block)
	blockchain.clear_transactions()
	return jsonify(block), 201


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
    app.run(host='0.0.0.0', port=5000, debug=True)