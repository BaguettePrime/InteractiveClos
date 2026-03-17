"""
Module 3 — Le Sommelier Virtuel.

Dégustation à l'aveugle en 3 étapes : Oeil, Nez, Bouche.
Le joueur doit deviner le cépage, la région et l'appellation.
"""

import random
from pathlib import Path

import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
import geopandas as gpd

from data.wine_knowledge import WINE_KNOWLEDGE

ASSETS_DIR = Path(__file__).resolve().parent.parent / "assets" / "labels"

ETAPES = ["oeil", "nez", "bouche"]
ETAPES_LABELS = {"oeil": "L'Oeil", "nez": "Le Nez", "bouche": "La Bouche"}
ETAPES_EMOJI = {"oeil": "👁️", "nez": "👃", "bouche": "👅"}


def render(
    gdf: gpd.GeoDataFrame | None = None,
    production_df: pd.DataFrame | None = None,
):
    """Affiche le module Sommelier Virtuel."""
    st.markdown("# Le Sommelier Virtuel")
    st.markdown(
        "*Entraînez votre palais virtuel : analysez le vin étape par étape "
        "et devinez l'appellation.*"
    )
    st.markdown('<hr class="gold-separator">', unsafe_allow_html=True)

    degustations = WINE_KNOWLEDGE["degustations"]
    if not degustations:
        st.warning("Aucune donnée de dégustation disponible.")
        return

    _init_state(degustations)
    state = st.session_state

    # Score
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Vin", f"{state.sommelier_wine_index + 1}/{len(degustations)}")
    with col2:
        st.metric("Score", f"{state.score}")

    # Partie terminée ?
    if state.sommelier_wine_index >= len(degustations):
        _afficher_fin(degustations)
        return

    vin = degustations[state.sommelier_wine_index]
    step = state.sommelier_step  # 0=oeil, 1=nez, 2=bouche, 3=réponse, 4=révélation

    st.markdown('<hr class="gold-separator">', unsafe_allow_html=True)

    # Étapes de dégustation (0-2)
    if step <= 2:
        etape_nom = ETAPES[step]
        emoji = ETAPES_EMOJI[etape_nom]
        label = ETAPES_LABELS[etape_nom]

        st.markdown(f"### {emoji} {label}")

        # Afficher les étapes précédentes
        for i in range(step):
            prev_nom = ETAPES[i]
            _afficher_etape(vin, prev_nom, collapsed=True)

        # Étape courante
        _afficher_etape(vin, etape_nom, collapsed=False)

        if st.button("Étape suivante", key=f"btn_next_step_{step}"):
            state.sommelier_step += 1
            st.rerun()

    # Étape réponse (3)
    elif step == 3:
        st.markdown("### Votre analyse")

        # Afficher un résumé des 3 étapes
        for etape_nom in ETAPES:
            _afficher_etape(vin, etape_nom, collapsed=True)

        st.markdown('<hr class="gold-separator">', unsafe_allow_html=True)
        st.markdown("### Devinez le vin !")

        # Choix du cépage
        all_cepages = list(set(
            d["cepage"] for d in degustations
        ))
        random.seed(state.sommelier_wine_index + 100)
        if len(all_cepages) > 6:
            cepages_choix = [vin["cepage"]] + random.sample(
                [c for c in all_cepages if c != vin["cepage"]],
                min(3, len(all_cepages) - 1),
            )
        else:
            cepages_choix = all_cepages
        random.shuffle(cepages_choix)

        rep_cepage = st.selectbox(
            "Cépage principal",
            cepages_choix,
            key=f"sel_cepage_{state.sommelier_wine_index}",
        )

        # Choix de la région
        all_regions = list(set(d["region"] for d in degustations))
        rep_region = st.selectbox(
            "Région",
            sorted(all_regions),
            key=f"sel_region_{state.sommelier_wine_index}",
        )

        # Choix de l'appellation
        all_aoc = list(set(d["aoc"] for d in degustations))
        rep_aoc = st.selectbox(
            "Appellation",
            sorted(all_aoc),
            key=f"sel_aoc_{state.sommelier_wine_index}",
        )

        if st.button("Révéler", key="btn_reveler"):
            # Calculer les points
            points = 0
            if rep_cepage == vin["cepage"]:
                points += 1
            if rep_region == vin["region"]:
                points += 1
            if rep_aoc == vin["aoc"]:
                points += 2

            state.score += points
            state.max_score += 4
            state.sommelier_step = 4
            state.sommelier_last_points = points
            state.sommelier_last_answers = {
                "cepage": rep_cepage,
                "region": rep_region,
                "aoc": rep_aoc,
            }
            st.rerun()

    # Révélation (4)
    elif step == 4:
        points = state.get("sommelier_last_points", 0)
        answers = state.get("sommelier_last_answers", {})

        if points >= 3:
            st.success(f"Excellent ! {points}/4 points !")
        elif points >= 1:
            st.warning(f"Pas mal ! {points}/4 points.")
        else:
            st.error(f"Raté ! {points}/4 points.")

        # Tableau de résultats
        st.markdown("| | Votre réponse | Bonne réponse |")
        st.markdown("|---|---|---|")
        st.markdown(
            f"| **Cépage** | {answers.get('cepage', '?')} | "
            f"{'✅' if answers.get('cepage') == vin['cepage'] else '❌'} {vin['cepage']} |"
        )
        st.markdown(
            f"| **Région** | {answers.get('region', '?')} | "
            f"{'✅' if answers.get('region') == vin['region'] else '❌'} {vin['region']} |"
        )
        st.markdown(
            f"| **Appellation** | {answers.get('aoc', '?')} | "
            f"{'✅' if answers.get('aoc') == vin['aoc'] else '❌'} {vin['aoc']} |"
        )

        # Image d'étiquette ou fallback
        _afficher_etiquette(vin)

        # Ajouter à la cave si bien répondu sur l'AOC
        if answers.get("aoc") == vin["aoc"]:
            if "unlocked_bottles" not in state:
                state.unlocked_bottles = []
            if vin["aoc"] not in state.unlocked_bottles:
                state.unlocked_bottles.append(vin["aoc"])

        # Données de production
        if production_df is not None:
            prod = production_df[production_df["appellation"] == vin["aoc"]]
            if not prod.empty:
                st.markdown(
                    f"**Production moyenne** : {prod['volume_hl'].mean():,.0f} hl/an"
                )

        # Mini-carte
        if gdf is not None:
            target = gdf[gdf["app"] == vin["aoc"]]
            if not target.empty:
                st.markdown("**Localisation**")
                bounds = target.total_bounds
                center_lat = (bounds[1] + bounds[3]) / 2
                center_lon = (bounds[0] + bounds[2]) / 2
                m = folium.Map(location=[center_lat, center_lon], zoom_start=9, tiles="CartoDB positron")
                folium.GeoJson(
                    target.geometry.values[0].__geo_interface__,
                    style_function=lambda x: {
                        "fillColor": "#630d16",
                        "color": "#AF9B60",
                        "weight": 2,
                        "fillOpacity": 0.5,
                    },
                    popup=folium.Popup(vin["aoc"], max_width=200),
                ).add_to(m)
                st_folium(m, width=400, height=300, key=f"map_somm_{state.sommelier_wine_index}")

        # Bouton suivant
        if st.button("Vin suivant", key="btn_next_wine"):
            state.sommelier_wine_index += 1
            state.sommelier_step = 0
            st.rerun()


