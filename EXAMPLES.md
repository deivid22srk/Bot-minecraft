# 💬 Exemplos de Comandos

Este documento mostra exemplos práticos de como interagir com o Bot Hailgames.

## 📋 Formato dos Comandos

Todos os comandos devem começar com `!BOT` seguido da sua instrução em linguagem natural.

```
!BOT [sua instrução aqui]
```

---

## 🚶 Navegação e Movimento

### Ir até o jogador
```
!BOT venha até mim
!BOT vem aqui
!BOT venha cá
!BOT vir para minha posição
```

**Resposta esperada:**
- "Estou indo até você!"
- O bot se move em direção ao jogador

---

### Seguir o jogador
```
!BOT me siga
!BOT siga-me
!BOT fique me seguindo
!BOT me acompanhe
```

**Resposta esperada:**
- "Seguindo você agora!"
- O bot começa a seguir o jogador automaticamente

---

### Parar de seguir
```
!BOT pare de seguir
!BOT parar
!BOT fique aqui
!BOT não me siga mais
```

**Resposta esperada:**
- "Ok, parando!"
- O bot para de seguir e fica parado

---

## ⛏️ Mineração e Coleta

### Coletar madeira
```
!BOT pegue madeira
!BOT pegue 10 madeiras
!BOT colete madeira para mim
!BOT mine árvores
!BOT busque 5 madeiras
```

**Resposta esperada:**
- "Vou buscar 10 madeiras para você!"
- O bot procura árvores próximas
- Minera a quantidade solicitada
- "Coletei 10 madeiras!"

---

### Coletar pedra
```
!BOT pegue pedra
!BOT mine 20 pedras
!BOT colete pedra
!BOT busque cobblestone
```

**Resposta esperada:**
- "Vou buscar 20 pedras para você!"
- O bot procura pedras próximas
- Minera a quantidade solicitada

---

### Coletar minérios
```
!BOT pegue carvão
!BOT mine 15 carvões
!BOT busque ferro
!BOT colete 10 ferros para mim
```

**Resposta esperada:**
- "Vou buscar 15 carvões para você!"
- O bot procura os minérios
- Minera a quantidade solicitada

---

## 🎁 Entrega de Itens

### Entregar itens coletados
```
!BOT me entregue a madeira
!BOT traga os itens
!BOT dê os recursos para mim
!BOT entregue o que coletou
!BOT me dê a madeira
```

**Resposta esperada:**
- "Entregando a madeira!"
- O bot vai até o jogador
- Entrega os itens coletados

---

### Comandos combinados
```
!BOT pegue 10 madeiras e me entregue
!BOT colete pedra e traga para mim
!BOT mine carvão e me dê
```

**Resposta esperada:**
- "Vou buscar 10 madeiras para você!"
- O bot coleta os recursos
- Vai até o jogador
- Entrega os itens

---

## 💬 Conversação

### Saudações
```
!BOT olá
!BOT oi
!BOT e aí
!BOT bom dia
```

**Resposta esperada:**
- "Olá! Como posso ajudar?"
- "Oi! O que você precisa?"

---

### Perguntas sobre capacidades
```
!BOT o que você pode fazer?
!BOT quais são seus comandos?
!BOT me ajude
!BOT como você funciona?
```

**Resposta esperada:**
- Explicação das funcionalidades
- Lista de comandos disponíveis

---

### Perguntas sobre status
```
!BOT onde você está?
!BOT o que tem no seu inventário?
!BOT quantos itens você tem?
```

**Resposta esperada:**
- Informações sobre posição
- Status do inventário

---

## 🎯 Comandos Complexos

### Tarefas múltiplas
```
!BOT pegue 20 madeiras, depois venha até mim e me entregue
!BOT colete pedra, depois me siga
!BOT me siga e colete madeira pelo caminho
```

**Resposta esperada:**
- O Gemini AI interpreta a sequência
- Executa as ações em ordem lógica

---

### Comandos contextuais
```
!BOT vá buscar mais
(após já ter pedido um recurso)

!BOT faça de novo
(repete a última ação)

!BOT traga isso aqui
(após mencionar um item)
```

**Resposta esperada:**
- O bot usa contexto da conversa anterior
- Executa a ação relacionada

---

## ⚠️ Tratamento de Erros

