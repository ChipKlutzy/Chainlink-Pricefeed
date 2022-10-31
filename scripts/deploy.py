from brownie import BTCUSDPrice, ETHUSDPrice, network, config, accounts
import time

def main():

    tx_sender = accounts.load("PolygonAccount1")

    print("1. Deploying BTCUSDPrice Contract Under Progress.......................\n")
    BTCUSD = BTCUSDPrice.deploy(
        config["networks"][network.show_active()]["BTC_USD_Price_Feeder"],
        {'from': tx_sender}
    )
    print(f"BTCUSDPrice deployed @ {BTCUSD.address}\n")

    print("2. Deploying ETHUSDPrice Contract Under Progress.......................\n")
    ETHUSD = ETHUSDPrice.deploy(
        config["networks"][network.show_active()]["ETH_USD_Price_Feeder"],
        {'from': tx_sender}
    )
    print(f"ETHUSDPrice deployed @ {ETHUSD.address}\n")

    ETHBTC = BTCUSD.getLatestPrice() / ETHUSD.getLatestPrice() 

    print(f"The cost of 1 BTC in terms of ETH = {round(ETHBTC, 2)} ETH/BTC")

    # while(True):
    #     Price = PC.getLatestPrice({'from': tx_sender})
    #     print(f"Present Exchange Rate of ETH/USD is ${Price / 1e8}\n")
    #     time.sleep(10)


