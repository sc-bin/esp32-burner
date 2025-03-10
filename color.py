class color:
    free = "rgb(255, 255, 255)"
    error = "rgb(255, 0, 0)"
    burn_runing = "rgb(113, 255, 47)"
    burn_end = "rgb(170, 108, 54)"
    send_runing = "rgb(85, 170, 255)"
    send_end = "rgb(152, 152, 44)"

    def __init__(self, prefix="", postfix=""):
        self.free = prefix + self.free + postfix
        self.error = prefix + self.error + postfix
        self.burn_runing = prefix + self.burn_runing + postfix
        self.burn_end = prefix + self.burn_end + postfix
        self.send_runing = prefix + self.send_runing + postfix
        self.send_end = prefix + self.send_end + postfix


label_background = color("background-color:")
