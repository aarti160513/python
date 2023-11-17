# pylint: disable=C0114
import locale

# Hello world mapping with IETF language tag as keys
hello_world_map = {
    'en': 'Hello World!',
    'fr': 'Bonjour le monde',
    'es': 'Hola Mundo',
    'ru': 'Привет, мир!',
    'de': 'Hallo Welt',
}
# enhancement - populate the dictionary using google translate API
# or read the mapping from a file (preferably yaml)

# mapping from language to IETF language tag
languages = {
    'english': 'en',
    'german': 'de',
    'french': 'fr',
    'russian': 'ru',
}


def tanslate_hello_world() -> str:
    '''
    Returns hello world in current locale.
        
        Returns:
              str: translated hello world
    '''
    # pylint: disable=W0612
    lang_country, encoding = locale.getlocale()

    # extract langauge and print Hello World in specific language
    if '_' in lang_country:
        lang = (lang_country.split('_')[0]).lower()
        try:
            return hello_world_map[lang]
        except KeyError:
            ietf_lang_code = languages[lang]
            return hello_world_map[ietf_lang_code]

    return "Hello World!"


if __name__ == "__main__":

    print(tanslate_hello_world())
