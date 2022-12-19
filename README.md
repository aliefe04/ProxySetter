# ProxySetter
This project aims to provide a simple and easy-to-use solution for setting a proxy.
## How to use
Clone this repository

Install the dependencies: pip install -r requirements.txt

Run the following command: py main.py -[args]

### Arguments
-status or -s: Check the current proxy status

-activate or -a: Activate the proxy

-deactivate or -d: Deactivate the proxy

-change or -c: Change the proxy address (must specify the new address as an additional argument, e.g. setproxy -c newproxy:8080)

-show: Show the current proxy address

Note: If an invalid argument is provided, the program will display an error message.

### TODO
- [ ] GUI
