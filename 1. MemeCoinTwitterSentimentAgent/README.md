# Memecoin Twitter Sentiment Agent

Welcome to the **Memecoin Twitter Sentiment Agent** tutorial! This guide will walk you through building a simple agent using Theoriq's SDK. The goal is to help you understand the foundational components and functionality of the Theoriq SDK by creating a real-world use case.

## Objectives

By following this tutorial, you will:

- Learn how to set up and configure Theoriq's SDK.
- Understand the main building blocks of the SDK.
- Build an agent that fetches latest tweets related to memecoins and analyzes their sentiment.



## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Running and testing the agent](#running-the-agent)


## Prerequisites

Before starting, ensure you have the following:

- Basic familiarity with Python
- A Twitter Developer account with API access
- OpenAI API Key
- Python 3.10 or later installed.


## Running and testing the agent

1. Create a `.env` file according to the `.env.example` file.
2. Create a local python environment using `conda` or `venv`.
3. Install all the required packages

``` shell
pip install -r requirements.txt
```

4. Run the agent by

``` shell
python src/app.py
```

5. Use [http/test.http](http/test.http) to send http requests to `http://localhost:5050/api/v1alpha1/execute`