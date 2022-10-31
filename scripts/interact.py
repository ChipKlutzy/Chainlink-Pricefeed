from brownie import BTCUSDPrice, ETHUSDPrice
from time import sleep

def priceQuery(BTC, ETH):

    print(f"\nBitcoin Price = ${round(BTC.getLatestPrice() / 1e8, 2)} \n")
    print(f"Ether Price = ${round(ETH.getLatestPrice() / 1e8, 2)} \n")

def main():

    BTCUSD = BTCUSDPrice.at("0x4DCB308AC98C63020b3FC0fa5738E4a7791d7FE5")
    ETHUSD = ETHUSDPrice.at("0xa592C36b16FCeeC055b474b89DAC82E3e003c3eF")

    while(True):
        priceQuery(BTCUSD, ETHUSD)
        sleep(60)
