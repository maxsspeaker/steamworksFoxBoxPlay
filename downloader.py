import subprocess
import tkinter as tk
import configparser
import re

## TODO
# manage login, move (& rename?) downloads


global textAppid
global textWIDs
global output
global button1
global running
global cfg
running = False


def download():
    # don't start multiple steamcmd instances
    global running
    if running:
        return
    running = True

    # assemble command line
    args = ['steamcmd/steamcmd.exe','+login anonymous']
    global textAppid
    appid = int(textAppid.get("1.0","end-1c"))
    # save appid to config
    global cfg
    cfg["general"]["appid"] = str(appid)
    global textWIDs
    for i in textWIDs.get("1.0",tk.END).splitlines():
        wid = re.search(r"id=([0-9]+)",i)
        if wid is None:
            wid = i
        else:
            wid = wid[1]
        args.append(f'+workshop_download_item {appid} {int(wid)}')
    args.append("+quit")

    # call steamcmd
    process = subprocess.Popen(args, stdout=subprocess.PIPE, errors='ignore', creationflags=subprocess.CREATE_NO_WINDOW)
    
    # show output
    global output
    while True:
        out = process.stdout.readline()
        #print(out.strip())
        output.insert(tk.END,out)
        output.update()
        return_code = process.poll()
        if return_code is not None:
            for out in process.stdout.readlines():
                #print(out.strip())
                output.insert(tk.END,out)
            break

    # reset state
    textWIDs.delete("1.0", tk.END)
    button1.state = "normal"
    running = False


# MAIN
cfg = configparser.ConfigParser()

# set defaults
cfg.read('downloader.ini')
if 'general' not in cfg:
	cfg['general'] = {'appid': '281990'}
elif 'appid' not in cfg['general']:
    cfg['general']['appid'] = str(281990)


# create UI            
root = tk.Tk()
    
canvas1 = tk.Canvas(root, width = 820, height = 300)
canvas1.pack()
    
textAppid = tk.Text(root, width = 30, height = 1)
canvas1.create_window(250,50,window=textAppid)

textAppid.insert(tk.END, cfg['general']['appid'])

labelAppid = tk.Label(root, text='App ID')
canvas1.create_window(50,50,window=labelAppid)

textWIDs = tk.Text(root, width = 30, height = 10)
canvas1.create_window(250,150,window=textWIDs)

labelWIDs = tk.Label(root, text='Workshop IDs')
canvas1.create_window(50,150,window=labelWIDs)

button1 = tk.Button(text='Download', command=download)
canvas1.create_window(200,270,window=button1)

output = tk.Text(root, width=50, height = 15)
canvas1.create_window(600,150,window=output)

root.mainloop()

# save config
with open('downloader.ini', 'w') as file:
    cfg.write(file)
