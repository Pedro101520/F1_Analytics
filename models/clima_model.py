class InfoClima:
    def __init__(self, clima, indice):
        self.temperatura = clima["daily"]["temperature_2m_max"][indice]
        self.chuva = clima["daily"]["precipitation_probability_max"][indice]
        self.vento = clima["daily"]["wind_speed_10m_max"][indice]
        self.umidade = clima["daily"]["relative_humidity_2m_mean"][indice]
        self.clima_texto = self.interpreta_code(clima["daily"]["weather_code"][indice])
        self.uv = self.formata_uv(clima["daily"]["uv_index_max"][indice]) 
    
    def formata_uv(self, uv):
        if uv <= 2:
            return f"{uv} · Baixo"
        elif uv >= 3 and uv <= 5.9:
            return f"{uv} · Moderado"
        elif uv >= 6 and uv <= 7.9:
            return f"{uv} · Alto"
        elif uv >= 8 and uv <= 10.9:
            return f"{uv} · Muito Alto"
        elif uv >= 11:
            return f"{uv} · Extremo"

    def interpreta_code(self, code):
        clima_code = {
            0: "Céu limpo",
            1: "Predominantemente limpo",
            2: "Parcialmente nublado",
            3: "Nublado",
            45: "Névoa",
            48: "Névoa com gelo",
            51: "Garoa leve",
            53: "Garoa moderada",
            55: "Garoa intensa",
            61: "Chuva leve",
            63: "Chuva moderada",
            65: "Chuva forte",
            71: "Neve leve",
            73: "Neve moderada",
            75: "Neve forte",
            80: "Pancadas leves",
            81: "Pancadas moderadas",
            82: "Pancadas fortes",
            95: "Trovoada",
            96: "Trovoada com granizo leve",
            99: "Trovoada com granizo forte",
        }
    
        return clima_code.get(code, " ")