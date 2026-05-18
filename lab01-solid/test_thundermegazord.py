import pytest
from thundermegazord import ThunderMegazord

def test_processamento_com_sucesso():
    megazord = ThunderMegazord()
    missao = {
        "itens": ["Item 1"],
        "valor_total": 100.0,
        "tipo_cliente": "vip",
        "regiao": "sul",
        "email": "teste@teste.com"
    }
    assert megazord.processar_comando_central(missao) is True

def test_falha_sem_itens():
    megazord = ThunderMegazord()
    missao = {
        "itens": [],
        "valor_total": 100.0,
        "tipo_cliente": "vip",
        "regiao": "sul",
        "email": "teste@teste.com"
    }
    assert megazord.processar_comando_central(missao) is False

def test_calculo_valor_vip_sul():
    # VIP: 15% de desconto (100 -> 85)
    # Sul: 30 de frete (85 + 30 = 115)
    megazord = ThunderMegazord()
    missao = {
        "itens": ["Item 1"],
        "valor_total": 100.0,
        "tipo_cliente": "vip",
        "regiao": "sul"
    }
    # Como o código usa prints, o teste valida o retorno booleano.
    # Em um lab avançado, poderíamos capturar o stdout para validar o valor final.
    assert megazord.processar_comando_central(missao) is True
