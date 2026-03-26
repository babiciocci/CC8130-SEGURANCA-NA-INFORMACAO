import hashlib

# ============================================================
# CC8130 - Segurança na Informação
# Atividade: Verificação de Hashes SHA256 e MD5
# Bruno Arthur Basso Silva - 22.123.067-5
# Gabriela Molina Ciocci - 22.222.032-9
# Guilherme Barboza de Albuquerque - 22.224.024-4
# Sergio Martins de Oliveira Santos - 22.222.021-2
# ============================================================
# Aspas do enunciado são só delimitadores — não entram no hash.

ALUNOS = [
    "Bruno Arthur Basso Silva - 22.123.067-5",
    "Gabriela Molina Ciocci - 22.222.032-9",
    "Guilherme Barboza de Albuquerque - 22.224.024-4",
    "Sergio Martins de Oliveira Santos - 22.222.021-2",
]

exemplos = [
    {
        "rotulo": "SHA256 e MD5 corretos",
        "texto": "SHA256 e MD5 corretos",
        "sha256_fornecido": "c034489664dd98c3a2b0d7c1afc0717378827d9fa778288c8bb1c567c8bc2ec1",
        "md5_fornecido": "19406b49ace5073c806a79061f58dbd3",
    },
    {
        "rotulo": "Somente SHA256 correto",
        "texto": "Somente SHA256 correto",
        "sha256_fornecido": "5b22f6bf621c2116f0d4589c3b5405ed3b5d768b9ba1dfafbae9292331ce9827",
        "md5_fornecido": "cfe69ac7a0b07810b391c27b1ea838cd",
    },
    {
        "rotulo": "Somente MD5 correto",
        "texto": "Somente MD5 correto",
        "sha256_fornecido": "58d909cc5c6ac58bb509d4651528c66a8b9bd8a197ec260dd7d6754b98b6b63e",
        "md5_fornecido": "c4e28d48ac81f88aaade5ed31f2e2c26",
    },
    {
        "rotulo": "Nenhum dos dois corretos",
        "texto": "Nenhum dos dois corretos",
        "sha256_fornecido": "d55825a0c3ee133ac29986b3fcefb30432968e99967787191bb48be89e485cf8",
        "md5_fornecido": "8bdf3218ccd26f327220ad0daf3d3ce0",
    },
]

