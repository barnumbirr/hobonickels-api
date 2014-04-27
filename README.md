<h1><img src="https://raw.github.com/c0ding/hobonickels-api/master/doc/hobonickels.png" height=55 alt="hobonickels" title="hobonickels"> hobonickels-api</h1>

[![PyPi Version](http://img.shields.io/pypi/v/hobonickels.svg)](https://pypi.python.org/pypi/hobonickels/)   [![Downloads](http://img.shields.io/pypi/dm/hobonickels.svg)](https://pypi.python.org/pypi/hobonickels/)

hobonickels is an APACHE licensed library written in Python designed to provide a simple to use API for the HoboNickels cryptocurrency.

## More about HoboNickels:

HoboNickels is a cryptographic currency, similar to Bitcoin, that is designed to make online transactions easy and efficient.

HoboNickels wallet clients are being actively developed and improved upon. HoboNickels (HBN) is an extremely fast and efficient crypto-currency. With a Proof of Work block time of 30 seconds coupled with fast Proof of Stake, it is pushing to be one of the fastest coins available. The 2-5% Proof of Stake is also one of the most generous staking algorithms released. The stake is designed to keep the inflation rate from getting out of control, with the % of stake decreasing as more people stake the coin. HoboNickels has the added security of a Proof of Stake coin with the addition of security features like Automated Block Checkpoints. HoboNickels are the first coin to use Multi-Wallet functionality.

## Installation:

From source use

    $ python setup.py install

or install from PyPi

    $ pip install hobonickels

## API Documentation:

This API can currently retrieve the following stats from [hbn.blockx.info](http://hbn.blockx.info/) and [CryptoCoin](http://www.cryptocoincharts.info)

### Network:

  - Difficulty:

```
>>> import hobonickels
>>> hobonickels.get_difficulty()
5.469
```

  - Hashrate:

```
>>> hobonickels.hashrate()
114711299
```

  - Block count:

```
>>> hobonickels.block_count()
783661.0
```

  - Total coins:

```
>>> hobonickels.total_coins()
4001078.78388
```

### Addresses:

  - Address balance:
    [PARAMETER] is required and should be a HBN address.

```
>>> hobonickels.addressbalance(PARAMETER)
333099.781601
```

  - Address to hash:
    [PARAMETER] is required and should be a HBN address.

```
>>> hobonickels.addresstohash(PARAMETER)
5A21B5DBCF936524C946A035AB6C572107B08F6C
```

  - Check address:
    [PARAMETER] is required and can be any crypto address.

```
>>> hobonickels.checkaddress(PARAMETER)
22
```

  - Get received by address:
    [PARAMETER] is required and should be a HBN address.

```
>>> hobonickels.getreceivedbyaddress(PARAMETER)
3009149.043709
```

  - Get sent by address:
    [PARAMETER] is required and should be a HBN address.

```
>>> hobonickels.getsentbyaddress(PARAMETER)
2676049.262108
```

  - PUBKEY hash:
    [PARAMETER] is required and should be a PUBKEY.

```
>>> hobonickels.hashpubkey(PARAMETER)
C16471CD10EC45881BFE7F75B291962000C67020
```

  - Hash to address:
    [PARAMETER] is required and should be an address hash.

```
>>> hobonickels.hashtoaddress(PARAMETER)
Es8mAQxXCKHA7YPnBhy4SzhLrmCH27sRu6
```

  - Translate address:
    [PARAMETER] is required and can be any crypto address.

```
>>> hobonickels.hashtoaddress(PARAMETER)
EuRyukrySwTiA4uQqPD8z3o7WsdeieD4Vo
```

  - Address/private key generation :

```
>>> hobonickels.generate_address()
{
    "address": "EwUemkvvJVnREy72fnTkpHsziBWviZaBRb", 
    "private_key": "QzxvMcixWv3ukY2ckmRMrmNwhRvipk6zoWYfqZPoZ4PW8WsLASuq" 
}
```

### Exchanges:

  - BTC:

```
>>> hobonickels.to_btc()
{
    "latest_trade": "2014-04-23 00:56:28", 
    "volume_btc": "3.75", 
    "price": "0.00030510", 
    "price_before_24h": "0.00029690", 
    "volume_first": "13142.7944186926", 
    "best_market": "cryptsy", 
    "volume_second": "3.75384861370549", 
    "id": "hbn/btc"
}
```

## License:

```
  Apache v2.0 License
  Copyright 2014 Martin Simon

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

     http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.

```

## Useful links:

* [Hobonickels website](http://www.hobonickels.info/)
* [Hobonickels Blockexplorer](http://hbn.blockx.info/)

## Buy me a coffee?

If you feel like buying me a coffee (or a beer?), donations are welcome:

```
WDC : WbcWJzVD8yXt3yLnnkCZtwQo4YgSUdELkj
HBN : F2Zs4igv8r4oJJzh4sh4bGmeqoUxLQHPki
DOGE: DRBkryyau5CMxpBzVmrBAjK6dVdMZSBsuS
```
