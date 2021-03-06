from .io import IO


_MAIN_BANNER = r"""{}
███████╗██╗   ██╗██╗██╗       ██╗     ██╗███╗   ███╗██╗████████╗███████╗██████╗ 
██╔════╝██║   ██║██║██║       ██║     ██║████╗ ████║██║╚══██╔══╝██╔════╝██╔══██╗
█████╗  ██║   ██║██║██║       ██║     ██║██╔████╔██║██║   ██║   █████╗  ██████╔╝
██╔══╝  ╚██╗ ██╔╝██║██║       ██║     ██║██║╚██╔╝██║██║   ██║   ██╔══╝  ██╔══██╗
███████╗ ╚████╔╝ ██║███████╗  ███████╗██║██║ ╚═╝ ██║██║   ██║   ███████╗██║  ██║
╚══════╝  ╚═══╝  ╚═╝╚══════╝  ╚══════╝╚═╝╚═╝     ╚═╝╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝
                {}by bitbrute  ~  limit devices on your network :3
                      edited by DSlite  ~  adding some stuff
                                    v[_V_]

""".format(IO.Fore.LIGHTRED_EX, IO.Style.RESET_ALL + IO.Style.BRIGHT)


def get_main_banner(version):
    return _MAIN_BANNER.replace('[_V_]', version)