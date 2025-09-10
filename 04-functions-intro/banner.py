def banner_text(text: str = " ", screen_width: int = 80):
    if len(text) > screen_width - 4:
        raise ValueError(f"String {text} is larger than the specified width {screen_width}")

    if text == "*":
        print("*" * screen_width)
    else:
        centered_text = text.center(screen_width - 4)
        output_string = "**{0}**".format(centered_text)
        print(output_string)


banner_text("*")
banner_text("Always look on the bright side of life...")
banner_text("If life seems jolly rotten,")
banner_text("There's something you've forgotten!")
banner_text("And that's to smile and dance and sing,")
banner_text()
banner_text("When you're feeling in the dumps,")
banner_text("Don't be silly chumps,")
banner_text("Just pursue your lips and whistle - that's the thing")
banner_text("And... always look on the bright side of life...")
banner_text("*")
