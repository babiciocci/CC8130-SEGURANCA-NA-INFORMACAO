## Resumo detalhado — Segurança da Informação

Este resumo cobre os 5 PDFs da disciplina, explicando de forma simples e direta os principais conceitos.

### 1) Segurança hoje (contexto geral)

Segurança da informação não é um detalhe técnico: ela define se um sistema é confiável ou não. No mundo real, existem ataques frequentes, vazamentos de dados e falhas que afetam milhões de pessoas. Por isso, a segurança deve ser pensada desde o começo do desenvolvimento.

Ideia central: **a qualidade de um sistema depende da qualidade do processo usado para construí‑lo e mantê‑lo**. Quando o processo é fraco, o sistema também será.

Exemplos atuais mostram que ataques ocorrem em celulares, carros, serviços on‑line e até na cadeia de suprimentos de software. Logo, segurança é um problema real e constante.

Exemplos e temas citados:

- vazamentos de dados (ex.: CPF, telefone, PIX);
- exploração de falhas em massa (Stagefright, Flash, Uconnect);
- questões legais e políticas públicas (SOPA/PIPA, Encrypt Act);
- cyberwar e incidentes de cadeia de suprimentos (ex.: backdoors);
- side‑channel e speculative execution;
- UEFI Secure Boot como tema de proteção em baixo nível.

### 2) Princípios de segurança (o básico)

Os três princípios mais importantes:

- **Confidencialidade**: só quem tem permissão vê a informação.
- **Integridade**: a informação não pode ser alterada indevidamente.
- **Disponibilidade**: a informação precisa estar acessível quando for necessária.

Além disso, há princípios de suporte:

- **Autenticação**: provar quem você é.
- **Autorização**: definir o que você pode fazer.
- **Auditoria/Logging**: registrar atividades importantes.
- **Tratamento de erros**: evitar vazamento de detalhes sensíveis.

#### Defeito, erro e falha

- **Defeito**: problema no código (ou hardware).
- **Erro**: acontece durante a execução por causa do defeito.
- **Falha**: o sistema se comporta de modo diferente do esperado.

#### Ativo, vulnerabilidade, ameaça e ataque

- **Ativo**: algo que deve ser protegido (dados, sistemas, serviços).
- **Vulnerabilidade**: fraqueza no ativo.
- **Ameaça**: alguém ou algo que pode explorar a fraqueza.
- **Ataque**: ação concreta de exploração.

### 3) Modelagem de ameaças

Modelagem de ameaças é uma forma de **imaginar e mapear possíveis ataques antes que eles aconteçam**.

#### STRIDE (tipos de ameaça)

- **S**poofing: fingir ser outra pessoa ou sistema.
- **T**ampering: adulterar dados.
- **R**epudiation: negar que fez algo.
- **I**nformation Disclosure: revelar dados.
- **D**enial of Service: tirar o sistema do ar.
- **E**levation of Privilege: obter privilégios indevidos.

#### DREAD (medir risco)

Cada ameaça pode ser avaliada por:

- **D**ano causado
- **R**eprodutibilidade do ataque
- **E**xplorabilidade (facilidade de execução)
- **A**fetados (quantos usuários)
- **D**escoberta (chance de ser encontrada)

Com essas notas, fica mais fácil priorizar o que corrigir primeiro.

#### Árvores de ataque/ameaça

Outra técnica prática é usar árvores para decompor um ataque em etapas, ajudando a visualizar caminhos possíveis e decidir onde colocar controles.

### 4) Processo de desenvolvimento de segurança preventiva

Segurança precisa estar presente em todas as fases:

- **Planejamento**: entender o público, o ambiente e o que deve ser protegido.
- **Projeto**: definir requisitos de segurança, modelar ameaças.
- **Desenvolvimento**: seguir diretrizes de codificação segura, revisar código.
- **Testes**: testar falhas de segurança, não só funcionalidades.
- **Manutenção**: corrigir falhas, responder a incidentes, atualizar.

#### Bug Bar

Define um “padrão mínimo” de gravidade para bugs de segurança. Ajuda a decidir o que é bloqueante e precisa ser corrigido antes da entrega.

#### Exemplos de requisitos típicos

- **Confidencialidade**: senhas com hash forte (ex.: SHA‑256), não guardar dados sensíveis em logs.
- **Integridade**: validar entradas, publicar checksums.
- **Disponibilidade**: redundância e recuperação rápida.
- **Autenticação/Autorização**: controle de acesso por níveis.
- **Auditoria**: registrar logins e ações críticas.
- **Erros e exceções**: mensagens simples, sem detalhes internos.

### 5) Criptografia e SSL/TLS

#### Criptografia (ideia simples)

Criptografia transforma dados legíveis em dados indecifráveis para quem não possui a chave correta.

#### Funções hash

Servem para verificar integridade de dados. Boas funções hash precisam:

- ser fáceis de calcular;
- ser praticamente impossíveis de inverter;
- evitar colisões (duas entradas gerarem o mesmo hash).

Exemplo: **SHA‑256** é considerado seguro; **MD5 e SHA‑1** são fracos.

#### Geração de chaves e aleatoriedade

Chaves criptográficas precisam ser geradas com boa aleatoriedade (não previsíveis). Usar bibliotecas e padrões consolidados é obrigatório; algoritmos “caseiros” devem ser evitados.

#### SSL/TLS

SSL (hoje substituído por TLS) cria um canal seguro entre cliente e servidor. Ele garante:

- **confidencialidade** (criptografia),
- **integridade** (mensagens não alteradas),
- **autenticação** (certificados digitais).

O processo envolve troca de mensagens, envio de certificado, geração de chaves e início da comunicação segura.

---

### Conclusão

Segurança não é um recurso isolado: é **parte do processo**. Para construir software seguro, é preciso entender ameaças, medir riscos e aplicar boas práticas desde o começo.
