import requests
from bs4 import BeautifulSoup
import re
import sys
import codecs


def get_words_from_wiki(url, maximum):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    right_attrs = soup.find_all('a', href=re.compile(r'^/wiki'), title=True)
    w = [a.get_text() for a in right_attrs if a.get_text() == a['title']]
    return set(w[:maximum*2])


def find_most_unique(dicts):
    pass


def get_dicts():
    spanish_url = 'https://en.wiktionary.org/wiki/Wiktionary:Frequency_lists/Spanish1000'
    german_url = 'https://en.wiktionary.org/wiki/Wiktionary:Frequency_lists/German_subtitles_1000'
    french_url = 'https://en.wiktionary.org/wiki/Wiktionary:French_frequency_lists/1-2000'
    english_url = 'https://en.wiktionary.org/wiki/Wiktionary:Frequency_lists/PG/2006/04/1-10000'

    spanish_set = get_words_from_wiki(spanish_url, 100)
    german_set = get_words_from_wiki(german_url, 100)
    french_set = get_words_from_wiki(french_url, 100)
    english_set = get_words_from_wiki(english_url, 100)

    return {'English': english_set, 'French': french_set,
            'German': german_set, 'Spanish': spanish_set}


def get_text():
    sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
    sys.stdin = codecs.getwriter("utf-8")(sys.stdin.detach())
    t = sys.stdin.read().decode("utf-8", "strict")
    return t


def score(wl, d):
    l = len(wl)
    if l == 0:
        return 0
    found = 0
    for word in wl:
        if word in d:
            found += 1
    return float(found) / l


def language_scores(wl, d):
    scores = []
    for key, value in d.items():
        s = score(wl, value)
        scores.append((key, s))
    scores.sort(key=lambda x: x[1], reverse=True)
    return scores


def best_language(wl, d):
    s = language_scores(wl, d)
    return s[0][0]


def explicit_dicts():
    d = dict()
    d['Spanish'] = {'qué', 'tu', 'más', 'era', 'un', 'si', 'hay', 'puedo', 'he', 'su', 'para', 'estás', 'sus', 'nos', 'quiero', 'creo', 'ir', 'sabes', 'porque', 'él', 'esto', 'tienes', 'ser', 'quieres', 'dos', 'dónde', 'voy', 'nunca', 'pero', 'en', 'nada', 'sí', 'es', 'ha', 'o', 'como', 'por', 'casar', 'muy', 'favor', 'al', 'bueno', 'este', 'poder', 'eres', 'puede', 'está', 'y', 'todo', 'haber', 'una', 'saber', 'la', 'a', 'vez', 'eso', 'lo', 'cómo', 'bien', 'algo', 'soy', 'ahora', 'fue', 'hola', 'estoy', 'quién', 'con', 'mi', 'las', 'el', 'no', 'yo', 'esta', 'hacer', 'son', 'ya', 'del', 'sé', 'tiene', 'estar', 'creer', 'señor', 'ese', 'tengo', 'los', 'Wiktionary:Frequency lists', 'tanto', 'se', 'tan', 'vamos', 'todos', 'tú', 'aquí', 'de', 'gracias', 'casa', 'comer', 'tener', 'tiempo', 'dios', 'sólo', 'te', 'así', 'cuando', 'ella', 'querer', 'que', 'me', 'esa', 'le'}
    d['German'] = {'doch', 'kein', 'war', 'wissen', 'sich', 'muss', 'wie', 'schon', 'können', 'sind', 'die', 'auch', 'nichts', 'einen', 'hast', 'mit', 'sie', 'mich', 'bist', 'zu', 'nur', 'werden', 'aus', 'müssen', 'uns', 'dir', 'ich', 'es', 'da', 'immer', 'ein', 'dass', 'im', 'er', 'ihn', 'in', 'sein', 'von', 'jetzt', 'ist', 'hat', 'was', 'mehr', 'habe', 'ihr', 'Du', 'so', 'will', 'nicht', 'gut', 'ja', 'wollen', 'oh', 'eine', 'haben', 'kann', 'noch', 'Sie', 'dann', 'wieder', 'aber', 'mein', 'hier', 'an', 'und', 'um', 'dem', 'mir', 'wir', 'auf', 'man', 'bin', 'dich', 'für', 'mal', 'Wiktionary:Frequency lists', 'keine', 'nein', 'der', 'du', 'als', 'den', 'alles', 'wenn', 'meine', 'oder', 'wird', 'das', 'weiß', 'etwas', 'nach'}
    d['English'] = {'may', 'things', 'face', 'himself', 'left', 'again', 'love', 'to', 'she', 'any', 'place', 'said', 'here', 'their', 'he', 'though', 'went', 'set', 'than', 'whom', 'we', 'make', 'against', 'shall', 'might', 'this', 'our', 'like', 'know', 'through', 'each', 'have', 'come', 'put', 'always', 'while', 'its', 'of', 'if', 'other', 'am', 'or', 'her', 'did', 'some', 'Mrs', 'say', 'go', 'work', 'time', 'part', 'away', 'long', 'good', 'little', 'my', 'what', 'as', 'people', 'must', 'once', 'never', 'three', 'out', 'on', 'old', 'into', 'called', 'in', 'that', 'own', 'head', 'which', 'great', 'many', 'years', 'took', 'heart', 'such', 'how', 'was', 'could', 'def', 'way', 'more', 'his', 'over', 'upon', 'these', 'first', 'give', 'few', 'for', 'is', 'us', 'with', 'can', 'both', 'they', 'hand', 'a', 'back', 'there', 'at', 'so', 'would', 'will', 'take', 'because', 'off', 'it', 'one', 'too', 'yet', 'where', 'ever', 'got', 'right', 'then', 'made', 'before', 'are', 'even', 'thought', 'thing', 'about', 'two', 'new', 'me', 'day', 'been', 'came', 'after', 'still', 'no', 'not', 'see', 'who', 'far', 'an', 'found', 'looked', 'world', 'the', 'think', 'much', 'night', 'had', 'now', 'without', 'down', 'saw', 'be', 'up', 'nothing', 'well', 'all', 'man', 'just', 'but', 'being', 'do', 'seemed', 'another', 'between', 'Wiktionary:Frequency lists', 'every', 'king', 'men', 'them', 'should', 'mind', 'those', 'from', 'get', 'were', 'by', 'life', 'de', 'also', 'god', 'you', 'house', 'under', 'whole', 'last', 'only', 'i', 'same', 'and', 'most', 'Mr', 'him', 'young', 'when', 'your', 'tell', 'has', 'eyes', 'very'}
    d['French'] = {'faut', 'partie', 'je', 'Wiktionary:French frequency lists', 'moins', 'millions', 'un', 'si', 'taux', 'premier', 'entreprises', 'hausse', 'cours', 'leurs', 'vers', 'place', 'par', 'faire', 'pourrait', 'cas', 'jour', 'sur', 'également', 'société', 'bénéfice', 'va', 'reste', 'nouvelle', 'deux', 'ce', 'une', 'mais', 'pour', 'pays', 'autre', 'vente', 'elle', 'entre', 'dans', 'nos', 'toute', 'ses', 'il', 'certains', 'devrait', 'peuvent', 'rapport', 'ainsi', 'nous', 'avait', 'avoir', "d'", 'les', 'lors', "d'une", 'part', 'politique', 'tout', 'en', 'baisse', 'Bourse', 'celui', 'est', 'on', 'avec', 'cela', 'fin', 'travail', "c'", 'votre', 'niveau', 'lui', 'qui', 'grande', 'sous', 'dont', 'L', 'exemple', "s'", 'bon', 'francs', 'mieux', 'Elle', 'année', 'effet', 'y', 'trois', 'ne', 'été', 'compte', 'leur', 'quelques', 'nouveau', 'tous', 'grand', 'la', 'a', 'chaque', 'F', 'était', 'personnes', 'qualité', 'bien', 'mois', 'nombre', 'et', 'pas', 'marché', 'point', 'terme', 'quelque', 'Belgique', 'avant', "qu'", 'milliards', 'sa', 'vie', 'toutes', 'ont', 'souvent', 'cette', 'd', 'fait', 'doit', 'contre', 'USD', 'peut', "aujourd'hui", 'A', 'sans', 'ces', 'plusieurs', 'son', 'aussi', 'années', 'soit', 'ou', 'alors', 'résultat', 'des', 'l', "l'on", 'fonds', 'ans', 'ils', 'vous', 'beaucoup', 'permet', 'comme', 'trop', 'risque', 'temps', 'chez', 'toujours', 'se', 'belge', 'peu', 'depuis', 'BEF', 'monde', 's', 'sont', 'de', 'France', 'autres', 'plus', 'au', 'action', 'fois', 'du', 'sera', 'donc', 'prix', 'produits', 'surtout', 'non', 'produit', 'début', 'base', 'chiffre', 'encore', 'banque', 'cet', 'production', 'Bruxelles', 'croissance', 'secteur', 'rien', 'aux', 'que', 'notre', 'dernier', 'jamais', 'le', 'groupe', 'valeur'}
    return d


