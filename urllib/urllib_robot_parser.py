from pathlib import Path
from urllib.request import urlopen

def download_robot_txt():
    filename = "robots.txt"

    with urlopen("https://www.python.org/robots.txt") as response, open(filename, "wb") as out_file:
        out_file.write(response.read())

# download_robot_txt()

from urllib.robotparser import RobotFileParser

def robot_parser_parse_robot_txt():
    parser = RobotFileParser("https://www.python.org")

    filename = "robots.txt"
    filepath = Path(filename)

    with filepath.open("r") as file:
        text = file.readlines()

    parser.parse(text)
    bot = "Krugle"
    print(parser.site_maps())
    print(parser.crawl_delay(bot))
    print(parser.can_fetch(bot, "https://www.python.org/webstats/testing"))

# robot_parser_parse_robot_txt()

def robot_parser_read_fron_link():
    parser = RobotFileParser("https://www.python.org/robots.txt")
    parser.read()

    bot = "Krugle"
    print("Allowed: ", parser.can_fetch(bot, "https://www.python.org/webstats/testing"))
    print("Allowed: ", parser.can_fetch(bot, "https://www.python.org"))

robot_parser_read_fron_link()