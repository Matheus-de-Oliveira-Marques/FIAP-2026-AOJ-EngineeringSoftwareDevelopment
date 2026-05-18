import uuid

class ProcessadorPedido:
    """
    CLASSE MONSTRO: Esta classe viola múltiplos princípios SOLID.
    - SRP: Faz tudo (validação, desconto, frete, persistência, notificação).
    - OCP: Se surgir um novo tipo de desconto ou frete, precisa editar esta classe.
    - DIP: Depende de implementações concretas (instancia serviços internamente).
    """
    
    def processar(self, pedido_data: dict) -> bool:
        # 1. Validação de Dados (Responsabilidade de Validação)
        if not pedido_data.get("itens"):
            print("Erro: Pedido sem itens")
            return False
            
        # 2. Cálculo de Desconto (Violação de OCP - Acoplamento com tipos de cliente)
        valor_total = pedido_data.get("valor_total", 0.0)
        tipo_cliente = pedido_data.get("tipo_cliente", "comum")
        
        if tipo_cliente == "vip":
            valor_total *= 0.85  # 15% de desconto
        elif tipo_cliente == "premium":
            valor_total *= 0.90  # 10% de desconto
        else:
            valor_total *= 0.95  # 5% de desconto (padrão)
            
        # 3. Cálculo de Frete (Violação de OCP - Acoplamento com regiões)
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
        
        # 4. Persistência (Violação de SRP/DIP - Conhecimento de IO/Banco)
        pedido_id = str(uuid.uuid4())[:8]
        print(f"Salvando pedido {pedido_id} no Banco de Dados...")
        print(f"Valor Final: R$ {valor_final:.2f}")
        
        # 5. Notificação (Violação de SRP/DIP - Conhecimento de E-mail)
        email = pedido_data.get("email")
        if email:
            print(f"Enviando e-mail de confirmação para {email}...")
            
        return True

# Exemplo de uso rápido para teste manual
if __name__ == "__main__":
    p = ProcessadorPedido()
    pedido = {
        "itens": ["Laptop", "Mouse"],
        "valor_total": 1000.0,
        "tipo_cliente": "vip",
        "regiao": "sul",
        "email": "aluno@fiap.com.br"
    }
    p.processar(pedido)
