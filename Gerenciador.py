"""
Gerenciador de Tarefas (TXT) - Simples
- Apenas listas, strings e funções (sem dicionários/classes/imports)
- Arquivo: tarefas.txt
- Cada linha: id;titulo;descricao;feito
  * feito: 0 (pendente) ou 1 (concluída)
"""

# ===========================
# SUBALGORITMOS DE PERSISTÊNCIA
# ===========================

def carregar(arq: str) -> list:
    tarefas = []
    try:
        f = open(arq, "r", encoding="utf-8")
        for linha in f:
            linha = linha.strip()
            if linha == "":
                continue
            partes = linha.split(";")
            while len(partes) < 4:
                partes.append("")
            tarefas.append(partes[:4])
        f.close()
    except FileNotFoundError:
        pass
    return tarefas


def salvar(arq: str, tarefas: list) -> None:
    try:
        f = open(arq, "w", encoding="utf-8")
        for t in tarefas:
            id_ = t[0]
            titulo = t[1].replace(";", ",")
            desc = t[2].replace(";", ",")
            feito = "1" if t[3] == "1" else "0"
            f.write(f"{id_};{titulo};{desc};{feito}\n")
        f.close()
    except:
        print("⚠️ Erro ao salvar o arquivo.")
        

def proximo_id(tarefas: list) -> str:
    maior = 0
    for t in tarefas:
        try:
            n = int(t[0])
            if n > maior:
                maior = n
        except:
            pass
    return str(maior + 1)