frases = [
    {
        "id": 1,
        "texto": "A primeira das instituições criadas pelo Pe. Roberto Sabóia de Medeiros foi a antiga Escola Superior de Administração de Negócios de São Paulo - ESAN/SP.",
        "sha256_fornecido": "d24de3ec3835115c576a55188a31761b73af93ed2c45a171c810bb66b24b08f9",
        "md5_fornecido": "c850e1a34a6ed572e0758ccd9c615bda",
    },
    {
        "id": 2,
        "texto": "A FEI é uma instituição vinculada estatutariamente à Companhia de Jesus",
        "sha256_fornecido": "6979a3d7a19e5921ae00ca7db9b814e1b83831dcedfca33dbb72e761ca084337",
        "md5_fornecido": "b710771da8d7521524f45233ea9dd9e1",
    },
    {
        "id": 3,
        "texto": "Em 20 de janeiro de 1951 foi realizada a sessão solene da congregação para a Colação de Grau da primeira turma da Faculdade de Engenharia Industrial.",
        "sha256_fornecido": "6c582a993ba3ea454f11221a374878e534cfe666060c87ba03127de07f1ca4e6",
        "md5_fornecido": "55748c2cb669a9d9508677cb914cb025",
    },
    {
        "id": 4,
        "texto": "A Capela Santo Inácio de Loyola foi construída no ano de 1978, em concreto aparente.",
        "sha256_fornecido": "254e695d0f8835651bc231f9cf1b2a7a097b849648f05f79f1855a55f85b089e",
        "md5_fornecido": "f4a8a299fd4da2a5d70b374be2e48147",
    },
    {
        "id": 5,
        "texto": "Tendo como função principal a promoção do aprimoramento profissional no campo administrativo e tecnológico, o IECAT (Instituto de Especialização em Ciências Administrativas e Tecnológicas) foi criado em 1982",
        "sha256_fornecido": "d2150d688c337fc57e235adafd57f86d7aba0b8682c249b1006ba592706f88a0",
        "md5_fornecido": "1c4ecc238571333ae507f82ff6a5e9e4",
    },
    {
        "id": 6,
        "texto": "Dentro de uma proposta de integração e de agregação de competências, visando a excelência de seus cursos, as instituições FEI, FCI e ESAN foram transformadas no Centro Universitário da FEI no ano de 2002.",
        "sha256_fornecido": "faefb927a21dd282ee00effe42bc0688f649450677a61edce15863a15461b721",
        "md5_fornecido": "98420532cbf1be32a98be579f592cd72",
    },
    {
        "id": 7,
        "texto": "O Centro Universitário da FEI passou a fazer parte do seleto grupo que produz ciência no Brasil, quando a CAPES aprovou o primeiro curso de Mestrado em Engenharia Elétrica em 2005.",
        "sha256_fornecido": "da9f214449005850f4fd552238658820434c15ca06389d018b1814bb376abaa6",
        "md5_fornecido": "2e20bfbece6fdc62de4c4bb80a77ba1f",
    },
    {
        "id": 8,
        "texto": "Em 2016 foi realizada a primeira edição do congresso de inovação - Megatendências 2050.",
        "sha256_fornecido": "56f4ba0ea34d91fe386f09dc687f1c35c757009b0230a828fa43e48ac08f8d0c",
        "md5_fornecido": "5cbf7c58bf9acd451c3bf1b48392a9e6",
    },
    {
        "id": 9,
        "texto": "Em 2012 o Centro Universitário FEI celebrou 70 anos de história e de excelência na inovação e na formação de mais de 50 mil profissionais altamente qualificados para o setor empresarial, entre Administradores, Engenheiros e Cientistas da Computação.",
        "sha256_fornecido": "2707325bd4929bbbadb422851a2248615bf7998bf3607b6ad934168be6a45859",
        "md5_fornecido": "a0a80cbc42bcd7b4b6ab317d0d2efa33",
    },
    {
        "id": 10,
        "texto": "Em 1999 iniciam-se as atividades da FCI (Faculdade de Informática), como o curso de Ciência da Computação.",
        "sha256_fornecido": "b2ff0457c8c20ccd84e20cd72f06c08140b8ea472d6a6848a5c291319bf9e4a8",
        "md5_fornecido": "0288b32001adf2f237ba8410f8415e50",
    },
]


def verificar_item(texto, sha256_fornecido, md5_fornecido):
    sha256_calc = hashlib.sha256(texto.encode("utf-8")).hexdigest()
    md5_calc = hashlib.md5(texto.encode("utf-8")).hexdigest()
    sha_ok = sha256_calc == sha256_fornecido
    md5_ok = md5_calc == md5_fornecido
    if sha_ok and md5_ok:
        resultado = "VERDADEIRA (SHA256 e MD5 corretos)"
    elif sha_ok:
        resultado = "FALSA (somente SHA256 correto)"
    elif md5_ok:
        resultado = "FALSA (somente MD5 correto)"
    else:
        resultado = "FALSA (nenhum dos dois corretos)"
    return resultado, sha256_calc, md5_calc, sha_ok, md5_ok


def imprimir_bloco(rotulo, texto, sha256_fornecido, md5_fornecido):
    resultado, sha256_calc, md5_calc, sha_ok, md5_ok = verificar_item(
        texto, sha256_fornecido, md5_fornecido
    )
    print(f"{rotulo}: {resultado}")
    preview = texto if len(texto) <= 80 else texto[:80] + "..."
    print(f"  Texto: \"{preview}\"")
    print(f"  SHA256 fornecido:  {sha256_fornecido}")
    print(f"  SHA256 calculado:  {sha256_calc}")
    print(f"  SHA256 confere:    {'SIM' if sha_ok else 'NAO'}")
    print(f"  MD5 fornecido:     {md5_fornecido}")
    print(f"  MD5 calculado:     {md5_calc}")
    print(f"  MD5 confere:       {'SIM' if md5_ok else 'NAO'}")
    print()
    return sha_ok, md5_ok


print("=" * 90)
print("CC8130 - Verificação de Hashes SHA256 e MD5")
for aluno in ALUNOS:
    print(aluno)
print("=" * 90)
print()

print("=" * 90)
print("EXEMPLOS DE VALIDAÇÃO")
print("=" * 90)
print()

for e in exemplos:
    imprimir_bloco("Exemplo - " + e["rotulo"], e["texto"], e["sha256_fornecido"], e["md5_fornecido"])

