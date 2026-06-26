# Sistema de Controle de Estoque e Vendas - Refatoração

Este projeto é um mini Ponto de Venda (PDV) integrado a um gerenciador de estoque. Ele foi documentado e refatorado (apenas nas dívidas técnicas selecionadas) como parte da disciplina DIM0501 - Boas Práticas de Programação, da Universidade Federal do Rio Grande do Norte (UFRN).

## Funcionalidades

O sistema foi desenhado para atuar no balcão de micro e pequenos negócios físicos (como quiosques e lanchonetes), permitindo as seguintes operações de terminal:

* *Cadastrar mercadorias:* Inserção temporária de novos produtos no sistema.


* *Realizar vendas:* Baixa no estoque da quantidade comprada e cálculo do valor total, aplicando regras de desconto.


* *Listar mercadorias:* Visualização rápida de todos os itens e preços em estoque.


* *Relatório de alerta:* Identificação e aviso sobre itens que possuem poucas unidades disponíveis.



## Melhorias e Quitação de Dívida Técnica

O código original passou por um processo analítico de identificação, classificação e priorização de dívidas técnicas. As principais refatorações focaram em "Ganhos Rápidos" de alto impacto, incluindo:

* *Isolamento de Regras de Negócio (Dívida D4):* A lógica de descontos foi extraída para a função aplicar_desconto, eliminando "números mágicos" e separando o cálculo financeiro da operação estrutural de baixa de estoque.


* *Robustez e Validação de Entradas (Dívida D8):* Foram criadas funções auxiliares (ler_numero_inteiro e ler_numero_real) utilizando blocos try/except. Isso garante que o sistema informe o usuário sobre inputs inválidos e continue rodando, em vez de quebrar abruptamente.

## Tecnologias Utilizadas

* *Linguagem:* Python (versão 3.13.11) 


* *Bibliotecas:* datetime (nativa), unittest e mock (nativas, para testes automatizados).

## Como Executar

Para iniciar o sistema de controle de estoque de forma interativa, execute o arquivo principal no seu terminal:

bash
python estoque.py



Para rodar a suíte de testes automatizados e verificar o comportamento das validações de input:

bash
python -m unittest tests/test_estoque.py
