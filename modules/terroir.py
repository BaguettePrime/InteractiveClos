"""
Module 2 — Terroir Geoguessr.

Jeu de devinettes géographiques basé sur les vraies
délimitations AOC (GeoJSON INAO) et les données de terroir.
"""

import random
import streamlit as st
import pandas as pd
import geopandas as gpd
import folium
from streamlit_folium import st_folium
from data.wine_knowledge import WINE_KNOWLEDGE


# Palette de couleurs par délégation territoriale
DT_COLORS = {
    "Bordeaux": "#630d16",
    "Dijon": "#8B4513",
    "Avignon": "#B8860B",
    "Tours": "#2E8B57",
    "Angers": "#4682B4",
    "Épernay": "#DAA520",
    "Colmar": "#6B8E23",
    "Marseille": "#CD853F",
    "Toulouse": "#9370DB",
    "Montpellier": "#D2691E",
}

# Nombre de rounds par partie
NB_ROUNDS = 10

# Points par indice
POINTS_PAR_INDICE = {0: 3, 1: 2, 2: 1}


def render(
    gdf: gpd.GeoDataFrame | None = None,
    production_df: pd.DataFrame | None = None,
):
    """Affiche le module Terroir Geoguessr."""
    st.markdown("# Terroir Geoguessr")
    st.markdown(
        "*Saurez-vous reconnaître les appellations françaises "
        "à partir de leurs indices de terroir ?*"
    )
    st.markdown('<hr class="gold-separator">', unsafe_allow_html=True)

    if gdf is None or gdf.empty:
        st.warning("Les données GeoJSON des AOC ne sont pas disponibles.")
        st.info("Exécutez `python scripts/prepare_data.py` pour générer les données.")
        return

    # Filtrer les AOC qui ont des données de terroir dans wine_knowledge
    terroirs = WINE_KNOWLEDGE["terroirs"]
    aoc_jouables = [
        aoc for aoc in terroirs.keys() if aoc in gdf["app"].values
    ]

    if not aoc_jouables:
        st.warning(
            "Aucune AOC jouable trouvée (pas de correspondance "
            "entre wine_knowledge et le GeoJSON)."
        )
        st.info(f"AOC dans le GeoJSON : {list(gdf['app'].unique()[:10])}...")
        return

    # Initialisation du state
    _init_state(aoc_jouables)

    state = st.session_state

    # Affichage du score
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Round", f"{state.terroir_round + 1}/{NB_ROUNDS}")
    with col2:
        st.metric("Score", f"{state.score}")
    with col3:
        st.metric("Max possible", f"{state.max_score}")

    # Partie terminée ?
    if state.terroir_round >= NB_ROUNDS:
        _afficher_fin_partie()
        return

    # Charger l'AOC courante
    aoc_courante = state.terroir_current_aoc
    info_terroir = terroirs[aoc_courante]

    # Afficher les indices
    st.markdown("### Indices")
    indices = info_terroir["indices"]
    hints_shown = state.terroir_hints_shown

    for i in range(min(hints_shown + 1, len(indices))):
        emoji = ["🪨", "🌤️", "🍇"][i] if i < 3 else "💡"
        label = ["Sol", "Climat", "Cépage"][i] if i < 3 else f"Indice {i+1}"
        st.markdown(
            f'<div class="hint-card">{emoji} <strong>{label}</strong> : '
            f"{indices[i]}</div>",
            unsafe_allow_html=True,
        )

    # Bouton pour indice supplémentaire
    if hints_shown < len(indices) - 1:
        if st.button("Indice suivant (-1 point)", key="btn_hint"):
            state.terroir_hints_shown += 1
            st.rerun()

    # Carte de France avec contours AOC (sans noms)
    st.markdown("### Carte des appellations")
    _afficher_carte_france(gdf, aoc_courante, show_answer=False)

    # Propositions (4 choix)
    st.markdown("### Votre réponse")
    choix = state.get("terroir_choices", [])
    if not choix:
        choix = _generer_choix(aoc_courante, aoc_jouables, terroirs)
        state.terroir_choices = choix

    reponse = st.radio(
        "Quelle est cette appellation ?",
        choix,
        key=f"radio_terroir_{state.terroir_round}",
    )

    if st.button("Valider", key="btn_valider_terroir"):
        _valider_reponse(
            reponse, aoc_courante, info_terroir, gdf, production_df, aoc_jouables
        )


def _init_state(aoc_jouables: list):
    """Initialise le session_state pour le module terroir."""
    if "terroir_round" not in st.session_state:
        st.session_state.terroir_round = 0
    if "terroir_hints_shown" not in st.session_state:
        st.session_state.terroir_hints_shown = 0
    if "terroir_current_aoc" not in st.session_state or st.session_state.terroir_current_aoc is None:
        st.session_state.terroir_current_aoc = random.choice(aoc_jouables)
    if "terroir_choices" not in st.session_state:
        st.session_state.terroir_choices = []
    if "terroir_answered" not in st.session_state:
        st.session_state.terroir_answered = []


def _generer_choix(aoc_correcte: str, aoc_jouables: list, terroirs: dict) -> list:
    """Génère 4 choix dont la bonne réponse, en privilégiant la même région."""
    region_correcte = terroirs[aoc_correcte].get("region", "")

    # Distracteurs de la même région
    meme_region = [
        a for a in aoc_jouables
        if a != aoc_correcte and terroirs[a].get("region") == region_correcte
    ]
    # Distracteurs d'autres régions
    autres = [
        a for a in aoc_jouables
        if a != aoc_correcte and a not in meme_region
    ]

    distracteurs = []
    # Prendre 1-2 de la même région si possible
    if meme_region:
        distracteurs.extend(random.sample(meme_region, min(2, len(meme_region))))
    # Compléter avec d'autres régions
    nb_restant = 3 - len(distracteurs)
    if autres and nb_restant > 0:
        distracteurs.extend(random.sample(autres, min(nb_restant, len(autres))))
    # Compléter si nécessaire
    while len(distracteurs) < 3:
        pool = [a for a in aoc_jouables if a != aoc_correcte and a not in distracteurs]
        if pool:
            distracteurs.append(random.choice(pool))
        else:
            break

    choix = [aoc_correcte] + distracteurs[:3]
    random.shuffle(choix)
    return choix


