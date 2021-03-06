"""sPoNgEtExT, by Al Sweigart al@inventwithpython.com
Translates English messages into sPOnGEtExT.
This and other games are available at https://nostarch.com/XX
Tags: tiny, beginner, word"""
__version__ = 0
import random

try:
    import pyperclip  # pyperclip copies text to the clipboard.
except ImportError:
    pass  # If pyperclip is not installed, do nothing. It's no big deal.


def main():
    """Run the Spongetext program."""
    print('''sPoNgEtExT, bY aL sWeIGaRt Al@iNvEnTwItHpYtHoN.cOm

eNtEr YoUr MeSsAgE:''')
    spongetext = englishToSpongetext(input('> '))
    print()
    print(spongetext)

    try:
        pyperclip.copy(spongetext)
        print('(cOpIed SpOnGeTexT to ClIpbOaRd.)')
    except:
        pass  # Do nothing if pyperclip wasn't installed.


def englishToSpongetext(message):
    """Return the spongetext form of the given string."""
    spongetext = ''
    useUpper = False

    for character in message:
        if not character.isalpha():
            spongetext += character
            continue

        if useUpper:
            spongetext += character.upper()
        else:
            spongetext += character.lower()

        useUpper = not useUpper  # Flip the case.

        # Randomly flip the case again in 1 in 10 characters.
        if random.randint(1, 10) == 1:
            useUpper = not useUpper
    return spongetext


# If this program was run (instead of imported), run the game:
if __name__ == '__main__':
    main()