def hacker_rank():
    my_dicts = explicit_dicts()
    text = get_text()
    print(best_language(text.split(), my_dicts))


def test():
    my_dicts = explicit_dicts()
    text_english = "The story of Rip Van Winkle is set in the years before and after the American Revolutionary War. In a pleasant village, at the foot of New York's Catskill Mountains, lives kindly Rip Van Winkle, a Dutch villager. Van Winkle enjoys solitary activities in the wilderness, but he is also loved by all in town—especially the children to whom he tells stories and gives toys. However, he tends to shirk hard work, to his nagging wife's dismay, which has caused his home and farm to fall into disarray. One autumn day, to escape his wife's nagging, Van Winkle wanders up the mountains with his dog, Wolf. Hearing his name called out, Rip sees a man wearing antiquated Dutch clothing; he is carrying a keg up the mountain and requires help."
    text_german = "Der Mann hatte einen Bart und war schon etwas älter; zu alt fast für die Frau.Und dann war auch noch das Kind da, ein ganz kleines.Das schrie dauernd, denn es hatte Hunger. Auch die Frau hatte Hunger. Aber sie war still, und wenn der Mann zu ihr hinsah, dann lächelte sie; oder sie versuchte es doch wenigstens. Der Mann hatte auch Hunger. Sie wussten nicht, wohin sie wollten; sie wussten nur, sie konnten in ihrer Heimat nicht bleiben, sie war zerstört. Sie liefen durch Wald, durch Kiefern. In denen knisterte es. Sonst war es still.Beeren oder Pilze gab es nicht; die hatte die Sonne verbrannt. Über den Schneisen flackerte Hitze. Das bisschen Wind wehte nur oben.Es war für den Bussard gut; Reh und Hase lagen hechelnd im Farn."
    print(language_scores(text_english.split(), my_dicts))
    print(language_scores(text_german.split(), my_dicts))

if __name__ == '__main__':
    hacker_rank()
