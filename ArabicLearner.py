
import time
import random

ARABIC_ALPHABET = [
    ("ا", "alif", "ah-leef"),
    ("ب", "ba", "bah"),
    ("ت", "ta", "tah"),
    ("ث", "tha", "thah"),
    ("ج", "jim", "jeem"),
    ("ح", "ha", "hah"),
    ("خ", "kha", "khah"),
    ("د", "dal", "dahl"),
    ("ذ", "dhal", "dhahl"),
    ("ر", "ra", "rah"),
    ("ز", "zay", "zay"),
    ("س", "sin", "seen"),
    ("ش", "shin", "sheen"),
    ("ص", "sad", "sahd"),
    ("ض", "dad", "dahd"),
    ("ط", "ta", "tah"),
    ("ظ", "za", "zah"),
    ("ع", "ayn", "ah-yin"),
    ("غ", "ghayn", "ghah-yin"),
    ("ف", "fa", "fah"),
    ("ق", "qaf", "kaf"),
    ("ك", "kaf", "kaf"),
    ("ل", "lam", "lahm"),
    ("م", "mim", "meem"),
    ("ن", "nun", "noon"),
    ("ه", "ha", "hah"),
    ("و", "waw", "wow"),
    ("ي", "ya", "yah")
]

ARABIC_WORDS = {
    "مَاء": ("water", "maa'"),
    "كَتَبَ": ("he wrote", "kataba"),
    "رَجُل": ("man", "rajul"),
    "جَمِيل": ("beautiful", "jamiil"),
    "بَيْت": ("house", "bayt"),
    "طَاوِلَة": ("table", "taawilah"),
    "سَيَّارَة": ("car", "sayyaarah"),
    "حَاسُوب": ("computer", "haasuub"),
    "قَطَّة": ("cat", "qittah"),
    "كِتَاب": ("book", "kitaab"),
    "سَمَاء": ("sky", "samaa'"),
    "شَمْس": ("sun", "shams"),
    "هَاتِف": ("phone", "haatif"),
    "شَجَرَة": ("tree", "shajarah"),
    "حَرْف": ("letter", "harf"),
    "شَمْعَة": ("candle", "shama'ah"),
    "قَلَم": ("pen", "qalam"),
    "فَنْجَان": ("cup", "fanjaan"),
    "جَرَيْدَة": ("newspaper", "jarayidah"),
    "صَبَاح": ("morning", "sabaaH"),
    "عَصَر": ("afternoon", "aSar"),
    "مَسَاء": ("evening", "masaa'"),
    "لَيْل": ("night", "layl"),
    "قَمِيص": ("shirt", "qamiis"),
    "فُستَان": ("dress", "fustaan"),
    "حِذَاء": ("shoe", "hiDHa'"),
    "جَوَّال": ("mobile phone", "jawwaal"),
    "مَطْبَخ": ("kitchen", "matbakh"),
    "مَجْلَس": ("living room", "majlis"),
    "غُرْفَة نَوْم": ("bedroom", "ghurfah nawm"),
    "حَمَّام": ("bathroom", "hammaam"),
    "تِلِفِزْيُون": ("television", "tilifizyuun"),
    "طَقْم أَسْنَان": ("toothbrush", "Taqm asnaan"),
    "مِصْلَاة": ("mosque", "miSlaah"),
    "كَعْب": ("heel", "ka'b"),
    "أُذُن": ("ear", "uDhun"),
    "عَيْن": ("eye", "ayn"),
    "أَنْف": ("nose", "anf"),
    "فَم": ("mouth", "fam"),
    "شَعْر": ("hair", "sha'r"),
    "رَأْس": ("head", "ra's"),
    "يَد": ("hand", "yad"),
    "سَاعَة": ("watch/clock", "saa'ah"),
    "حَذَاء": ("boot", "HaDHa'"),
    "صَحْن": ("plate", "SaHn"),
    "خِدَاج": ("glass", "khidaaj"),
    "قَنِّينَة": ("bottle", "qanniinah"),
    "مِفْتَاح": ("key", "miftaah"),
    "مِلْعَقَة": ("spoon", "mil'aqah"),
    "شَوْكَة": ("fork", "shawkah"),
    "سِكِّين": ("knife", "sikkiiN"),
    "صَابُون": ("soap", "Saabuun"),
    "مَعْجُون أَسْنَان": ("toothpaste", "ma'juun asnaan"),
    "مِنْشَفَة": ("towel", "minshafah"),
    "مَنْظَار": ("telescope/binoculars", "manDhaar"),
    "قِمَّة": ("summit", "qimah"),
    "عُنُق": ("neck", "unuq"),
    "أَصَابِع القَدَم": ("toes", "asaabi' alqadam"),
    "شَمْسِيَّة": ("sunglasses", "shamsiyyah"),
    "نَظَّارَة": ("eyeglasses", "naZZaarah"),
    "كَرِسِيُّ الْمَكْتَب": ("office chair", "karisiyyu almaktab"),
    "فَرْشَة": ("brush", "farshah"),
    "فَرَاشَة": ("butterfly", "faraashah"),
    "جَرَادَة": ("grasshopper", "jaraadah"),
    "فَأْر": ("mouse", "fa'r"),
    "كَلْب": ("dog", "kalb"),
    "خَنْزِير": ("pig", "khanziir"),
    "بَقَرَة": ("cow", "baqarah"),
    "فَأْرَة الحَاسُوب": ("computer mouse", "fa'ratu alhaasuub"),
    "سَمَك": ("fish", "samak"),
    "فَرَاش": ("mattress", "farash"),
    "تُرَمَّة": ("pomegranate", "turammah"),
    "تِفَاح": ("apple", "tifaaH"),
    "بُرْتُقَال": ("orange", "burTuqaal"),
    "لَيْمُون": ("lemon", "laymuun"),
    "فَرَاوَل": ("strawberry", "faraawal"),
    "تُمْر": ("dates", "tumr"),
    "فَاكِهَة": ("fruit", "fakiHah"),
    "خُضْرَة": ("vegetables", "khudrah"),
    "جَزَر": ("carrot", "jazar"),
    "بَصَل": ("onion", "basaal"),
    "ثَوْم": ("garlic", "thawm"),
    "شَمْنْدَر": ("beetroot", "shamindar"),
    "فَاصُولِيَا": ("green beans", "faSuuliyyah"),
    "خِيَار": ("cucumber", "khiyaar"),
    "بَطَاطَا": ("potato", "bataata"),
    "طَمَاطِم": ("tomato", "TamaaTim"),
    "كَرْفَس": ("celery", "karfas"),
    "فُول": ("fava beans", "ful"),
    "كُوسَا": ("zucchini", "kuusa"),
    "لُوْبِيَاء": ("black-eyed peas", "lubiyaa"),
    "فِرْنَان": ("eggplant", "firnaan"),
    "جَوْز الهِنْد": ("coconut", "jawz alhind"),
    "بَنَان": ("banana", "banaan"),
    "كَمْثَرَى": ("pear", "kamtharaa"),
    "عِنَب": ("grapes", "inab"),
    "رُمَّان": ("pomegranate", "rummaan"),
    "تِين": ("fig", "tiin"),
    "لَوْز": ("almond", "lawz"),
    "كَاجُو": ("cashew", "kaaju"),
    "فِسْتُوق": ("pistachio", "fistuuq"),
    "مَكَادَيْمْيَا": ("macadamia", "makaadaymyaa"),
    "مَانْجَا": ("mango", "maanja"),
    "جَوْز": ("walnut", "jawz"),
    "عِين الجَمَل": ("camel's milk", "ein aljamal"),
    "حَلِيب": ("milk", "Haliib"),
    "لَبَن": ("yogurt", "laban"),
    "جُبْن": ("cheese", "jubn"),
    "زَبَدَة": ("butter", "zabada"),
    "زَيْتُون": ("olive oil", "zaytuun"),
    "سَكَّر": ("sugar", "sakkar"),
    "مِلْح": ("salt", "milH"),
    "فَلْفَل": ("pepper", "filfil"),
    "كُمُّون": ("cumin", "kummun"),
    "كُرْكُم": ("turmeric", "kurkum"),
    "زَعْفَرَان": ("saffron", "za'faraan"),
    "قِرْفَة": ("cinnamon", "qirfaH"),
    "كَزْبَرَة": ("coriander", "kazbara"),
    "شَبْت": ("dill", "shabt"),
    "نَعْنَاع": ("mint", "na'nā'"),
    "خَرْدَل": ("mustard", "khurdal"),
    "خَمِيرَة": ("yeast", "khameerah"),
    "مِرْقَة": ("broth/stock", "mirqah"),
    "شَورْبَة": ("soup", "shurbaH"),
    "بَسْلَة": ("pea", "baslah"),
    "جَزَر مَبْشُور": ("grated carrot", "jazar mabshuur"),
    "سَلَطَة": ("salad", "salata"),
    "خُبْز": ("bread", "khobz"),
    "عَيْش": ("bread", "aysh"),
    "فَطِيرَة": ("pie", "fatirah"),
    "كَعْك": ("cookie/cake", "ka'k"),
    "كُنَافَة": ("Kunafa (sweet cheese pastry)", "kunafah"),
    "بَقْلاَوَة": ("baklava", "baqlawah"),
    "كَبْكَة": ("Kabka (sweet cheese pastry)", "kabkah"),
    "هُمُّوْس": ("hummus", "hummuus"),
    "بَابَا غَنُوْج": ("Baba Ghanoush (eggplant dip)", "baba ghannuuj"),
    "فَتَوْش": ("Fattoush (bread salad)", "fattuush"),
    "طَحِينَة": ("tahini", "Tahiinah"),
    "زَعْتَر": ("za'atar (spice blend)", "za'tar"),
    "بَسْبُوسَة": ("basbousa (semolina cake)", "basbuusa"),
    "مَمُوْل": ("ma'amoul (date-filled cookie)", "ma'muul"),
    "حَلاَوَة": ("halva (sweet)", "Halawa"),
    "مَعْكَروْنَة": ("pasta", "ma'karonah"),
    "رُز": ("rice", "ruz"),
    "كُسْكُس": ("couscous", "kuskuus"),
    "فَرِيْكَة": ("freekeh (roasted green wheat)", "fariikah"),
    "حَمُّص": ("chickpeas", "Hammus"),
    "عَدِس": ("lentils", "adis"),
    "فَاصُولِيَا بَيْضَاء": ("white beans", "faSuuliyyah bayDa'"),
    "فَاصُولِيَا حَمْرَاء": ("red beans", "faSuuliyyah Hamaaraa"),
    "فَاصُولِيَا سَّودَاء": ("black beans", "faSuuliyyah sauda'"),
    "جَوْز الطَّيْب": ("nutmeg", "jawz aTTayb"),
    "هَيل": ("cardamom", "hayl"),
    "جِنْزَبِيل": ("ginger", "jinzebeel"),
    "شَمَّر": ("fennel", "shammar"),
    "كُرْفَس": ("celery", "kurfaas"),
    "حَبَّة سَوْدَاء": ("black seed", "habbat sawdaa'"),
    "عَسَل": ("honey", "'asal"),
    "زَهْرَة اللَّوْز": ("orange blossom", "zahrat al-lawz"),
    "عُود الثَّنَّاء": ("sandalwood", "ood ath-thanna'"),
    "خَشَب الأُرُز": ("cedarwood", "khushab al-'arz"),
    "عَطَر": ("perfume", "aTir"),
    "صَابُون": ("soap", "Saabuun"),
    "شَامْبُو": ("shampoo", "shampoo"),
    "زُبَدَة الشَّيْا": ("shea butter", "zubadat ash-shayaa"),
    "أَبْرِيق": ("teapot", "abriiq"),
    "فِنْجَان": ("cup", "finjaan"),
    "صَحْن": ("plate", "sahhn"),
    "كَوْب": ("glass", "kob"),
    "سِكِّيْن": ("knife", "sikkiin"),
    "شَوْكَة": ("fork", "shawkah"),
    "مَلْعَقَة": ("spoon", "mal'aqah"),
    "صَحْن التَّقْديْم": ("serving platter", "sahhn at-taqdiim"),
    "مَلْحَقَات الطَّعَام": ("utensils", "malHaqaat at-ta'aam"),
    "غَرْفَة الطَّعَام": ("dining room", "ghurfat at-ta'aam"),
    "مَطْبَخ": ("kitchen", "matbakh"),
    "ثَلَّاجَة": ("refrigerator", "thallajah"),
    "مِيْزَان": ("scale", "mizaan"),
    "فُرْن": ("oven", "furn"),
    "مِقْلاَة": ("frying pan", "miqlaah"),
    "طَاسَة": ("pot", "taasah"),
    "غَلاَّيَة": ("teakettle", "ghallayyah"),
    "شَاي": ("tea", "shay"),
    "قَهْوَة": ("coffee", "qahwah"),
    "مَاء": ("water", "maa'"),
    "لَيْمُون": ("lemon", "laymuun"),
    "تُفَّاح": ("apple", "tuffaah"),
    "كُمَّثْرَى": ("pear", "kummithrah"),
    "مَوْز": ("banana", "mawz"),
    "جَوَّافَة": ("guava", "jawwaafa")
}


