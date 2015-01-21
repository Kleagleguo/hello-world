import re

def stripVersion(filename):
	pattern = r'(?P<filename>[\w\-]*)(?P<version>\-\d.*)(?P<extension>\.\w+$)'
	match = re.match(pattern, filename)
	if match:
		return match.group('filename') + match.group('extension')
	else:
		return filename

if __name__ == '__main__':
	print stripVersion('druid-common.jar')