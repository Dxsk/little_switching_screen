import sys
import time

from monitor import Monitor


def main(argument: str) -> None:
    monitor = Monitor()
    is_seconds_pc: bool = (argument == "switch_to_second_pc")
    is_this_pc: bool = (argument == "switch_this_pc")

    if is_seconds_pc:
        print('run is_seconds_pc')
        monitor.switch_to('internal')
        time.sleep(15)
        monitor.switch_to('external')

    elif is_this_pc:
        print('run is_this_pc')
        monitor.switch_to('extend')

    else:
        print('bad argument. : [switch_to_second_pc, switch_this_pc]')
        sys.exit(1)


if __name__ == '__main__':
    args: list[str] = sys.argv
    if len(args) <= 1:
        print('need argument.')
        sys.exit(1)
    main(args[1])