def _init_state(degustations: list):
    """Initialise le session_state pour le module sommelier."""
    if "sommelier_wine_index" not in st.session_state:
        st.session_state.sommelier_wine_index = 0
    if "sommelier_step" not in st.session_state:
        st.session_state.sommelier_step = 0


def _afficher_etape(vin: dict, etape: str, collapsed: bool):
    """Affiche les détails d'une étape de dégustation."""
    emoji = ETAPES_EMOJI[etape]
    label = ETAPES_LABELS[etape]
    data = vin.get(etape, {})

    if collapsed:
        with st.expander(f"{emoji} {label}", expanded=False):
            for cle, valeur in data.items():
                st.markdown(f"**{cle.replace('_', ' ').title()}** : {valeur}")
    else:
        for cle, valeur in data.items():
            st.markdown(
                f'<div class="hint-card"><strong>{cle.replace("_", " ").title()}</strong> '
                f": {valeur}</div>",
                unsafe_allow_html=True,
            )


def _afficher_etiquette(vin: dict):
    """Affiche l'image de l'étiquette ou un fallback CSS."""
    aoc_slug = vin["aoc"].lower().replace(" ", "_").replace("-", "_").replace("'", "")
    image_path = ASSETS_DIR / f"{aoc_slug}.jpg"

    if image_path.exists():
        st.image(str(image_path), caption=vin["aoc"], width=300)
    else:
        # Fallback : card CSS stylisée
        st.markdown(
            f"""
            <div class="label-card">
                <div class="wine-name">{vin['aoc']}</div>
                <div class="wine-region">{vin['region']}</div>
                <div style="font-size: 3rem; margin: 0.5rem 0;">🍷</div>
                <div style="color: #ccc; font-size: 0.9rem;">
                    {vin['cepage']} — {vin.get('couleur', 'rouge')}
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )


def _afficher_fin(degustations: list):
    """Affiche l'écran de fin du module sommelier."""
    state = st.session_state
    total = len(degustations) * 4
    pct = (state.score / total * 100) if total > 0 else 0

    st.markdown("### Dégustation terminée !")
    st.markdown(
        f'<div class="score-badge">{state.score} / {total} points ({pct:.0f}%)</div>',
        unsafe_allow_html=True,
    )

    if pct >= 66:
        st.balloons()
        st.markdown("**Maître Sommelier** — Votre palais est remarquable !")
    elif pct >= 33:
        st.markdown("**Oenophile averti** — Vous avez du nez !")
    else:
        st.markdown("**Apprenti caviste** — Continuez à déguster, c'est en forgeant...")

    if st.button("Recommencer", key="btn_restart_somm"):
        state.sommelier_wine_index = 0
        state.sommelier_step = 0
        st.rerun()
