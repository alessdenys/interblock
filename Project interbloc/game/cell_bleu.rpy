
label cell_bleu:
    i "Sais-tu ce qui s’est passé chez les DACU qui sont devenues bleues ? Il s’agit d’une mutation. Une mutation est un changement dans une structure très importante qui compose notre organisme qui s’appelle ADN. Ainsi une mutation peut avoir un effet bénéfique comme un effet néfaste ou neutre."
    i "Dans notre cas, la mutation de l’ADN d’une cellule de DACU la rendue bleue. Les mutations sont donc des phénomènes aléatoires qui peuvent intervenir à tout moment et rendre un individu résistant ou non à un critère de son environnement."
    hide cell with dissolve
    scene mer with fade
    show blue at right with dissolve
    i "Les cellules bleues sont amenées dans un environnement un peu plus exposé au soleil que le lieu où elles étaient à l’origine. Et elles se multiplient en grand nombre et de nouvelles mutations ont lieu."
    menu:
        i "Soudain un nouveau courant marin entraînent une partie des cellules vers une partie inexplorée de la planète Nemo, que souhaites tu faire"
        "rester avec les cellules ?":
            scene construct
            "WIP"
            return
        "partir avec les autres ?":
            scene construct
            "WIP"
    "STOP"
    return
