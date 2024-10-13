# Índice

1. [Introdução](#breakmips)
2. [Estrutura de Arquivos](#estrutura-de-arquivos)
3. [Descrição das Funções](#descrição-das-funções)  
   3.1 [Funções Principais](#funções-principais)  
   3.2 [Funções Auxiliares](#funções-auxiliares)
4. [Como Jogar](#como-jogar)
5. [Configurações e Ajustes](#configurações-e-ajustes) 

# BreakMips
Este projeto é uma implementação do clássico jogo **Breakout**, desenvolvida em Assembly MIPS para ser executada no simulador MARS. O objetivo é controlar uma palheta, movimentando-a para a esquerda e direita para rebater uma bola que destrói blocos no topo da tela. Se a bola passar pela palheta, o jogo é perdido. O jogo continua até que todos os blocos sejam destruídos ou a bola ultrapasse a palheta.

## Estrutura de Arquivos

- **Constants**: Contém as definições de configuração do jogo, como dimensões da tela, blocos, palheta e bola, bem como cores e outras constantes relevantes.
- **Data Section**: Contém variáveis globais do jogo, como posições da palheta e da bola, estado do jogo, matriz de blocos e contadores.

## Descrição das Funções

### Funções Principais

1. **main**:
   - Inicia o jogo exibindo o menu principal.

2. **main_game_loop**:
   - Loop principal do jogo. Monitora o estado do teclado, move a bola, detecta colisões e verifica se o jogo foi ganho ou perdido.

3. **fall_ball**:
   - Responsável por fazer a bola "cair" quando está em estado de queda. Atualiza as coordenadas da bola com base em sua velocidade atual.

4. **handle_ball**:
   - Executa as ações relacionadas ao movimento da bola. Chama a função correta para lidar com o movimento, dependendo se a bola está subindo ou descendo.

5. **ball_wall_collision**:
   - Lida com a colisão da bola com as bordas da tela (superior, inferior, esquerda, direita). A direção da bola é invertida quando uma colisão ocorre.

6. **ball_paddle_collision**:
   - Detecta quando a bola colide com a palheta. Se houver colisão, a direção vertical da bola é invertida, simulando o rebote.

7. **move_paddle_left** e **move_paddle_right**:
   - Movem a palheta para a esquerda e direita, respectivamente, com base na entrada do usuário. Asseguram que a palheta não ultrapasse as bordas da tela.

### Funções Auxiliares

1. **draw_image**:
   - Desenha imagens na tela, como o fundo do menu, a palheta, a bola, ou blocos. Utiliza coordenadas para posicionar corretamente os elementos gráficos.

2. **erase**:
   - Apaga uma área específica da tela, usada para limpar a posição anterior da bola e da palheta antes de desenhar suas novas posições.

3. **frame_sync_delay**:
   - Introduz um atraso no loop principal para garantir que a movimentação dos elementos na tela ocorra de forma sincronizada e com a velocidade correta.

4. **reset_blocks**:
   - Reinicia o estado dos blocos quando o jogo é perdido ou reiniciado, restaurando sua matriz de posições e estado ativo.

5. **ganhou**:
   - Exibe a tela de vitória quando o jogador destrói todos os blocos.

6. **perdeu**:
   - Exibe a tela de derrota quando a bola ultrapassa a palheta e permite reiniciar o jogo ou voltar ao menu principal.

7. **play_sound**:
   - Função para tocar sons MIDI. Define o tom, duração, instrumento e volume dos sons, como o som de colisões.

## Como Jogar

- Configure o bitmap display, mantendo o tamanho padrão da tela, coloque o tamanho dos pixels em 4 e a posição inicial no $gp.
- Abra o keyboard do Mars e conecte.
- Use as teclas **A** e **D** para mover a palheta para a esquerda e direita, respectivamente ou use qualquer outra tecla para parar a palheta.
- Rebata a bola contra os blocos para destruí-los.
- Evite que a bola ultrapasse a palheta, ou o jogo será perdido.
- Destrua todos os blocos para vencer.

## Configurações e Ajustes

Você pode modificar as configurações do jogo alterando as constantes no início do código. As principais constantes incluem:
- **Dimensões da tela** (`S_W`, `S_H`)
- **Dimensões da palheta** (`P_W`, `P_H`)
- **Velocidade da palheta** (`P_SPEED`)
- **Dimensões dos blocos** (`BL_W`, `BL_H`)
- **Velocidade da bola** (`ball_vx`, `ball_vy`)