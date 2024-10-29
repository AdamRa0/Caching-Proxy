# Caching-Proxy
CLI tool that acts as a proxy server that caches responses from forwarded requests.


## Requirements
- Python 3.12
- Poetry

## Instructions
To run this project locally
- Clone the project
- cd into clone project and run the following commands
```bash
    # Unix systems
    EXPORT ORIGIN < url to forward traffic to >

    # Windows systems
    SET ORIGIN < url to forward traffic to >

    poetry shell
    poetry install
    pip install -e .

    pproxy run
```

Visit browser and being using the proxy. For instance, if ORIGIN set to https://reddit.com, visiting localhost:5000/r/asm will take you to the asm subreddit