def initialize_world():
    global mailbox,starter,north,east,west,south,world
	world=World()
    mailbox=Mailbox()
    mailbox.desc='It is a mailbox with the flag up and the front closed'
    mailbox.action='interact'
    mailbox.contains=letter
    mailbox.in_room=0
    starter=room("You are in a room with four exits \033[1m north east south west\033[0m. There is a single mailbox before you.",mailbox,None,0,0,[0,1,2,3])
	letter=Item()
	letter.desc="It's a letter you found in the mailbox."
	letter.interact="The letters have faded but you can make out a single sentence 'Those in the dark fear the light.'"
	letter.location=starter._id
	player=Player()
	inventory=Inventory()


