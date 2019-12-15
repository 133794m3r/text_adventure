#!/usr/bin/python3
import templates
import sys

#def intialize():
#    module_name=globals()['__name__']
#    module_obj=sys.modules[modname]

#def main():
#    intialize()

#main()
prefix='> '
room_ids={'starter':0,'north':1,'east':2,'south':3,'west':4}
valid_moves={0:[0,1,2,3],1:[1],2:[2],3:[0],4:[3]}
directions=['north','south','west','east']
verbs=['look','grab','move','interact']
items={'Mailbox':{'desc':'It is a mailbox with the flag up and the front closed','action':'interact','contains':'letter'},'flashlight':{'desc':'A bright flashlight that\'s still burning.','action':'interact','contains':'batteries'}}
mobs=['grue','fish']
item_interactions={'Mailbox':'You opened the mailbox and found a letter.','Flashlight':'You picked up the flashlight and started using it.'}
mob_interactions={'grue':'You were eaten by a grue','fish':{'The fish is flopping helplessly'}}
rooms={0:{'items':'Mailbox','mobs':None,'desc':'You are in a room with four exits \033[1m north east south west\033[0m. There is a single mailbox before you.'},1:{'items':None,'mobs':'grue','desc':'dark, and you were eaten by a grue'},2:{'items':'flashlight','mobs':None,'desc':'You are in a room with a single source of light. A \033[1m flashlight.\033[0m'},3:{'item':'Rope','enemy':'fish','desc':'You are in a wet room. There is a fish flopping on the ground before you.'},4:{'items':None,'mobs':None,'desc':'You are in an empty room. You can see nothing else.'}}
current_room=0
print('Enter your name brave traveller.')
name=input(prefix)
print(f'{name} is in a room.')
print('Your action verbs are \033[1m{}\033[0m'.format(' '.join(verbs)))
print('Your possible movements are \033[1m{}\033[0m'.format(' '.join(directions)))

#rewrite to have it look through the 4 cardinal directions to make it more easy for them to add items to it.
def check_move(direction):
    global current_room
    if direction not in directions:
        print('You didn\'t enter a valid movement.')
    else:
        dir_id=directions.index(direction)
        if dir_id in valid_moves[current_room]:
            if current_room != 0:
                current_room=0
            else:
                if dir_id == 0:
                    current_room=1
                elif dir_id == 1:
                    current_room=3
                elif dir_id == 2:
                    current_room=4
                elif dir_id == 3:
                    current_room=2
        
def look(obj):
    if obj is None:
        print(rooms[current_room]['desc'])
    else:
        if obj in rooms[current_room]['items']:
            print(items[obj]['desc'])
#            print('testme')

def interact(obj):
    if obj is None:
        print('You flail your arms about in the air making quite a fool of yourself.')
    else:
        print(items[''])

def check_input(usr_input):
    inputs=usr_input.split(' ')
    verb=inputs[0]
    if len(inputs) >= 2:
        obj=inputs[1]
    else:
        obj=None
        
    if verb in verbs:
        if verb == 'move':
            check_move(obj)
        elif verb == 'look':
            look(obj)
    else:
        print('not valid')

def main_loop():
    dead=False
    while dead == False:
        usr_input=input(prefix)
        check_input(usr_input)
#        dead=True


main_loop()
