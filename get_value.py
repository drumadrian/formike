# Notes: 

# use debug statements to keep you output clean when you are not trying to debug:
# debug = True
debug = False

# 1) To help think about your card better, I would represent your card data using a dictionary. 
#     It takes up a little more space in memory but it works great for reading the code


sample_card_1 = {}
sample_card_1['face'] = 8
sample_card_1['suit'] = 'spaid'

sample_card_2 = {}
sample_card_2['face'] = 10
sample_card_2['suit'] = 'spaid'

if debug:
  print(sample_card_1)
  print(sample_card_2)


# So now, your list of cards can be declared like this:
player_hand = list()
# or you can use:
player_hand = []


# And now, your list of cards can use the append() function:
player_hand.append(sample_card_1)
player_hand.append(sample_card_2)

if debug:
  print(player_hand)

# Next, I assume you are trying to do something for each card in a hand.  
#   You wrote nice and consice code, I would make it more verbose for the firt version so it is easy to reinterpret when you walk away and come back to this code. 
#    Hint: it also makes it easier for the next programmer to see your intentions
#       I would also make it more verbose so you can more easily debug code when things don't work well. You can observe/inspect the contents of variables in a debugger when you have verbose code.

hand_face_value = 0

def get_value(hand):
  value = 0
  for card in hand:
    value = value + do_something(card)
  
  return value

# Here it is easy to focus on the operation per card.  Your original code did not declare the variable "item", outside of the for loop, 
#      so your code will only do this in the scope of a loop iteration for a single card: 

#             if item == int():
#               item += item

# I Think(my guess) you want to add up each face value for each card in the hand, and test the item to see if it is an integer before adding it to the total hand face value.  
#   Note: card.values() is a very important syntax for using dictionaries.  Read about it here:  https://note.nkmk.me/en/python-dict-keys-values-items/
# So I would write it this way: 

def do_something(card):
  card_face_value = 0
  for item in card.values():
    if isinstance(item, int):
      card_face_value = card_face_value + item

  if debug:
    print('card_face_value') 
    print(card_face_value) 
  
  # Finally, return card_face_value which is the output of 'doing something'  
  return card_face_value


# In conclusion, you did not save the return of the get_value() function call.  I assume you either want to save the value or just print the value.  Since you had a return statement in your function, I'll do both.  :-) 
hand_face_value = get_value(player_hand)

print("\n player_hand=", player_hand)
print("\n hand_face_value=", hand_face_value)



####################################################################################################################################
###################################################  END   #########################################################################
############################################ ADRIAN'S CODE ##################################################################
####################################################################################################################################




####################################################################################################################################
############################################ Final Thoughts ##################################################################

# This was written using Python 3.8.9

# You are going to get really good at coding.  Trying building your skill using leetcode.com
# 
# https://leetcode.com/  

#        :-) 

####################################################################################################################################
####################################################################################################################################






####################################################################################################################################
###################################################  BEGIN   #######################################################################
############################################ MIKE'S ORIGINAL CODE ##################################################################
####################################################################################################################################

# player_hand = [[8, "spaids"], [10, "spaids"]]

# def get_value(hand):
#   for card in hand:
#     for item in card:
#       if item == int():
#         item += item
#         return item

# get_value(player_hand)
# print(player_hand)

####################################################################################################################################
###################################################  END   #########################################################################
############################################ MIKE'S ORIGINAL CODE ##################################################################
####################################################################################################################################