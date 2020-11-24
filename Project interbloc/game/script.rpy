# Vous pouvez placer le script de votre jeu dans ce fichier.

# Déclarez sous cette ligne les images, avec l'instruction 'image'
# ex: image eileen heureuse = "eileen_heureuse.png"

# Déclarez les personnages utilisés dans le jeu.
define i = Character('Iuna', color="#c8ffc8")


# Le jeu commence ici
label start:
    scene planet
    with fade
    i "Bienvenue à toi jeune scientifique, voici la planète Nemo. On y a détecté de la vie et on aimerait que tu y jettes un coup d’œil pour alimenter notre base de données. Alors c’est parti !"
    scene fond01
    with fade
    show cell at right
    with dissolve 
    i "Il semblerait que tu sois arrivé au stade du début de la vie sur cette planète. Nous te présentons la cellule DACU (le dernier ancêtre commun). Il s’agit d’une cellule dont toute la vie future sur cette planète descendra. C’est pour ça qu’on l’appelle l’ancêtre commun. Pour nous il y a aussi eu un ancêtre commun sur Terre."
    i "DACU vit dans un environnement aquatique, en effet comme sur la Terre il y a 3.3 milliards d’années, le monde Nemo est un immense océan où la vie émerge tout doucement. Dans cette immensité, on retrouve DACU qui vit paisiblement en se clonant par division créeant ainsi plein de DACU."
    show blue at left with dissolve
    i "Cependant un changement, va se produire. Un DACU lorsqu’il se divise va créer un nouveau type de cellule. En effet plus elles divisent plus certain DACU deviennent bleus, jusqu’à devenir complètement bleu ! Soudain un courant marin intervient et emporte une partie des cellules bleus."
    menu:
        i "Que préfères-tu ? Choisir de suivre les cellules bleues ou rester avec celles qui sont toujours DACU ?"
        "Je veux choisir les cellules bleues":
            jump cell_bleu
        "Je veux choisir les DACU":
            i "Sais-tu ce qui s’est passé chez les DACU qui sont devenues bleues ? Il s’agit d’une mutation. Une mutation est un changement dans une structure très importante qui compose notre organisme qui s’appelle ADN. Ainsi une mutation peut avoir un effet bénéfique comme un effet néfaste ou neutre."
    i "Dans notre cas, la mutation de l’ADN d’une cellule de DACU la rendue bleue. Les mutations sont donc des phénomènes aléatoires qui peuvent intervenir à tout moment et rendre un individu résistant ou non à un critère de son environnement."
    hide blue with dissolve
    i "Les cellules DACU qui sont restées, ont commencée à elles aussi mutées et à donner de nouvelles sortes de cellules de toutes les couleurs."
    hide cell
    show psych at right with dissolve
    i " Une tempête à la surface de la planète va alors entraîner certaines d’entre elles là ou les cellules bleues sont parties et d’autres dans un environnement inconnu."
    scene mer02 with fade
    menu:
        i "Préferes tu"
        "voir ce que les cellules bleues sont devenues":
            scene construct with fade
            "WIP"
            return
        "partir à l’aventure":
            scene construct with fade
            "Wip"
    "STOP"
    return