def _afficher_carte_france(
    gdf: gpd.GeoDataFrame, aoc_cible: str, show_answer: bool = False
):
    """Affiche la carte Folium de France avec les contours AOC."""
    m = folium.Map(
        location=[46.8, 2.5],
        zoom_start=6,
        tiles="CartoDB positron",
    )

    # Ajouter les contours AOC colorés par dt
    for _, row in gdf.iterrows():
        dt = row.get("dt", "Autre")
        color = DT_COLORS.get(dt, "#888888")
        aoc_name = row.get("app", "Inconnu")

        # Mettre en évidence la bonne réponse si show_answer
        if show_answer and aoc_name == aoc_cible:
            style = {
                "fillColor": "#FFD700",
                "color": "#630d16",
                "weight": 3,
                "fillOpacity": 0.6,
            }
            popup_text = f"<b>{aoc_name}</b>"
        else:
            style = {
                "fillColor": color,
                "color": color,
                "weight": 1,
                "fillOpacity": 0.3,
            }
            popup_text = None if not show_answer else aoc_name

        geojson = folium.GeoJson(
            row.geometry.__geo_interface__,
            style_function=lambda x, s=style: s,
            popup=folium.Popup(popup_text, max_width=200) if popup_text else None,
        )
        geojson.add_to(m)

    # Zoom sur la cible si show_answer
    if show_answer:
        target = gdf[gdf["app"] == aoc_cible]
        if not target.empty:
            bounds = target.total_bounds  # [minx, miny, maxx, maxy]
            m.fit_bounds([[bounds[1], bounds[0]], [bounds[3], bounds[2]]])

    st_folium(m, width=700, height=450, key=f"map_terroir_{show_answer}")


def _valider_reponse(
    reponse: str,
    aoc_correcte: str,
    info_terroir: dict,
    gdf: gpd.GeoDataFrame,
    production_df: pd.DataFrame | None,
    aoc_jouables: list,
):
    """Valide la réponse du joueur et passe au round suivant."""
    state = st.session_state
    correct = reponse == aoc_correcte
    points = POINTS_PAR_INDICE.get(state.terroir_hints_shown, 1) if correct else 0

    state.score += points
    state.max_score += 3

    if correct:
        st.success(
            f"Bravo ! C'est bien **{aoc_correcte}** ! (+{points} points)"
        )
        # Ajouter à la cave
        if aoc_correcte not in state.get("unlocked_bottles", []):
            if "unlocked_bottles" not in state:
                state.unlocked_bottles = []
            state.unlocked_bottles.append(aoc_correcte)
    else:
        st.error(
            f"Raté ! La bonne réponse était **{aoc_correcte}**. "
            f"Vous avez répondu {reponse}."
        )

    # Feedback : carte zoomée sur la bonne AOC
    st.markdown(f"### {aoc_correcte} — {info_terroir['region']}")
    st.markdown(f"**Sol** : {info_terroir['sol']}")
    st.markdown(f"**Climat** : {info_terroir['climat']}")
    st.markdown(f"**Cépages** : {', '.join(info_terroir['cepages'])}")
    st.markdown(f"*{info_terroir['impact_geologique']}*")

    _afficher_carte_france(gdf, aoc_correcte, show_answer=True)

    # Données de production
    if production_df is not None:
        prod = production_df[production_df["appellation"] == aoc_correcte]
        if not prod.empty:
            st.markdown(f"**Production annuelle moyenne** : "
                       f"{prod['volume_hl'].mean():,.0f} hl")

    # Passer au round suivant
    state.terroir_round += 1
    state.terroir_hints_shown = 0
    state.terroir_choices = []
    state.terroir_answered.append(aoc_correcte)

    # Choisir une nouvelle AOC (pas déjà vue)
    restantes = [a for a in aoc_jouables if a not in state.terroir_answered]
    if restantes:
        state.terroir_current_aoc = random.choice(restantes)
    elif state.terroir_round < NB_ROUNDS:
        state.terroir_current_aoc = random.choice(aoc_jouables)


def _afficher_fin_partie():
    """Affiche l'écran de fin de partie."""
    state = st.session_state
    pct = (state.score / state.max_score * 100) if state.max_score > 0 else 0

    st.markdown("### Partie terminée !")
    st.markdown(
        f'<div class="score-badge">{state.score} / {state.max_score} points '
        f"({pct:.0f}%)</div>",
        unsafe_allow_html=True,
    )

    if pct >= 66:
        st.balloons()
        st.markdown("**Maître Sommelier** — Vous connaissez vos terroirs sur le bout des doigts !")
    elif pct >= 33:
        st.markdown("**Oenophile averti** — Beau parcours, continuez à explorer !")
    else:
        st.markdown("**Apprenti caviste** — Rome ne s'est pas faite en un jour, ni la Romanée-Conti !")

    if st.button("Rejouer", key="btn_rejouer_terroir"):
        state.terroir_round = 0
        state.terroir_hints_shown = 0
        state.terroir_current_aoc = None
        state.terroir_choices = []
        state.terroir_answered = []
        st.rerun()
