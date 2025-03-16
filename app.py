from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import logging

# ✅ Initialize Flask app
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

# ✅ Setup logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

@app.route("/")
def home():
    return "Hello, Kool Kids Die Young Flask API is running!"

@app.route("/mint-nft", methods=["POST"])
def mint_nft():
    try:
        if not request.is_json:
            app.logger.warning("Mint request failed - Request body is not JSON")
            return jsonify({"error": "Request body must be JSON"}), 400

        data = request.get_json()
        claim_code = data.get("claim_code")
        wallet_address = data.get("wallet_address")

        # ✅ Log request details
        app.logger.info(f"Received mint request - Claim Code: {claim_code}, Wallet: {wallet_address}")

        # ✅ Validate request data
        if not claim_code or not wallet_address:
            app.logger.warning("Mint request failed - Missing claim_code or wallet_address")
            return jsonify({"error": "Missing claim_code or wallet_address"}), 400

        # ✅ Simulate NFT minting process (Replace this with real minting logic)
        minted_nft = {
            "message": "NFT minted successfully!",
            "claim_code": claim_code,
            "wallet_address": wallet_address
        }

        app.logger.info(f"NFT Minted Successfully: {minted_nft}")
        return jsonify(minted_nft)

    except Exception as e:
        app.logger.error(f"Error processing mint request: {str(e)}")
        return jsonify({"error": "Internal Server Error"}), 500

# ✅ Debugging: Print all registered routes
def print_routes():
    with app.app_context():
        print("Registered Routes:", app.url_map)

# ✅ Ensure Railway uses the correct port
if __name__ == "__main__":
    print_routes()  # ✅ Now correctly prints routes before app starts
    port = int(os.environ.get("PORT", 5000))  # Use 5000 as fallback if PORT is missing
    app.run(host="0.0.0.0", port=port)

