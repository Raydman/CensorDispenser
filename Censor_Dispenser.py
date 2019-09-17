# These are the emails you will be censoring.
# The open() function is opening the text file
# that the emails are contained in and the .read() method is allowing us to save
# their contexts to the following variables:
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()

new_lst = []

def censor_one(input_text, censor):
  censored_item = ""
  for x in range(0,len(censor)):
    if censor[x] == " ":
      censored_item += " "
    else:
      censored_item += "X"
  return input_text.replace(censor, censored_item)

#print(censor_one(email_one, "learning algorithm"))

proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "her", "herself"]


def censor_two(input_text, censor_lst):
  for word in censor_lst:
    censored_word = ""
    for x in range(0, len(word)):
      if word[x] == " ":
        censored_word += " "
      else:
        censored_word += "X"
    input_text = input_text.replace(word, censored_word)
  return input_text

#print(censor_two(email_two, proprietary_terms))










