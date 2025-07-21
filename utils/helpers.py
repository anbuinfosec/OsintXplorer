import time
import sys
from utils.color import green, red, cyan, yellow
from tabulate import tabulate

def print_results(data):
    for section, content in data.items():
        print(f"\n\033[1m[{section}]\033[0m")

        if isinstance(content, dict):
            if all(isinstance(v, dict) for v in content.values()):
                for key, subdict in content.items():
                    print(f"\n{green('[+]')} {key}")
                    rows = []
                    for k,v in subdict.items():
                        val_str = str(v).lower()
                        icon = green("[+]")
                        text = v
                        if any(x in val_str for x in ["not found", "error", "invalid", "false", "no"]):
                            icon = red("[-]")
                            text = red(v)
                        elif any(x in val_str for x in ["warning", "warn", "caution"]):
                            icon = yellow("[!]")
                            text = yellow(v)
                        elif any(x in val_str for x in ["info", "status code", "unknown"]):
                            icon = cyan("[i]")
                            text = cyan(v)
                        rows.append([icon, k, text])
                    print(tabulate(rows, headers=["", "Field", "Value"], tablefmt="fancy_grid"))
            else:
                rows = []
                for k,v in content.items():
                    val_str = str(v).lower()
                    icon = green("[+]")
                    text = v
                    if any(x in val_str for x in ["not found", "error", "invalid", "false", "no"]):
                        icon = red("[-]")
                        text = red(v)
                    elif any(x in val_str for x in ["warning", "warn", "caution"]):
                        icon = yellow("[!]")
                        text = yellow(v)
                    elif any(x in val_str for x in ["info", "status code", "unknown"]):
                        icon = cyan("[i]")
                        text = cyan(v)
                    rows.append([icon, k, text])
                print(tabulate(rows, headers=["", "Field", "Value"], tablefmt="fancy_grid"))

        elif isinstance(content, list):
            for item in content:
                print(f"  {green('[+]')} {item}")
        else:
            print(f"  {green('[+]')} {content}")



def progress_bar(task="Processing", total=20, delay=0.05):
    colored_task = cyan(task)  # Color the task text in cyan
    for i in range(total + 1):
        percent = int(100 * i / total)
        bar = "█" * i + "░" * (total - i)
        sys.stdout.write(f"\r{colored_task}: [{bar}] {percent}%")
        sys.stdout.flush()
        time.sleep(delay)
    print()