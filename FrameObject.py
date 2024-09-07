import tkinter
import Player

# We want to pass in the player name and this will give back a frame object with that name
def frameObject(name: str, number: int, frame, rowNum: int) -> tkinter.LabelFrame:
    
    def hitInPlayButton():
        player.hitInPlay()
        initialFrameLabel.config(text = "Efficiency: " + str(player.he))

    def killButton():
        player.killScored()
        initialFrameLabel.config(text = "Efficiency: " + str(player.he))

    def errorButton():
        player.errorRecorded()
        initialFrameLabel.config(text= "Efficiency: " + str((player.he)))

    player = Player.Player(name, number)
    userText = name + " #" + str(number) 
    initialFrame = tkinter.LabelFrame(frame, text=userText)
    initialFrame.grid(row = rowNum, column = 0)
    hitEfficiency = 0.0

    initialFrameLabel = tkinter.Label(initialFrame, text="Efficiency: " + str(hitEfficiency))
    initialFrameLabel.grid(row=0, column=0)
    initialFrameButton = tkinter.Button(initialFrame, text="Hit in play", command=hitInPlayButton)
    initialFrameButton.grid(row=0, column=1)
    initialFrameButton1 = tkinter.Button(initialFrame, text="Kill", command=killButton)
    initialFrameButton1.grid(row=0, column=2)
    initialFrameButton2 = tkinter.Button(initialFrame, text="Error", command=errorButton)
    initialFrameButton2.grid(row=0, column=3)
    pass