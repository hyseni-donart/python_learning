import colorama

BLACK = '\u001b[30m'
RED = '\u001b[31m'
GREEN = '\u001b[32m'
YELLOW = '\u001b[33m'
BLUE = '\u001b[34m'
MAGENTA = '\u001b[35m'
CYAN = '\u001b[36m'
WHITE = '\u001b[37m'
RESET = '\u001b[0m'

BOLD = '\u001b[1m'
UNDERLINE = '\u001b[4m'
REVERSE = '\u001b[7m'

def color_print(text: str, effect: str) -> None:
    """
    Print text to the console with a given color or style effect.

    This function wraps the input text with the specified ANSI effect
    code and resets the style after printing. It can be used to
    apply colors, bold, underline, or reverse effects to terminal output.

    Args:
        text (str): The text to be printed.
        effect (str): The ANSI escape code for the desired color or style.
            For example, RED, GREEN, BOLD, UNDERLINE, REVERSE, etc.

    Returns:
        None: This function prints directly to the console and does not return a value.
    """
    output_string = f"{effect}{text}{RESET}"
    print(output_string)


colorama.init()
color_print("Hello, Red", RED)
# Test that the text was reset
print("This should be on the default terminal color")
color_print("Hello, Blue", BLUE)
color_print("Hello, Yellow", YELLOW)
color_print("Hello, Bold", BOLD)
color_print("Hello, Underline", UNDERLINE)
color_print("Hello, Reverse", REVERSE)
color_print("Hello, Black", BLACK)
colorama.deinit()