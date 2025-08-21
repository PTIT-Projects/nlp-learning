from vncorenlp import VnCoreNLP
text = "Hôm nay là thứ Tư. Chúng tôi có tiết học về phân tích và xử lý dữ liệu văn bản. Tiết học khá thú vị tuy nhiên vẫn còn nhiều thứ chưa hiểu hết"
# https://github.com/vntk/dictionary/blob/master/data/Viet11K.txt

def read_dictionary(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]

def longest_matching(input_text, dictionary):
    max_word_len = max(len(word) for word in dictionary)
    words = []
    i = 0
    text_len = len(input_text)
    while i < text_len:
        matched = False
        # Skip spaces
        if input_text[i].isspace():
            i += 1
            continue
        # Try to match the longest word first
        for l in range(min(max_word_len, text_len - i), 0, -1):
            word = input_text[i:i + l]
            if word in dictionary:
                words.append(word)
                i += l
                matched = True
                break
        if not matched:
            # Collect consecutive unknown characters as one token
            start = i
            while i < text_len and not input_text[i].isspace():
                i += 1
            words.append(input_text[start:i])
    return words
def maximum_matching_tokenize(input_text, dictionary):
    max_word_len = max(len(word) for word in dictionary)
    words = []
    i = 0
    text_len = len(input_text)
    while i < text_len:
        if input_text[i].isspace():
            i += 1
            continue
        matched = False
        # Try to match the longest word first
        for l in range(min(max_word_len, text_len - i), 0, -1):
            word = input_text[i:i + l]
            if word in dictionary:
                words.append(word)
                i += l
                matched = True
                break
        if not matched:
            # Collect consecutive unknown characters as one token
            start = i
            while i < text_len and not input_text[i].isspace():
                # Stop if a substring matches the dictionary
                found = False
                for l in range(min(max_word_len, text_len - i), 0, -1):
                    if input_text[i:i + l] in dictionary:
                        found = True
                        break
                if found:
                    break
                i += 1
            words.append(input_text[start:i])
    return words

def removing_stopwords(words, dictionary):
    res = []
    for word in words:
        if word not in dictionary:
            res.append(word)
    return res
def main():
    dictionary = read_dictionary("dictionary/dict.txt")
    stop_words_dictionary = read_dictionary('dictionary/stop-words.txt')
    print("Longest matching")
    longest_matching_result = longest_matching(text, dictionary)
    print(longest_matching_result)
    print("==============================================")
    print("Maximum matching")
    maximum_matching_result = maximum_matching_tokenize(text, dictionary)
    print(maximum_matching_result)
    print("==============================================")
    print("Using VnCoreNLP")
    vncorenlp = VnCoreNLP("../VnCoreNLP/VnCoreNLP-1.2.jar")
    result = vncorenlp.annotate(text, annotators="wseg")
    tokenize_result = result['sentences']
    tokenize_result_list = []
    for result in tokenize_result:
        for word in result:
            tokenize_result_list.append(word['form'])
    print(tokenize_result_list)
    print("============================================")
    print("Start removing stopwords")
    print("Longest matching")
    print(removing_stopwords(longest_matching_result))
    print("==============================================")
    print("Maximum matching")
    print(removing_stopwords(maximum_matching_result))
    print("==============================================")
    print("Using VnCoreNLP")
    print(removing_stopwords(tokenize_result_list))

main()