# States contains in memory

from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory storage for wallet data
wallet_data = {
    "id": "6ef31ed3-f396-4b6c-8049-674ddede1b16",
    "owned_by": "526ea8b2-428e-403b-b9fd-f10972e0d6fe",
    "status": "enabled",
    "balance": 0
}

deposits = []
withdrawals = []

@app.route('/api/v1/wallet/deposits', methods=['POST'])
def add_deposit():
    if 'Authorization' not in request.headers or not request.headers['Authorization'].startswith('Token'):
        return jsonify({"status": "error", "message": "Unauthorized"}), 401

    amount = int(request.form.get('amount'))
    reference_id = request.form.get('reference_id')

    # Perform deposit logic here
    # You should generate a unique deposit ID and update wallet balance
    deposit = {
        "id": "<unique_deposit_id>",
        "deposited_by": wallet_data['owned_by'],
        "status": "success",
        "deposited_at": "1994-11-05T08:15:30-05:00",
        "amount": amount,
        "reference_id": reference_id
    }

    deposits.append(deposit)
    wallet_data['balance'] += amount

    return jsonify({"status": "success", "data": {"deposit": deposit}}), 201

@app.route('/api/v1/wallet/withdrawals', methods=['POST'])
def withdraw():
    if 'Authorization' not in request.headers or not request.headers['Authorization'].startswith('Token'):
        return jsonify({"status": "error", "message": "Unauthorized"}), 401

    amount = int(request.form.get('amount'))
    reference_id = request.form.get('reference_id')

    # Perform withdrawal logic here
    # You should check if the withdrawal amount is valid and update wallet balance
    if amount > wallet_data['balance']:
        return jsonify({"status": "error", "message": "Insufficient balance"}), 400

    withdrawal = {
        "id": "<unique_withdrawal_id>",
        "withdrawn_by": wallet_data['owned_by'],
        "status": "success",
        "withdrawn_at": "1994-11-05T08:15:30-05:00",
        "amount": amount,
        "reference_id": reference_id
    }

    withdrawals.append(withdrawal)
    wallet_data['balance'] -= amount

    return jsonify({"status": "success", "data": {"withdrawal": withdrawal}}), 201

@app.route('/api/v1/wallet', methods=['PATCH'])
def disable_wallet():
    if 'Authorization' not in request.headers or not request.headers['Authorization'].startswith('Token'):
        return jsonify({"status": "error", "message": "Unauthorized"}), 401

    is_disabled = request.form.get('is_disabled')

    # Perform wallet disable logic here
    wallet_data['status'] = "disabled"
    wallet_data['disabled_at'] = "1994-11-05T08:15:30-05:00"

    return jsonify({"status": "success", "data": {"wallet": wallet_data}}), 200

if __name__ == '__main__':
    app.run(debug=True)
