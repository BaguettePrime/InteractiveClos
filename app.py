"""
Le Clos Interactif — Application Streamlit ludo-éducative sur le vin français.

Point d'entrée : navigation entre les 4 modules et initialisation du session_state.
"""

from pathlib import Path

import streamlit as st
import pandas as pd
import geopandas as gpd

from styles.custom_css import inject_css
from modules import timeline, terroir, sommelier, cave

# === Configuration de la page ===
st.set_page_config(
    page_title="Le Clos Interactif",
    page_icon="🍇",
    layout="wide",
    initial_sidebar_state="expanded",
)

# === Injection du CSS ===
inject_css()

# === Chemins des données ===
DATA_DIR = Path(__file__).resolve().parent / "data"
GEOJSON_PATH = DATA_DIR / "aoc_simplified.geojson"
CSV_PATH = DATA_DIR / "production_aoc.csv"


# === Chargement des données (avec cache) ===
@st.cache_data
def charger_geojson() -> gpd.GeoDataFrame | None:
    """Charge le GeoJSON des AOC viticoles."""
    if GEOJSON_PATH.exists():
        gdf = gpd.read_file(GEOJSON_PATH)
        return gdf
    return None


@st.cache_data
def charger_production() -> pd.DataFrame | None:
    """Charge le CSV de production viticole."""
    if CSV_PATH.exists():
        return pd.read_csv(CSV_PATH, encoding="utf-8")
    return None


# === Initialisation du session_state ===
DEFAULT_STATE = {
    "score": 0,
    "max_score": 0,
    "current_module": "accueil",
    "timeline_step": 0,
    "terroir_round": 0,
    "terroir_hints_shown": 0,
    "terroir_current_aoc": None,
    "sommelier_wine_index": 0,
    "sommelier_step": 0,
    "unlocked_bottles": [],
}

for key, default in DEFAULT_STATE.items():
    if key not in st.session_state:
        st.session_state[key] = default


# === Chargement des données ===
gdf = charger_geojson()
production_df = charger_production()


# === Sidebar — Navigation ===
with st.sidebar:
    st.markdown("# 🍇 Le Clos Interactif")
    st.markdown('<hr class="gold-separator">', unsafe_allow_html=True)

    module = st.radio(
        "Navigation",
        ["Accueil", "L'Épopée du Vin", "Terroir Geoguessr",
         "Le Sommelier Virtuel", "La Cave aux Trésors"],
        key="nav_radio",
    )

    st.markdown('<hr class="gold-separator">', unsafe_allow_html=True)

    # Score global
    score = st.session_state.score
    max_score = st.session_state.max_score
    st.markdown(f"**Score** : {score} pts")
    if max_score > 0:
        st.progress(score / max_score)

    # Bouteilles débloquées
    nb_bottles = len(st.session_state.unlocked_bottles)
    st.markdown(f"**Cave** : {nb_bottles} bouteille{'s' if nb_bottles != 1 else ''}")

    st.markdown('<hr class="gold-separator">', unsafe_allow_html=True)

    # Status des données
    st.markdown("##### Données")
    if gdf is not None:
        st.markdown(f"✅ GeoJSON : {len(gdf)} AOC")
    else:
        st.markdown("⚠️ GeoJSON non disponible")

    if production_df is not None:
        st.markdown(f"✅ Production : {len(production_df)} lignes")
    else:
        st.markdown("⚠️ CSV production non disponible")


def _afficher_accueil(gdf, production_df):
    """Page d'accueil de l'application."""
    st.markdown("# 🍇 Le Clos Interactif")
    st.markdown(
        "### *Explorez le patrimoine viticole français à travers "
        "4 expériences ludiques et éducatives*"
    )

    st.markdown('<hr class="gold-separator">', unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(
            """
            <div class="wine-card">
                <h3>📜 L'Épopée du Vin</h3>
                <p>Traversez 2 600 ans d'histoire viticole française,
                des amphores grecques aux vins nature.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.markdown(
            """
            <div class="wine-card">
                <h3>🗺️ Terroir Geoguessr</h3>
                <p>Devinez les appellations à partir d'indices sur le sol,
                le climat et les cépages. Carte interactive incluse !</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            """
            <div class="wine-card">
                <h3>🍷 Le Sommelier Virtuel</h3>
                <p>Dégustation à l'aveugle en 3 étapes : analysez l'œil,
                le nez et la bouche pour identifier le vin.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.markdown(
            """
            <div class="wine-card">
                <h3>🏆 La Cave aux Trésors</h3>
                <p>Collectionnez des bouteilles en jouant ! Chaque bonne
                réponse enrichit votre cave personnelle.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown('<hr class="gold-separator">', unsafe_allow_html=True)

    # Mini stats
    if production_df is not None:
        st.markdown("### La France viticole en chiffres")
        c1, c2, c3, c4 = st.columns(4)
        with c1:
            nb_aoc = production_df["appellation"].nunique()
            st.metric("Appellations", nb_aoc)
        with c2:
            vol_total = production_df[production_df["annee"] == 2019]["volume_hl"].sum()
            st.metric("Production 2019", f"{vol_total / 1e6:.1f} M hl")
        with c3:
            if gdf is not None:
                st.metric("Régions cartographiées", gdf["dt"].nunique() if "dt" in gdf.columns else "—")
        with c4:
            st.metric("Années de données", "2009-2019")

    st.markdown(
        "*Sélectionnez un module dans la barre latérale pour commencer l'aventure !*"
    )


# === Routage des modules ===
if module == "Accueil":
    _afficher_accueil(gdf, production_df)
elif module == "L'Épopée du Vin":
    timeline.render(production_df)
elif module == "Terroir Geoguessr":
    terroir.render(gdf, production_df)
elif module == "Le Sommelier Virtuel":
    sommelier.render(gdf, production_df)
elif module == "La Cave aux Trésors":
    cave.render(gdf, production_df)
