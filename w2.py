from tkinter import *
import requests
root = Tk()


url='https://radar.weather.gov/ridge/standard/KHGX_loop.gif'
#url='blob:https://www.star.nesdis.noaa.gov/57b1463b-7559-4794-8ebb-d421d39a2343'

def download_gif(url, save_path):
    response = requests.get(url)
    if response.status_code == 200:
        with open(save_path, 'wb') as file:
            file.write(response.content)
        print("GIF downloaded successfully!")
    else:
        print("Failed to download GIF.")

def update(ind):
    frame = frames[ind]
    ind += 1
    #print(ind)
    #print(ind)
    if ind > 8:  # With this condition it will play gif infinitely
        ind = 0
    label.configure(image=frame)
    root.after(1000, update, ind)


download_gif(url , './KHGX_loop.gif')

frames = [
    PhotoImage(file="./KHGX_loop.gif", format="gif -index %i" % (i))
    for i in range(9)
]

label = Label(root)
label.pack()
root.after(0, update, 0)
root.mainloop()