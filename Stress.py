class Character:
    # The set of recognized vowels
    vowels = ['a', 'ɑ', 'æ', 'ɐ', 'ɑ̃',
            'e', 'ə', 'ɚ', 'ɵ', 
            'ɛ', 'ɜ', 'ɝ', 'ɛ̃',
            'i', 'ɪ', 'ɨ', 'ɪ̈',
            'o', 'ɔ', 'œ', 'ɒ', 'ɔ̃',
            'ø',
            'u', 'ʊ', 'ʉ']
    # The set of recognized consonants/consonant parts
    consonants = [['b', 'β', 'ɓ',
                'c', 'ç', 'ɕ',
                'd', 'ð', 'ɗ', 'ɖ',
                'f', 
                'g', 'ɠ', 'ɢ',
                'h', 'ħ', 'ɦ', 'ɥ', 'ɧ', 'ʜ',
                'j', 'ʝ', 'ɟ',
                'k', 
                'l', 'ɫ', 'ɭ', 'ɬ', 'ʟ', 'ɮ',
                'm', 'ɱ',
                'n', 'ŋ', 'ɲ', 'ɳ', 'ɴ',
                'p', 'ɸ',
                'q', 
                'r', 'ɾ', 'ɹ', 'ʁ', 'ʀ', 'ɻ', 'ɽ',
                's', 'ʃ', 'ʂ',
                't', 'θ', 'ʈ',
                'v', 'ʌ', 'ʋ',
                'w', 'ɯ', 'ʍ',
                'x', 'χ',
                'y', 'ɣ', 'ʎ', 'ʏ', 'ɤ',
                'z', 'ʒ', 'ʐ', 'ʑ'],
                ['d͡ʒ',  
                't͡ʃ', 't͡s']]
    # Returns True if input is a vowel, False otherwise
    def is_vowel(a):
        return a in Character.vowels
    # Returns True if input is a consonant, False otherwise
    def is_consonant(b):
        return b in Character.consonants[0]
    # Returns True if input is a string of multiple characters to be considered one consonant part
    def is_binded_consonant(bcd):
        return bcd in Character.consonants[1]
    
class Syllable:
    # Returns True if the syllable has a coda, False otherwise, to determine whether the final syllable is stressed
    def is_heavy(syllable):
        return (len(syllable) > 1 and Character.is_consonant(syllable[len(syllable)-1])) or (len(syllable) > 3 and Character.is_binded_consonant(syllable[len(syllable)-3:]))
    # Returns the input content as an array of syllable strings
    def to_syllables(string):
        syllables = []
        syllable_indices = []
        # Identifies each vowel or consecutive vowels as a nucleus
        for i in range(len(string)):
            if Character.is_vowel(string[i]):
                if i == 0 or (i >= 1 and Character.is_consonant(string[i-1])) or (i >= 3 and Character.is_binded_consonant(string[i-3:i])):
                    syllables += string[i]
                    syllable_indices += [i]
                else:
                    syllables[len(syllables)-1] += string[i]
        # Appends onsets and codas to the nucleus
        for i in range(len(syllable_indices)):
            index = syllable_indices[i]
            if index >= 3 and Character.is_binded_consonant(string[index-3:index]):
                syllables[i] = string[index-3:index+1]
            elif index >= 1 and Character.is_consonant(string[index-1]):
                syllables[i] = string[index-1:index+1]
            if index + 3 < len(string) and Character.is_binded_consonant(string[index+1:index+4]):
                if not (index + 4 in syllable_indices) or index + 4 >= len(string):
                    syllables[i] = syllables[i] + string[index+1:index+4]
            elif index + 1 < len(string) and Character.is_consonant(string[index+1]):
                if not (index + 2 in syllable_indices) or index + 2 >= len(string):
                    syllables[i] = syllables[i] + string[index+1]
        return syllables
    # Returns an array of the input syllables with stress information
    def to_syllables_stress(syllables):
        syllables_stress = []
        for syllable in syllables:
            syllables_stress += [[syllable,"undetermined"]]
        for i in range(len(syllables)):
            if i % 2 == 0:
                if i == 0:
                    syllables_stress[i][1] = "primary"
                elif i != len(syllables) - 1 or Syllable.is_heavy(syllables[i]):
                    syllables_stress[i][1] = "secondary"
                else:
                    syllables_stress[i][1] = "unstressed"
            else:
                syllables_stress[i][1] = "unstressed"
        return syllables_stress
    # Prints the syllables with stress information together as a word
    def print_syllables_stress(syllables_stress):
        for i in range(len(syllables_stress)):
            match syllables_stress[i][1]:
                case 'primary':
                    print("ˈ" + syllables_stress[i][0], end="")
                case 'secondary':
                    print("ˌ" + syllables_stress[i][0], end="")
                case 'unstressed':
                    print(syllables_stress[i][0], end="")

def main():
    string = input("Please enter a word: ")
    syllables = Syllable.to_syllables(string)
    syllables_stress = Syllable.to_syllables_stress(syllables)
    Syllable.print_syllables_stress(syllables_stress)
    
main()