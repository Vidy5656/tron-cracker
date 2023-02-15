const TronWeb = require('tronweb');
const hdWallet = require('tron-wallet-hd');

const utils = hdWallet.utils;

const HttpProvider = TronWeb.providers.HttpProvider;
const fullNode = new HttpProvider("https://api.trongrid.io");
const solidityNode = new HttpProvider("https://api.trongrid.io:8091");
const eventServer = new HttpProvider("https://api.trongrid.io:8092");

async function get_balance(seed) { 
  const account = await utils.getAccountAtIndex(seed, 0);
  const privateKey = account.privateKey;
  const tronWeb = new TronWeb(fullNode, solidityNode, eventServer, privateKey);
  const address = tronWeb.defaultAddress.base58;
  const balance = await tronWeb.trx.getBalance(address);
  console.log(balance);
}

const args = process.argv;
const seed = args[2];
get_balance(seed);
