# Lab Autoguiado: Missão Refactoring & SOLID 🚀

Neste laboratório, você assumirá o papel de Engenheiro(a) de Software Sênior. Você acabou de herdar um sistema crítico legado (o temido *Thunder Megazord*) que está impossibilitando a evolução técnica da empresa devido ao seu alto acoplamento e múltiplas responsabilidades.

Sua missão é desmontar esse "Megazord" em componentes menores, especializados e fáceis de testar, aplicando os princípios do **SOLID**.

⏱️ **Tempo Estimado:** 30 minutos

---

## 🎯 Objetivo Final
Refatorar a classe `ThunderMegazord` para que ela não viole os princípios **SRP** (Responsabilidade Única) e **OCP** (Aberto-Fechado), sem quebrar os testes automatizados já existentes.

**Critério de Sucesso:** Executar o comando `pytest` no terminal e obter **100% de sucesso (Verde)** após todas as refatorações.

---

## 🗺️ Passo 1: Acesso, Setup e Briefing do Problema
1. Acesse o link do repositório da disciplina no GitHub fornecido pelo professor.
2. No repositório, clique no botão verde **`<> Code`**.
3. Selecione a aba **`Codespaces`** e clique no botão **`+`** (ou `Create codespace on main`).
4. Aguarde o ambiente carregar no seu navegador. Abra um Terminal (`Ctrl+J` ou `Cmd+J`) e navegue até a pasta do lab:
   ```bash
   cd lab01-solid
   ```
5. **Briefing do Problema:** Abra o arquivo `thundermegazord.py` e leia o código. Ele é o que chamamos de *God Class* (Faz tudo). Resumo do desastre:
   * **Problema 1 (SRP):** Ele mistura lógica de negócio com infraestrutura (print simulando banco de dados e envio de e-mail).
   * **Problema 2 (OCP):** Ele tem `if/else` gigantes para Descontos e Fretes. Toda vez que o marketing inventa uma promoção nova, você tem que abrir esse arquivo e adicionar mais um `if`.
6. Rode os testes para garantir que o Megazord está rodando (mesmo sendo feio):
   ```bash
   pytest test_thundermegazord.py -v
   ```
   *Se estiver verde, hora de começar a desmontar!*

---

## ✂️ Passo 2: O Princípio da Responsabilidade Única (SRP)
O arquivo possui funções de IO (banco e e-mail) misturadas com regras de negócio. Vamos extrair isso.

**1. Remova do Megazord:**
```python
# Apague isso na classe principal:
pedido_id = str(uuid.uuid4())[:8]
print(f"[LOG] Gravando dados no cristal de memória {pedido_id}...")

email = pedido_data.get("email")
if email:
    print(f"[SINAL] Enviando telemetria para {email}...")
```

**2. Crie as novas classes (no topo do arquivo ou em um novo arquivo):**
```python
class RepositorioPedido:
    def salvar(self, valor_final: float):
        pedido_id = str(uuid.uuid4())[:8]
        print(f"[LOG] Gravando dados no cristal de memória {pedido_id}...")
        print(f"[STATUS] Energia Final Requerida: R$ {valor_final:.2f}")

class ServicoNotificacao:
    def notificar(self, email: str):
        if email:
            print(f"[SINAL] Enviando telemetria para {email}...")
```

**3. Utilize as classes extraídas no Megazord:**
```python
# No final do método processar_comando_central, adicione:
RepositorioPedido().salvar(valor_final)
ServicoNotificacao().notificar(pedido_data.get("email"))
```
*Rode `pytest`. Continuou verde? Menos peso no Megazord!*

---

## 🧩 Passo 3: O Princípio Aberto-Fechado (OCP) - Descontos
Vamos remover o pesadelo de Ifs usando o **Strategy Pattern**.

**1. Remova do Megazord:**
```python
# Apague isso:
if tipo_cliente == "vip":
    valor_total *= 0.85
elif tipo_cliente == "premium":
    valor_total *= 0.90
else:
    valor_total *= 0.95
```

**2. Crie a Interface e as Estratégias Concretas (no topo do arquivo):**
```python
from abc import ABC, abstractmethod

class CalculadoraDesconto(ABC):
    @abstractmethod
    def calcular(self, valor: float) -> float: pass

class DescontoVIP(CalculadoraDesconto):
    def calcular(self, valor: float) -> float: return valor * 0.85

class DescontoPremium(CalculadoraDesconto):
    def calcular(self, valor: float) -> float: return valor * 0.90

class DescontoComum(CalculadoraDesconto):
    def calcular(self, valor: float) -> float: return valor * 0.95
```

**3. Crie a Factory no Megazord e calcule dinamicamente:**
```python
# Substitua onde ficavam os "ifs" por isto:
estrategias_desconto = {
    "vip": DescontoVIP(),
    "premium": DescontoPremium(),
    "comum": DescontoComum()
}

estrategia_atual = estrategias_desconto.get(tipo_cliente, DescontoComum())
valor_total = estrategia_atual.calcular(valor_total)
```
*Rode `pytest` novamente. Extensibilidade de desconto adicionada com sucesso.*

---

## 🚚 Passo 4: O Princípio Aberto-Fechado (OCP) - Fretes
Vamos aplicar o exato mesmo padrão (Strategy) para limpar a lógica de Regiões.

**1. Remova do Megazord:**
```python
# Apague isso:
frete = 0.0
if regiao == "norte":
    frete = 50.0
elif regiao == "nordeste":
    frete = 40.0
elif regiao == "sul":
    frete = 30.0
else:
    frete = 20.0
```

**2. Crie a Interface e as Estratégias Concretas (no topo do arquivo):**
```python
class CalculadoraFrete(ABC):
    @abstractmethod
    def calcular(self) -> float: pass

class FreteNorte(CalculadoraFrete):
    def calcular(self) -> float: return 50.0

class FreteNordeste(CalculadoraFrete):
    def calcular(self) -> float: return 40.0

class FreteSul(CalculadoraFrete):
    def calcular(self) -> float: return 30.0

class FretePadrao(CalculadoraFrete):
    def calcular(self) -> float: return 20.0
```

**3. Crie a Factory no Megazord e calcule o frete dinamicamente:**
```python
# Substitua onde ficavam os "ifs" de frete por isto:
estrategias_frete = {
    "norte": FreteNorte(),
    "nordeste": FreteNordeste(),
    "sul": FreteSul()
}

estrategia_frete_atual = estrategias_frete.get(regiao, FretePadrao())
frete = estrategia_frete_atual.calcular()
```

**Validação Final:**
Execute seu último teste:
```bash
pytest test_thundermegazord.py -v
```

Se tudo estiver verde, **missão cumprida!** Você desmontou o Megazord e salvou o projeto do caos arquitetural.
