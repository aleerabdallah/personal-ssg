from frontmatter import Post
from pathlib import Path

import frontmatter


BASE_DIR = Path(__file__).parent.parent / "content"


def parse_metadata(file):
    data = Post(file)
    print(data.content)


def read_file():
    with open(f"{BASE_DIR}/index.md") as file:
        # print(file.read())
        meta, content = frontmatter.parse(file.read())
        print(content)


if __name__ == "__main__":
    # print(BASE_DIR)
    print("===================")
    read_file()
