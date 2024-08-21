from bs4 import BeautifulSoup
import requests
import time

def print_wotd():
    
    english_text = requests.get('https://www.merriam-webster.com/word-of-the-day').text
    soup = BeautifulSoup(english_text, 'lxml')

    english_word = soup.find('h2', class_ = 'word-header-txt').text
    word_class = soup.find('span', class_ = 'main-attr').text
    definition_section = soup.find('div', class_ = 'wod-definition-container')
    word_definition = definition_section.find('p').text.strip()
    example_sentence = definition_section.find('p').find_next_sibling('p').text.strip().replace('//', '')

    print(f'Word of the day is {english_word}, it is a {word_class}. Its definition is: {word_definition} An example of {english_word} used in a sentence:{example_sentence}')
    
if __name__ == '__main__':
    while True:
        print_wotd()
        time.sleep(86400)
        print("\nProgram in sleep mode for 24h...")