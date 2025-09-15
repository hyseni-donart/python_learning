def banner_text(text: str = " ", screen_width: int = 80) -> None:
    """
    Print a centered banner of text with decorative borders.

    This function prints a line of text centered within a specified
    screen width, surrounded by two asterisks (`**`) on each side.
    If the text is a single asterisk (`*`), it prints a full-width line
    of asterisks instead.

    Args:
        text (str, optional): The text to display in the banner.
            Defaults to a single space (" ").
        screen_width (int, optional): The total width of the banner.
            Defaults to 80.

    Raises:
        ValueError: If the length of `text` is greater than
            `screen_width - 4`.

    Returns:
        None: This function prints directly to the console and
        does not return anything.
    """
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
