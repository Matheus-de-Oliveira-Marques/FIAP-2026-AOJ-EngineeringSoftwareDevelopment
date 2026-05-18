import uuid

class ThunderMegazord:
    """
    THUNDER MEGAZORD: Uma classe gigante que faz tudo ao mesmo tempo.
    Sua missão é desmontar este Megazord em componentes menores e especializados (SOLID).
    
    Violações:
    - SRP: Valida, calcula desconto, calcula frete, salva no banco e envia e-mail.
    - OCP: Adicionar novos descontos ou regiões exige abrir este peito de metal e soldar novo código.
    - DIP: Totalmente acoplado a implementações concretas de IO e Log.
    """
    
    def processar_comando_central(self, pedido_data: dict) -> bool:
        print("--- INICIANDO PROTOCOLO MEGAZORD ---")
        
        # 1. Sensores de Validação
        if not pedido_data.get("itens"):
            print("[ALERTA] Sistema sem munição (pedido sem itens)")
            return False
            
        # 2. Núcleo de Desconto (OCP Nightmare)
        valor_total = pedido_data.get("valor_total", 0.0)
        tipo_cliente = pedido_data.get("tipo_cliente", "comum")
        
        if tipo_cliente == "vip":
            valor_total *= 0.85
        elif tipo_cliente == "premium":
            valor_total *= 0.90
        else:
            valor_total *= 0.95
            
        # 3. Propulsores de Frete (OCP Nightmare)
        regiao = pedido_data.get("regiao", "sudeste")
        frete = 0.0
        if regiao == "norte":
            frete = 50.0
        elif regiao == "nordeste":
            frete = 40.0
        elif regiao == "sul":
            frete = 30.0
        else:
            frete = 20.0
            
        valor_final = valor_total + frete
        
        # 4. Memória de Armazenamento (SRP/DIP Violation)
        pedido_id = str(uuid.uuid4())[:8]
        print(f"[LOG] Gravando dados no cristal de memória {pedido_id}...")
        print(f"[STATUS] Energia Final Requerida: R$ {valor_final:.2f}")
        
        # 5. Comunicação Intergaláctica (SRP/DIP Violation)
        email = pedido_data.get("email")
        if email:
            print(f"[SINAL] Enviando telemetria para {email}...")
            
        print("--- OPERAÇÃO MEGAZORD CONCLUÍDA ---")
        return True

if __name__ == "__main__":
    megazord = ThunderMegazord()
    missao = {
        "itens": ["Espada Thunder", "Escudo"],
        "valor_total": 5000.0,
        "tipo_cliente": "vip",
        "regiao": "norte",
        "email": "zordon@alameda.com"
    }
    megazord.processar_comando_central(missao)
