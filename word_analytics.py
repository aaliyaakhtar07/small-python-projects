#Word Analytics
def analyze_text(text):
    words = [word.strip('.,!?:;"()') for word in text.lower().split()]
    
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    
    unique_count = len(set(words))
    
    repeated_words = {word for word, count in word_count.items() if count > 1}
    
    palindromes = {word for word in set(words) 
                  if word.replace(' ', '') == word.replace(' ', '')[::-1]}
    
    return {
        'unique_count': unique_count,
        'repeated_words': sorted(repeated_words),
        'palindromes': sorted(palindromes)
    }
text = "Wow! Did Hannah see that Race car? Mom was there too. Hannah did see it!"
print(analyze_text(text))