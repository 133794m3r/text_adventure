#!/usr/bin/python3
'''
This script will test if the system supports all of the different colors and
text options by printing them out in groups with a tab separating them.
'''
def test_formatting():
	clear='\033[0m'
	i=0;
	formatters={'bold':'\033[1m','dim':'\033[2m','italic':'\033[3m','underline':'\033[4m','blinking':'\033[5m','inverted':'\033[7m','hidden':'\033[8m'}
	for key in formatters:
		string='code:\\033[{}m {} {}text{}'.format(i,key,formatters[key],clear)
		#end is python3 to make it run on python2 simply change this line to remove the ,end='    '
		print(string,end='    ')
		if i % 2:
			print("")
		i+=1
	print("\n")

def test_colors():
	clear='\033[0m'
	colors={
	'Default':{'fg':'\033[39m', 'bg':'\033[49m'},
	'Black':{'fg':'\033[30m', 'bg':'\033[40m'},
	'Red':{'fg':'\033[31m', 'bg':'\033[41m'},
	'Green':{'fg':'\033[32m', 'bg':'\033[42m'},
	'Brown':{'fg':'\033[33m', 'bg':'\033[43m'},
	'Blue':{'fg':'\033[34m', 'bg':'\033[44m'},
	'Purple':{'fg':'\033[35m', 'bg':'\033[45m'},
	'Cyan':{'fg':'\033[36m', 'bg':'\033[46m'},
	'Light Gray':{'fg':'\033[37m', 'bg':'\033[47m'},
	'Dark Gray':{'fg':'\033[90m', 'bg':'\033[100m'},
	'Light Red':{'fg':'\033[91m', 'bg':'\033[101m'},
	'Light Green':{'fg':'\033[92m', 'bg':'\033[102m'},
	'Yellow':{'fg':'\033[1;33m', 'bg':'\033[103m'},
	'Light Blue':{'fg':'\033[94m', 'bg':'\033[104m'},
	'Light Purpple':{'fg':'\033[95m', 'bg':'\033[105m'},
	'Light Cyan':{'fg':'\033[96m', 'bg':'\033[106m'},
	'White':{'fg':'\033[97m', 'bg':'\033[107m'}
	}
	codes={
	'Default':{'fg':'\\033[39m', 'bg':'\\033[49m'},
	'Black':{'fg':'\\033[30m', 'bg':'\\033[40m'},
	'Red':{'fg':'\\033[31m', 'bg':'\\033[41m'},
	'Green':{'fg':'\\033[32m', 'bg':'\\033[42m'},
	'Brown':{'fg':'\\033[33m', 'bg':'\\033[43m'},
	'Blue':{'fg':'\\033[34m', 'bg':'\\033[44m'},
	'Purple':{'fg':'\\033[35m', 'bg':'\\033[45m'},
	'Cyan':{'fg':'\\033[36m', 'bg':'\\033[46m'},
	'Light Gray':{'fg':'\\033[37m', 'bg':'\\033[47m'},
	'Dark Gray':{'fg':'\\033[1;30m or \\033[90m','bg':'\\033[1;40m or \\033[100m'},
	'Light Red':{'fg':'\\033[1;31m or \\033[91m','bg':'\\033[1;41m or \\033[101m'},
	'Light Green':{'fg':'\\033[1;32m or \\033[92m','bg':'\\033[1;42m or \\033[102m'},
	'Yellow':{'fg':'\\033[1;33m or \\033[93m','bg':'\\033[1;43m or \\033[103m'},
	'Light Blue':{'fg':'\\033[1;34m or \\033[94','bg':'\\033[1;44m or \\033[104m'},
	'Light Purpple':{'fg':'\\033[1;35m or \\033[95','bg':'\\033[1;45m or \\033[105m'},
	'Light Cyan':{'fg':'\\033[1;36m or \\033[96','bg':'\\033[1;46m or \\033[106m'},
	'White':{'fg':'\\033[1;37m or \\033[97','bg':'\\033[1;47m or \\033[107m'}
	}
	i=0;
	for key in colors:
		print("="*80)
		print('Color {} '.format(key),end='    ')
		print('Foreground Code: {} Background Code: {}'.format(codes[key]['fg'],codes[key]['bg']))
		print('Foreground {}color{} Background {}color{}'.format(colors[key]['fg'],clear,colors[key]['bg'],clear))
		i+=1
	print("")
print("The code below will give you the escape codes to utilize for the formats.\nThey are used like thus {code}String_to_Format{clear_code}\n")
test_formatting()
test_colors()
print("You can also combine multiple ones by adding a ; between the modifiers. So bold and underline would be \\033[1;4m \033[1;4mUnderlined & Bolded\033[0m")
