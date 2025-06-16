import streamlit as st
import pandas as pd
import plotly.express as px

character_df = pd.read_csv(r"D:\sem 3\pai\PAI PROJECT\cleaned_data.csv", low_memory=False)
anime_df = pd.read_csv(r"D:\sem 3\pai\PAI PROJECT\archive\anime.csv", low_memory=False)
manga_df = pd.read_csv(r"D:\sem 3\pai\PAI PROJECT\archive (1)\manga.csv", low_memory=False)
if 'tags' in character_df.columns:
    character_df['tags'] = character_df['tags'].apply(eval)  # Parse stringified lists if needed

# Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Select a page", ["Home", "Anime Analysis", "Manga Analysis"])

# Home Page
if page == "Home":
    
    st.markdown("""
        <style>
            .header {
                background-color: #6C63FF;
                padding: 20px;
                border-radius: 8px;
                text-align: center;
                color: white;
                font-size: 2em;
                font-weight: bold;
            }
        </style>
    """, unsafe_allow_html=True)

    # Header
    st.markdown('<div class="header">OtakuLens</div>', unsafe_allow_html=True)

    # Main content
    st.write("Welcome! Use this tool to explore and filter anime characters based on various attributes like gender, hair color, and personality traits.")
    st.write("Choose your options from the menu below, and let’s dive into the anime world!")
    st.title("Anime Character Tag Selector")

    # GENDER selection
    gender = st.selectbox("Gender", ["None", "Male", "Female", "Other"])

    # HAIR COLOR selection
    hair_color = st.selectbox("Hair Color", ["Brown Hair", "Blue Hair", "Blonde Hair", "Black Hair", "Red Hair", "Magenta Hair", 
                "White Hair", "Grey Hair", "Orange Hair", "Purple Hair", "Green Hair", "Pink Hair", 
                "Multicolored Hair", "Turquoise Hair", "Gray Hair", "Other"])

    # EYE COLOR selection
    eye_color = st.selectbox("Eye Color", ["Black", 'Brown' ,'Purple', 'Grey' ,'Green', 'Blue' ,'Magenta', 'Red' ,'Yellow',
    'Pink','Turquoise', 'Orange', 'Brown Brown', 'Black Blue', 'White',
    'Black Black' ,'Green Red', 'Red Green' ,'Yellow Green' ,'Red Red',
    'Blue Black', 'Yellow Orange', 'Green Orange', 'Blue Yellow' ,'Grey Magenta',
    'Red Brown' ,'Green Brown' ,'Green Green' ,'Blue Purple' ,'Blue Green',
    'Red Orange' ,'Blue Grey' ,'Purple Yellow', 'Black Green' ,'Blue Magenta',
    'Brown Blue' ,'Black Red', 'Blue Blue'])

    # Section: CHARACTER TYPES AND TRAITS
    st.subheader("Character Traits")
    character_traits = ["Masochistic","Bassist","Gymnast","Sniper","Swimmer","Sailor","Tennis Player","Shamisen Player","Firefighter"
    ,"Werewolf","Exorcist","Wrestler","Magical Familiar","Volleyball Player","Musician","Cow","Rancher","Biker","Cyclist","Rapper"
    ,"Butler","Baseball Player","Poison User","Thief","Catgirl","Maid","Chef","Baker","Nurse","Bodyguard","Animal Lover","Kitsune","Shapeshifter","Transgender"
    ,"Soldier","Police","Mercenary","Martial Artist","Alchemist","Scientist","Chef","Dancer","Shaman","Teacher","Writer","Politician"
    ,"Leader","Gambler","Mechanic","Pirate","Reporter","Student","Ninja","Hunter","Witch","Tyrant","Clumsy","Traveler","Bounty Hunter","Cook"
    ,"Cyborg","Warrior","Swordsman","Scholar","Princess","Hero","Assassin","Heroine","Demon"
    ]
    # char_vars = []
    # for idx, trait in enumerate(character_traits):
    #     char_vars.append(st.checkbox(trait, key=f"char_{idx}"))
    char_vars = []
    for i in range(0, len(character_traits), 3):  # Loop through in steps of 3
        cols = st.columns(3)  # Create three columns
        for j, col in enumerate(cols):
            if i + j < len(character_traits):  # Check to avoid index error
                trait = character_traits[i + j]
                char_vars.append(col.checkbox(trait, key=f"char_{i + j}"))


    # Section: SUPERPOWERS AND ABILITIES
    st.subheader("Superpowers and Abilities")
    superpowers = ["Wind Powers","Ice Powers","Blood Power","Lightning Powers","Teleportation Powers","Time Manipulator","Darkness Powers","Invisibility Powers","Superpowers"
    ,"Psychic Powers","Shapeshifting","Healing Powers"]
    # power_vars = []
    # for idx, power in enumerate(superpowers):
    #     power_vars.append(st.checkbox(power, key=f"power_{idx}"))
    power_vars = []
    for i in range(0, len(superpowers), 3):
        cols = st.columns(3)
        for j, col in enumerate(cols):
            if i + j < len(superpowers):
                power = superpowers[i + j]
                power_vars.append(col.checkbox(power, key=f"power_{i + j}"))

    # Section: PHYSICAL FEATURES
    st.subheader("Physical Features")
    physical_features = ["Big Nose","Snaggletooth","Rosy Cheeks","Hair Antenna","Heterochromia","Claw Weapons","Eye Patch","Rapunzel Hair","Red Nose"
    ,"Sharp Teeth","Blinding Bangs","Bandages","Bindi","Sideburns","Pompadour","No Eyebrows","Freckles","Sunglasses","Bald","Unibrow"
    ,"Dreadlocks","Goggles","Monocle","Large Ears","Hair Buns","Ponytail","Bowl Cut","Buzz Cut","Verbal Tic"]
    # phys_vars = []
    # for idx, feature in enumerate(physical_features):
    #     phys_vars.append(st.checkbox(feature, key=f"phys_{idx}"))
    phys_vars = []
    for i in range(0, len(physical_features), 3):
        cols = st.columns(3)
        for j, col in enumerate(cols):
            if i + j < len(physical_features):
                feature = physical_features[i + j]
                phys_vars.append(col.checkbox(feature, key=f"phys_{i + j}"))


    # Section: PERSONALITY TRAITS
    st.subheader("Personality Traits")
    personality_traits = ["Comedic Relief","Eternal Optimist","Selfish","Stoic","Mischievous","Pacifist","Shy","Hyperactive","Cowardly","Bossy"
    ,"Sadistic","Arrogant","Cynical","Lazy","Loyal","Joker","Shrewd","Dandere","Tsundere","Yandere","Dojikko","Silly","Tomboyish","Pervert","Flamboyant","Analytical"]
    person_vars = []
    for i in range(0, len(personality_traits), 3):
        cols = st.columns(3)
        for j, col in enumerate(cols):
            if i + j < len(personality_traits):
                pertrait = personality_traits[i + j]
                person_vars.append(col.checkbox(pertrait, key=f"per_{i + j}"))


    # Section: CULTURAL REFERENCES
    st.subheader("Cultural References")
    cultural_references = ["Feudal Lord","Nobility","Historical Figure","King","Royalty","Shinto Priest","Samurai","Sakura","Ninja"
    ,"Monk","Geisha","Empress"]
    cult_vars = []
    for i in range(0, len(cultural_references), 3):
        cols = st.columns(3)
        for j, col in enumerate(cols):
            if i + j < len(cultural_references):
                ref =cultural_references[i + j]
                cult_vars.append(col.checkbox(ref, key=f"cult_{i + j}"))

    # Section: MISCELLANEOUS TRAITS
    st.subheader("Miscellaneous Traits")
    misc_traits = ["Zombie","Animal Ears","Exotic Eyes","Kawaii","Animal Hood","Tail","Tattoo","Gloves","Suspenders","Face Markings"
    ,"Piercings","Headband","Hats","Costumes","Toys","Clothing"]
    mis_vars = []
    for i in range(0, len(misc_traits), 3):
        cols = st.columns(3)
        for j, col in enumerate(cols):
            if i + j < len(misc_traits):
                mis =misc_traits[i + j]
                mis_vars.append(col.checkbox(mis, key=f"misc_{i + j}"))

    # Filter dataset based on selected filters
    def contains_any_tags(row_tags, selected_tags):
        return any(tag in row_tags for tag in selected_tags)

    def filter_dataset():
        # Collect selected tags
        selected_tags = []

        # Gather selected traits and features
        selected_tags.extend([trait for idx, trait in enumerate(character_traits) if char_vars[idx]])
        selected_tags.extend([power for idx, power in enumerate(superpowers) if power_vars[idx]])
        selected_tags.extend([feature for idx, feature in enumerate(physical_features) if phys_vars[idx]])
        selected_tags.extend([trait for idx, trait in enumerate(personality_traits) if person_vars[idx]])
        selected_tags.extend([reference for idx, reference in enumerate(cultural_references) if cult_vars[idx]])
        selected_tags.extend([trait for idx, trait in enumerate(misc_traits) if mis_vars[idx]])

        # Filter the DataFrame based on selected tags
        filtered_df = character_df.copy()

        if gender != "None":
            filtered_df = filtered_df[filtered_df['Gender'] == gender]
        if hair_color != "None":
            filtered_df = filtered_df[filtered_df['Hair color'] == hair_color]
        if eye_color != "None":
            filtered_df = filtered_df[filtered_df['Eye color'] == eye_color]

        if selected_tags:
            filtered_df = filtered_df[filtered_df['tags'].apply(lambda tags: contains_any_tags(tags, selected_tags))]

        return filtered_df, selected_tags

    # Button to apply filter
    if st.button("Submit Selection"):
        filtered_df, selected_tags = filter_dataset()
        
        # Display summary
        st.subheader("Summary of Selected Filters")
        st.write(f"Gender: {gender if gender != 'None' else 'Not selected'}")
        st.write(f"Hair Color: {hair_color if hair_color != 'None' else 'Not selected'}")
        st.write(f"Eye Color: {eye_color if eye_color != 'None' else 'Not selected'}")
        st.write(f"Tags: {', '.join(selected_tags) if selected_tags else 'None selected'}")

        # Display filtered data
        if filtered_df.empty:
            st.write("No results found!")
        else:
            st.dataframe(filtered_df)


