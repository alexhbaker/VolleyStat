import tkinter
import Player

p1 = Player.Player("Alex", 27)
print(p1.name)
print(p1.number)
print(p1.attempts)
p1.killScored()
p1.hitInPlay()
p1.hitInPlay()
p1.hitInPlay()
p1.hitInPlay()
p1.hitInPlay()
print(p1.he)
hittingEfficiency = p1.he

def hitInPlayButton():
    p1.hitInPlay()
    initialFrameLabel.config(text = p1.he)

window = tkinter.Tk()
window.title("VolleyStat - Fun, Free statistics")

frame = tkinter.Frame(window)
frame.pack()

initialFrame = tkinter.LabelFrame(frame, text="User Info")
initialFrame.grid(row = 1, column = 0)

initialFrameLabel = tkinter.Label(initialFrame, text=hittingEfficiency)
initialFrameLabel.grid(row=0, column=0)
initialFrameButton = tkinter.Button(initialFrame, text="Hit in play", command=hitInPlayButton)
initialFrameButton.grid(row=0, column=1)

window.mainloop()

print(p1.he)



#tkinter.Button("hello")