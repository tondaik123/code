from aptos_sdk.account import Account
from aptos_sdk.client import RestClient
import time
from datetime import datetime
import sys
import json

NODE_URL = 'https://fullnode.mainnet.aptoslabs.com/v1'
# https://fullnode.mainnet.aptoslabs.com/v1
# https://fullnode.testnet.aptoslabs.com/v1

rest_client = RestClient(NODE_URL)
print(f'Connect to chain ID = {rest_client.chain_id}')

# Run multiple
if len(sys.argv) > 1:
  listPrivate = sys.argv[1]

account = Account.load_key(str(listPrivate))
address = account.address()
publicKey = account.public_key()
privateKey = account.private_key

payload = {
  "function": "0x8eafc4721064e0d0a20da5c696f8874a3c38967936f0f96b418e13f2a31dcf4c::factory::mint_with_quantity",
  "type_arguments": [],
  "arguments": [
    "1"
  ],
  "type": "entry_function_payload"
}

def timestamp():
    timeNow = datetime.now()
    return timeNow

try:
  while True:
    timeNow = time.time()
    startTime = 1666540800
    countdown = (int(timeNow)-startTime)
    if countdown > -3:
      txh = rest_client.submit_transaction(account, payload)
      print(f'Transaction: {txh}')
      print(rest_client.wait_for_transaction(txh))
      break
    else:
      print(f'{timestamp()} | BlueMove Loading... {countdown} seconds | {str(address)[60:]}')
except Exception as exc:
  print(exc)

input('Pause - Press Enter to exit...')
