### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:


  def check_for_ace(self, card):
    # double equal (==) needed below to check if values are truly equal
    if card.value = 1:
      return True
      # else statement below missing a colon
    else 
      return False
   

  dif highest_card(self, card1 card2):
  # dif should be def and also missing a comma after card 1
  if card1.value > card2.value: 
    # if statement above should be indented which throws off the whole block of code
    return card
    # above card should be returning card1
  else:
    return card2
  


def cards_total(self, cards):
  # the function above is not indented properly so is outside the class
  total
  # total is undefined so it has no value
  for card in cards:
    total += card.value
    return "You have a total of" + total
    # return has to be outside of the for loop should not be indented. Total is also currently an integer so cannot be concatenated unless total is converted to string
  
```
