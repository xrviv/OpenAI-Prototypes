import hashlib
import json

class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.hash_block()

    def hash_block(self):
        sha = hashlib.sha256()
        sha.update(str(self.index).encode() +
                   str(self.timestamp).encode() +
                   json.dumps(self.data).encode() +
                   str(self.previous_hash).encode())
        return sha.hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, "01/01/2017", "Genesis Block", "genesis_block_hash")

    def add_block(self, new_block):
        new_block.previous_hash = self.chain[-1].hash
        new_block.hash = new_block.hash_block()
        self.chain.append(new_block)

blockchain = Blockchain()
blockchain.add_block(Block(1, "01/01/2018", {"amount": 4}, blockchain.chain[-1].hash))
blockchain.add_block(Block(2, "01/01/2019", {"amount": 8}, blockchain.chain[-1].hash))

for block in blockchain.chain:
    print(f'Index: {block.index}')
    print(f'Timestamp: {block.timestamp}')
    print(f'Data: {block.data}')
    print(f'Hash: {block.hash}')
    print()
