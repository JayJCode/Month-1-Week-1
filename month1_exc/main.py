"""
Week 1
1) Program should read data.txt
2) Count the numbers of words and lines.
3) Find "key" word.

Week 2
1) Extend your previous script to use Python’s argparse.
2) Integrate at least one standard library (os/sys/datetime) in a meaningful way.
3) Populate data in the text file you are working with by fetching it from an external API using requests.

Week 3
1) Reorganize program (use functions, main etc.).
2) Use classes (APIClient, FileManager).
3) Create tests using pytest in separate folder (tests).

Week 4
1) Create a Dockerfile
2) Build and run a docker image (docker build -t nazwa .) (docker run -d nazwa)
3) Create a workflow file in .github/workflows/ci.yml (checks out code, installs dependencies, runs tests, builds docker image)
"""

import argparse

from src.api_client import APIClient
from src.file_manager import FileManager

def argparse_init():
    """
    Example use: py month1_exc/main.py -f month1_exc/src/data.txt -k name -c region -v africa
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", help="The name of the file we filter through")
    parser.add_argument("-k", "--key", help="The key name or symbol to be filtered in file")
    parser.add_argument("-c", "--category", help="The category name of which data will be download to data.txt")
    parser.add_argument("-v", "--value", help="The value name of which data will be download to data.txt")
    return parser.parse_args()

def main():
    args = argparse_init()

    # Get data from API
    api_client = APIClient()
    data = api_client.get_data(args.category, args.value)

    # Maintain on it locally
    file_manager = FileManager(args.file)
    file_manager.save(data)
    print(file_manager.get_file_info())
    file_manager.read()
    print(file_manager.investigate_file(args.key))

if __name__=="__main__":
    main()