import os, re, subprocess
#import ctypes
from tkinter import *
from tkinter import simpledialog

window = Tk()
window.geometry("600x800+400+50")
window.title("Giochi Steam - GamesLauncher")
window.resizable(False, False)
#window.iconbitmap(default="Games.ico")
#myappid = 'Chry55Player.GamesLauncher.py.1.0' # arbitrary string
#ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

def mousewheelevent(event):
    cTableContainer.yview_scroll(int(-2*(event.delta/120)), "units")

# Tkinter widgets needed for scrolling.  The only native scrollable container that Tkinter provides is a canvas.
# A Frame is needed inside the Canvas so that widgets can be added to the Frame and the Canvas makes it scrollable.
cTableContainer = Canvas(window)
fTable = Frame(cTableContainer)
fTable.config(background="black")
sbVerticalScrollBar = Scrollbar(window)

# Updates the scrollable region of the Canvas to encompass all the widgets in the Frame
def updateScrollRegion():
	cTableContainer.update_idletasks()
	cTableContainer.config(scrollregion=fTable.bbox())

# Sets up the Canvas, Frame, and scrollbars for scrolling
def createScrollableContainer():
    cTableContainer.config(yscrollcommand=sbVerticalScrollBar.set, highlightthickness=0, background="black")
    sbVerticalScrollBar.config(orient=VERTICAL, command=cTableContainer.yview)
    sbVerticalScrollBar.pack(fill=Y, side=RIGHT, expand=FALSE)
    cTableContainer.pack(fill=BOTH, side=LEFT, expand=TRUE)
    cTableContainer.create_window(0, 0, window=fTable, anchor=NW)
    cTableContainer.bind_all("<MouseWheel>", mousewheelevent)

def steam():
    with open('src/steam.txt', encoding="utf-8") as f:
        SteamGames=f.readlines()
        for i in range(len(SteamGames)):
            SteamGames[i]=SteamGames[i].replace("\n", "")
    with open('src/steam_bin.txt', encoding="utf-8") as f:
        SteamBin=f.readlines()
        for i in range(len(SteamBin)):
            SteamBin[i]=SteamBin[i].replace("\n", "")
    window.title("Giochi Steam - GamesLauncher")
    cTableContainer.yview_moveto(0)
    l=2
    for i in range(0, len(SteamGames)):
        v = "l" + str(l)
        try:
            globals()[v].grid_forget()
        except:
            pass
        la = lambda launch=SteamBin[i]: os.system(launch)
        globals()[v] = Button(fTable, text=SteamGames[i], font=("Arial", 12), background="black", fg="white", command=la, bd=0)
        globals()[v].grid(row=l, sticky=W)
        l+=1
    try:
        for i in range(l, 100):
            v = "l" + str(l)
            globals()[v]['text']=""
            globals()[v].grid_forget()
            l+=1
    except:
        pass
    updateScrollRegion()

def others():
    with open('src/o.txt') as f:
        OtherGames=f.readlines()
    with open('src/o_bin.txt') as f:
        OBin=f.readlines()
    window.title("Giochi Vari - GamesLauncher")
    cTableContainer.yview_moveto(0)
    l=2
    for i in range(0, len(OtherGames)):
        v = "l" + str(l)
        try:
            globals()[v].grid_forget()
        except:
            pass
        globals()[v] = Button(fTable, text=OtherGames[i], font=("Arial", 12), background="black", fg="white", command=os.system(OBin[i]), bd=0)
        globals()[v].grid(row=l, sticky=W)
        l+=1
    try:
        for i in range(l, 100):
            v = "l" + str(l)
            globals()[v]['text']=""
            globals()[v].grid_forget()
            l+=1
    except:
        pass
    updateScrollRegion()

def gc():
    with open('src/gc.txt') as f:
        GCGames=f.readlines()
    with open('src/gc_bin.txt') as f:
        GCBin=f.readlines()
    window.title("Giochi GameCube - GamesLauncher")
    cTableContainer.yview_moveto(0)
    l=2
    for i in range(0, len(GCGames)):
        v = "l" + str(l)
        try:
            globals()[v].grid_forget()
        except:
            pass
        globals()[v] = Button(fTable, text=GCGames[i], font=("Arial", 12), background="black", fg="white", command=os.system(GCBin[i]), bd=0)
        globals()[v].grid(row=l, sticky=W)
        l+=1
    try:
        for i in range(l, 100):
            v = "l" + str(l)
            globals()[v]['text']=""
            globals()[v].grid_forget()
            l+=1
    except:
        pass
    updateScrollRegion()

def wiiu():
    with open('src/u.txt') as f:
        UGames=f.readlines()
    with open('src/u_bin.txt') as f:
        UBin=f.readlines()
    window.title("Giochi Wii U - GamesLauncher")
    cTableContainer.yview_moveto(0)
    l=2
    for i in range(0, len(UGames)):
        v = "l" + str(l)
        try:
            globals()[v].grid_forget()
        except:
            pass
        globals()[v] = Button(fTable, text=UGames[i], font=("Arial", 12), background="black", fg="white", command=os.system(UBin[i]), bd=0)
        globals()[v].grid(row=l, sticky=W)
        l+=1
    try:
        for i in range(l, 100):
            v = "l" + str(l)
            globals()[v]['text']=""
            globals()[v].grid_forget()
            l+=1
    except:
        pass
    updateScrollRegion()

