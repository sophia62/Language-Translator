import csv
### Here I am going to import my CSV file. I have It set up into three columns. The first one being the subject, than the verb, than the object.
def read_categorized_translations(csv_filename):
    translations = {"subject": {}, "verb": {}, "object": {}}
    with open(csv_filename, "rt", encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  
        for row in reader:
            if len(row) == 3:  
                category, english, chinese = row
                # Here I am making sure that no matter what the person type then if it's capital or not it's fine
                if category.strip().lower() in translations:  
                    translations[category.strip().lower()][english.strip().lower()] = chinese.strip()
                    
            else:
                print(f"Skipping invalid row: {row}")  # Optionally log skipped rows for debugging
    return translations
# Here we will translate the sentence put in to match in SVO grammar.
def translate_svo(sentence, translations):
    words = sentence.split()
    chi_translated_parts = {'subject': '', 'verb': '', 'object': ''}
    eng_reconstruction = {'subject': '', 'verb': '', 'object': ''}

    for word in words:
        lower_word = word.lower()
        found = False
        for category in ['subject', 'verb', 'object']:
            if lower_word in translations[category]:
                chi_translated_parts[category] += translations[category][lower_word]  
                if not eng_reconstruction[category]:  # Preserve original case for English reconstruction
                    eng_reconstruction[category] = word
                found = True
                break
        if not found and not eng_reconstruction['object']: 
            eng_reconstruction['object'] += word

    chi_translated_sentence = ''.join(chi_translated_parts.values())
    eng_ordered = [eng_reconstruction['subject'], eng_reconstruction['verb'], eng_reconstruction['object']]
    eng_restructured_sentence = ' '.join(filter(None, eng_ordered)).strip()

    return chi_translated_sentence, eng_restructured_sentence

def main():
    translations = read_categorized_translations("/Users/sophiabeebe/Desktop/BYUI/Winter_2024/Programming_with_Fuctions/week_12final/translation.csv")  # Adjust the path as necessary
    while True:
        user_input = input("Enter an English sentence to translate (or type 'quit' to exit): ")
        if user_input.lower() == 'quit':
            break
        chi_translated_sentence, eng_restructured_sentence = translate_svo(user_input, translations)
        print("Translation:", chi_translated_sentence)
        print("English SVO:", eng_restructured_sentence)

if __name__ == "__main__":
    main()