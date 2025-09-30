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

# ===========================
# SUBALGORITMOS DE OPERAÇÃO
# ===========================

def listar(tarefas: list) -> None:
    print("\n📋 Lista de tarefas")
    if len(tarefas) == 0:
        print("Nenhuma tarefa cadastrada.")
        return
    print("-" * 70)
    print(f"{'ID':<4} {'Título':<30} {'Status':<12} Descrição")
    print("-" * 70)
    for t in tarefas:
        status = "Concluída" if t[3] == "1" else "Pendente"
        titulo = t[1]
        if len(titulo) > 30:
            titulo = titulo[:27] + "..."
        print(f"{t[0]:<4} {titulo:<30} {status:<12} {t[2]}")
    print("-" * 70)


def adicionar(tarefas: list, arq: str) -> None:
    print("\n➕ Adicionar tarefa")
    while True:
        titulo = input("Título: ").strip()
        if titulo != "":
            break
        print("❌ Título não pode ser vazio.")
    descricao = input("Descrição (opcional): ").strip()
    nova = [proximo_id(tarefas), titulo, descricao, "0"]
    tarefas.append(nova)
    salvar(arq, tarefas)
    print("✅ Tarefa adicionada!")


def encontrar_indice_por_id(tarefas: list, tid: str) -> int:
    for i in range(len(tarefas)):
        if tarefas[i][0] == tid:
            return i
    return -1


def alternar_status(tarefas: list, arq: str) -> None:
    print("\n✔️ Concluir/Reabrir")
    tid = input("ID da tarefa: ").strip()
    idx = encontrar_indice_por_id(tarefas, tid)
    if idx == -1:
        print("❌ Tarefa não encontrada.")
        return
    if tarefas[idx][3] == "1":
        tarefas[idx][3] = "0"
        print("🔁 Tarefa reaberta.")
    else:
        tarefas[idx][3] = "1"
        print("✅ Tarefa concluída.")
    salvar(arq, tarefas)


def excluir(tarefas: list, arq: str) -> None:
    print("\n🗑️ Excluir tarefa")
    tid = input("ID da tarefa: ").strip()
    idx = encontrar_indice_por_id(tarefas, tid)
    if idx == -1:
        print("❌ Tarefa não encontrada.")
        return
    confirma = input(f"Excluir tarefa #{tid}? (s/N): ").lower().strip()
    if confirma == "s":
        tarefas.pop(idx)
        salvar(arq, tarefas)
        print("✅ Excluída!")
    else:
        print("Operação cancelada.")

# ===========================
# MENU / INTERFACE
# ===========================
def menu() -> None:
    print("\n" + "=" * 52)
    print("   GERENCIADOR DE TAREFAS - SIMPLES (TXT)")
    print("=" * 52)
    print("1 - Adicionar tarefa")
    print("2 - Listar tarefas")
    print("3 - Concluir/Reabrir tarefa")
    print("4 - Excluir tarefa")
    print("0 - Sair")


def programa() -> None:
    arq = "tarefas.txt"
    tarefas = carregar(arq)
    while True:
        menu()
        opcao = input("Escolha: ").strip()
        match opcao:
            case "0":
                print("Até mais! 👋")
                break
            case "1":
                adicionar(tarefas, arq)
            case "2":
                listar(tarefas)
            case "3":
                alternar_status(tarefas, arq)
            case "4":
                excluir(tarefas, arq)
            case _:
                print("❌ Opção inválida.")

# ===========================
# EXECUÇÃO
# ===========================
programa()        