elif page == "Anime Analysis":
    st.title("Anime Analysis")
    st.markdown("Explore trends and insights from the anime dataset!")

    # Sidebar filters for Anime Analysis
    st.sidebar.header("Anime Filters")
    selected_type = st.sidebar.multiselect("Select Anime Type", anime_df['type'].unique(), default=anime_df['type'].unique())
    selected_rating = st.sidebar.multiselect("Select Rating", anime_df['rating'].unique(), default=anime_df['rating'].unique())
    selected_year = st.sidebar.slider(
        "Select Start Year", 
        int(anime_df['start_year'].min()), 
        int(anime_df['start_year'].max()), 
        (2000, 2020)
    )

    # Filter anime dataset
    filtered_anime_df = anime_df[
        (anime_df['type'].isin(selected_type)) &
        (anime_df['rating'].isin(selected_rating)) &
        (anime_df['start_year'].between(*selected_year))
    ]

    # Top-rated Anime
    st.subheader("Top-Rated Anime")
    top_anime = filtered_anime_df.nlargest(10, 'score')[['title', 'score', 'members']]
    fig_top = px.bar(
        top_anime, x='score', y='title', orientation='h',
        title="Top 10 Highest Rated Anime",
        color='score', labels={'title': 'Anime Title', 'score': 'Score'}
    )
    st.plotly_chart(fig_top)

    # Anime Type Distribution
    st.subheader("Anime Type Distribution")
    type_count = filtered_anime_df['type'].value_counts()
    fig_type = px.pie(
        type_count, values=type_count.values, names=type_count.index,
        title="Distribution of Anime Types"
    )
    st.plotly_chart(fig_type)

    # Yearly Trends in Scores
    st.subheader("Yearly Trends in Anime Scores")
    yearly_avg_score = filtered_anime_df.groupby('start_year')['score'].mean().reset_index()
    fig_trends = px.line(
        yearly_avg_score, x='start_year', y='score',
        title="Average Anime Scores by Year",
        labels={'start_year': 'Year', 'score': 'Average Score'}
    )
    st.plotly_chart(fig_trends)

    # Genre Popularity
    #########fix this
    st.subheader("Genre Popularity by Member Count")
    genre_df = filtered_anime_df[['genres', 'members']].dropna()
    genre_exploded = genre_df.assign(genres=genre_df['genres'].str.split(',')).explode('genres')
    genre_popularity = genre_exploded.groupby('genres')['members'].sum().reset_index().nlargest(10, 'members')
    fig_genres = px.bar(
        genre_popularity, x='members', y='genres', orientation='h',
        title="Top 10 Popular Genres",
        labels={'genres': 'Genre', 'members': 'Member Count'}
    )
    st.plotly_chart(fig_genres)


    # Average Score by Rating
    st.subheader("Average Score by Rating")
    avg_score_rating = filtered_anime_df.groupby('rating')['score'].mean().reset_index().sort_values('score', ascending=False)
    fig_rating = px.bar(
        avg_score_rating, x='rating', y='score',
        title="Average Score by Rating",
        labels={'rating': 'Rating', 'score': 'Average Score'},
        color='score', color_continuous_scale='Blues'
    )
    st.plotly_chart(fig_rating)

    
    # 2. Average Score by Genre
    st.subheader("Average Score by Genre")

    # Filter rows where genres are not null or empty
    valid_genres = filtered_anime_df[
        filtered_anime_df['genres'].notna() & 
        (filtered_anime_df['genres'] != '[]')
    ]

    # Explode the genres column to process individual genres
    genre_exploded = valid_genres.copy()
    genre_exploded['genres'] = genre_exploded['genres'].apply(eval)  # Convert stringified list to list
    genre_exploded = genre_exploded.explode('genres')  # Split list into individual rows

    # Group by genres and calculate the average score
    avg_score_genre = genre_exploded.groupby('genres')['score'].mean().reset_index()

    # Create a bar chart for average score by genre
    fig_genre_score = px.bar(
        avg_score_genre, x='genres', y='score',
        title="Average Score by Genre",
        labels={'genres': 'Genre', 'score': 'Average Score'},
        color='score', color_continuous_scale='Blues'
    )

    st.plotly_chart(fig_genre_score)


    # 4. Anime by Start Year
    st.subheader("Anime by Start Year")
    anime_count_by_year = filtered_anime_df['start_year'].value_counts().sort_index()
    fig_yearly_count = px.line(
        anime_count_by_year, x=anime_count_by_year.index, y=anime_count_by_year.values,
        title="Anime Releases by Start Year",
        labels={'x': 'Start Year', 'y': 'Count'}
    )
    st.plotly_chart(fig_yearly_count)

    # 5. Most Common Genres
    ############3fix this
    st.subheader("Most Common Genres")
    common_genres = genre_exploded['genres'].value_counts().head(10)
    fig_genre_popularity = px.bar(
        common_genres, x=common_genres.index, y=common_genres.values,
        title="Most Common Genres",
        labels={'x': 'Genre', 'y': 'Count'}
    )
    st.plotly_chart(fig_genre_popularity)

    # 7. Popular Studios
    st.subheader("Popular Studios")

    # Filter rows where studios are not null or empty
    valid_studios = filtered_anime_df[
        filtered_anime_df['studios'].notna() & 
        (filtered_anime_df['studios'] != '[]')
    ]

    # Parse and explode the studios column
    studios_exploded = valid_studios.copy()
    studios_exploded['studios'] = studios_exploded['studios'].apply(eval)  # Convert stringified list to list
    studios_exploded = studios_exploded.explode('studios')  # Split list into individual rows

    # Count the occurrences of each studio and take the top 10
    studio_counts = studios_exploded['studios'].value_counts().head(10)

    # Create a bar chart for the top 10 popular studios
    fig_popular_studios = px.bar(
        x=studio_counts.index, y=studio_counts.values,
        title="Top 10 Popular Studios",
        labels={'x': 'Studio', 'y': 'Count'},
        text=studio_counts.values
    )

    # Add data labels for clarity
    fig_popular_studios.update_traces(textposition='outside')

    st.plotly_chart(fig_popular_studios)



    # 9. Rating Distribution
    st.subheader("Rating Distribution")
    rating_count = filtered_anime_df['rating'].value_counts()
    fig_rating_dist = px.pie(
        rating_count, values=rating_count.values, names=rating_count.index,
        title="Rating Distribution"
    )
    st.plotly_chart(fig_rating_dist)

    # 10. Seasonal Trends
    st.subheader("Seasonal Trends")
    filtered_anime_df['start_season'] = filtered_anime_df['start_season'].fillna('Unknown')
    season_count = filtered_anime_df['start_season'].value_counts()
    fig_season_trends = px.bar(
        season_count, x=season_count.index, y=season_count.values,
        title="Seasonal Trends",
        labels={'x': 'Season', 'y': 'Count'}
    )
    st.plotly_chart(fig_season_trends)

    # 11. Duration Analysis
    st.subheader("Duration Analysis")
    fig_duration_box = px.box(
        filtered_anime_df, x='type', y='episode_duration',
        title="Duration Analysis by Type",
        labels={'type': 'Anime Type', 'episode_duration': 'Episode Duration'}
    )
    st.plotly_chart(fig_duration_box)

    # 12. Favorite Counts by Genre

    st.subheader("Favorite Counts by Genre")

    # Filter rows where genres are not null or empty
    valid_genres = filtered_anime_df[
        filtered_anime_df['genres'].notna() & 
        (filtered_anime_df['genres'] != '[]')
    ]

    # Explode the genres column to count individual genres
    genre_exploded = valid_genres.copy()
    genre_exploded['genres'] = genre_exploded['genres'].apply(eval)  # Convert stringified list to list
    genre_exploded = genre_exploded.explode('genres')  # Split list into individual rows

    # Group by genres and calculate total favorites
    genre_favorites = genre_exploded.groupby('genres')['favorites'].sum().reset_index()

    # Sort and select top 10 genres
    genre_favorites = genre_favorites.nlargest(10, 'favorites')

    # Create a bar chart for favorite counts by genre
    fig_genre_favorites = px.bar(
        genre_favorites, x='genres', y='favorites',
        title="Favorite Counts by Genre",
        labels={'genres': 'Genre', 'favorites': 'Favorite Count'}
    )

    st.plotly_chart(fig_genre_favorites)



    # 14. Demographics
    st.subheader("Demographics")

    # Filter rows where demographics are not null or empty
    valid_demographics = filtered_anime_df[
        filtered_anime_df['demographics'].notna() & 
        (filtered_anime_df['demographics'] != '[]')
    ]

    # Explode the demographics column to count individual demographics
    demographic_exploded = valid_demographics.copy()
    demographic_exploded['demographics'] = demographic_exploded['demographics'].apply(eval)  # Convert stringified list to list
    demographic_exploded = demographic_exploded.explode('demographics')  # Split list into individual rows

    # Group by demographics and count occurrences
    demographic_count = demographic_exploded['demographics'].value_counts().reset_index()
    demographic_count.columns = ['Demographic', 'Count']

    # Create a bar chart for demographics distribution
    fig_demographics = px.bar(
        demographic_count, x='Demographic', y='Count',
        title="Demographics Distribution",
        labels={'Demographic': 'Demographic', 'Count': 'Count'}
    )

    st.plotly_chart(fig_demographics)

    # Search Anime
    st.subheader("Search Anime")
    search_term = st.text_input("Search by Anime Title or Synopsis")
    if search_term:
        search_results = anime_df[
            anime_df['title'].str.contains(search_term, case=False, na=False) | 
            anime_df['synopsis'].str.contains(search_term, case=False, na=False)
        ]
        if not search_results.empty:
            st.write(search_results[['title', 'type', 'score', 'members','genres']])
        else:
            st.warning("No results found!")

