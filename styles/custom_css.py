"""
Styles CSS centralisés pour Le Clos Interactif.

Charte graphique :
- Fond crème : #fdfaf5
- Texte anthracite : #2c2c2c
- Accent vin : #630d16
- Bordure dorée : #AF9B60
- Titres : Playfair Display (serif)
- Corps : Lato (sans-serif)
"""

import streamlit as st


def inject_css():
    """Injecte les styles CSS globaux dans l'application Streamlit."""
    st.markdown(_GLOBAL_CSS, unsafe_allow_html=True)


_GLOBAL_CSS = """
<style>
/* === Import Google Fonts === */
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,700;1,400&family=Lato:wght@300;400;700&display=swap');

/* === Variables CSS === */
:root {
    --bg-cream: #fdfaf5;
    --text-anthracite: #2c2c2c;
    --accent-wine: #630d16;
    --border-gold: #AF9B60;
    --font-heading: 'Playfair Display', serif;
    --font-body: 'Lato', sans-serif;
}

/* === Corps principal === */
.stApp, .main .block-container {
    background-color: var(--bg-cream) !important;
    color: var(--text-anthracite) !important;
    font-family: var(--font-body) !important;
}

/* === Titres === */
h1, h2, h3 {
    font-family: var(--font-heading) !important;
    color: var(--accent-wine) !important;
}
h1 { font-size: 2.5rem !important; }
h2 { font-size: 1.8rem !important; }
h3 { font-size: 1.4rem !important; }

/* === Paragraphes === */
p, li, label, .stMarkdown {
    font-family: var(--font-body) !important;
    color: var(--text-anthracite) !important;
    line-height: 1.6 !important;
}

/* === Sidebar === */
[data-testid="stSidebar"] {
    background-color: #f5efe6 !important;
    border-right: 2px solid var(--border-gold) !important;
}
[data-testid="stSidebar"] h1,
[data-testid="stSidebar"] h2,
[data-testid="stSidebar"] h3 {
    color: var(--accent-wine) !important;
}

/* === Boutons === */
.stButton > button {
    background-color: var(--accent-wine) !important;
    color: #fff !important;
    border: none !important;
    border-radius: 8px !important;
    font-family: var(--font-body) !important;
    font-weight: 700 !important;
    padding: 0.5rem 1.5rem !important;
    transition: all 0.3s ease !important;
}
.stButton > button:hover {
    background-color: #8b1a25 !important;
    box-shadow: 0 4px 12px rgba(99, 13, 22, 0.3) !important;
    transform: translateY(-1px) !important;
}
.stButton > button:active {
    transform: translateY(0) !important;
}

/* === Selectbox === */
.stSelectbox > div > div {
    border: 1px solid var(--border-gold) !important;
    border-radius: 8px !important;
    font-family: var(--font-body) !important;
}

/* === Radio === */
.stRadio > div {
    font-family: var(--font-body) !important;
}

/* === Expander === */
.streamlit-expanderHeader {
    background-color: #f5efe6 !important;
    border: 1px solid var(--border-gold) !important;
    border-radius: 8px !important;
    font-family: var(--font-heading) !important;
    color: var(--accent-wine) !important;
}

/* === Progress bar === */
.stProgress > div > div > div {
    background-color: var(--accent-wine) !important;
}

/* === Cards génériques === */
.wine-card {
    background: #fff;
    border: 1px solid var(--border-gold);
    border-radius: 8px;
    padding: 1.5rem;
    margin: 0.5rem 0;
    box-shadow: 0 2px 8px rgba(0,0,0,0.05);
    transition: transform 0.2s ease, box-shadow 0.2s ease;
}
.wine-card:hover {
    transform: translateY(-2px);
    box-shadow: 0 4px 16px rgba(0,0,0,0.1);
}

/* === Card verrouillée === */
.wine-card-locked {
    background: #e8e4de;
    border: 1px solid #ccc;
    border-radius: 8px;
    padding: 1.5rem;
    margin: 0.5rem 0;
    text-align: center;
    opacity: 0.6;
    filter: grayscale(100%);
}

/* === Timeline === */
.timeline-container {
    position: relative;
    padding-left: 40px;
    margin: 1rem 0;
}
.timeline-container::before {
    content: '';
    position: absolute;
    left: 15px;
    top: 0;
    bottom: 0;
    width: 3px;
    background: linear-gradient(to bottom, var(--accent-wine), var(--border-gold));
}
.timeline-item {
    position: relative;
    margin-bottom: 2rem;
    padding: 1rem 1.5rem;
    background: #fff;
    border: 1px solid var(--border-gold);
    border-radius: 8px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.05);
}
.timeline-item::before {
    content: '';
    position: absolute;
    left: -33px;
    top: 1.2rem;
    width: 14px;
    height: 14px;
    background: var(--accent-wine);
    border: 3px solid var(--border-gold);
    border-radius: 50%;
}
.timeline-date {
    font-family: var(--font-heading);
    color: var(--accent-wine);
    font-weight: 700;
    font-size: 1.1rem;
    margin-bottom: 0.3rem;
}
.timeline-title {
    font-family: var(--font-heading);
    font-size: 1.3rem;
    color: var(--text-anthracite);
    margin-bottom: 0.5rem;
}
.timeline-description {
    font-family: var(--font-body);
    color: var(--text-anthracite);
    line-height: 1.6;
}

/* === Séparateur doré === */
.gold-separator {
    border: none;
    height: 2px;
    background: linear-gradient(to right, transparent, var(--border-gold), transparent);
    margin: 2rem 0;
}

/* === Score badge === */
.score-badge {
    display: inline-block;
    background: var(--accent-wine);
    color: #fff;
    font-family: var(--font-heading);
    font-size: 1.2rem;
    padding: 0.3rem 1rem;
    border-radius: 20px;
    margin: 0.5rem 0;
}

/* === Indice card === */
.hint-card {
    background: linear-gradient(135deg, #fff 0%, #f5efe6 100%);
    border-left: 4px solid var(--accent-wine);
    border-radius: 0 8px 8px 0;
    padding: 1rem 1.5rem;
    margin: 0.5rem 0;
    font-family: var(--font-body);
}

/* === Étiquette fallback === */
.label-card {
    background: linear-gradient(135deg, #2c2c2c 0%, #630d16 100%);
    color: #fff;
    border: 2px solid var(--border-gold);
    border-radius: 8px;
    padding: 2rem;
    text-align: center;
    font-family: var(--font-heading);
    min-height: 200px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}
.label-card .wine-name {
    font-size: 1.5rem;
    font-weight: 700;
    margin-bottom: 0.5rem;
    color: var(--border-gold);
}
.label-card .wine-region {
    font-size: 1rem;
    font-style: italic;
    color: #ddd;
}

/* === Grille cave === */
.cave-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
    gap: 1rem;
    padding: 1rem 0;
}

/* === Masquer le header Streamlit par défaut === */
header[data-testid="stHeader"] {
    background-color: var(--bg-cream) !important;
}

/* === Tabs === */
.stTabs [data-baseweb="tab-list"] {
    gap: 2px;
}
.stTabs [data-baseweb="tab"] {
    font-family: var(--font-heading) !important;
    color: var(--text-anthracite) !important;
}
.stTabs [aria-selected="true"] {
    color: var(--accent-wine) !important;
    border-bottom-color: var(--accent-wine) !important;
}

/* === Metric === */
[data-testid="stMetricValue"] {
    font-family: var(--font-heading) !important;
    color: var(--accent-wine) !important;
}
</style>
"""
