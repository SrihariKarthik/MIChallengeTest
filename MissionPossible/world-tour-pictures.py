"""Python Code to Store a text into an Image and Extracting it using the LSB library """
from stegano import lsb

from googletrans import Translator


def secret(image, output, text):
    """Function to hide the text in an Image using the LSB library"""
    img = lsb.hide(image, text)
    img.save(output)


def reveal(image):
    """Function to reveal the text hidden in the Image using LSB Library"""
    hiddentext = lsb.reveal(image)
    ListofHiddenText.append(hiddentext)
    return ListofHiddenText

#List to Store the Path of the Images, required to Hide the Text
ListofImages = [
    "Non Hidden Pictures/PlainPicture1.png",
    "Non Hidden Pictures/PlainPicture2.png",
    "Non Hidden Pictures/PlainPicture3.png",
    "Non Hidden Pictures/PlainPicture4.png",
    "Non Hidden Pictures/PlainPicture5.png",
]
#List to Store the Path of the Output Images which Contain the Hidden Text
ListofEncrypted = [
    "Picture1.png",
    "Picture2.png",
    "Picture3.png",
    "Picture4.png",
    "Picture5.png",
]
#List to Store the Text that needs to be Hidden in the Image
ListofText = [
    "Painting and Fashion",
    "Great Technology",
    "Ancient Ruins",
    "Culture and Heritage",
    "The Silicon Valley",
]

# Initializing a List to store the Text hidden in the Five Pictures
ListofHiddenText = []

for idx,data in enumerate(ListofImages):
    secret(ListofImages[idx], ListofEncrypted[idx], ListofText[idx])


# Iterarting through the Pictures having hidden text and revealing the hidden text
for i in ListofEncrypted:
    reveal(i)
# Printing out the List which holds the hidden text
print(ListofHiddenText)

# Creating an Instance of the Translator class
translator = Translator()

# Creating a List to Store the Transalated Text
ListofTranslated = []
# Creating a List to Store the Language the Text needs to be Translated to
ListofLang = ["fr", "ja", "it", "ms", "en"]

# Iterating through the List of Hidden Text and translating into the specified Language
for idx,data in enumerate(ListofHiddenText):
    TranslatedText = translator.translate(ListofHiddenText[idx], dest=ListofLang[idx])
    ListofTranslated.append(TranslatedText.text)


# Creating a String to Store the Transalated Text in Order Seperated by an '_'
RESULT = ""

for i in ListofTranslated:
    RESULT += i.lower()
    if i != ListofTranslated[-1]:
        RESULT += "_"


print(f"This is the Translated Hidden Text : {RESULT}")
