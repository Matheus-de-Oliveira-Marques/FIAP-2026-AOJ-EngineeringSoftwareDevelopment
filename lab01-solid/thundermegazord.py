import uuid

from abc import ABC, abstractmethod


class CalculadoraDesconto(ABC):
    @abstractmethod
    def calcular(self, valor: float) -> float:
        pass


class DescontoVIP(CalculadoraDesconto):
    def calcular(self, valor: float) -> float:
        return valor * 0.85


class DescontoPremium(CalculadoraDesconto):
    def calcular(self, valor: float) -> float:
        return valor * 0.90


class DescontoComum(CalculadoraDesconto):
    def calcular(self, valor: float) -> float:
        return valor * 0.95


class RepositorioPedido:
    def salvar(self, valor_final: float):
        pedido_id = str(uuid.uuid4())[:8]
        print(f"[LOG] Gravando dados no cristal de memória {pedido_id}...")
        print(f"[STATUS] Energia Final Requerida: R$ {valor_final:.2f}")


class ServicoNotificacao:
    def notificar(self, email: str):
        if email:
            print(f"[SINAL] Enviando telemetria para {email}...")


class CalculadoraFrete(ABC):
    @abstractmethod
    def calcular(self) -> float:
        pass


class FreteNorte(CalculadoraFrete):
    def calcular(self) -> float:
        return 50.0


class FreteNordeste(CalculadoraFrete):
    def calcular(self) -> float:
        return 40.0


class FreteSul(CalculadoraFrete):
    def calcular(self) -> float:
        return 30.0


class FretePadrao(CalculadoraFrete):
    def calcular(self) -> float:
        return 20.0


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
        estrategias_desconto = {
            "vip": DescontoVIP(),
            "premium": DescontoPremium(),
            "comum": DescontoComum(),
        }

        estrategia_atual = estrategias_desconto.get(tipo_cliente, DescontoComum())
        valor_total = estrategia_atual.calcular(valor_total)

        # 3. Propulsores de Frete (OCP Nightmare)
        regiao = pedido_data.get("regiao", "sudeste")
        estrategias_frete = {
            "norte": FreteNorte(),
            "nordeste": FreteNordeste(),
            "sul": FreteSul(),
        }
        estrategia_frete_atual = estrategias_frete.get(regiao, FretePadrao())
        frete = estrategia_frete_atual.calcular()
        valor_final = valor_total + frete

        # 4. Memória de Armazenamento (SRP/DIP Violation)
        RepositorioPedido().salvar(valor_final)

        print(f"[STATUS] Energia Final Requerida: R$ {valor_final:.2f}")

        # 5. Comunicação Intergaláctica (SRP/DIP Violation)

        ServicoNotificacao().notificar(pedido_data.get("email"))

        print("--- OPERAÇÃO MEGAZORD CONCLUÍDA ---")

        return True


if __name__ == "__main__":
    megazord = ThunderMegazord()
    missao = {
        "itens": ["Espada Thunder", "Escudo"],
        "valor_total": 5000.0,
        "tipo_cliente": "vip",
        "regiao": "norte",
        "email": "zordon@alameda.com",
    }
    megazord.processar_comando_central(missao)
