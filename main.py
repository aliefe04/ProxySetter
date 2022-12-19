import win32api
import subprocess
import sys
proxy_server_query = 'reg query "HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings" /v ProxyServer'
proxy_status_query = 'reg query "HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings" /v ProxyEnable'
deactivate_proxy = 'reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings" /v ProxyEnable /t REG_DWORD /d 0 /f'
activate_proxy = 'reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings" /v ProxyEnable /t REG_DWORD /d 1 /f'

win32api.ShellExecute(0, 'open', 'cmd.exe', '/c ' + deactivate_proxy,'',0)

def activate_proxy():
    win32api.ShellExecute(0, 'open', 'cmd.exe', '/c ' + activate_proxy,'',0)
    print('Proxy activated')


def deactivate_proxy():
    win32api.ShellExecute(0, 'open', 'cmd.exe', '/c ' + deactivate_proxy,'',0)
    print('Proxy deactivated')
    
# def change_address(new_address):
#     shell.ShellExecuteEx(lpFile='cmd.exe',
#                          lpParameters='/c ' + f'reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings" /v ProxyServer /t REG_SZ /d {new_address} /f')
#     print(f"Changed Proxy Server to {new_address}")

def change_address(new_address):
    win32api.ShellExecute(0, 'open', 'cmd.exe', '/c ' + f'reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings" /v ProxyServer /t REG_SZ /d {new_address} /f','',0)
    print(f"Changed Proxy Server to {new_address}")

# returns latest proxy server address
def fill_in():
    try:
        value = subprocess.check_output(
            proxy_server_query).decode("utf-8").split()[-1]
        return value
    except:
        value = "0.0.0.0:0"
        return value

def status_check():
    # check current regkey value for proxy
    regkey_check = subprocess.Popen(
        proxy_status_query, shell=True, stdout=subprocess.PIPE)
    regkey_check_return = regkey_check.stdout.read().split()

    if regkey_check_return[-1] == b'0x0':
        print('Proxy is currently inactive')
        return
    if regkey_check_return[-1] == b'0x1':
        print('Proxy is currently active')
        return
    else:
        print(
            f"{regkey_check_return[-1]}, {type(regkey_check_return[-1])}")
        
if sys.argv[1] == '-status' or sys.argv[1] == '-s':
    status_check()
elif sys.argv[1] == '-activate' or sys.argv[1] == '-a':
    activate_proxy()
elif sys.argv[1] == '-deactivate' or sys.argv[1] == '-d':
    deactivate_proxy()
elif sys.argv[1] == '-change' or sys.argv[1] == '-c':
    if IndexError:
        print('Please enter a proxy address "-c newproxy:8080"')
    else :
        change_address(sys.argv[2])
elif sys.argv[1] == '-show' or sys.argv[1] == '-show':
    print(fill_in())
else:
    print('Wrong argument')