def intro():
    print("Welcome to the Arabic reading program by Modib Qadir!")
    time.sleep(2)
    print("In this program, you will learn the basics of reading Arabic, including the alphabet and basic vocabulary words.")
    time.sleep(2)
    print("Hopefully by the end of this program, you will be able to read the Quran and gain a deeper understanding of Islam.")
    time.sleep(2)
    print()

def print_letter(index):
    if index >= len(ARABIC_ALPHABET):
        return
    arabic_letter, english_name, english_pronunciation = ARABIC_ALPHABET[index]
    print(f"Here is the letter {arabic_letter} ({english_name}).")
    print(f"Now, try to pronounce it out loud: {english_pronunciation}.")
    time.sleep(1)
    print("Great job! Let's move on to the next letter.")
    time.sleep(2)
    print()
    print_letter(index+1)

def arabic_alphabet():
    print("Let's start with the Arabic alphabet.")
    print("There are 28 letters in the Arabic alphabet.")
    time.sleep(2)
    print("I'll show you each letter and its pronunciation in English. Try to repeat after me!")
    print()
    print_letter(0)
    print("That's the end of the Arabic alphabet! Well done.")
    print()

def arabic_word_basic():
    print("Here are some basic Arabic words:")
    while True:
        words = random.sample(list(ARABIC_WORDS.items()), 5)
        for arabic_word, english_translation in words:
            print(f"{arabic_word} - {english_translation}")
            time.sleep(1)
        print()
        choice = input("Press 'n' for a new set of words or any other key to continue: ")
        print()
        if choice != 'n':
            break
        print("Here are more basic Arabic Words:")

def english_to_arabic():
    while True:
        eng_word = input("Enter an English word (or 'exit' to quit): ")
        if eng_word == 'exit':
            break
        translator = Translator()
        translation = translator.translate(eng_word, dest="ar")
        ar_word = translation.text
        en_pronunciation = translation.pronunciation
        print(f"The Arabic translation of '{eng_word}' is '{ar_word}', pronounced in English as '{en_pronunciation}'.")
        print()
    
# Add more functions for teaching pronunciation, etc.

def main():
    intro()
    print("Please choose what you want to learn:")
    while True:
        print("1. Learn the Arabic Alphabet")
        print("2. Learn Basic Arabic Words")
        print("3. Translate English to Arabic")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")
        print()
        if choice == "1":
            arabic_alphabet()
        elif choice == "2":
            arabic_word_basic()
        elif choice == "3":
            english_to_arabic()
        elif choice == "4":
            print("Thank you for learning!")
            break
        else:
            print("Invalid choice. Please try again.")
    print()

if __name__ == "__main__":
    main()
