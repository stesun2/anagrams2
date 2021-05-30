# Don't forget to run the tests (and create some of your own)

# NOT USING BUILT IN SORT METHOD
# Count the number of letter of occurence of given word using dictionary
# Compare the number of occurence in each string
# If the number of occurences matches the word store the matched word in a new list.
# Repeat until all words have been processed


def anagrams_for(word, list_of_words):
	# Convert all strings into lowercase
	word = word.lower()
	for i in list_of_words:
		list_of_words = i.lower()
		print(list_of_words)

	# print(word, list_of_words)
		# your code here

# print(anagrams_for("saltier"))
# anagrams_for("saltier", "cognac")
anagrams_for("saltier", ["cogNac", "SALTIER", "realist", "RETAILS"])
# anagrams_for("threads", ["threads", "trashed", "hardest", "hatreds"])