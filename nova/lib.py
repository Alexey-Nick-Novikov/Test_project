from termcolor import colored, cprint

def try_me():
    text = colored('Hello, World!', 'red', attrs=['reverse', 'blink'])
    print(text)
    cprint('Hello, World!', 'green', 'on_red')

    print_red_on_cyan = lambda x: cprint(x, 'red', 'on_cyan')
    print_red_on_cyan('Hello, World!')

    for i in range(10):
        cprint(i, 'magenta', end=' ')