### Comando não compreendido
**Você:**
```
!BOT fkjdshfkjsh
```

**Bot:**
```
Desculpe, não entendi o comando. Pode repetir?
```

---

### Recurso não disponível
**Você:**
```
!BOT pegue 100 diamantes
```

**Bot:**
```
Procurando por diamantes...
Só consegui encontrar 3 diamantes. Não há mais por perto.
```

---

### Ação impossível
**Você:**
```
!BOT voe até a lua
```

**Bot:**
```
Desculpe, não posso fazer isso no momento.
```

---

## 🎮 Cenários de Uso

### Cenário 1: Construção
```
Jogador: !BOT pegue 64 madeiras
Bot: Vou buscar 64 madeiras para você!
[Bot coleta madeiras]
Bot: Coletei 64 madeiras!

Jogador: !BOT me entregue
Bot: Entregando a madeira!
[Bot vai até o jogador]
Bot: Cheguei!
```

---

### Cenário 2: Exploração
```
Jogador: !BOT me siga
Bot: Seguindo você agora!
[Bot segue o jogador]

Jogador: !BOT pegue carvão que você encontrar
Bot: Vou buscar carvão...
[Bot coleta enquanto segue]

Jogador: !BOT pare
Bot: Ok, parando!
```

---

### Cenário 3: Mineração
```
Jogador: !BOT pegue 20 pedras e 10 carvões
Bot: Vou buscar recursos para você!
[Bot coleta pedras]
[Bot coleta carvões]
Bot: Coletei tudo!

Jogador: !BOT venha até mim e me entregue
Bot: Estou indo até você!
[Bot vai até o jogador]
Bot: Entregando os itens!
```

---

## 💡 Dicas de Uso

### ✅ Boas Práticas

1. **Seja específico com quantidades**
   ```
   ✅ !BOT pegue 10 madeiras
   ❌ !BOT pegue algumas madeiras
   ```

2. **Use comandos claros**
   ```
   ✅ !BOT venha até mim
   ❌ !BOT vvvvv
   ```

3. **Um comando por vez**
   ```
   ✅ !BOT pegue madeira
   ✅ !BOT me entregue
   
   ⚠️ !BOT pegue madeira e pedra e ferro e carvão e me entregue tudo
   ```

4. **Aguarde o bot completar a ação**
   - Não envie múltiplos comandos rapidamente
   - Espere a resposta do bot antes do próximo comando

---

### 🎯 Comandos Eficientes

**Em vez de:**
```
!BOT pegue madeira
[espera]
!BOT venha até mim
[espera]
!BOT me entregue
```

**Use:**
```
!BOT pegue madeira e me entregue
```

---

## 🔧 Customização

### Mudar o prefixo dos comandos

Edite o `config.json`:
```json
{
  "commandPrefix": "!BOT"
}
```

Você pode mudar para:
- `@bot`
- `hey bot`
- `!hailgames`
- Qualquer outro prefixo

**Exemplo:**
```json
{
  "commandPrefix": "@bot"
}
```

Então use:
```
@bot venha até mim
@bot pegue madeira
```

---

## 📊 Lista Completa de Ações

| Ação | Exemplo | Descrição |
|------|---------|-----------|
| **goto** | `!BOT venha até mim` | Vai até o jogador |
| **follow** | `!BOT me siga` | Segue o jogador continuamente |
| **stop** | `!BOT pare` | Para de seguir/mover |
| **mine** | `!BOT pegue 10 madeiras` | Minera recursos específicos |
| **give** | `!BOT me entregue` | Entrega itens coletados |
| **respond** | `!BOT olá` | Apenas responde ao jogador |

---

## 🌟 Comandos Criativos

Teste a IA do Gemini com comandos criativos:

```
!BOT você pode construir uma casa?
!BOT me proteja dos monstros
!BOT encontre uma caverna
!BOT ache o bioma de floresta
!BOT faça uma fazenda
!BOT organize meu inventário
```

> **Nota:** Algumas funcionalidades avançadas ainda estão em desenvolvimento!

---

## 📞 Suporte

Se algum comando não funcionar como esperado:

1. Verifique os logs no console do Termux
2. Confirme que usou o prefixo `!BOT`
3. Tente reformular o comando
4. Reporte bugs no GitHub

---

**Divirta-se com seu bot inteligente! 🤖✨**
