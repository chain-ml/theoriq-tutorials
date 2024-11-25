"""Script to create new keypair to sign biscuits"""
from biscuit_auth import KeyPair
from theoriq.biscuit import AgentAddress

if __name__ == "__main__":
    agent_kp = KeyPair()

    print("AGENT_PRIVATE_KEY =", agent_kp.private_key.to_hex())
    print("AGENT_PUBLIC_KEY =", agent_kp.public_key.to_hex())
    print("AGENT_ADDRESS =", AgentAddress.from_public_key(agent_kp.public_key))
