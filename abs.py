#!/usr/bin/env python3
from sys import argv, exit
from helpers import log_in, assmnt_setup, execute_nursing_form


def main():
    log_in()
    assmnt_setup()
    execute_nursing_form()


if __name__ == "__main__":
    main()