elif page == "Manga Analysis":
    st.title("Manga Analysis")
    st.markdown("Explore trends and insights from the manga dataset!")

    # Sidebar Filters
    st.sidebar.header("Manga Filters")
    selected_type = st.sidebar.multiselect("Select Manga Type", manga_df['type'].dropna().unique(), default=manga_df['type'].dropna().unique())
    selected_status = st.sidebar.multiselect("Select Status", manga_df['status'].dropna().unique(), default=manga_df['status'].dropna().unique())

    # Date Handling
    manga_df['published_from'] = pd.to_datetime(manga_df['published_from'], errors='coerce')
    valid_published_from = manga_df['published_from'].dropna()
    valid_years = valid_published_from.dt.year

    if not valid_years.empty:
        selected_year = st.sidebar.slider(
            "Select Start Year", 
            int(valid_years.min()), 
            int(valid_years.max()), 
            (2000, 2020)
        )

    # Apply Filters
    filtered_manga_df = manga_df[
        (manga_df['type'].isin(selected_type)) &
        (manga_df['status'].isin(selected_status)) &
        (manga_df['published_from'].dt.year.between(*selected_year))
    ]

    if filtered_manga_df.empty:
        st.warning("No manga matches the selected filters.")
    else:
        # Top-Rated Manga
        st.subheader("Top-Rated Manga")
        top_manga = filtered_manga_df.nlargest(10, 'score')[['title', 'score', 'members']]
        fig_top_manga = px.bar(
            top_manga, x='score', y='title', orientation='h',
            title="Top 10 Highest Rated Manga",
            color='score', labels={'title': 'Manga Title', 'score': 'Score'}
        )
        st.plotly_chart(fig_top_manga)

        # Manga Type Distribution
        st.subheader("Manga Type Distribution")
        type_count_manga = filtered_manga_df['type'].value_counts()
        fig_type_manga = px.pie(
            type_count_manga, values=type_count_manga.values, names=type_count_manga.index,
            title="Distribution of Manga Types"
        )
        st.plotly_chart(fig_type_manga)

        # Yearly Trends in Scores
        st.subheader("Yearly Trends in Manga Scores")
        yearly_avg_score_manga = filtered_manga_df.groupby(filtered_manga_df['published_from'].dt.year)['score'].mean().reset_index()
        fig_trends_manga = px.line(
            yearly_avg_score_manga, x='published_from', y='score',
            title="Average Manga Scores by Year",
            labels={'published_from': 'Year', 'score': 'Average Score'}
        )
        st.plotly_chart(fig_trends_manga)

        # Genre Popularity by Member Count
        st.subheader("Genre Popularity by Member Count")
        genre_df_manga = filtered_manga_df[['genres', 'members']].dropna()
        genre_df_manga['genres'] = genre_df_manga['genres'].apply(eval)  # Convert stringified list to list
        genre_exploded_manga = genre_df_manga.explode('genres')
        genre_popularity_manga = genre_exploded_manga.groupby('genres')['members'].sum().reset_index().nlargest(10, 'members')
        fig_genres_manga = px.bar(
            genre_popularity_manga, x='members', y='genres', orientation='h',
            title="Top 10 Popular Manga Genres",
            labels={'genres': 'Genre', 'members': 'Member Count'}
        )
        st.plotly_chart(fig_genres_manga)

        # Average Score by Genre
        # st.subheader("Average Score by Genre")
        # avg_score_genre_manga = manga_df.groupby('genres')['score'].mean().reset_index()
        # fig_genre_score_manga = px.bar(
        #     avg_score_genre_manga, x='genres', y='score',
        #     title="Average Score by Genre",
        #     labels={'genres': 'Genre', 'score': 'Average Score'},
        #     color='score', color_continuous_scale='Blues'
        # )
        # st.plotly_chart(fig_genre_score_manga)
        st.subheader("Average Score by Genre")

