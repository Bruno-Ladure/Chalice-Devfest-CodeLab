# -*- coding: utf-8 -*-​
import random

_CITATIONS = [
    (
        'Kurt Cobain',
        'Vouloir être quelqu’un d’autre c’est gâcher la personne que vous êtes.',
    ),
    (
        'Jim Morrisson',
        'Confrontes-toi à ta peur la plus profonde ; après cela, '
        'la peur n’a plus de pouvoir, et la peur de la liberté '
        's’éloigne et disparaît. Tu es libre.',
    ),
    (
        'Bob Dylan',
        'Celui qui n’est pas occupé à naître est occupé à mourir.',
    ), (
        'Jimi Hendrix',
        'La connaissance parle, mais la sagesse écoute',
    ),
    (
        'Paul McCartney',
        'J’avais l’habitude de penser que tous ceux qui font des choses bizarres '
        'sont bizarres. Maintenant, je sais que ce sont les personnes qui en '
        'appellent d’autres bizarres qui sont bizarres.',
    ),
    (
        'Frank Zappa',
        'Je n’ai jamais cherché à être bizarre. C’est toujours les autres qui '
        'm’ont qualifié de bizarre.',
    ),
    (
        'John Lennon',
        'Si tout le monde souhaitait la paix plutôt qu’une autre télé, '
        'alors il y aurait la paix.',
    ),
    (
        'Keith Richards',
        'Au départ, le peintre a une toile. L’écrivain a une feuille de papier. '
        'Le musicien, lui, a le silence.',
    ), (
        'Ted Nugent',
        'Si c’est trop fort, c’est que vous êtes trop vieux.',
    ),
    (
        'Lemmy Kilmister',
        'Je n’ai pas de regrets. Les regrets sont inutiles. '
        'Il est trop tard pour les regrets. Ce qui est fait est fait. '
        'Vous avez vécu votre vie. Cela n’a aucun sens de vouloir la changer.',
    ),
    (
        'Chuck Berry',
        'Je ne suis pas le roi du rock’n’roll, mais jCen suis le Premier ministre.'
    ),
    (
        'John Lennon',
        'Si vous cherchez un autre nom à donner au rock’n’roll, vous devez l’appeler Chuck Berry.'
    ),
    (
        'Elvis Presley',
        'Let’s Rock !.'
    ),
    (
        'Elvis Presley',
        'Le rock and roll existe depuis un moment. Avant, on appelait ça le rythme and blues. '
        'C’était déjà un truc formidable. C’est devenu encore plus énorme. '
        'On a alors prétendu qu’il exerçait une mauvaise influence sur les jeunes. '
        'Pour moi, le rock n’est rien d’autre que de la musique. '
        'Et je suis persuadé qu’il est là pour un bout de temps. '
        'Ou bien il faudra trouver quelque chose de très fort pour le remplacer.'
    ),
    (
        'Lemmy Kilmister',
        'Quelle période géniale, l’été 71. Je m’en souviens pas, mais je ne l’oublierai jamais.'
    ),
    (
        'Ozzy Osbourne',
        'De toutes les choses que j’ai perdues, mon esprit me manque le plus'
    ),
    (
        'Keith Richards',
        'Je n’ai chamais eu de problème avec les drogues, j’ai eu des problèmes avec la police'
    ),
    (
        'John Lennon',
        'Le Rock français, c’est comme le vin anglais.'
    )

]

def get_one():
    index = random.randint(0, len(_CITATIONS) - 1)
    return _CITATIONS[index]
