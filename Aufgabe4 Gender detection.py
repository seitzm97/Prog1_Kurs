def text_to_list(text):
    word_list = list(text.split(" "))
    return word_list

def word_counter(text_to_analyze):
    total_count = text_to_analyze.count(" ")
    return total_count

def sentence_counter(text_to_analyze):
    total_count = text_to_analyze.count(".")
    return total_count

def avg_words_per_sen(counted_words, counted_sentences):
    avg_words = counted_words / counted_sentences
    return avg_words

def pronoun_counter(list_of_words):
    cap_me_count = list_of_words.count("Me")
    me_count = list_of_words.count("me")
    I_count = list_of_words.count("I")
    my_count = list_of_words.count("my")
    cap_my_count = list_of_words.count("My")
    count_of_pronouns = cap_me_count + me_count + I_count + cap_my_count + my_count
    return count_of_pronouns

def hedgephrase_counter(text_to_analyze):
    ithink_count = text_to_analyze.count("I think")
    ibelieve_count = text_to_analyze.count("I believe")
    count_of_hedgephrases = ithink_count + ibelieve_count
    return count_of_hedgephrases

def gender_detection(avg_hedge_pronouns):
    if avg_hedge_pronouns >= 2:
        result = ("The autor is likely female.")
    else:
        result = ("The autor is likely male.")
    return result

text_to_analyze = input("Enter text you would like to analyse:")

list_of_words = text_to_list(text_to_analyze)
counted_words = word_counter(text_to_analyze)
counted_pronouns = pronoun_counter(list_of_words)
counted_hedgephrases = hedgephrase_counter(text_to_analyze)
avg_hedge_pronouns = (counted_hedgephrases + counted_pronouns) / counted_words
counted_sentences = sentence_counter(text_to_analyze)
avg_words = avg_words_per_sen(counted_words, counted_sentences)
gender_detected = gender_detection(avg_hedge_pronouns)


print("There are",counted_pronouns, "pronouns in this text.")
print("There are",counted_hedgephrases, "hedgephrases in this text")
print("There are",counted_words, "Words in this text.")
print("There are", counted_sentences, "sentences in this text.")
print("There is an average of", avg_words, "words per sentence.")
print(gender_detected)

