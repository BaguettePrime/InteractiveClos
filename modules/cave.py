"""
Module 4 — La Cave aux Trésors.

Grille visuelle des bouteilles débloquées par le joueur
dans les modules Terroir et Sommelier.
"""

import streamlit as st
import pandas as pd
import geopandas as gpd
import folium
from streamlit_folium import st_folium

from data.wine_knowledge import WINE_KNOWLEDGE


# Liste des AOC affichables dans la cave (toutes celles avec des données terroir)
TOUTES_AOC = list(WINE_KNOWLEDGE["terroirs"].keys())


def render(
    gdf: gpd.GeoDataFrame | None = None,
    production_df: pd.DataFrame | None = None,
):
    """Affiche le module Cave aux Trésors."""
    st.markdown("# La Cave aux Trésors")
    st.markdown(
        "*Votre collection personnelle de bouteilles débloquées "
        "au fil de vos explorations.*"
    )
    st.markdown('<hr class="gold-separator">', unsafe_allow_html=True)

    unlocked = st.session_state.get("unlocked_bottles", [])
    total = len(TOUTES_AOC)
    nb_unlocked = len([b for b in unlocked if b in TOUTES_AOC])

    # Barre de progression
    pct = nb_unlocked / total if total > 0 else 0
    st.progress(pct)

    # Titre adaptatif
    if pct >= 0.66:
        titre_niveau = "Maître Sommelier"
        msg = "Votre cave est impressionnante !"
    elif pct >= 0.33:
        titre_niveau = "Oenophile averti"
        msg = "Belle collection, continuez l'exploration !"
    else:
        titre_niveau = "Apprenti caviste"
        msg = "Chaque bouteille débloquée enrichit votre savoir."

    st.markdown(
        f'<div class="score-badge">{titre_niveau}</div> '
        f"<span>{nb_unlocked}/{total} bouteilles — {msg}</span>",
        unsafe_allow_html=True,
    )

    st.markdown('<hr class="gold-separator">', unsafe_allow_html=True)

    # Grille de bouteilles
    cols_per_row = 3
    for i in range(0, len(TOUTES_AOC), cols_per_row):
        cols = st.columns(cols_per_row)
        for j, col in enumerate(cols):
            idx = i + j
            if idx >= len(TOUTES_AOC):
                break
            aoc = TOUTES_AOC[idx]
            is_unlocked = aoc in unlocked

            with col:
                if is_unlocked:
                    _afficher_bouteille_debloquee(aoc, gdf, production_df)
                else:
                    _afficher_bouteille_verrouillee(aoc)


def _afficher_bouteille_debloquee(
    aoc: str,
    gdf: gpd.GeoDataFrame | None,
    production_df: pd.DataFrame | None,
):
    """Affiche une card de bouteille débloquée."""
    terroir = WINE_KNOWLEDGE["terroirs"].get(aoc, {})
    region = terroir.get("region", "France")
    couleur = terroir.get("couleur_principale", "rouge")

    # Emoji selon la couleur
    emoji_map = {
        "rouge": "🍷",
        "blanc": "🥂",
        "rosé": "🌸",
        "effervescent": "🍾",
    }
    emoji = emoji_map.get(couleur, "🍷")

    # Volume de production
    volume_text = ""
    if production_df is not None:
        prod = production_df[production_df["appellation"] == aoc]
        if not prod.empty:
            vol_moyen = prod["volume_hl"].mean()
            volume_text = f"{vol_moyen:,.0f} hl/an"

    st.markdown(
        f"""
        <div class="wine-card">
            <div style="font-size: 2rem; text-align: center;">{emoji}</div>
            <h3 style="text-align: center; margin: 0.3rem 0; font-size: 1.1rem;">{aoc}</h3>
            <p style="text-align: center; font-style: italic; margin: 0; font-size: 0.85rem;">{region}</p>
            <p style="text-align: center; color: #888; font-size: 0.8rem; margin: 0.2rem 0;">
                {couleur.capitalize()} {('— ' + volume_text) if volume_text else ''}
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Mini-carte dans un expander
    if gdf is not None:
        with st.expander(f"Voir {aoc} sur la carte"):
            target = gdf[gdf["app"] == aoc]
            if not target.empty:
                bounds = target.total_bounds
                center_lat = (bounds[1] + bounds[3]) / 2
                center_lon = (bounds[0] + bounds[2]) / 2
                m = folium.Map(
                    location=[center_lat, center_lon],
                    zoom_start=10,
                    tiles="CartoDB positron",
                )
                folium.GeoJson(
                    target.geometry.values[0].__geo_interface__,
                    style_function=lambda x: {
                        "fillColor": "#630d16",
                        "color": "#AF9B60",
                        "weight": 2,
                        "fillOpacity": 0.5,
                    },
                ).add_to(m)
                st_folium(m, width=250, height=200, key=f"cave_map_{aoc}")


def _afficher_bouteille_verrouillee(aoc: str):
    """Affiche une card de bouteille verrouillée."""
    st.markdown(
        f"""
        <div class="wine-card-locked">
            <div style="font-size: 2rem;">🔒</div>
            <p style="margin: 0.3rem 0; font-size: 0.9rem; color: #999;">???</p>
            <p style="font-size: 0.75rem; color: #bbb;">
                Jouez aux modules Terroir ou Sommelier pour débloquer
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )
