
class Solution:

    def parsing_words(self, word):
        current_word = ""
        letter_dict = {}
        word_count = {}
        for c in 'abcdefghijklmnopqrstuvwxyz':
            letter_dict[c] = 0
        for i in range(len(word)):
            current_letter = word[i]
            if current_letter.isspace():
                if current_word:
                    if current_word not in word_count:

                         
                        word_count[current_word] = 0
                    word_count[current_word] += 1
                    current_word = ""

            if not current_letter.isalpha():
                continue
            if not current_letter.islower():
                continue
            letter_dict[current_letter] += 1
            current_word += current_letter
        if current_word :
            if current_word not in word_count:
                word_count[current_word] = 0
            word_count[current_word] += 1


        print(letter_dict)
        print(word_count)
        return



sol = Solution()
print(sol.parsing_words("asd asdjl io &*& a9s8kkkd79 a98ffhs7d& anbsd 21f3 adsd asd"))