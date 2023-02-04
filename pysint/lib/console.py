# RED = "\u001b[1;91m"
# RESET = "\u001b[0m"
# CYAN = "\u001b[1;96m"
# PURPLE = "\u001b[1;95m"
# GREEN = "\u001b[1;92m"
# WHITE = "\u001b[1;97m"
# BLUE = "\u001b[1;94m"

from datetime import datetime
from colorama import init
from time import sleep
from getpass import getuser
from rich.live import Live
from rich.table import Table, Column
from rich.console import Console
from rich.box import SIMPLE_HEAVY
from rich.progress import Progress
from queue import Queue

import os

init(True)
class Console(Console):
    __BANNER = f"""
\t\t[bold cyan]                        ,---.
\t\t                       /    |
\t\t                      /     |
\t\t                     /      |
\t\t                    /       |
\t\t               ___,'        |
\t\t             <  -'          :
\t\t              `-.__..--'``-,_\_
\t\t                 |o/ ` :,.)_`>
\t\t                :/ `     ||/)
\t\t                 (_.).__,-` |\\
\t\t                 /( `.``   `| :
\t\t                 \'`-.)  `  ; ;
\t\t                 | `       /-<
\t\t                 |     `  /   `.
\t\t ,-_-..____     /|  `    :__..-'\\
\t\t/,'-.__\\  ``-./ :`      ;       \\
\t\t`\ `\  `\\  \ :  (   `  /  ,   `. \\
\t\t  \` \   \\   |  | `   :  :     .\ \\
\t\t   \ `\_  ))  :  ;     |  |      ):
\t\t  (`-.-'\ ||  |\ \   ` ;  ;       |
\t\t   \-_   `;;._   ( `  /  /_       |
\t\t    `-.-.// ,'`-._\__/_,'         ;
\t\t       \:: :     /     `     ,   /  
\t\t        || |    (        ,' /   /   
\t\t   [bold magenta]     ||                ,'   /           
\t\t\t [bold purple]\\ _      __(_)_______/
\t\t\t  | | /| / / / ___/ _ \\
\t\t\t  | |/ |/ / (__  )  __/
\t\t\t  |__/|__/_/____/\___/
\t\t\t    [bold magenta]source: [link=https://github.com/Arif-Helmsys]GITHUB[/link]"""

    def display_links(self,*printable:str):
        output = ""
        for out in printable:
            output += out + chr(32)
        self.print(f"{chr(32)*3}🟢 [purple]{output}",soft_wrap=True)

    def display(self,*obj:object):
        output = ""
        for out in obj:
            output += out + chr(32)
        return self.print(f"{chr(32)*3}🔵 [green]{output}")

    def warn_display(self,printable:str):
        return self.print(f"{chr(32)*3}🟠 [green]{printable}")
    

    def err_display(self,printable:str):
        return self.print(f"{chr(32)*3}🔴 [green]{printable}")

    def setTable(self,*column,title):
        columns:list[Column] = []
        for c in column:
            columns.append(Column(c,justify="center",no_wrap=True))

        self.table_ = Table(*columns,box=SIMPLE_HEAVY,title=title)

    def table(self,row):
        if type(row) is not  Queue:
            rows:list[str] = []
            for r in row:
                rows.append(r)

        with Live(self.table_):
            if type(row) is Queue:
                while not row.empty():
                    a,b,c = row.get()
                    self.table_.add_row(a,b,c)
                    sleep(0.2)
            else:
                self.table_.add_row(*rows)
                sleep(0.2)
    
    def progress_bar(self,thread_num):
        with Progress() as progress:
            task1 = progress.add_task(f"{chr(32)*3}🟡 [bold green]Threads Running[bold]", total=thread_num)
            while not progress.finished:
                progress.update(task1,advance=0.3)
                sleep(0.2)
    @property
    def BANNER(self):
        return self.print(self.__BANNER)

# print("threads = 15         query = deneme")
# print("filter = twitter     social_media = False")