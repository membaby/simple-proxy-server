# Simple Proxy Server
### Processes HTTP requests on the server-side and returns the HTML content of the requested URL

## How to Install:
### Pre-Requirements:
- [Python 3.x](https://python.org/download)
- Flask library (`pip install flask`)

### Configurations
- `ALLOWED_IPS`: List of IP addresses allowed to use the service. When set, only these IPs are allowed to make requests, other IPs requests are aborted.

- `BLOCKED_IPS`: List of IP addresses not allowed to use the service. When set, all IPs are allowed except the ones in the list.

- `PORT`: port number that listens to requests for the app.

### Running
- Run the file `app.py` with command: `python app.py`