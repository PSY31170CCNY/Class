tweet_string = "Thanks to the historic TAX CUTS that I signed into law, your paychecks are going way UP, your taxes are going way DOWN, and America is once again OPEN FOR BUSINESS!"
tweet_words = tweet_string.split()
number_of_words = len(tweet_words)

number_of_good_words = 0
number_of_bad_words = 0

good_words = ["Thanks", "historic", "paychecks"]
bad_words = ["taxes"]

# Iterate through the words in the tweet string
for w in tweet_words:
    print(w)
    if w in good_words:
        number_of_good_words += 1  # same as writing number_of_good_words = number_of_good_words + 1
    elif w in bad_words:
        number_of_bad_words += 1

print ("There are " + str(number_of_good_words) + " good words in this tweet")
print ("There are " + str(number_of_bad_words) + " bad words in this tweet")

if number_of_good_words > number_of_bad_words:
    print ("Go back to Puerto Rico")
else:
    print ("Taking Trump out will be the beginning of the end for the left.!")
