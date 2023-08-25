# play = True

# while play == True:
#     name = input('What is your name?: ')
#     print('Hey', name)
#     print('Welcome to the Quest Game!')
#     # Use \n to print the next statements on a new line
#     print('1. Wonderland \n2. Lala land \n3. Space')
#     # Wrap the input method with int() to convert to an integer
#     choice = int(input('Where would you like to go today?: '))
#     if choice == 1:
#         print('Welcome to Wonderland!')
#         print('There is lots to do here, but first you must say beetle juice 3 times.')
#         print('1. Say beetle juice to continue. \n2. Quit game')
#         first_choice = int(input('Would you like to continue?: '))
#         if first_choice == 1:
#             for i in range(3):
#                 # print('Beetle juice.')
#                 input()
#             print('Great choice! Let us see how far you get.')
#             colour = input('What is the colour of your fear (yellow or red): ')
#             if colour == 'yellow' or 'blue':
#                 print("That's very mild you seem to fear nothing")
#             elif colour == 'red':
#                 print('You have a lot of fears young one!')
#             else:
#                 print('Make the correct choice.')
#         else:
#             print('Thank you for playing!')
#             play = False
#     elif choice == 2:
#         print('Welcome to Lala land!')
    
# Terminal Game


play = True

def bad_choice():
	print('YOUR COMMAND WAS UNWISE. YOU DIED!')
	play = False



while play == True:

	print("Remember the rules./n You have to type your commands always in UPERCASE and type them correctly. OR ELSE!\n")
	choice = input("Welcome you mighty Samurai!\n The ORDER are giving you a mission to eliminate Hanisuka the Gladiator Warrior.\n Are you ready for the challenge? YES or NO?: \n")
	if choice == "YES":
		name = input('Enter your name you brave one: ')		
	elif choice != choice.upper():
		bad_choice()
		break
	else:
		print("Live like a coward!")
		break

	if name != name.upper():
		bad_choice()
		break

	print("You entered in a big dark hall room with little candle light inside.\n A lighting strikes and makes the room alive.\n In that quick moment you see Hanisuka with his golden armour.\n")

	choice = input("The candle light reflect clearly on his armour.\n He has helmet and a mask that covers his face.\n He laughs an says\n 'The order sent you?'YES or NO:\n")

	if choice == "YES":
		print(f"He laughs and says 'You must be {name} the legendary Samurai.\n I will enjoy killing you.'\n")
	else:
		question = input("Go away then! You have nothing to do here.\n I am only waiting for a mighty Samurai. What is your name? \n")
		if question == name:
			print(f"You are {name}! I have been waiting to fight the mightiest Samurai in all of Japan.\n And you have come to me.\n")
		else:
			print("A lighting strikes and the mirror behind Hanisuka blinds you.\n He also like lighting throws his long spear.\n")
			bad_choice()
			break
	first_choice = input("You say to him. I came to eliminate you.\n He replies 'I want to see you try.\n What you do? WAIT or STRIKE first?\n")
	if first_choice == "WAIT":
		print("He almost motionless gets closer to you.\n 'I am the great Hanisuka! A gladiator of a thousand battles in the colliseums of Rome.\n All this beautiful golden armour you see and this golden spear, sharp as death itself, I won it with blood shed.\n Do you believe you can defeat me?' ")
		second_choice = input("You RESPOND or remain SILENT? ")
		if second_choice == "RESPOND":
			print("A lighting strikes blinding you for a second.\n When you open your eyes you see Hanisuka's spear coming at you.\n You try to dodge it but it is too late.\n")
			bad_choice()
			break
		elif second_choice == "SILENT":
			third_choice = input(("He laughs and says 'I will take your silence as a yes.'\n He throws his spear at you. You DODGE or BLOCK?\n"))
			if third_choice == "DODGE":
				print("You roll to the left and throww him a kunai that he easily deflects with his hidden infamous sword. The double edge sword!!!!\n")
			elif third_choice == "BLOCK":
				print("You block his frontal strike to the side and quick as lighting with your Katana slash from above and cut his spear in half.\n Hanisuka rolls fast to the back and stands quickly with sword in hand. He holds his long and deadly double edge sword!!!\n")
		else:
			bad_choice()
			break
	elif first_choice == "STRIKE":
		fourth_choice = input("Without hesitation like a snake you throw your Kunai towards him and move fast towards him.\n He deflects the Kunai easyily with his spear\n But you got close enough to make a long SLASH or throw another KUNAI?\n")
		if fourth_choice == "SLASH":
			print("He parries it easily but your close enough to give him a might upper slash woth you mighty Katana!\n You cut his spear in half and he rolls back and stands up with his deadly and infamous double edge sword in hand.\n")
		elif fourth_choice == "KUNAI":
			fifth_choice = input("He expecting it deflects it easily with his spear again throws sand to you that blind you for a second.\n You like a master Samurai feel his strike and deflect it.\n You can roll back and REGAIN you stand or you can SLASH back!\n")
			if fifth_choice == "REGAIN":
				print("You move backwards barely deflecting his frenzy strikes.\n Your vision comes back and you give a surprise side slash that cuts his spear in half.\n He rolls back and stands up with his deadly and infamous double edge sword in hand.\n")
			elif fifth_choice == "SLASH":
				print("You slash back and cut his spear in half.\m But your blindness did not anticipate his hidden deadly double edge sword from his back. He cuts your head clean of your shoulder.\n YOU DIED\n")
				break
		else:
			bad_choice()
			break
	else:
		bad_choice()
		break
	print("Congrats you have survied this long. The battle will continue...")
	play = False

