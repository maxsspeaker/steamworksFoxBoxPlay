import subprocess
import tkinter
import configparser
import re

## TODO
# add mods file system?...


global textAppid
global textWIDs
global output
global button1
global running
global cfg
import os
running = False

EditTheme=False

Theme="Black"
if(Theme=="Black"):
            bgapp="#333"
            bgappbattan="#555"
            textappColr="#eee"
elif(Theme=="White"):
            bgapp="#e8e8e8"
            bgappbattan="#e8e8e8" 
            textappColr="#000000"

def GetIdItem(IdStings):
    for i in IdStings.splitlines():
        wid = re.search(r"id=([0-9]+)",i)
        if wid is None:
            wid = i
        else:
            wid = wid[1]
    return wid


def download(appid,wid): 
    global SteamPach
    # don't start multiple steamcmd instances
    global running
    global textWIDs
    global outputCmdBox
    global cfg
    if running:
        return
    running = True

    contentFolder=cfg['general']['SteamPach']+"steamapps/workshop/content/"
    # assemble command line
    args = [cfg['general']['SteamPach']+"steamcmd.exe",'+login anonymous']
    global textAppid
    #appid = int(textAppid.get("1.0","end-1c"))
    cfg["general"]["appid"] = str(appid)


    args.append(f'+workshop_download_item {appid} {int(wid)}')
    args.append("+quit")
    if(os.path.exists('mods/'+wid)):
        outputCmdBox.insert(tkinter.END,"Moving the file to the Steam folder.\n")
        os.replace(('mods/'+wid),contentFolder+str(appid)+r"/"+wid)
    # save appid to config

    #wid=GetIdItem(wid):

    # call steamcmd
    process = subprocess.Popen(args, stdout=subprocess.PIPE, errors='ignore', creationflags=subprocess.CREATE_NO_WINDOW)
    
    # show output
    while True:
        out = process.stdout.readline()
        #print(out.strip())
        outputCmdBox.insert(tkinter.END,out)
        outputCmdBox.update()
        return_code = process.poll()
        if return_code is not None:
            for out in process.stdout.readlines():
                #print(out.strip())
                outputCmdBox.insert(tkinter.END,out)
            break

    # reset state
    if(os.path.exists(contentFolder+str(appid)+r"/"+wid)):
        outputCmdBox.insert(tkinter.END,"Moving the file to the mods folder\n")
        os.replace(contentFolder+str(appid)+r"/"+wid,('mods/'+wid))
        
    #textWIDs.delete("1.0", tkinter.END)
    #button1.state = "normal"
    
    running = False


# MAIN

    
##canvas1 = tkinter.Canvas(root, width = 820, height = 300)
##canvas1.pack()
##canvas1["bg"] = bgapp
##    
##textAppid = tkinter.Text(root, width = 30, height = 1,fg=textappColr, bg=bgapp)
##canvas1.create_window(250,50,window=textAppid)
##
##textAppid.insert(tkinter.END, cfg['general']['appid'])
##
##labelAppid = tkinter.Label(root, text='App ID', fg=textappColr, bg=bgapp)
##canvas1.create_window(50,50,window=labelAppid)
##
##textWIDs = tkinter.Text(root, width = 30, height = 10,fg=textappColr, bg=bgapp)
##canvas1.create_window(250,150,window=textWIDs)
##
##labelWIDs = tkinter.Label(root, text='Workshop IDs', fg=textappColr, bg=bgapp)
##canvas1.create_window(50,150,window=labelWIDs)
##
##button1 = tkinter.Button(text='Download', command=download,fg=textappColr, bg=bgappbattan)
##canvas1.create_window(200,270,window=button1)
##
##output = tkinter.Text(root, width=50, height = 15,fg=textappColr, bg=bgapp)
##canvas1.create_window(600,150,window=output)


def ThemeEdit(Theme): 
        global bgapp
        global bgappbattan
        global textappColr
        global EditTheme
        global rott
        EditTheme=True

        if(Theme=="Black"):
            bgapp="#333"
            bgappbattan="#555"
            textappColr="#eee"
        elif(Theme=="White"):
            bgapp="#e8e8e8"
            bgappbattan="#e8e8e8" 
            textappColr="#000000"
        root.destroy()
        Main()

def OpenSaveFile():
    pass
def exitinSDK():
    pass
def AddKey():
    pass
def SelectBox():
    pass
def Edit_menu():
    pass

def exitinSDK():
        global root
        root.destroy()

def Main():
    global root
    global cfg
    global SteamPach
    global outputCmdBox
    
    cfg = configparser.ConfigParser()
    # set defaults
    cfg.read('downloader.ini')
    if 'general' not in cfg:
        cfg['general'] = {'appid': '281990'}
    elif 'appid' not in cfg['general']:
        cfg['general']['appid'] = str(281990)

    if 'SteamPach' not in cfg['general']:
        pass

    # create UI
    root = tkinter.Tk()
    root["bg"] = bgapp
    
    main_menu = tkinter.Menu()
    Theme_menu = tkinter.Menu(tearoff=0)
    Theme_menu.add_command(label="Black",command=lambda:ThemeEdit("Black"))
    Theme_menu.add_command(label="White",command=lambda:ThemeEdit("White"))
    
    View_menu = tkinter.Menu(tearoff=0)
    View_menu.add_cascade(label="Theme", menu=Theme_menu)

    main_menu.add_cascade(label="View", menu=View_menu)

    #root.config(menu=main_menu)

    scrollbar = tkinter.Scrollbar(troughcolor=textappColr, bg=bgapp) 
    scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)

    outputCmdBox = tkinter.Text(yscrollcommand=scrollbar.set, width=5,fg=textappColr, bg=bgapp) #

    outputCmdBox.pack(padx=0, pady=0, expand=1, fill=tkinter.BOTH) 
    scrollbar.config(command=outputCmdBox.yview)

    btn1 = tkinter.Button(text="Download", background="#555", foreground="#ccc",
              padx="2", pady="7",command=lambda:download(IdAppSteamS.get(),GetIdItem(IdItemBoxS.get())))
    btn1.pack(side=tkinter.LEFT)

    IdItemBoxS = tkinter.StringVar()
    IdItemBox = tkinter.Entry(textvariable=IdItemBoxS)
    
    IdItemBox.pack(side=tkinter.BOTTOM, fill=tkinter.X)

    IdItemBox.insert(tkinter.END,"ItemID")

    IdAppSteamS = tkinter.StringVar()
    IdAppSteam = tkinter.Entry(textvariable=IdAppSteamS)
    
    IdAppSteam.pack(side=tkinter.BOTTOM, fill=tkinter.X)

    IdAppSteam.insert(tkinter.END,cfg['general']['appid']) 


    try:root.iconbitmap('app.ico')
    except:
        try:root.iconbitmap(os.path.basename(sys.argv[0]))
        except:pass

    root.title("WorkshopFoxBoxPlay")
    root.geometry("500x500")

    EditTheme=False

    root.mainloop()

    # save config
    with open('downloader.ini', 'w') as file:
        cfg.write(file)

Main()