# Filter rows where genres are not null or empty
    valid_genres_manga = manga_df[
        manga_df['genres'].notna() & 
        (manga_df['genres'] != '[]')
    ]

    # Explode the genres column to process individual genres
    genre_exploded_manga = valid_genres_manga.copy()
    genre_exploded_manga['genres'] = genre_exploded_manga['genres'].apply(eval)  # Convert stringified list to list
    genre_exploded_manga = genre_exploded_manga.explode('genres')  # Split list into individual rows

    # Group by genres and calculate the average score
    avg_score_genre_manga = genre_exploded_manga.groupby('genres')['score'].mean().reset_index()

    # Create a bar chart for average score by genre
    fig_genre_score_manga = px.bar(
        avg_score_genre_manga, x='genres', y='score',
        title="Average Score by Genre",
        labels={'genres': 'Genre', 'score': 'Average Score'},
        color='score', color_continuous_scale='Blues'
    )

    st.plotly_chart(fig_genre_score_manga)

        # Search Functionality
    st.subheader("Search Manga by Title")

    # User input for searching manga titles
    search_query = st.text_input("Enter a keyword to search for manga titles:")

    # Filter manga dataset based on search query
    if search_query.strip():  # Ensure the search query is not empty
        search_results = manga_df[manga_df['title'].str.contains(search_query, case=False, na=False)]
        if not search_results.empty:
            st.write(f"Showing results for **'{search_query}'**:")
            st.dataframe(search_results[['title', 'type', 'score','demographics', 'published_from', 'synopsis']])
        else:
            st.write(f"No results found for **'{search_query}'**.")
    else:
        st.write("Enter a keyword above to search for manga titles.")
st.markdown("""
    <style>
        .footer {
            background-color: #333333;
            padding: 10px 10px; /* Adjust padding for better size */
            color: white;
            font-size: 1em;
            text-align: center;
            position: fixed;
            bottom: 0;
            left: 0;
            width: 100%; /* Ensure full width */
            z-index: 100; /* Bring footer above other content */
        }
        /* Override Streamlit's default padding */
        .main .block-container {
            padding-bottom: 50px; /* Adjust to avoid content overlap with footer */
        }
    </style>
""", unsafe_allow_html=True)


st.markdown('<div class="footer">Created by Fatima Khan | 4+4 = ATE </div>', unsafe_allow_html=True)
