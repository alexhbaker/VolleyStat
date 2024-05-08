import tkinter
import Player

p1 = Player.Player("Alex", 27)
hittingEfficiency = p1.he

def hitInPlayButton():
    p1.hitInPlay()
    initialFrameLabel.config(text = "Efficiency: " + str(p1.he))

def killButton():
    p1.killScored()
    initialFrameLabel.config(text = "Efficiency: " + str(p1.he))

def errorButton():
    p1.errorRecorded()
    initialFrameLabel.config(text= "Efficiency: " + str((p1.he)))

window = tkinter.Tk()
window.title("VolleyStat - Fun, Free statistics")

frame = tkinter.Frame(window)
frame.pack()

initialFrame = tkinter.LabelFrame(frame, text="User Info")
initialFrame.grid(row = 1, column = 0)

initialFrameLabel = tkinter.Label(initialFrame, text="Efficiency: " + str(hittingEfficiency))
initialFrameLabel.grid(row=0, column=0)
initialFrameButton = tkinter.Button(initialFrame, text="Hit in play", command=hitInPlayButton)
initialFrameButton.grid(row=0, column=1)
initialFrameButton1 = tkinter.Button(initialFrame, text="Kill", command=killButton)
initialFrameButton1.grid(row=0, column=2)
initialFrameButton2 = tkinter.Button(initialFrame, text="Error", command=errorButton)
initialFrameButton2.grid(row=0, column=3)

window.mainloop()

print(p1.he)



#tkinter.Button("hello")