import tkinter

window = tkinter.Tk()
window.title("VolleyStat - Fun, Free statistics")

frame = tkinter.Frame(window)
frame.pack()

initialFrame = tkinter.LabelFrame(frame, text="User Info")
initialFrame.grid(row = 0, column = 0)

initialFrameLabel = tkinter.Label(initialFrame, text="testing")
initialFrameLabel.grid(row=0, column=0)

window.mainloop()

#tkinter.Button("hello")