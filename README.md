# Otimização do Prompt - bug_to_user_story_v2

## Objetivo

O prompt foi refatorado para melhorar a qualidade, consistência e previsibilidade da conversão de relatos de bugs em User Stories para equipes de desenvolvimento ágil.

---

# Técnicas de Prompt Engineering Utilizadas

## 1. Few-Shot Learning

### Descrição

Foram adicionados exemplos completos de entrada e saída para demonstrar explicitamente ao modelo como um relato de bug deve ser transformado em uma User Story.

### Motivo da escolha

O prompt original não fornecia exemplos de comportamento esperado, deixando a interpretação totalmente aberta ao modelo.

Com Few-Shot Learning, o modelo passa a entender:

- Como identificar o problema relatado.
- Como estruturar uma User Story.
- Como escrever critérios de aceitação.
- Quando gerar uma User Story.
- Quando não gerar uma User Story.

### Exemplos adicionados

- Falha ao salvar cadastro.
- Duplicidade em relatório financeiro.
- Relato genérico sem contexto.
- Relato ambíguo após atualização.

### Benefícios

- Maior consistência nas respostas.
- Menor variação de formato.
- Melhor aderência ao padrão ágil de documentação.
- Melhor tratamento de entradas incompletas.

---

## 2. Role Prompting

### Descrição

Foi definida a seguinte persona:

> Product Owner Sênior especializado em levantamento de requisitos, refinamento de backlog e escrita de User Stories.

### Motivo da escolha

O prompt original apenas informava que o modelo deveria transformar bugs em tarefas.

Ao definir um papel específico, o modelo passa a responder com foco em:

- Requisitos funcionais.
- Valor para o usuário.
- Critérios de aceitação.
- Boas práticas de Product Management.

### Benefícios

- Respostas mais profissionais.
- Melhor alinhamento com metodologias ágeis.
- Histórias mais úteis para times de desenvolvimento.

---

## 3. Skeleton of Thought

### Descrição

Foi definido um processo explícito de análise:

1. Identificar o problema relatado.
2. Identificar quem é impactado.
3. Identificar o comportamento esperado.
4. Verificar se existem informações suficientes.
5. Gerar a User Story quando possível.
6. Gerar critérios de aceitação.
7. Solicitar informações adicionais quando necessário.

### Motivo da escolha

O prompt original não orientava como o raciocínio deveria ocorrer.

Ao estruturar o processo de pensamento, o modelo passa a seguir uma sequência lógica antes de produzir a resposta.

### Benefícios

- Melhor interpretação dos relatos.
- Menor chance de omitir informações importantes.
- Respostas mais consistentes e completas.

---

# Demais Melhorias

## Instruções Claras e Específicas

O prompt agora define explicitamente:

- Objetivo da tarefa.
- Formato obrigatório de saída.
- Processo de análise.
- Regras de comportamento.
- Critérios para geração da User Story.
- Critérios para rejeição por falta de contexto.

Isso reduz ambiguidades e melhora a previsibilidade das respostas.

---

## Regras Explícitas de Comportamento

Foram adicionadas regras como:

- Não inventar funcionalidades.
- Não assumir informações não presentes no relato.
- Não adicionar requisitos sem evidências.
- Gerar User Story apenas quando houver informações suficientes.
- Gerar critérios de aceitação apenas quando a User Story puder ser criada.
- Solicitar informações adicionais quando o contexto for insuficiente.

Essas regras reduzem alucinações e aumentam a confiabilidade da saída.

---

## Tratamento de Edge Cases

O prompt considera cenários em que o relato de bug não possui informações suficientes para gerar uma User Story confiável.

Nesses casos, o modelo não deve inventar requisitos, funcionalidades ou comportamentos esperados.

Em vez disso, deve informar explicitamente que não foi possível gerar a User Story e indicar quais informações são necessárias para o refinamento.

### Edge Case 1 — Relato Genérico

Entrada:

```text
Não funciona.
```

Saída:

```text
Não foi possível gerar uma User Story.

Motivo:
O relato não informa qual funcionalidade está apresentando problema nem qual comportamento é esperado.

Informações necessárias:
- Funcionalidade afetada
- Comportamento atual
- Comportamento esperado
- Passos para reprodução
```

### Edge Case 2 — Relato Ambíguo

Entrada:

```text
Após a atualização da versão o sistema ficou diferente.
```

Saída:

```text
Não foi possível gerar uma User Story.

Motivo:
O relato não especifica quais funcionalidades foram impactadas nem quais alterações são consideradas incorretas.

Informações necessárias:
- Funcionalidade afetada
- Comportamento anterior
- Comportamento atual
- Evidências do problema
```

### Benefícios

- Evita geração de requisitos fictícios.
- Reduz alucinações do modelo.
- Incentiva relatos mais completos.
- Produz resultados mais confiáveis para refinamento de backlog.

---

## Separação Correta entre System Prompt e User Prompt

### System Prompt

Responsável por definir:

- Persona.
- Objetivo.
- Regras.
- Processo de análise.
- Exemplos.
- Formato obrigatório.
- Tratamento de edge cases.

### User Prompt

Responsável apenas por fornecer o relato de bug recebido.

Exemplo:

```text
Relato de Bug:

{bug_report}
```

### Benefícios

- Melhor separação de responsabilidades.
- Maior reutilização do prompt.
- Aderência às boas práticas de Prompt Engineering.

---

# Resultado Esperado

A versão v2 produz User Stories mais consistentes, completas e alinhadas às práticas ágeis, reduzindo ambiguidades, evitando requisitos fictícios e tornando o processo mais robusto diante de relatos incompletos ou ambíguos.