def switch():
    with open('src/switch.txt') as f:
        SwitchGames=f.readlines()
    with open('src/switch_bin.txt') as f:
        SwitchBin=f.readlines()
    window.title("Giochi Switch - GamesLauncher")
    cTableContainer.yview_moveto(0)
    l=2
    for i in range(0, len(SwitchGames)):
        v = "l" + str(l)
        try:
            globals()[v].grid_forget()
        except:
            pass
        globals()[v] = Button(fTable, text=SwitchGames[i], font=("Arial", 12), background="black", fg="white", command=os.system(SwitchBin[i]), bd=0)
        globals()[v].grid(row=l, sticky=W)
        l+=1
    try:
        for i in range(l, 100):
            v = "l" + str(l)
            globals()[v]['text']=""
            globals()[v].grid_forget()
            l+=1
    except:
        pass
    updateScrollRegion()

def wii():
    with open('src/wii.txt') as f:
        WiiGames=f.readlines()
    with open('src/wii_bin.txt') as f:
        WiiBin=f.readlines()
    window.title("Giochi Wii - GamesLauncher")
    cTableContainer.yview_moveto(0)
    l=2
    for i in range(0, len(WiiGames)):
        v = "l" + str(l)
        try:
            globals()[v].grid_forget()
        except:
            pass
        globals()[v] = Button(fTable, text=WiiGames[i], font=("Arial", 12), background="black", fg="white", command=os.system(WiiBin[i]), bd=0)
        globals()[v].grid(row=l, sticky=W)
        l+=1
    try:
        for i in range(l, 100):
            v = "l" + str(l)
            globals()[v]['text']=""
            globals()[v].grid_forget()
            l+=1
    except:
        pass
    updateScrollRegion()

l1 = Label(fTable, text="                                          ", font=("Arial", 46), background="black", fg="white").grid(row=1, sticky=W)

i1 = PhotoImage(file="src/steam-logo-white.png", width="50", height="50")
img1 = Button(window, image=i1, background="black", command=steam).place(x=0, y=0)

i2 = PhotoImage(file="src/joystick.png", width="50", height="50")
img2 = Button(window, image=i2, background="black", command=others).place(x=55, y=0)

i3 = PhotoImage(file="src/gamecube.png", width="50", height="50")
img3 = Button(window, image=i3, background="black", command=gc).place(x=110, y=0)

i4 = PhotoImage(file="src/wii.png", width="50", height="50")
img4 = Button(window, image=i4, background="black", command=wii).place(x=165, y=0)

i5 = PhotoImage(file="src/wiiu.png", width="50", height="50")
img5 = Button(window, image=i5, background="black", command=wiiu).place(x=220, y=0)

i6 = PhotoImage(file="src/switch.png", width="50", height="50")
img6 = Button(window, image=i6, background="black", command=switch).place(x=275, y=0)

def add():
    title = simpledialog.askstring(title="Add", prompt="Enter game name:", parent=window)
    bin = simpledialog.askstring(title="Add", prompt="Enter game executable:", parent=window)
    type = simpledialog.askstring(title="Add", prompt="Enter game category:", parent=window)
    try:
        with open("src/"+type+'.txt', mode="r+") as f:
            list=f.readlines()
            list.append(title)
            for i in range(len(list)):
                list[i]=list[i].replace("\n", "")
            f.write(list[-1]+"\n")
        with open("src/"+type+'_bin.txt', mode="r+") as f:
            list=f.readlines()
            list.append(bin)
            for i in range(len(list)):
                list[i]=list[i].replace("\n", "")
            f.write(list[-1]+"\n")

    except:
        pass
img7 = Button(window, text="+", background="black", fg="white", font=("Arial", 25), command=add, bd=0).place(x=535, y=0)

def Search():
    var2=2
    for i in range(2, 100):
        v = "l" + str(i)
        try:
            pattern = re.compile(t.get().casefold())
            match = re.search(pattern, globals()[v]['text'].casefold())
            if match:
                globals()[v].grid(row=var2, sticky=W)
                var2 += 1
            else:
                globals()[v].grid_forget()
        except:
            pass
    updateScrollRegion()

t = Entry(window, background="black", fg="white", width=30, font=("Arial", 12))
t.place(x=0, y=55)
t1 = Button(window, text="Cerca", font=("Arial", 12), background="black", fg="white", command=Search)
t1.place(x=274, y=55)
steam()
updateScrollRegion()

createScrollableContainer()

def func(event):
    Search()
cTableContainer.bind_all('<Return>', func)

if __name__ == "__main__":
	window.mainloop()