print("=" * 90)
print("FRASES DO ENUNCIADO")
print("=" * 90)
print()

for f in frases:
    imprimir_bloco("Frase " + str(f["id"]), f["texto"], f["sha256_fornecido"], f["md5_fornecido"])

print("=" * 90)
print("RESUMO - EXEMPLOS")
print("=" * 90)
print(f"{'Caso':<40} {'SHA256':<10} {'MD5':<10} {'Veredicto'}")
print("-" * 70)
for e in exemplos:
    _, _, _, sha_ok, md5_ok = verificar_item(
        e["texto"], e["sha256_fornecido"], e["md5_fornecido"]
    )
    v = "VERDADEIRA" if (sha_ok and md5_ok) else "FALSA"
    print(f"  {e['rotulo']:<38} {'OK' if sha_ok else 'FALHOU':<10} {'OK' if md5_ok else 'FALHOU':<10} {v}")

print()
print("=" * 90)
print("RESUMO - FRASES")
print("=" * 90)
print(f"{'Frase':<8} {'SHA256':<10} {'MD5':<10} {'Veredicto'}")
print("-" * 70)
for f in frases:
    _, _, _, sha_ok, md5_ok = verificar_item(
        f["texto"], f["sha256_fornecido"], f["md5_fornecido"]
    )
    v = "VERDADEIRA" if (sha_ok and md5_ok) else "FALSA"
    print(f"  {f['id']:<6} {'OK' if sha_ok else 'FALHOU':<10} {'OK' if md5_ok else 'FALHOU':<10} {v}")

# --- arquivo texto (tabela para entrega) ---

linhas = []
linhas.append("CC8130 - Verificação de Hashes SHA256 e MD5")
linhas.append("Integrantes do grupo:")
for aluno in ALUNOS:
    linhas.append("  - " + aluno)
linhas.append("")
linhas.append("Critério: a frase é VERDADEIRA somente se SHA256 e MD5 conferem com o texto (UTF-8, sem aspas externas).")
linhas.append("")
linhas.append("=== TABELA 1 - Exemplos de validação ===")
linhas.append("")
linhas.append(
    f"{'Caso':<40} {'SHA256':^10} {'MD5':^10} {'Verdadeira?':<14} {'Classificação'}"
)
linhas.append("-" * 95)
for e in exemplos:
    resultado, _, _, sha_ok, md5_ok = verificar_item(
        e["texto"], e["sha256_fornecido"], e["md5_fornecido"]
    )
    linhas.append(
        f"{e['rotulo']:<40} {'OK' if sha_ok else 'FALHOU':^10} "
        f"{'OK' if md5_ok else 'FALHOU':^10} {'SIM' if (sha_ok and md5_ok) else 'NÃO':<14} {resultado}"
    )
linhas.append("")
linhas.append("=== TABELA 2 - Frases do enunciado (verdadeira = ambos os hashes corretos) ===")
linhas.append("")
linhas.append(f"{'#':<4} {'SHA256':^10} {'MD5':^10} {'Verdadeira?':<14} {'Trecho da frase'}")
linhas.append("-" * 95)
for f in frases:
    resultado, _, _, sha_ok, md5_ok = verificar_item(
        f["texto"], f["sha256_fornecido"], f["md5_fornecido"]
    )
    trecho = f["texto"][:67] + "..." if len(f["texto"]) > 70 else f["texto"]
    linhas.append(
        f"{f['id']:<4} {'OK' if sha_ok else 'FALHOU':^10} "
        f"{'OK' if md5_ok else 'FALHOU':^10} {'SIM' if (sha_ok and md5_ok) else 'NÃO':<14} {trecho}"
    )
linhas.append("")
ids_ok = []
for f in frases:
    _, _, _, s_ok, m_ok = verificar_item(f["texto"], f["sha256_fornecido"], f["md5_fornecido"])
    if s_ok and m_ok:
        ids_ok.append(f["id"])
linhas.append("Resumo: frases verdadeiras (IDs): " + ", ".join(str(i) for i in ids_ok))
linhas.append(f"Total verdadeiras: {len(ids_ok)} de {len(frases)}")
linhas.append("")

with open("RESULTADO_VERIFICACAO_HASHES.txt", "w", encoding="utf-8") as arq:
    arq.write("\n".join(linhas))

print()
print("Arquivo gerado: RESULTADO_VERIFICACAO_HASHES.txt")
