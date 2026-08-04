def extraer_enfrentamientos(df, team_a, team_b):
    """
    Extrae todas las filas de enfrentamientos entre team_a y team_b.
    Usa operaciones vectorizadas de pandas (muy rápido).
    """
    # Paso 1: Encontrar los gameid donde jugaron AMBOS equipos
    # groupby agrupa por gameid, y apply(set) crea un conjunto con los 2 equipos
    teams_por_game = df.groupby('gameid')['team'].apply(set)
    
    # Filtramos los gameid donde están team_a Y team_b
    gameids_validos = teams_por_game[
        teams_por_game.apply(lambda equipos: team_a in equipos and team_b in equipos)
    ].index
    
    # Paso 2: Extraer todas las filas de esos gameid
    df_enfrentamientos = df[df['gameid'].isin(gameids_validos)].copy()
    
    return df_enfrentamientos