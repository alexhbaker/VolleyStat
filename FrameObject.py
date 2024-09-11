import ttkbootstrap as ttk
import Player

# We want to pass in the player name and this will give back a frame object with that name

# -1 to 1 in 1 to 100

def frameObject(name: str, number: int, frame, rowNum: int) -> ttk.LabelFrame:
    
    def hitInPlayButton():
        player.hitInPlay()
        progressBarColor()
        hitEfficiency = hittingEfficiencyString()
        initialFrameLabel.config(text= "Efficiency: " + hitEfficiencyJust())
        progressFrame['value'] = hitEfficiency
        meterFrame.amountusedvar.set(player.kp)

    def killButton():
        player.killScored()
        progressBarColor()
        hitEfficiency = hittingEfficiencyString()
        initialFrameLabel.config(text= "Efficiency: " + hitEfficiencyJust())
        progressFrame['value'] = hitEfficiency
        meterFrame.amountusedvar.set(player.kp)

    def errorButton():
        player.errorRecorded()
        progressBarColor()
        hitEfficiency = hittingEfficiencyString()
        initialFrameLabel.config(text= "Efficiency: " + hitEfficiencyJust())
        print(len(str(player.he)))
        progressFrame['value'] = hitEfficiency
        meterFrame.amountusedvar.set(player.kp)

    def hittingEfficiencyString() -> str:
        hitEfficiency = f"{((player.he*50)+50):.4f}"
        return hitEfficiency
    
    def hitEfficiencyJust() -> str:
        strHE = str(player.he)
        if player.he >= 0:
            return strHE.ljust(6, '0')
        else:
            return strHE.ljust(7, '0')
        # return strHE

    def progressBarColor():
        s = ttk.Style()
        s.configure('red.Vertical.TProgressbar',background="#e74c3c", lightcolor="#e74c3c", darkcolor="#e74c3c")
        s.configure('yellow.Vertical.TProgressbar',background="#f39c12", lightcolor="#f39c12", darkcolor="#f39c12")
        s.configure('green.Vertical.TProgressbar',background="#00bc8c", lightcolor="#00bc8c", darkcolor="#00bc8c")
        if player.he < 0:
            # progressFrame['style'] = 'Danger'
            
            progressFrame['style'] = "red.Vertical.TProgressbar"
        elif player.he > .3:
            progressFrame['style'] = 'green.Vertical.TProgressbar'
        else:
            progressFrame['style'] = 'yellow.Vertical.TProgressbar'

    # Creating the player object
    player = Player.Player(name, number)

    # Creating the frame that the player's stats and tracking will be in 
    userText = name + " #" + str(number)
    initialFrame = ttk.LabelFrame(frame, text=userText)
    initialFrame.columnconfigure((0,1), weight=1)
    print("row - " + str(rowNum/2) + " column - " + str(rowNum%2))
    initialFrame.grid(row = int(rowNum/2), column = rowNum%2)

    initialFrameLabel = ttk.Label(initialFrame, text="Efficiency: " + hitEfficiencyJust())

    initialFrameLabel.grid(row=0, column=3, padx=5, pady=2)
    initialFrameButton = ttk.Button(initialFrame, text="Hit in play", command=hitInPlayButton, bootstyle="outline-info")
    initialFrameButton.grid(row=0, column=0, padx=5, pady=2)
    initialFrameButton1 = ttk.Button(initialFrame, text="Kill", command=killButton, bootstyle="outline-success")
    initialFrameButton1.grid(row=0, column=1, padx=5, pady=2)
    initialFrameButton2 = ttk.Button(initialFrame, text="Error", command=errorButton, bootstyle="outline-danger")
    initialFrameButton2.grid(row=0, column=2, padx=5, pady=2)

    progressFrame = ttk.Progressbar(initialFrame, value=50, style='Danger.Vertical', orient='vertical')
    progressFrame.grid(row=0, column=4, padx=5, pady=2)

    meterFrame = ttk.Meter(initialFrame, amountused=player.kp, arcrange=180, interactive=False, amounttotal=100, subtext="Kill Percentage", textright="%", metersize=150)
    meterFrame.grid(row=0, column=5, padx=5, pady=2)
    pass