import sys
from commands.reverse import reverse
from commands.copy import copy
from commands.duplicate_contents import duplicate_contents
from commands.replace_string import replace_string
from exceptions import InvalidCommandException, InvalidArgException


try:
    if len(sys.argv) < 2:
        raise InvalidCommandException
    else:
        command = sys.argv[1]
        if command == 'reverse':
            if len(sys.argv) != 4:
                raise InvalidArgException
            else:
                reverse(sys.argv[2], sys.argv[3])
        elif command == 'copy':
            if len(sys.argv) != 4:
                raise InvalidArgException
            else:
                copy(sys.argv[2], sys.argv[3])
        elif command == 'duplicate-contents':
            if len(sys.argv) != 4:
                raise InvalidArgException
            else:
                duplicate_contents(sys.argv[2], int(sys.argv[3]))
        elif command == 'replace-string':
            if len(sys.argv) != 5:
                raise InvalidArgException
            else:
                replace_string(sys.argv[2], sys.argv[3], sys.argv[4])
        else:
            raise InvalidCommandException
except InvalidCommandException:
    print('Invalid command! Commands supported are `reverse`, `copy`, `duplicate_contents` and `replace-string`.')
except InvalidArgException:
    print('Invalid number of arguments!')
