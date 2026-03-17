"""
Données complémentaires sur le vin français.

Ce fichier contient les connaissances œnologiques qui ne sont pas couvertes
par les datasets open data (GeoJSON INAO, CSV production).
Les clés 'aoc' correspondent aux noms d'appellation du GeoJSON.
"""

WINE_KNOWLEDGE = {
    # =========================================================================
    # CHRONOLOGIE — L'Épopée du Vin
    # =========================================================================
    "history": [
        {
            "date": "600 av. J.-C.",
            "titre": "Les Grecs apportent la vigne",
            "description": (
                "Les Phocéens fondent Massalia (Marseille) et plantent les "
                "premiers vignobles en Gaule. La vigne méditerranéenne commence "
                "sa lente conquête du territoire."
            ),
            "anecdote": (
                "Les Gaulois préféraient la cervoise (bière d'orge) au vin grec, "
                "qu'ils trouvaient trop acide. Ils inventèrent le tonneau en bois "
                "pour remplacer les amphores — une révolution qui changea le goût "
                "du vin pour toujours !"
            ),
            "epoque": "antiquite",
        },
        {
            "date": "Ier siècle",
            "titre": "Rome développe le vignoble gaulois",
            "description": (
                "Sous l'Empire romain, la viticulture explose en Gaule. "
                "Les légions plantent des vignes le long du Rhône, en Bourgogne "
                "et à Bordeaux. Le vin gaulois rivalise bientôt avec les crus italiens."
            ),
            "anecdote": (
                "L'empereur Domitien ordonna en 92 l'arrachage de la moitié des "
                "vignes gauloises — officiellement pour protéger les céréales, "
                "mais surtout parce que le vin gaulois faisait trop d'ombre aux "
                "producteurs romains ! L'édit de Probus en 280 annula cette mesure."
            ),
            "epoque": "antiquite",
        },
        {
            "date": "XIIe siècle",
            "titre": "Les moines cisterciens, premiers œnologues",
            "description": (
                "Les moines de Cîteaux et Cluny développent la notion de terroir "
                "en Bourgogne. Ils identifient les « climats », ces parcelles aux "
                "caractéristiques uniques, et perfectionnent les techniques de "
                "vinification."
            ),
            "anecdote": (
                "Les moines goûtaient la terre pour comprendre les sols ! Le Clos "
                "de Vougeot, créé par les cisterciens, fait 50 hectares entourés "
                "d'un mur de pierre — il fallut 300 ans pour le construire. "
                "Aujourd'hui encore, les militaires français saluent le Clos "
                "en passant devant."
            ),
            "epoque": "moyen_age",
        },
        {
            "date": "1855",
            "titre": "La Classification de Bordeaux",
            "description": (
                "À la demande de Napoléon III pour l'Exposition universelle de Paris, "
                "les courtiers bordelais classent les vins du Médoc en 5 crus. "
                "Cette hiérarchie, basée sur les prix des vins, est encore en vigueur "
                "170 ans plus tard."
            ),
            "anecdote": (
                "Le Château Mouton Rothschild a attendu 118 ans pour passer de "
                "second à premier cru (1973). Son propriétaire, le baron Philippe, "
                "avait fait graver : « Premier ne puis, second ne daigne, Mouton suis. » "
                "Après sa promotion : « Premier je suis, second je fus, Mouton ne change. »"
            ),
            "epoque": "moderne",
        },
        {
            "date": "1863-1890",
            "titre": "La catastrophe du Phylloxéra",
            "description": (
                "Un minuscule puceron américain, le phylloxéra, détruit la quasi-totalité "
                "du vignoble français. Sur 2,5 millions d'hectares, il n'en reste "
                "que quelques milliers. La solution : greffer les cépages français "
                "sur des porte-greffes américains résistants."
            ),
            "anecdote": (
                "Avant de trouver le remède du greffage, on a tout essayé : "
                "inonder les vignes, enterrer des crapauds vivants sous les pieds, "
                "et même arroser au sulfure de carbone (un explosif !). Le vignoble "
                "français d'aujourd'hui est donc, techniquement, à moitié américain."
            ),
            "epoque": "moderne",
        },
        {
            "date": "1935",
            "titre": "Naissance des AOC",
            "description": (
                "Le baron Pierre Le Roy de Boiseaumarié, vigneron à Châteauneuf-du-Pape, "
                "crée le système d'Appellation d'Origine Contrôlée (AOC). "
                "Pour la première fois, un cadre juridique protège l'origine et la "
                "qualité des vins, définissant cépages, rendements et zones de production."
            ),
            "anecdote": (
                "Le décret fondateur de Châteauneuf-du-Pape interdit "
                "l'atterrissage de soucoupes volantes et d'engins volants "
                "non identifiés sur le territoire de la commune. Cet arrêté "
                "municipal de 1954 est toujours en vigueur !"
            ),
            "epoque": "contemporain",
        },
        {
            "date": "1982",
            "titre": "La révolution Robert Parker",
            "description": (
                "Le critique américain Robert Parker lance sa notation sur 100 points. "
                "Son palais influence le style des vins du monde entier : les vignerons "
                "recherchent concentration, extraction et boisé. Le « goût Parker » "
                "uniformise une partie de la production mondiale."
            ),
            "anecdote": (
                "Parker a déclaré que le millésime 1982 à Bordeaux était exceptionnel "
                "alors que tous les critiques français le jugeaient médiocre. "
                "Les prix ont explosé, lui donnant raison. Son assurance Lloyd's "
                "couvrait son nez pour 1 million de dollars !"
            ),
            "epoque": "contemporain",
        },
        {
            "date": "2000-aujourd'hui",
            "titre": "Bio, biodynamie et vins nature",
            "description": (
                "Face au changement climatique et à la demande des consommateurs, "
                "la viticulture française se réinvente. Le bio explose (+400% en 10 ans), "
                "la biodynamie gagne les plus grands domaines, et les vins nature "
                "(sans sulfites ajoutés) créent un nouveau marché."
            ),
            "anecdote": (
                "La biodynamie prescrit d'enterrer une corne de vache remplie de "
                "bouse (préparation 500) et de la déterrer 6 mois plus tard pour "
                "dynamiser les sols. Ésotérique ? Peut-être, mais le Domaine de la "
                "Romanée-Conti (le vin le plus cher du monde) est en biodynamie "
                "depuis 2007."
            ),
            "epoque": "contemporain",
        },
    ],

    # =========================================================================
    # TERROIRS — Données pour le Geoguessr viticole
    # Les clés correspondent aux noms d'appellation (colonne 'app') du GeoJSON
    # =========================================================================
    "terroirs": {
        "Chablis": {
            "region": "Bourgogne",
            "sol": "Kimméridgien (calcaire à petites huîtres fossiles)",
            "climat": "Semi-continental, gelées printanières fréquentes",
            "cepages": ["Chardonnay"],
            "indices": [
                "Sol marin fossile du Jurassique — on y trouve des coquilles d'huîtres",
                "Climat froid avec risque de gel printanier dévastateur",
                "Cépage blanc unique, pas de Pinot ici",
            ],
            "couleur_principale": "blanc",
            "impact_geologique": (
                "Les fossiles d'huîtres Exogyra virgula dans le sol kimméridgien "
                "apportent une minéralité saline et crayeuse caractéristique. "
                "C'est le même sol qu'à Sancerre, à 150 km de là."
            ),
        },
        "Pommard": {
            "region": "Bourgogne",
            "sol": "Argilo-calcaire à fer (terre rouge)",
            "climat": "Continental, étés chauds et hivers rigoureux",
            "cepages": ["Pinot Noir"],
            "indices": [
                "Terre rouge riche en oxyde de fer — couleur sang de la terre",
                "Au cœur de la Côte de Beaune, climat continental classique",
                "Cépage noble rouge, roi de la Bourgogne",
            ],
            "couleur_principale": "rouge",
            "impact_geologique": (
                "L'argile ferrugineuse donne des vins puissants et colorés, "
                "inhabituellement tanniques pour du Pinot Noir. Les Rugiens, "
                "premier cru emblématique, tirent leur nom de la couleur rouge du sol."
            ),
        },
        "Gevrey-Chambertin": {
            "region": "Bourgogne",
            "sol": "Calcaire et marnes sur éboulis du Jurassique",
            "climat": "Continental avec influence semi-montagnarde",
            "cepages": ["Pinot Noir"],
            "indices": [
                "Éboulis calcaires du Jurassique, combe de Lavaux à proximité",
                "Nord de la Côte de Nuits, exposé est, altitude 250-350m",
                "Grand cru mythique au nom composé d'un village et d'un champ",
            ],
            "couleur_principale": "rouge",
            "impact_geologique": (
                "La combe de Lavaux crée un cône d'éboulis calcaires qui confère "
                "aux vins leur structure et leur potentiel de garde légendaire. "
                "Napoléon ne buvait que du Chambertin."
            ),
        },
        "Meursault": {
            "region": "Bourgogne",
            "sol": "Calcaires blancs et marnes argileuses",
            "climat": "Continental tempéré, exposé est/sud-est",
            "cepages": ["Chardonnay"],
            "indices": [
                "Calcaire blanc donnant des vins gras et beurrés",
                "Côte de Beaune, voisin de Puligny-Montrachet",
                "Grands blancs opulents, souvent élevés en fût de chêne",
            ],
            "couleur_principale": "blanc",
            "impact_geologique": (
                "Les marnes blanches du Bathonien supérieur donnent un Chardonnay "
                "riche et noisette, à l'opposé du Chablis minéral. La célèbre "
                "Paulée de Meursault est le plus grand banquet viticole de France."
            ),
        },
        "Nuits-Saint-Georges": {
            "region": "Bourgogne",
            "sol": "Calcaire à entroques et marnes",
            "climat": "Continental, coteaux bien exposés",
            "cepages": ["Pinot Noir"],
            "indices": [
                "Calcaire à crinoïdes (fossiles d'étoiles de mer)",
                "Ville-porte de la Côte de Nuits, 41 premiers crus",
                "Vins rouges structurés, la 'capitale' commerciale de la Bourgogne",
            ],
            "couleur_principale": "rouge",
            "impact_geologique": (
                "Le calcaire à entroques (crinoïdes fossiles) donne des vins "
                "fermes et structurés qui demandent de la patience. En 1971, "
                "Apollo 15 emporta une bouteille de Nuits-Saint-Georges sur la Lune."
            ),
        },
        "Châteauneuf-du-Pape": {
            "region": "Vallée du Rhône",
            "sol": "Galets roulés du Quaternaire sur argile rouge",
            "climat": "Méditerranéen, mistral dominant, 2 800h d'ensoleillement/an",
            "cepages": ["Grenache", "Syrah", "Mourvèdre", "et 10 autres"],
            "indices": [
                "Gros galets ronds qui emmagasinent la chaleur du soleil",
                "Région la plus chaude du Rhône, 300 jours de soleil, vent violent",
                "13 cépages autorisés — le plus grand assemblage de France",
            ],
            "couleur_principale": "rouge",
            "impact_geologique": (
                "Les galets roulés (quartzite alpine charriée par le Rhône) "
                "restituent la chaleur la nuit, permettant une maturation optimale. "
                "Ils empêchent aussi l'évaporation et protègent du splash de pluie."
            ),
        },
        "Hermitage": {
            "region": "Vallée du Rhône",
            "sol": "Granit, gneiss et loess",
            "climat": "Continental à influence méditerranéenne, mistral",
            "cepages": ["Syrah"],
            "indices": [
                "Colline granitique majestueuse dominant le Rhône",
                "Confluence des climats continental et méditerranéen",
                "Syrah pure, un des vins les plus prestigieux du Rhône Nord",
            ],
            "couleur_principale": "rouge",
            "impact_geologique": (
                "La colline de l'Hermitage expose 3 types de sols différents "
                "(granit, loess, calcaire) sur un seul coteau. Au XIXe siècle, "
                "l'Hermitage était plus cher que le Bordeaux."
            ),
        },
        "Côte-Rôtie": {
            "region": "Vallée du Rhône",
            "sol": "Schistes et gneiss (Côte Brune) / Granit et sable (Côte Blonde)",
            "climat": "Continental à influence méditerranéenne",
            "cepages": ["Syrah", "Viognier (jusqu'à 20%)"],
            "indices": [
                "Coteaux vertigineux en terrasses, schiste et granit",
                "Appellation la plus septentrionale du Rhône, pentes à 60°",
                "Syrah parfumée, co-plantée avec un cépage blanc aromatique",
            ],
            "couleur_principale": "rouge",
            "impact_geologique": (
                "La Côte Brune (schiste, fer) donne des vins sombres et puissants ; "
                "la Côte Blonde (granit, sable) produit des vins plus fins et parfumés. "
                "La légende dit qu'un seigneur partagea ses vignes entre ses deux filles, "
                "une brune et une blonde."
            ),
        },
        "Côtes du Rhône": {
            "region": "Vallée du Rhône",
            "sol": "Varié : galets, argile, calcaire, sable",
            "climat": "Méditerranéen dominant, mistral",
            "cepages": ["Grenache", "Syrah", "Mourvèdre"],
            "indices": [
                "La plus vaste appellation de la vallée, sols très variés",
                "Climat méditerranéen, vent du nord puissant et froid",
                "Assemblage méridional classique, rouge fruité et épicé",
            ],
            "couleur_principale": "rouge",
            "impact_geologique": (
                "L'appellation s'étend sur 6 départements avec une grande diversité "
                "de terroirs. C'est la deuxième plus grande AOC de France après Bordeaux."
            ),
        },
        "Gigondas": {
            "region": "Vallée du Rhône",
            "sol": "Argilo-calcaire et galets",
            "climat": "Méditerranéen, dentelles de Montmirail",
            "cepages": ["Grenache", "Syrah", "Mourvèdre"],
            "indices": [
                "Au pied de dentelles calcaires spectaculaires",
                "Climat chaud méditerranéen, altitude modérée apportant fraîcheur",
                "Longtemps surnommé le 'Châteauneuf-du-Pape du pauvre'",
            ],
            "couleur_principale": "rouge",
            "impact_geologique": (
                "Les Dentelles de Montmirail (crêtes calcaires du Trias) "
                "créent un microclimat unique avec des nuits fraîches qui "
                "préservent l'acidité et l'élégance des vins."
            ),
        },
        "Condrieu": {
            "region": "Vallée du Rhône",
            "sol": "Granit à mica (arzelle)",
            "climat": "Continental avec influences méditerranéennes",
            "cepages": ["Viognier"],
            "indices": [
                "Granit micacé en terrasses vertigineuses",
                "Juste au sud de Lyon, coteaux abrupts au-dessus du Rhône",
                "Cépage blanc aromatique rarissime, abricot et fleurs blanches",
            ],
            "couleur_principale": "blanc",
            "impact_geologique": (
                "Le granit à mica (localement appelé 'arzelle') se décompose en "
                "arène sablonneuse qui donne au Viognier ses arômes d'abricot "
                "et de pêche blanche caractéristiques."
            ),
        },
        "Bordeaux": {
            "region": "Bordeaux",
            "sol": "Graves (galets), argilo-calcaire, sable",
            "climat": "Océanique tempéré, influence de l'estuaire",
            "cepages": ["Merlot", "Cabernet Sauvignon", "Cabernet Franc"],
            "indices": [
                "Graves et galets drainants des terrasses alluviales de la Garonne",
                "Climat océanique, douceur atlantique, risque de pluie en vendanges",
                "Assemblage bordelais classique, première AOC de France en volume",
            ],
            "couleur_principale": "rouge",
            "impact_geologique": (
                "Les graves (galets de quartz charriés par la Garonne depuis les Pyrénées) "
                "assurent un drainage parfait et restituent la chaleur la nuit. "
                "La diversité des sols explique les 57 appellations du Bordelais."
            ),
        },
        "Saint-Émilion": {
            "region": "Bordeaux",
            "sol": "Plateau calcaire, côtes argilo-calcaires, graves",
            "climat": "Océanique avec influence continentale",
            "cepages": ["Merlot", "Cabernet Franc"],
            "indices": [
                "Plateau calcaire perché, caves creusées dans la roche",
                "Rive droite de la Dordogne, sols plus frais que le Médoc",
                "Le Merlot domine ici, donnant des vins ronds et veloutés",
            ],
            "couleur_principale": "rouge",
            "impact_geologique": (
                "Le plateau calcaire de Saint-Émilion est truffé de galeries "
                "souterraines (les catacombes). L'église monolithe, creusée dans "
                "la roche au XIe siècle, est la plus grande d'Europe."
            ),
        },
        "Pomerol": {
            "region": "Bordeaux",
            "sol": "Argile bleue (crasse de fer) et graves",
            "climat": "Océanique tempéré",
            "cepages": ["Merlot", "Cabernet Franc"],
            "indices": [
                "Argile bleue unique avec oxydes de fer (crasse de fer)",
                "Plus petite grande appellation de Bordeaux, pas de classement officiel",
                "Merlot quasi exclusif, vins soyeux et truffe",
            ],
            "couleur_principale": "rouge",
            "impact_geologique": (
                "La « crasse de fer » (argile bleue mêlée d'oxydes de fer) est unique "
                "à Pomerol et confère à Petrus sa texture veloutée légendaire. "
                "Cette appellation n'a jamais eu de classement officiel."
            ),
        },
        "Margaux": {
            "region": "Bordeaux",
            "sol": "Graves fines (galets et gravier)",
            "climat": "Océanique, influence de l'estuaire de la Gironde",
            "cepages": ["Cabernet Sauvignon", "Merlot"],
            "indices": [
                "Graves fines et bien drainées, les plus élégantes du Médoc",
                "Bord de l'estuaire, climat tempéré par les eaux",
                "Finesse et parfum plus que puissance, le 'féminin' du Médoc",
            ],
            "couleur_principale": "rouge",
            "impact_geologique": (
                "Les graves de Margaux sont les plus fines du Médoc, donnant des vins "
                "d'une élégance incomparable. Le Château Margaux est le seul premier "
                "cru à porter le nom de son appellation."
            ),
        },
        "Pauillac": {
            "region": "Bordeaux",
            "sol": "Grosses graves profondes sur sous-sol calcaire",
            "climat": "Océanique, protégé par la forêt des Landes",
            "cepages": ["Cabernet Sauvignon", "Merlot"],
            "indices": [
                "Grosses graves profondes de plusieurs mètres sur calcaire",
                "Cœur du Médoc, 3 premiers crus classés sur 5",
                "Cabernet Sauvignon roi, vins de très longue garde",
            ],
            "couleur_principale": "rouge",
            "impact_geologique": (
                "Les croupes de graves de Pauillac atteignent parfois 10 mètres "
                "de profondeur — un drainage exceptionnel. 3 des 5 premiers crus 1855 "
                "sont ici : Lafite, Latour et Mouton Rothschild."
            ),
        },
        "Sauternes": {
            "region": "Bordeaux",
            "sol": "Graves, argile et calcaire",
            "climat": "Océanique avec brumes automnales (Ciron)",
            "cepages": ["Sémillon", "Sauvignon Blanc", "Muscadelle"],
            "indices": [
                "Sol varié mais surtout le brouillard matinal qui fait tout",
                "Confluence du Ciron et de la Garonne, brumes d'automne",
                "Vendanges par tries successives, grain par grain, vins liquoreux",
            ],
            "couleur_principale": "blanc",
            "impact_geologique": (
                "Le Ciron, rivière froide, rencontre la Garonne tiède et crée "
                "des brumes matinales qui favorisent le Botrytis cinerea (pourriture noble). "
                "Au Château d'Yquem, un pied de vigne produit un seul verre de vin."
            ),
        },
        "Pessac-Léognan": {
            "region": "Bordeaux",
            "sol": "Graves profondes (galets de quartz)",
            "climat": "Océanique, proximité urbaine de Bordeaux",
            "cepages": ["Cabernet Sauvignon", "Merlot", "Sauvignon Blanc", "Sémillon"],
            "indices": [
                "Graves profondes les plus anciennes du Bordelais",
                "Aux portes de Bordeaux, anciennement 'Graves'",
                "Seule appellation bordelaise classée à la fois en rouge ET blanc",
            ],
            "couleur_principale": "rouge",
            "impact_geologique": (
                "Les graves de Pessac-Léognan sont les plus anciennes du Bordelais "
                "(Günz, 600 000 ans). Le Château Haut-Brion, en pleine ville, "
                "est le seul premier cru hors du Médoc."
            ),
        },
        "Champagne": {
            "region": "Champagne",
            "sol": "Craie (Campanien), calcaire et argile",
            "climat": "Continental froid, limite nord de la viticulture",
            "cepages": ["Chardonnay", "Pinot Noir", "Pinot Meunier"],
            "indices": [
                "Sous-sol de craie blanche, caves creusées dans la roche",
                "Région la plus septentrionale de France, acidité naturelle élevée",
                "Méthode traditionnelle, assemblage de 3 cépages, bulles fines",
            ],
            "couleur_principale": "effervescent",
            "impact_geologique": (
                "La craie campanienne (70 millions d'années) est un réservoir d'eau "
                "naturel qui régule l'hydratation de la vigne. Les crayères (carrières "
                "de craie romaines) servent de caves à 10°C constant."
            ),
        },
        "Alsace": {
            "region": "Alsace",
            "sol": "Mosaïque : granit, grès, calcaire, marnes, loess",
            "climat": "Semi-continental, protégé par les Vosges (le plus sec de France)",
            "cepages": ["Riesling", "Gewurztraminer", "Pinot Gris", "Muscat"],
            "indices": [
                "13 types de sols différents sur une bande étroite — mosaïque géologique",
                "À l'abri des Vosges, climat très sec, 300 jours sans pluie par an",
                "Vins blancs monocépages portant le nom du cépage sur l'étiquette",
            ],
            "couleur_principale": "blanc",
            "impact_geologique": (
                "L'effondrement du fossé rhénan a créé une faille géologique "
                "juxtaposant 13 types de sols sur 120 km. Chaque Grand Cru "
                "exprime un terroir unique. L'Alsace est la seule région française "
                "à indiquer le cépage sur l'étiquette."
            ),
        },
        "Sancerre": {
            "region": "Loire",
            "sol": "Silex, calcaire (caillottes), argilo-calcaire (terres blanches)",
            "climat": "Semi-continental, influence océanique lointaine",
            "cepages": ["Sauvignon Blanc", "Pinot Noir"],
            "indices": [
                "Trois types de sols donnant trois styles différents du même cépage",
                "Colline dominant la Loire, climat frais à influence continentale",
                "Le Sauvignon Blanc le plus célèbre de France",
            ],
            "couleur_principale": "blanc",
            "impact_geologique": (
                "Les silex donnent des vins fumés et minéraux, les caillottes "
                "des vins fruités et légers, les terres blanches des vins riches "
                "et complexes. Même sol kimméridgien qu'à Chablis !"
            ),
        },
        "Pouilly-Fumé": {
            "region": "Loire",
            "sol": "Silex, marnes kimméridgiennes",
            "climat": "Semi-continental, gelées fréquentes",
            "cepages": ["Sauvignon Blanc"],
            "indices": [
                "Silex et kimméridgien, vins au caractère 'fumé' emblématique",
                "Face à Sancerre de l'autre côté de la Loire",
                "Sauvignon Blanc exclusif, arômes de pierre à fusil",
            ],
            "couleur_principale": "blanc",
            "impact_geologique": (
                "Le 'fumé' du nom vient de la pruine grise sur les raisins mûrs "
                "(pas de la fumée !). Le silex donne ce goût caractéristique de "
                "pierre à fusil que les Anglais appellent 'gunflint'."
            ),
        },
        "Vouvray": {
            "region": "Loire",
            "sol": "Tuffeau (calcaire tendre) et argile à silex",
            "climat": "Océanique tempéré, automnes prolongés",
            "cepages": ["Chenin Blanc"],
            "indices": [
                "Tuffeau blanc creusé en caves troglodytes",
                "Touraine, influence océanique, vendanges tardives possibles",
                "Monocépage blanc pouvant donner sec, demi-sec, moelleux ou effervescent",
            ],
            "couleur_principale": "blanc",
            "impact_geologique": (
                "Le tuffeau (craie du Turonien) est si tendre qu'on y creuse des "
                "caves depuis des siècles. Un seul cépage, le Chenin, produit ici "
                "4 styles différents selon le millésime : sec, demi-sec, moelleux et pétillant."
            ),
        },
        "Chinon": {
            "region": "Loire",
            "sol": "Tuffeau, graviers, sables de la Vienne",
            "climat": "Océanique tempéré avec influence continentale",
            "cepages": ["Cabernet Franc"],
            "indices": [
                "Tuffeau et graviers en bord de Vienne",
                "Touraine, château de Chinon (Jeanne d'Arc !), climat doux",
                "Le Cabernet Franc à l'état pur, arômes de poivron et violette",
            ],
            "couleur_principale": "rouge",
            "impact_geologique": (
                "Rabelais, enfant du pays, célébrait déjà le vin de Chinon au XVIe siècle. "
                "Les « graviers » des bords de Vienne donnent des vins légers et fruités, "
                "le coteau calcaire des vins de garde plus structurés."
            ),
        },
        "Muscadet": {
            "region": "Loire",
            "sol": "Gneiss, gabbro, granite, schiste",
            "climat": "Océanique, influence atlantique directe",
            "cepages": ["Melon de Bourgogne"],
            "indices": [
                "Roches métamorphiques anciennes (gneiss, gabbro)",
                "Embouchure de la Loire, climat atlantique pur",
                "Élevage sur lies fines, vin sec et iodé, parfait avec les fruits de mer",
            ],
            "couleur_principale": "blanc",
            "impact_geologique": (
                "Le Melon de Bourgogne (unique cépage) a survécu au gel de 1709 "
                "qui détruisit les cépages rouges. L'élevage sur lies (dépôt de "
                "levures mortes) donne cette texture crémeuse et ce perlant subtil."
            ),
        },
        "Anjou": {
            "region": "Loire",
            "sol": "Schiste, grès, calcaire, tuffeau",
            "climat": "Océanique tempéré",
            "cepages": ["Chenin Blanc", "Cabernet Franc", "Grolleau"],
            "indices": [
                "Schiste et tuffeau, grande diversité géologique",
                "Douceur angevine, carrefour océanique et continental",
                "Appellations multiples : blanc sec, rosé, rouge, liquoreux",
            ],
            "couleur_principale": "rouge",
            "impact_geologique": (
                "L'Anjou est un carrefour géologique : le Massif armoricain (schiste) "
                "rencontre le Bassin parisien (calcaire). Cette diversité explique "
                "la variété exceptionnelle des vins produits."
            ),
        },
        "Bandol": {
            "region": "Provence",
            "sol": "Calcaire, marnes, grès, éboulis",
            "climat": "Méditerranéen, amphithéâtre face à la mer",
            "cepages": ["Mourvèdre", "Grenache", "Cinsault"],
            "indices": [
                "Restanques (terrasses) calcaires face à la Méditerranée",
                "Amphithéâtre naturel protégé du mistral, ensoleillement maximum",
                "Le Mourvèdre, cépage roi, exige chaleur et proximité de la mer",
            ],
            "couleur_principale": "rouge",
            "impact_geologique": (
                "Les restanques (terrasses de pierre sèche) datent du XVIIIe siècle. "
                "Le Mourvèdre a besoin de 'voir la mer' pour mûrir — à Bandol, "
                "les vignes sont en amphithéâtre face à la Méditerranée."
            ),
        },
        "Côtes de Provence": {
            "region": "Provence",
            "sol": "Calcaire, schiste, grès, cristallin",
            "climat": "Méditerranéen, 3 000h d'ensoleillement, mistral",
            "cepages": ["Grenache", "Cinsault", "Syrah", "Mourvèdre"],
            "indices": [
                "Sols variés, du cristallin des Maures au calcaire de Sainte-Victoire",
                "Le plus grand ensoleillement de France, mistral omniprésent",
                "Premier producteur français de rosé, 88% de la production",
            ],
            "couleur_principale": "rosé",
            "impact_geologique": (
                "Les Côtes de Provence produisent 88% de rosé, ce qui en fait "
                "la capitale mondiale du rosé. Le terroir très varié s'étend "
                "du massif cristallin des Maures aux falaises calcaires de Sainte-Victoire."
            ),
        },
        "Cahors": {
            "region": "Sud-Ouest",
            "sol": "Causse calcaire (plateau) et alluvions du Lot (terrasses)",
            "climat": "Océanique à influence méditerranéenne",
            "cepages": ["Malbec (Côt)", "Merlot"],
            "indices": [
                "Causse calcaire au-dessus de la vallée du Lot",
                "Climat de transition, entre Atlantique et Méditerranée",
                "Le 'vin noir' historique, cépage d'origine du Malbec argentin",
            ],
            "couleur_principale": "rouge",
            "impact_geologique": (
                "Le Malbec (appelé Côt ou Auxerrois localement) a été exporté "
                "en Argentine au XIXe siècle après le phylloxéra. Le 'vin noir' "
                "de Cahors était si sombre qu'on l'utilisait pour colorer les "
                "Bordeaux au Moyen Âge."
            ),
        },
        "Madiran": {
            "region": "Sud-Ouest",
            "sol": "Argilo-calcaire, galets, graves",
            "climat": "Océanique à influence pyrénéenne, effet de foehn",
            "cepages": ["Tannat", "Cabernet Franc"],
            "indices": [
                "Argile et galets aux pieds des Pyrénées",
                "Climat doux d'influence pyrénéenne, vent chaud de foehn",
                "Cépage le plus tannique de France — son nom dit tout",
            ],
            "couleur_principale": "rouge",
            "impact_geologique": (
                "Le Tannat (de 'tanin') est le cépage le plus tannique au monde. "
                "Des études scientifiques ont montré que les habitants de Madiran "
                "ont une longévité supérieure à la moyenne, attribuée aux "
                "procyanidines du Tannat — le 'French Paradox' dans le paradox."
            ),
        },
        "Jurançon": {
            "region": "Sud-Ouest",
            "sol": "Poudingue (galets cimentés) et argile",
            "climat": "Pyrénéen, influence du foehn, automnes dorés",
            "cepages": ["Gros Manseng", "Petit Manseng"],
            "indices": [
                "Poudingue (conglomérat de galets) sur les coteaux pyrénéens",
                "Vent chaud du sud (foehn) qui assèche les raisins en automne",
                "Vins blancs doux de vendanges tardives, cépages locaux uniques",
            ],
            "couleur_principale": "blanc",
            "impact_geologique": (
                "À la naissance d'Henri IV (1553), on lui frotta les lèvres "
                "avec une gousse d'ail et une goutte de Jurançon — tradition "
                "béarnaise toujours vivante. Le Petit Manseng, passerillé sur pied, "
                "atteint des concentrations en sucre extraordinaires."
            ),
        },
        "Corbières": {
            "region": "Languedoc-Roussillon",
            "sol": "Schiste, calcaire, grès, argile — grande diversité",
            "climat": "Méditerranéen venteux, garrigue",
            "cepages": ["Carignan", "Grenache", "Syrah", "Mourvèdre"],
            "indices": [
                "Mosaïque de schiste, calcaire et grès dans les contreforts",
                "Garrigue méditerranéenne, Tramontane et Cers (vents dominants)",
                "L'appellation historique du Languedoc, le Carignan y est roi",
            ],
            "couleur_principale": "rouge",
            "impact_geologique": (
                "Les Corbières abritent le village de Tautavel, où l'on a trouvé "
                "les plus anciens restes humains d'Europe (450 000 ans). Le Carignan, "
                "longtemps méprisé, connaît une renaissance grâce aux vieilles vignes "
                "centenaires."
            ),
        },
        "Minervois": {
            "region": "Languedoc-Roussillon",
            "sol": "Calcaire, schiste, grès rouge",
            "climat": "Méditerranéen, influence de la Montagne Noire",
            "cepages": ["Syrah", "Grenache", "Carignan", "Mourvèdre"],
            "indices": [
                "Grès rouge caractéristique, adossé à la Montagne Noire",
                "Entre Canal du Midi et Montagne Noire, garrigues parfumées",
                "Vins épicés et garrigués, thym et romarin dans le verre",
            ],
            "couleur_principale": "rouge",
            "impact_geologique": (
                "Le Minervois est traversé par le Canal du Midi, inscrit au "
                "patrimoine mondial UNESCO. Le mot 'Minerve' vient du village "
                "cathare perché sur un éperon rocheux — haut lieu de résistance "
                "lors de la croisade des Albigeois."
            ),
        },
        "Languedoc": {
            "region": "Languedoc-Roussillon",
            "sol": "Calcaire, galets, schiste, basalte",
            "climat": "Méditerranéen, le plus ensoleillé de France",
            "cepages": ["Grenache", "Syrah", "Mourvèdre", "Carignan"],
            "indices": [
                "Du basalte volcanique au calcaire littoral, sols très variés",
                "Le plus vaste vignoble de France, 3e mondial en superficie",
                "Révolution qualitative depuis les années 2000, vins de garrigue",
            ],
            "couleur_principale": "rouge",
            "impact_geologique": (
                "Le Languedoc est le plus grand vignoble du monde en superficie. "
                "Longtemps associé au vin de table bon marché, la région connaît "
                "une révolution qualitative spectaculaire depuis 20 ans."
            ),
        },
    },

    # =========================================================================
    # DÉGUSTATIONS — Données pour le Sommelier Virtuel
    # Les clés 'aoc' correspondent aux noms d'appellation du GeoJSON
    # =========================================================================
    "degustations": [
        {
            "aoc": "Pommard",
            "cepage": "Pinot Noir",
            "region": "Bourgogne",
            "couleur": "rouge",
            "oeil": {
                "couleur": "Rubis soutenu aux reflets grenat",
                "viscosite": "Larmes lentes et régulières — alcool modéré",
                "limpidite": "Limpide, brillant",
            },
            "nez": {
                "premier": "Cerise noire, mûre, cassis",
                "deuxieme": "Sous-bois, cuir, champignon",
                "troisieme": "Épices douces (cannelle, réglisse)",
            },
            "bouche": {
                "attaque": "Franche et fruitée",
                "milieu": "Tanins fermes mais soyeux, belle matière",
                "finale": "Longue, sur le fruit noir et la terre",
            },
        },
        {
            "aoc": "Chablis",
            "cepage": "Chardonnay",
            "region": "Bourgogne",
            "couleur": "blanc",
            "oeil": {
                "couleur": "Or pâle aux reflets verts",
                "viscosite": "Fines larmes — vin sec et tendu",
                "limpidite": "Cristallin, éclat minéral",
            },
            "nez": {
                "premier": "Citron vert, pomme verte, poire",
                "deuxieme": "Craie, silex, pierre à fusil",
                "troisieme": "Fleurs blanches (acacia, aubépine)",
            },
            "bouche": {
                "attaque": "Vive et minérale",
                "milieu": "Tension saline, acidité croquante",
                "finale": "Longue, iodée, salivante",
            },
        },
        {
            "aoc": "Châteauneuf-du-Pape",
            "cepage": "Grenache (dominant)",
            "region": "Vallée du Rhône",
            "couleur": "rouge",
            "oeil": {
                "couleur": "Rouge profond, presque noir, reflets violets",
                "viscosite": "Larmes épaisses et lentes — vin généreux (15°+)",
                "limpidite": "Dense, légèrement trouble (non filtré souvent)",
            },
            "nez": {
                "premier": "Fruits noirs confits, figue, pruneau",
                "deuxieme": "Garrigue (thym, romarin, lavande)",
                "troisieme": "Chocolat noir, tabac, épices orientales",
            },
            "bouche": {
                "attaque": "Puissante et chaleureuse",
                "milieu": "Volume impressionnant, tanins fondus, alcool présent",
                "finale": "Très longue, sur les épices et le cacao",
            },
        },
        {
            "aoc": "Champagne",
            "cepage": "Chardonnay / Pinot Noir / Pinot Meunier",
            "region": "Champagne",
            "couleur": "effervescent",
            "oeil": {
                "couleur": "Or pâle à reflets dorés",
                "viscosite": "Bulles fines et persistantes, cordon régulier",
                "limpidite": "Brillant, effervescence vive",
            },
            "nez": {
                "premier": "Pomme, poire, agrumes",
                "deuxieme": "Brioche, pain grillé, noisette",
                "troisieme": "Craie, minéralité, miel d'acacia",
            },
            "bouche": {
                "attaque": "Fraîche et pétillante, mousse crémeuse",
                "milieu": "Équilibre entre vivacité et rondeur, bulles soyeuses",
                "finale": "Longue, saline et toastée",
            },
        },
        {
            "aoc": "Sancerre",
            "cepage": "Sauvignon Blanc",
            "region": "Loire",
            "couleur": "blanc",
            "oeil": {
                "couleur": "Jaune pâle à reflets argentés",
                "viscosite": "Fines larmes — vin vif et léger",
                "limpidite": "Cristallin, brillant",
            },
            "nez": {
                "premier": "Pamplemousse, citron, fruit de la passion",
                "deuxieme": "Buis, bourgeon de cassis, herbe fraîche",
                "troisieme": "Silex, fumée (terroir de silex)",
            },
            "bouche": {
                "attaque": "Franche et croquante",
                "milieu": "Acidité rafraîchissante, tension minérale",
                "finale": "Nette et citronnée, légère amertume noble",
            },
        },
        {
            "aoc": "Côtes de Provence",
            "cepage": "Grenache / Cinsault",
            "region": "Provence",
            "couleur": "rosé",
            "oeil": {
                "couleur": "Rose pâle, pelure d'oignon, reflets saumonés",
                "viscosite": "Fines larmes, vin frais et léger",
                "limpidite": "Cristallin, lumineux",
            },
            "nez": {
                "premier": "Pêche blanche, fraise des bois, groseille",
                "deuxieme": "Fleurs (rose, pivoine)",
                "troisieme": "Zeste d'agrumes, bonbon anglais",
            },
            "bouche": {
                "attaque": "Fraîche et fruitée",
                "milieu": "Rondeur délicate, finale saline",
                "finale": "Courte mais agréable, amertume fine d'agrumes",
            },
        },
        {
            "aoc": "Hermitage",
            "cepage": "Syrah",
            "region": "Vallée du Rhône",
            "couleur": "rouge",
            "oeil": {
                "couleur": "Pourpre intense, presque noir, reflets violets",
                "viscosite": "Larmes denses et colorées",
                "limpidite": "Profond, opaque au centre",
            },
            "nez": {
                "premier": "Violette, myrtille, cassis",
                "deuxieme": "Poivre noir, olive noire, lard fumé",
                "troisieme": "Cuir, truffe, graphite",
            },
            "bouche": {
                "attaque": "Dense et concentrée",
                "milieu": "Tanins puissants mais fins, grande matière",
                "finale": "Interminable, sur le poivre et la violette",
            },
        },
        {
            "aoc": "Sauternes",
            "cepage": "Sémillon (dominant)",
            "region": "Bordeaux",
            "couleur": "blanc",
            "oeil": {
                "couleur": "Or intense à reflets ambrés",
                "viscosite": "Larmes très épaisses et lentes — vin liquoreux",
                "limpidite": "Brillant, doré profond",
            },
            "nez": {
                "premier": "Abricot confit, mangue, ananas rôti",
                "deuxieme": "Miel, cire d'abeille, safran",
                "troisieme": "Écorce d'orange confite, crème brûlée",
            },
            "bouche": {
                "attaque": "Onctueuse et sucrée, mais pas lourde",
                "milieu": "Équilibre sucre/acidité magistral, texture soyeuse",
                "finale": "Très longue, sur l'abricot et le miel, fraîcheur en fin",
            },
        },
    ],
}
