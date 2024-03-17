import hashlib
import hmac
import base64
from blockchain import Blockchain

def create_hmac(message, secret_key):
    """
    Create an HMAC (Hash-based Message Authentication Code) for the given message and secret key.
    """
    hmac_digest = hmac.new(secret_key.encode(), message.encode(), hashlib.sha256).digest()
    return base64.b64encode(hmac_digest).decode()

def create_crypto_protocol(protocol_name, secret_key):
    """
    Create a cryptographic protocol function for the given protocol name and secret key.
    """
    if protocol_name == "QM_Protocols":
        def qm_protocol(message):
            """
            Encrypt the given message using the QM_Protocols cryptographic protocol.
            """
            return create_hmac(message, secret_key)
        return qm_protocol
    else:
        raise ValueError(f"Unsupported protocol: {protocol_name}")

def blockchain_integrate(protocol_name, secret_key, message):
    """
    Integrate the given message with the specified cryptographic protocol and secret key into a blockchain.
    """
    # Create the cryptographic protocol function
    crypto_protocol = create_crypto_protocol(protocol_name, secret_key)

    # Encrypt the message using the cryptographic protocol
    encrypted_message = crypto_protocol(message)

    # Create a new blockchain
    blockchain = Blockchain()

    # Add the encrypted message to the blockchain as a new block
    blockchain.add_block(encrypted_message)

    # Return the blockchain
    return blockchain

# Example usage
secret_key = "my_secret_key"
message = "Hello, world!"
blockchain = blockchain_integrate("QM_Protocols", secret_key, message)
print(f"Blockchain: {blockchain}")
