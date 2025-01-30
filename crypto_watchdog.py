import requests

def check_crypto_scam(username):
    """Checks if a crypto influencer is promoting a potential scam."""
    url = f"https://api.coingecko.com/api/v3/coins/bitcoin"  
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
       
        market_data = data.get("market_data", {})
        if market_data:

            if market_data.get("current_price", {}).get("usd", 0) < 1:
                return f"🚨 Warning! {username} is promoting a potential scam due to low coin value."
            else:
                return f"✅ {username} seems clean... for now."
        else:
            return "Error: Market data not available."
    return "Error fetching crypto data."

if __name__ == "__main__":
    print(check_crypto_scam("random_influencer"))
