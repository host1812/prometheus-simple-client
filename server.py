import logging
import sys

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
logger = logging.getLogger("__main__")


def main():
    logger.info("started: main")
    logger.info("finished: main")

if __name__ == "__main__":
    main()
