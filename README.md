# BreakMips
Implementação do jogo breakout em Asembly MIPS para o simulador Mars

# Definições e Configurações Iniciais:
1. **Configurações da Tela:**
   - `S_BS`, `S_W`, `S_H`, `S_WB`, `S_HB`: Definem o endereço base da tela, a largura e altura, além de suas versões em logaritmos (`log2`), usados para cálculos rápidos.

2. **Configurações do Jogo:**
   - `DLY`: Determina o atraso do loop principal (o número de ciclos).
   - `FRMB`: Atraso dos quadros.
   - `MUSIC_ON`, `INSTRUMENT`, `VOLUMN`, `MUSIC_DLY`: Controlam aspectos relacionados à música no jogo.

3. **Cores:**
   - `C_BG`: Define a cor de fundo (um valor hexadecimal correspondente a uma cor específica).

## Seção `.data`:
- **`menu_img`**: Uma imagem do menu armazenada em forma de dados (pixels em hexadecimal).
- **Contadores de jogo:** `main_cnt`, `score_cnt`, `best_cnt`: Mantêm informações sobre o estado do jogo, como contagem principal, pontuação atual e melhor pontuação.

## Funções Importantes:

1. **`main`:** Função principal do jogo.
   - **Inicializa o jogo** e executa o menu inicial, chamando a função `draw_image` para desenhar a imagem do menu.
   - Verifica a entrada do teclado e faz a transição para o jogo ou sai.

2. **`draw_image`:** Função para desenhar uma imagem na tela.
   - Usa os registradores `$a0` (endereço da imagem), `$a1` (posição inicial da altura) e `$a2` (posição inicial da largura) para calcular a posição de cada pixel da imagem e transferi-lo para a memória da tela.
   - Usa um loop para percorrer cada pixel da imagem e verificar se está dentro dos limites da tela antes de desenhá-lo.

3. **`erase`:** Limpa uma região da tela preenchendo com a cor de fundo.
   - Usa os registradores `$a0`, `$a1`, `$a2`, `$a3` para definir a área a ser apagada.

4. **`add64`:** Implementa uma adição de 64 bits, combinando dois valores de 32 bits de alta e baixa ordem.

5. **`frame_sync_init` e `frame_sync_delay`:** Sincronizam a execução do jogo para manter uma taxa de quadros estável.
   - **`frame_sync_init`** salva o tempo do sistema.
   - **`frame_sync_delay`** compara o tempo atual com o anterior e aplica um atraso para garantir a consistência da execução.
