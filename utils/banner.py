from utils.color import green, cyan, yellow

def print_banner():
    line = cyan("=" * 50)
    print(line)
    print(green(r'''
   ____      _       _  __   __      _                     
  / __ \    (_)     | | \ \ / /     | |                    
 | |  | |___ _ _ __ | |_ \ V / _ __ | | ___  _ __ ___ _ __ 
 | |  | / __| | '_ \| __| > < | '_ \| |/ _ \| '__/ _ \ '__|
 | |__| \__ \ | | | | |_ / . \| |_) | | (_) | | |  __/ |   
  \____/|___/_|_| |_|\__/_/ \_\ .__/|_|\___/|_|  \___|_|   
                              | |                          
                              |_|                          
'''))
    print(cyan(line))
    print(yellow(" Name    : Mohammad Alamin"))
    print(yellow(" GitHub  : https://github.com/anbuinfosec"))
    print(cyan(line))
