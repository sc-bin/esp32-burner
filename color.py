class _color:
    free = "rgb(255, 255, 255)"
    error = "rgb(255, 0, 0)"
    burn_running = "rgb(113, 255, 47)"
    burn_end = "rgb(170, 108, 54)"
    send_running = "rgb(85, 170, 255)"
    send_end = "rgb(152, 152, 44)"

    def __init__(self, prefix="", postfix=""):
        self.free = prefix + self.free + postfix
        self.error = prefix + self.error + postfix
        self.burn_running = prefix + self.burn_running + postfix
        self.burn_end = prefix + self.burn_end + postfix
        self.send_running = prefix + self.send_running + postfix
        self.send_end = prefix + self.send_end + postfix


color = _color()
label_background = _color("background-color:")
