"""
Module 1 — L'Épopée du Vin.

Chronologie verticale CSS custom du vin français,
enrichie de graphiques Plotly (évolution des volumes de production).
"""

import streamlit as st
import pandas as pd
import plotly.express as px
from data.wine_knowledge import WINE_KNOWLEDGE


def render(production_df: pd.DataFrame | None = None):
    """Affiche le module Timeline."""
    st.markdown("# L'Épopée du Vin")
    st.markdown(
        "*Traversez 2 600 ans d'histoire viticole française, "
        "des amphores grecques aux vins nature.*"
    )
    st.markdown('<hr class="gold-separator">', unsafe_allow_html=True)

    history = WINE_KNOWLEDGE["history"]

    # Chronologie verticale CSS
    st.markdown('<div class="timeline-container">', unsafe_allow_html=True)

    for i, etape in enumerate(history):
        # Card de la timeline
        st.markdown(
            f"""
            <div class="timeline-item">
                <div class="timeline-date">{etape['date']}</div>
                <div class="timeline-title">{etape['titre']}</div>
                <div class="timeline-description">{etape['description']}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        # Anecdote de comptoir
        with st.expander(f"Anecdote de Comptoir {etape['date']}"):
            st.markdown(f"*{etape['anecdote']}*")

        # Graphique Plotly pour les époques contemporaines si données disponibles
        if etape.get("epoque") == "contemporain" and production_df is not None:
            _afficher_graphique_production(etape, production_df, i)

    st.markdown("</div>", unsafe_allow_html=True)

    # Graphique global d'évolution de la production
    if production_df is not None:
        st.markdown('<hr class="gold-separator">', unsafe_allow_html=True)
        st.markdown("### Production viticole française (2009-2019)")
        st.markdown(
            "*Données basées sur les volumes de production par AOC. "
            "Notez l'impact dramatique du gel 2016-2017.*"
        )
        _afficher_graphique_global(production_df)


def _afficher_graphique_production(
    etape: dict, df: pd.DataFrame, index: int
):
    """Affiche un graphique Plotly contextuel pour une étape de la timeline."""
    if "gel" in etape["titre"].lower() or "bio" in etape["titre"].lower() or index >= 6:
        # Montrer l'impact du gel ou l'évolution récente
        df_annuel = (
            df.groupby("annee")["volume_hl"]
            .sum()
            .reset_index()
        )
        df_annuel["volume_mhl"] = df_annuel["volume_hl"] / 1_000_000

        fig = px.bar(
            df_annuel,
            x="annee",
            y="volume_mhl",
            title="Volume total de production (millions d'hectolitres)",
            labels={"annee": "Année", "volume_mhl": "Volume (M hl)"},
            color="volume_mhl",
            color_continuous_scale=["#630d16", "#AF9B60"],
        )
        fig.update_layout(
            plot_bgcolor="rgba(0,0,0,0)",
            paper_bgcolor="rgba(0,0,0,0)",
            font=dict(family="Lato, sans-serif", color="#2c2c2c"),
            showlegend=False,
            coloraxis_showscale=False,
        )
        fig.update_xaxes(dtick=1)
        st.plotly_chart(fig, use_container_width=True)


def _afficher_graphique_global(df: pd.DataFrame):
    """Affiche le graphique global d'évolution de la production par couleur."""
    df_couleur = (
        df.groupby(["annee", "couleur"])["volume_hl"]
        .sum()
        .reset_index()
    )
    df_couleur["volume_mhl"] = df_couleur["volume_hl"] / 1_000_000

    couleur_map = {
        "rouge": "#630d16",
        "blanc": "#AF9B60",
        "rosé": "#e8a0b4",
        "effervescent": "#d4af37",
    }

    fig = px.area(
        df_couleur,
        x="annee",
        y="volume_mhl",
        color="couleur",
        title="Évolution par type de vin",
        labels={"annee": "Année", "volume_mhl": "Volume (M hl)", "couleur": "Type"},
        color_discrete_map=couleur_map,
    )
    fig.update_layout(
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        font=dict(family="Lato, sans-serif", color="#2c2c2c"),
    )
    fig.update_xaxes(dtick=1)
    st.plotly_chart(fig, use_container_width=True)
