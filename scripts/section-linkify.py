import re
import sys
import functools


GFM_DISALLOWED_CHAR_REGEX = '[^a-zA-Z0-9\-_]'

HEADER_LINE_REGEX = re.compile(r'^#+\s+(?P<section_number>\d(\.\d+)*)\s+(?P<section_name>.+)$')

TEXT_SECTION_REF_REGEX = r'[Ss]ection\s+(?P<section_number>\d(.\d+)*)'


def convert_header_to_gfm_id(header):
	return re.sub(
		GFM_DISALLOWED_CHAR_REGEX,
		'',
		header.replace(' ', '-')
	).lower()


def create_link(section_to_identifiers, m):
	section_number = m['section_number']
	section_name = section_to_identifiers.get(section_number)

	if section_name is None:
		return m[0]

	gfm_id = convert_header_to_gfm_id(f'{section_number}-{section_name}')

	return f'[{m[0]}](#{gfm_id})'


lines = [ l.rstrip('\n') for l in sys.stdin.readlines()]

section_to_identifers = {
	m['section_number']: m['section_name']
	for m in map(lambda l: HEADER_LINE_REGEX.match(l), lines)
	if m is not None
}

repl_func = functools.partial(create_link, section_to_identifers)

sys.stdout.writelines((
	re.sub(TEXT_SECTION_REF_REGEX, repl_func, l) + '\n'
	for l in lines
))
