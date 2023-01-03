import win32api
import subprocess
import sys

proxy_server_querys = 'reg query "HKCU\Software\Micro   soft\Windows\CurrentVersion\Internet Settings" /v ProxyServer'
proxy_status_querys = 'reg query "HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings" /v ProxyEnable'
deactivate_proxys = 'reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings" /v ProxyEnable /t REG_DWORD /d 0 /f'
activate_proxys = 'reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings" /v ProxyEnable /t REG_DWORD /d 1 /f'

win32api.ShellExecute(0, "open", "cmd.exe", "/c " + deactivate_proxys, "", 0)


def activate_proxy():
    win32api.ShellExecute(0, "open", "cmd.exe", "/c " + activate_proxys, "", 0)
    print("Proxy activated")

def deactivate_proxy():
    win32api.ShellExecute(0, "open", "cmd.exe", "/c " + deactivate_proxys, "", 0)
    print("Proxy deactivated")


def change_address(new_address):
    win32api.ShellExecute(
        0,
        "open",
        "cmd.exe",
        "/c "
        + f'reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings" /v ProxyServer /t REG_SZ /d {new_address} /f',
        "",
        0,
    )
    print(f"Changed Proxy Server to {new_address}")


# returns latest proxy server address
def fill_in():
    try:
        value = subprocess.check_output(proxy_server_querys).decode("utf-8").split()[-1]
        return value
    except:
        value = "0.0.0.0:0"
        return value


def status_check():
    # check current regkey value for proxy
    regkey_check = subprocess.Popen(
        proxy_status_querys, shell=True, stdout=subprocess.PIPE
    )
    regkey_check_return = regkey_check.stdout.read().split()

    if regkey_check_return[-1] == b"0x0":
        print("Proxy is currently inactive")
        return
    if regkey_check_return[-1] == b"0x1":
        print("Proxy is currently active")
        return
    else:
        print(f"{regkey_check_return[-1]}, {type(regkey_check_return[-1])}")


if sys.argv[1] == "-status" or sys.argv[1] == "-s":
    status_check()
elif sys.argv[1] == "-activate" or sys.argv[1] == "-a":
    activate_proxy()
elif sys.argv[1] == "-deactivate" or sys.argv[1] == "-d":
    deactivate_proxy()
elif sys.argv[1] == "-change" or sys.argv[1] == "-c":
        if len(sys.argv) == 3:
            change_address(sys.argv[2])
        else :
            print('Please enter a proxy address "-c newproxy:PORT"')
elif sys.argv[1] == "-show" or sys.argv[1] == "-show":
    print(fill_in())
elif sys.argv[1] == "-help" or sys.argv[1] == "-h":
    print("\n\n-status or -s: Check the current proxy status\n-activate or -a: Activate the proxy\n-deactivate or -d: Deactivate the proxy\n-change or -c: Change the proxy address (must specify the new address as an additional argument, e.g. setproxy -c newproxy:8080)\n-show: Show the current proxy address\nNote: If an invalid argument is provided, the program will display an error message.\n\n")
else:
    print("Wrong argument")
