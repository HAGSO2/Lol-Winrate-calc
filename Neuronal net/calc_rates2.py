def calc_rates(df):
    # ==========================================================
    # 1. Inicializar todas las columnas nuevas
    # ==========================================================
    df["wins_vs_opponent"] = 0
    
    # Columnas contra el rival específico
    df["avg_dragons_vs_opp"] = 0.0
    df["avg_barons_vs_opp"] = 0.0
    df["avg_heralds_vs_opp"] = 0.0
    df["avg_towers_vs_opp"] = 0.0
    
    # Columnas globales del equipo (útil cuando no hay historial)
    df["avg_dragons_team"] = 0.0
    df["avg_barons_team"] = 0.0
    df["avg_heralds_team"] = 0.0
    df["avg_towers_team"] = 0.0
    
    # ==========================================================
    # 2. Diccionarios para acumular historial
    # ==========================================================
    # (equipo, rival) -> {wins, dragons_sum, barons_sum, ...}
    history_vs_opp = {}
    
    # equipo -> {games, dragons_sum, barons_sum, ...}
    history_team = {}
    
    # ==========================================================
    # 3. Bucle principal
    # ==========================================================
    for idx in range(len(df)):
        side = df.loc[idx, "side"]
        
        # Índice del rival
        opp_idx = idx + 1 if side else idx - 1
        if opp_idx < 0 or opp_idx >= len(df):
            continue
        
        team = df.loc[idx, "team"]
        opponent = df.loc[opp_idx, "team"]
        
        # Valores de la partida ACTUAL (aún no se han añadido al historial)
        dragons = df.loc[idx, "dragons"]
        barons = df.loc[idx, "barons"]
        heralds = df.loc[idx, "heralds"]
        towers = df.loc[idx, "towers"]
        
        # ----------------------------------------------------------
        # A) Estadísticas contra el rival específico
        # ----------------------------------------------------------
        key_opp = (team, opponent)
        hist_opp = history_vs_opp.get(key_opp, {
            "wins": 0, "games": 0,
            "dragons_sum": 0, "barons_sum": 0, 
            "heralds_sum": 0, "towers_sum": 0
        })
        
        df.loc[idx, "wins_vs_opponent"] = hist_opp["wins"]
        
        if hist_opp["games"] > 0:
            df.loc[idx, "avg_dragons_vs_opp"] = hist_opp["dragons_sum"] / hist_opp["games"]
            df.loc[idx, "avg_barons_vs_opp"] = hist_opp["barons_sum"] / hist_opp["games"]
            df.loc[idx, "avg_heralds_vs_opp"] = hist_opp["heralds_sum"] / hist_opp["games"]
            df.loc[idx, "avg_towers_vs_opp"] = hist_opp["towers_sum"] / hist_opp["games"]
        
        # ----------------------------------------------------------
        # B) Estadísticas globales del equipo
        # ----------------------------------------------------------
        hist_team = history_team.get(team, {
            "games": 0,
            "dragons_sum": 0, "barons_sum": 0,
            "heralds_sum": 0, "towers_sum": 0
        })
        
        if hist_team["games"] > 0:
            df.loc[idx, "avg_dragons_team"] = hist_team["dragons_sum"] / hist_team["games"]
            df.loc[idx, "avg_barons_team"] = hist_team["barons_sum"] / hist_team["games"]
            df.loc[idx, "avg_heralds_team"] = hist_team["heralds_sum"] / hist_team["games"]
            df.loc[idx, "avg_towers_team"] = hist_team["towers_sum"] / hist_team["games"]
        
        # ----------------------------------------------------------
        # C) Actualizar historial DESPUÉS de calcular (evita leakage)
        # ----------------------------------------------------------
        # Contra el rival
        hist_opp["games"] += 1
        hist_opp["dragons_sum"] += dragons
        hist_opp["barons_sum"] += barons
        hist_opp["heralds_sum"] += heralds
        hist_opp["towers_sum"] += towers
        if df.loc[idx, "result"] == 1:
            hist_opp["wins"] += 1
        history_vs_opp[key_opp] = hist_opp
        
        # Global del equipo
        hist_team["games"] += 1
        hist_team["dragons_sum"] += dragons
        hist_team["barons_sum"] += barons
        hist_team["heralds_sum"] += heralds
        hist_team["towers_sum"] += towers
        history_team[team] = hist_team
    
    return df