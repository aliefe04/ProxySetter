import win32api
import subprocess
import tkinter
import customtkinter


proxy_server_querys = 'reg query "HKCU\Software\Micro   soft\Windows\CurrentVersion\Internet Settings" /v ProxyServer'
proxy_status_querys = 'reg query "HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings" /v ProxyEnable'
deactivate_proxys = 'reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings" /v ProxyEnable /t REG_DWORD /d 0 /f'
activate_proxys = 'reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings" /v ProxyEnable /t REG_DWORD /d 1 /f'


def check_active_proxy():
    regkey_check = subprocess.Popen(
        proxy_status_querys, shell=False, stdout=subprocess.PIPE
    )
    regkey_check_return = regkey_check.stdout.read().split()

    if regkey_check_return[-1] == b"0x0":
        return "Proxy is currently inactive"
    if regkey_check_return[-1] == b"0x1":
        return "Proxy is currently active"
    else:
        print(f"{regkey_check_return[-1]}, {type(regkey_check_return[-1])}")


def check_proxy_address():
    try:
        result = subprocess.run(
            'reg query "HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings" /v ProxyServer',
            shell=False,
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        stdout = result.stdout.decode()
        proxy_address = stdout.strip().split('    ')[-1]
        return proxy_address
    except subprocess.CalledProcessError:
        return None

def activate_proxy():
    win32api.ShellExecute(0, "open", "cmd.exe", "/c " + activate_proxys, "", 0)
    if activeproxy.winfo_exists() == 1:
        activeproxy.destroy()
    customtkinter.CTkLabel(master=app, text="Proxy activated").place(
        relx=0.05, rely=0.4, anchor=tkinter.NW
    )


def deactivate_proxy():
    win32api.ShellExecute(0, "open", "cmd.exe", "/c " + deactivate_proxys, "", 0)
    if activeproxy.winfo_exists() == 1:
        activeproxy.destroy()
    customtkinter.CTkLabel(master=app, text="Proxy deactivated").place(
        relx=0.05, rely=0.4, anchor=tkinter.NW
    )

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
    i = customtkinter.CTkLabel(master=app, text=f"Changed Proxy Server to {new_address}")
    
    if new_address == "":
        pass
    else:
        i.place(
         relx=0.05, rely=0.5, anchor=tkinter.NW)
        i.after(3000, i.destroy)


def button_click_event():
    dialog = customtkinter.CTkInputDialog(text=f"Type new proxy\n current proxy is:\n {check_proxy_address()} ", title="Change Proxy")
    response = dialog.get_input()
    if response == None:
        pass
    else:
        change_address(response)

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")
app = customtkinter.CTk()
app.geometry("300x400")
app.title("Proxy Manager")
customtkinter.CTkButton(app, text="Change Proxy", command=button_click_event).place(
    relx=0.05, rely=0.3, anchor=tkinter.NW
)
customtkinter.CTkButton(
    master=app, text="Activate proxy", command=activate_proxy
).place(relx=0.05, rely=0.10, anchor=tkinter.NW)
customtkinter.CTkButton(
    master=app, text="Deactivate proxy", command=deactivate_proxy
).place(relx=0.05, rely=0.2, anchor=tkinter.NW)
activeproxy = customtkinter.CTkLabel(master=app, text=check_active_proxy())
activeproxy.place(relx=0.05, rely=0.4, anchor=tkinter.NW)
app.mainloop()