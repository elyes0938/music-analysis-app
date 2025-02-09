import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Load the dataset
data = pd.read_csv('songs_normalize.csv')

# Streamlit Configuration
st.set_page_config(page_title="Analyse Musicale", layout="wide")

# Page d'accueil
def homepage():
    st.markdown("""
        <div style="background-color: #1f77b4; padding: 50px; border-radius: 20px; text-align: center; display: flex; flex-direction: column; align-items: center;">
            <div style="display: flex; gap: 20px; justify-content: center;">
                <span style="font-size: 48px; color: white;">🎵</span>
                <h1 style="color: white; font-size: 48px;">Bienvenue sur l'Application d'Analyse Musicale</h1>
                <span style="font-size: 48px; color: white;">🎶</span>
            </div>
            <p style="color: white; font-size: 20px;">Découvrez quel style de musique maximise les ventes grâce à nos analyses interactives.</p>
            <h3 style="color: white;">"Explorez, Analysez, Ressentez la musique comme jamais auparavant!" 🎧</h3>
            <a href="/?page=dashboard" style="background-color: white; color: #1f77b4; padding: 15px 30px; text-decoration: none; border-radius: 10px; font-weight: bold; font-size: 20px;">Accéder au Dashboard</a>
        </div>
    """, unsafe_allow_html=True)

# Dashboard
def dashboard():
    st.title("Dashboard d'Analyse Musicale")

    # Popularité par Artiste (Line Chart)
    st.subheader("Évolution de la Popularité par Artiste")
    selected_artist = st.selectbox("Sélectionnez un artiste:", data['artist'].unique())
    artist_data = data[data['artist'] == selected_artist]
    fig2 = px.line(artist_data, x='year', y='popularity', title=f'Popularité de {selected_artist} au fil du temps', markers=True, color_discrete_sequence=['#1f77b4'])
    st.plotly_chart(fig2)

    # Corrélation entre Tempo et Energy
    st.subheader("Corrélation entre Tempo et Énergie")
    fig3 = px.scatter(data, x='tempo', y='energy', title='Corrélation entre Tempo et Énergie', color_discrete_sequence=['#1f77b4'])
    st.plotly_chart(fig3)

    st.markdown("""
    #### Interprétation de la Corrélation entre Tempo et Énergie
    Cette visualisation montre la relation entre le **tempo** (vitesse de la musique) et **l'énergie** des morceaux. 
    - **Observation principale :** Il y a une concentration de morceaux avec des niveaux d'énergie élevés (proche de 1) sur une large plage de tempo, entre 80 et 160 BPM.
    - **Interprétation :** Les morceaux à haute énergie ne sont pas limités à des tempos rapides, ce qui suggère que d'autres facteurs influencent l'énergie d'un morceau, comme la densité sonore ou l'instrumentation.
    - **Insight clé :** L'énergie ne dépend pas uniquement du tempo ; des morceaux à tempo modéré peuvent aussi être très énergiques.
    """)

    # Matrice de Corrélation
    st.subheader("Matrice de Corrélation")
    numeric_data = data.select_dtypes(include='number')
    correlation_matrix = numeric_data.corr()
    fig4 = px.imshow(correlation_matrix, text_auto=True, title='Matrice de Corrélation des Variables Numériques', width=1000, height=800, color_continuous_scale='Blues')
    st.plotly_chart(fig4)

    # Boxplots Dynamiques
    st.subheader("Boxplot Dynamique")
    selected_boxplot_col = st.selectbox("Sélectionnez une colonne pour afficher son Boxplot:", numeric_data.columns)
    fig_box = px.box(data, y=selected_boxplot_col, title=f'Boxplot de {selected_boxplot_col}', color_discrete_sequence=['#1f77b4'])
    st.plotly_chart(fig_box)

    # Histogramme Dynamique
    st.subheader("Histogramme Dynamique")
    selected_hist_col = st.selectbox("Sélectionnez une colonne pour afficher son Histogramme:", numeric_data.columns)
    fig_hist = px.histogram(data, x=selected_hist_col, nbins=30, title=f'Histogramme de {selected_hist_col}', color_discrete_sequence=['#1f77b4'])
    st.plotly_chart(fig_hist)

    # Popularité vs Énergie
    st.subheader("Popularité vs Énergie")
    fig_scatter = px.scatter(data, x='popularity', y='energy', color='artist', title='Popularité vs Énergie par Artiste', color_discrete_sequence=px.colors.sequential.Blues)
    st.plotly_chart(fig_scatter)

    # Distribution de la Danceability par Genre
    st.subheader("Distribution de la Danceability par Genre")
    fig5 = px.box(data, x='genre', y='danceability', title='Distribution de la Danceability par Genre', color_discrete_sequence=['#1f77b4'])
    st.plotly_chart(fig5)

    # Relation entre Acousticness et Valence
    st.subheader("Relation entre Acousticness et Valence")
    fig6 = px.scatter(data, x='acousticness', y='valence', color='genre', title='Relation entre Acousticness et Valence', color_discrete_sequence=px.colors.sequential.Blues)
    st.plotly_chart(fig6)

    # Interprétation
    st.markdown("""
    ### Interprétations
    - **Évolution de la Popularité par Artiste :** Visualise la tendance de la popularité d'un artiste au fil du temps.
    - **Corrélation entre Tempo et Énergie :** Met en évidence la relation entre le tempo et l'énergie des morceaux.
    - **Matrice de Corrélation :** Affiche les corrélations entre les variables numériques avec des teintes de bleu.
    - **Boxplot Dynamique :** Visualisation interactive des distributions de données.
    - **Histogramme Dynamique :** Permet d'explorer la distribution des différentes variables.
    - **Popularité vs Énergie :** Analyse de la relation entre la popularité et l'énergie des chansons.
    - **Distribution de la Danceability par Genre :** Comparaison des genres musicaux.
    - **Relation entre Acousticness et Valence :** Analyse de la relation entre l'acoustique et la valence.
    """)

# Navigation
page = st.query_params.get("page", "home")

if page == "dashboard":
    dashboard()
else:
    homepage()
