import scrapper
import html_renderer

import os


if __name__ == "__main__":
    print(os.getcwd())
    scrapper.starter()
    html_renderer.renderer(10000)
    import server
    server.create()
