# Mini Wallet API

This is a simple Flask-based API for managing a mini wallet as part of a technical exercise. The API allows users to add virtual money to the wallet, withdraw virtual money, and disable the wallet.

## Prerequisites

- Python 3.x
- Flask

## Installation

1. Clone this repository to your local machine:

   ```bash
   git clone git@github.com:sammarth-kapse/julo-wallet.git

2. Navigate to the project directory:
    ```bash
   cd julo-wallet
3. Create a virtual environment:
    ```bash
   python3 -m venv venv
4. Activate the virtual environment:
   * On macOS and Linux:
      ```bash
      source venv/bin/activate
      ```   
   * On Windows:
      ```bash
      venv\Scripts\activate
      ```   
5. Install the required packages:
   ```bash
   pip install -r requirements.txt

## How In-Memory Wallets are manage:
* Upon initiating the wallet a token is generated and corresponding wallet with respective id is composed.
* We store wallets in dictionary mapping from id to object.
* We map token to wallet id. To have multiple running wallets.
* Each wallet can only be accessed via the token which was first generated.

## Usage

1. Start the Flask application:
   ```bash
   python app.py

2. Use an API client like curl or Postman to interact with the API.
<br> Use 127.0.0.1:5000 instead of localhost as port 80 might be busy.
 #### CURLs: 
   * Initialize my account for wallet
      ```bash
     curl --location 'http://127.0.0.1:5000/api/v1/wallet' \
     --form 'customer_id="ea0212d3-abd6-406f-8c67-868e814a2436"'
     ```
     This will give token. Which will map (using in auth) to all the functions for that wallet.
   <br></br>
   
   * Enable my wallet
     ```bash
     curl --location --request POST 'http://127.0.0.1:5000/api/v1/wallet' \
     --header 'Authorization: Token 6b3f7dc70abe8aed3e56658b86fa508b472bf238'
     ``` 
   
   * View my wallet balance
     ```bash
     curl --location 'http://127.0.0.1:5000/api/v1/wallet' \
     --header 'Authorization: Token 6b3f7dc70abe8aed3e56658b86fa508b472bf238'
     ``` 
     
   * View my wallet transactions
     ```bash
     curl --location 'http://127.0.0.1:5000/api/v1/wallet/transactions' \
     --header 'Authorization: Token b24add242529d5968c3ae7e811e3294319ce0d80a8'
     ``` 
   
   * Add virtual money to my wallet
     ```bash
     curl --location 'http://127.0.0.1:5000/api/v1/wallet/deposits' \
     --header 'Authorization: Token b24add242529d5968c3ae7e811e3294319ce0d80a8' \
     --form 'amount="10000"' \
     --form 'reference_id="50535246-dcb2-4929-8cc9-004ea06f5241"'
     ```
     
   * Use virtual money from my wallet
     ```bash
     curl --location 'http://127.0.0.1:5000/api/v1/wallet/withdrawals' \
     --header 'Authorization: Token b24add242529d5968c3ae7e811e3294319ce0d80a8' \
     --form 'reference_id="50535246-dcb2-4929-8cc9-004ea06f5244"' \
     --form 'amount="20"'
     ```
   
   * Disable Wallet
      ```bash
     curl --location --request PATCH 'http://127.0.0.1:5000/api/v1/wallet' \
     --header 'Authorization: Token b24add242529d5968c3ae7e811e3294319ce0d80a8' \
     --form 'is_disabled="true"'
     ```

   