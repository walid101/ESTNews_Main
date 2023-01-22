import textwrap


def h1(
    txt: str,
    width: int = 80
    ) -> str:
    """
     ╔════════════════════════════════╗
     ║                                ║
     ║   Lorem ipsum dolor sit amet   ║
     ║                                ║
     ╚════════════════════════════════╝

    Lorem ipsum dolor sit amet


     ╔════════════════════════════════════════════════════════════════════════════════╗
     ║                                                                                ║
     ║   Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy     ║
     ║   eirmod tempor invidunt ut labore et dolore magna                             ║
     ║                                                                                ║
     ╚════════════════════════════════════════════════════════════════════════════════╝

    Lorem ipsum dolor sit amet
    """
    format_line = lambda l, w: ' ║   ' + l.ljust(w, ' ') + '   ║'

    txt_width: int = len(txt) if len(txt) + 6 < width else width - 6
    box_width: int = txt_width + 6
    lines: list = textwrap.wrap(txt, width=width - 6)
    msg: str = '\n\n'
    msg += ' ╔' + '═' * box_width + '╗' + '\n'
    msg += ' ║' + ' ' * box_width + '║' + '\n'
    msg += '\n'.join([format_line(line, txt_width) for line in lines]) + '\n'
    msg += ' ║' + ' ' * box_width + '║' + '\n'
    msg += ' ╚' + '═' * box_width + '╝' + '\n'
    return msg


def h2(
    txt: str,
    width: int = 80
    ) -> str:
    """
     ┌────────────────────────────┐
     │ Lorem ipsum dolor sit amet │
     └────────────────────────────┘

    Lorem ipsum dolor sit amet


     ┌────────────────────────────────────────────────────────────────────────────────┐
     │ Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy       │
     │ eirmod tempor invidunt ut labore et dolore magna                               │
     └────────────────────────────────────────────────────────────────────────────────┘

    Lorem ipsum dolor sit amet
    """
    format_line = lambda l, w: ' │ ' + l.ljust(w, ' ') + ' │'

    txt_width: int = len(txt) if len(txt) + 2 < width else width - 2
    box_width: int = txt_width + 2
    lines: list = textwrap.wrap(txt, width=width - 2)
    msg: str = '\n\n'
    msg += ' ┌' + '─' * box_width + '┐' + '\n'
    msg += '\n'.join([format_line(line, txt_width) for line in lines]) + '\n'
    msg += ' └' + '─' * box_width + '┘' + '\n'
    return msg


def h3(
    txt: str,
    width: int = 80
    ) -> str:
    """
     Lorem ipsum dolor sit amet
     ──────────────────────────

    Lorem ipsum dolor sit amet


     Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod
     tempor invidunt ut labore et dolore magna
     ────────────────────────────────────────────────────────────────────────────────

    Lorem ipsum dolor sit amet,

    """
    format_line = lambda l, w: ' ' + l.ljust(w, ' ') + ''

    txt_width: int = len(txt) if len(txt) + 0 < width else width - 0
    box_width: int = txt_width + 0
    lines: list = textwrap.wrap(txt, width=width - 0)
    msg: str = '\n\n'
    msg += '\n'.join([format_line(line, txt_width) for line in lines]) + '\n'
    msg += ' ' + '─' * (box_width) + '\n'
    return msg


def h4(
    txt: str,
    width: int = 80
    ) -> str:
    """
     # Lorem ipsum dolor sit amet

    Lorem ipsum dolor sit amet


     # Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy
     # eirmod tempor invidunt ut labore et dolore magna

    Lorem ipsum dolor sit amet
    """
    format_line = lambda l, w: ' # ' + l + ''

    txt_width: int = len(txt) if len(txt) + 4 < width else width - 4
    # box_width = txt_width + 4
    lines: list = textwrap.wrap(txt, width=width - 4)
    msg: str = '\n\n' + '\n'.join([format_line(line, txt_width) for line in lines]) + '\n'
    return msg
