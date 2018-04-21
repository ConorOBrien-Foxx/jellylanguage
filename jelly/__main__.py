#!python3

if __package__ == '':
	from os.path import dirname
	from sys import path

	path[0] = dirname(path[0])

from jelly import code_page, main, try_eval, ascii_to_jelly, jelly_to_ascii
from sys import argv

translate = False
flag_utf8 = False
end = ''

usage = '''Usage:

    jelly f <file> [input]    Reads the Jelly program stored in the
                              specified file, using the Jelly code page.
                              This option should be considered the default,
                              but it exists solely for scoring purposes in
                              code golf contests.

    jelly fu <file> [input]   Reads the Jelly program stored in the
                              specified file, using the UTF-8 encoding.
    
    jelly ft <file>           Translates an ascii representation of Jelly
                              code stored in the specified file into Jelly.

    jelly e <code> [input]    Reads a Jelly program as a command line
                              argument, using the Jelly code page. This
                              requires setting the environment variable
                              LANG (or your OS's equivalent) to en_US or
                              compatible.

    jelly eu <code> [input]   Reads a Jelly program as a command line
                              argument, using the UTF-8 encoding. This
                              requires setting the environment variable
                              LANG (or your OS's equivalent) to en_US.UTF8
                              or compatible.
    
    jelly et <code>           Translates an ascii representation of Jelly
                              code from a command line argument.

    Append an `n` to the flag list to append a trailing newline to the
    program's output.

Visit http://github.com/DennisMitchell/jellylanguage for more information.'''

if len(argv) < 3:
	raise SystemExit(usage)

for char in argv[1]:
	if char == 'f':
		flag_file = True
	elif char == 'u':
		flag_utf8 = True
	elif char == 'e':
		flag_file = False
	elif char == 'n':
		end = '\n'
	elif char == 't':
		translate = True

if flag_file:
	with open(argv[2], 'rb') as file:
		code = file.read()
	if flag_utf8:
		code = ''.join(char for char in code.decode('utf-8').replace('\n', '¶') if char in code_page)
	else:
		code = ''.join(code_page[i] for i in code)
else:
	code = argv[2]
	if flag_utf8:
		code = ''.join(char for char in code.replace('\n', '¶') if char in code_page)
	else:
		code = ''.join(code_page[ord(i)] for i in code)

if translate:
	print(ascii_to_jelly(code))
	exit()

args = list(map(try_eval, argv[3:]))

raise SystemExit(main(code, args, end))
