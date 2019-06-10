from time import sleep

art = """
 _   __                _             _       _            
| | / /               | |           | |     (_)           
| |/ / _   _ _ __ ___ | | _____   __| | __ _ _ _ __ _   _ 
|    \| | | |  __/ _ \| |/ / _ \ / _` |/ _` | |  __| | | |
| |\  | |_| | | | (_) |   | (_) | (_| | (_| | | |  | |_| |
\_| \_/\____|_|  \___/|_|\_\___/ \____|\____|_|_|   \____|

"""

menuStr = """
\t <01> App 1
\t <02> App 2
\t <03> App 3
"""

while True:
    print(art)
    print(menuStr)

    try:
        print("Enter Number")
        choice = int(input(">"))
        break
    except(KeyboardInterrupt):
        exit()
    except:
        print("Enter a valid number.")
        sleep(1)


if(choice == 1):
    print(str(choice) + "nr 1")
elif(choice == 2):
    print(choice)
else:
    print("not 1 or 2")

