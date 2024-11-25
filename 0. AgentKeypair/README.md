# Keypair generator for signing the biscuits

To register an agent on the Theoriq ecosystem, developers need to generate an ed25519 private key for their agent.
To generate **PRIVATE_KEY**, **PUBLIC_KEY**, and **ADDRESS** for an agent, follow the following steps:

1. Create a local python environment (python version 3.10 or higher)
2. Install the Theoriq SDK from the [requirements.txt](requirements.txt)
``` shell
pip install -r requirements.txt
```
3. Run [setup_config.py](setup_config.py) script
``` shell
python setup_config.py
```

Store these values for the agent, as they will be required for registration of the agent on the Theoriq protocol, signing the biscuits, and agent-to-agent communications.