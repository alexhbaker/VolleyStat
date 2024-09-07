import tkinter
import Player
import FrameObject
# from ttk import ttk
import ttkbootstrap as ttk

# TODO
# Add a button to add a player / DONE
# Figure out how to show multiple players at the same time / DONE
# Find a way on how to input a player's name and number into the add player button / DONE
# Make it looker prettier using ttkbootstrap? :]

row = 2

def newPlayerButton():
    global row
    FrameObject.frameObject(output.get("1.0","end-1c"), numberOutput.get("1.0","end-1c"), frame, row)
    row+=1

window = ttk.Window(themename="darkly")
window.title("VolleyStat - Fun, Free statistics")

frame = ttk.Frame(window)
frame.pack()

initialFrame = ttk.LabelFrame(frame, text="User Info")
initialFrame.grid(row = 1, column = 0)

initialFrameButton = ttk.Button(initialFrame, text="New Player", command = newPlayerButton)
initialFrameButton.grid(row=0, column=1)
nameText = ttk.Label(initialFrame, text="Name: ")
nameText.grid(row=0, column=2)
output = ttk.Text(initialFrame, height = 1, width = 10, bg = "light cyan")
output.grid(row=0, column=3)
numberText = ttk.Label(initialFrame, text="Number: ")
numberText.grid(row=0, column=4)
numberOutput = ttk.Text(initialFrame, height=1, width=2, bg="light cyan")
numberOutput.grid(row=0,column=5)

window.mainloop()