import numpy as np
import pandas as pd

def calc_rates(df):
    
    # ==========================================================
    # 1. Winrate con el campeón en las últimas 30 partidas
    # ==========================================================
    
    for i in range(1, 6):
    
        player_col = f"p{i}_name"
        champ_col = f"p{i}_champion"
    
        new_col = f"p{i}_champion_last30_winrate"
    
        # Historial por jugador + campeón
        df.insert(5+(17*(i-1)),new_col,(
            round(df.groupby([player_col, champ_col])["result"]
              .transform(lambda s: s.shift(1).rolling(30, min_periods=1).mean()),3)
        ))
        
        df[new_col] = df[new_col].fillna(0)
    
    # ==========================================================
    # 2. Número de victorias históricas contra el rival
    # ==========================================================
    
    df["wins_vs_opponent"] = 0
    
    # Diccionario:
    # (equipo, rival) -> victorias del equipo sobre el rival
    history = {}
    
    for idx in range(len(df)):
    
        side = df.loc[idx, "side"]
    
        # Obtener índice del rival
        if side:
            opp_idx = idx + 1
        else:
            opp_idx = idx - 1
    
        if opp_idx < 0 or opp_idx >= len(df):
            continue
    
        team = df.loc[idx, "team"]
        opponent = df.loc[opp_idx, "team"]
    
        # Número de victorias previas
        df.loc[idx, "wins_vs_opponent"] = history.get((team, opponent), 0)
    
        # Actualizar historial únicamente si gana esta partida
        if df.loc[idx, "result"] == 1:
            history[(team, opponent)] = history.get((team, opponent), 0) + 1
    
    # =========================
    # Devolver resultado
    # =========================
    return df