import ttkbootstrap as ttk
import Player

# We want to pass in the player name and this will give back a frame object with that name

# -1 to 1 in 1 to 100

def frameObject(name: str, number: int, frame, rowNum: int) -> ttk.LabelFrame:
    
    def hitInPlayButton():
        player.hitInPlay()
        hitEfficiency = f"{((player.he*50)+50):.4f}"
        initialFrameLabel.config(text= "Efficiency: " + str(hitEfficiency))
        progressFrame['value'] = hitEfficiency
        meterFrame.amountusedvar.set(player.kp)

    def killButton():
        player.killScored()
        hitEfficiency = f"{((player.he*50)+50):.4f}"
        initialFrameLabel.config(text= "Efficiency: " + str(hitEfficiency))
        progressFrame['value'] = hitEfficiency
        meterFrame.amountusedvar.set(player.kp)

    def errorButton():
        player.errorRecorded()
        if player.he < 0:
            meterFrame['bootstyle'] = 'Danger'
        hitEfficiency = f"{((player.he*50)+50):.4f}"
        initialFrameLabel.config(text= "Efficiency: " + str(hitEfficiency))
        progressFrame['value'] = hitEfficiency
        meterFrame.amountusedvar.set(player.kp)

    player = Player.Player(name, number)
    userText = name + " #" + str(number) 
    initialFrame = ttk.LabelFrame(frame, text=userText)
    initialFrame.columnconfigure((0,1), weight=1)
    initialFrame.grid(row = rowNum, column = 0)

    initialFrameLabel = ttk.Label(initialFrame, text="Efficiency: " + str(player.he))
    initialFrameLabel.grid(row=0, column=0, padx=5, pady=2)
    initialFrameButton = ttk.Button(initialFrame, text="Hit in play", command=hitInPlayButton, bootstyle="outline-info")
    initialFrameButton.grid(row=0, column=1, padx=5, pady=2)
    initialFrameButton1 = ttk.Button(initialFrame, text="Kill", command=killButton, bootstyle="outline-success")
    initialFrameButton1.grid(row=0, column=2, padx=5, pady=2)
    initialFrameButton2 = ttk.Button(initialFrame, text="Error", command=errorButton, bootstyle="outline-danger")
    initialFrameButton2.grid(row=0, column=3, padx=5, pady=2)

    progressFrame = ttk.Progressbar(initialFrame, value=50, orient='vertical', style='Warning', )
    progressFrame.grid(row=0, column=4, padx=5, pady=2)

    meterFrame = ttk.Meter(initialFrame, amountused=player.kp, arcrange=180, interactive=False, amounttotal=100, subtext="Kill Percentage", textright="%")
    meterFrame.grid(row=0, column=5, padx=5, pady=2)
    pass