import pygame
import sys
import os

# --- CONFIGURAÇÕES DO JOGO ---
LARGURA, ALTURA = 800, 600
TILE_SIZE = 32  # Tamanho dos blocos de arte (padrão de pixel art)
FPS = 60

# Cores de backup (caso a imagem não carregue)
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)

# --- SISTEMA DE CARREGAMENTO DE ARTE ---
# Define o caminho para a pasta de arte
PASTA_ARTE = os.path.join(os.path.dirname(__file__), 'arte')

def carregar_imagem(nome, tamanho=None):
    """Carrega uma imagem e ajusta seu tamanho se necessário."""
    caminho = os.path.join(PASTA_ARTE, nome)
    try:
        imagem = pygame.image.load(caminho).convert_alpha()
        if tamanho:
            imagem = pygame.transform.scale(imagem, tamanho)
        return imagem
    except pygame.error:
        # Se não encontrar a imagem, cria um quadrado colorido de backup
        print(f"AVISO: Imagem {nome} não encontrada em {caminho}. Usando backup.")
        superficie = pygame.Surface((TILE_SIZE, TILE_SIZE))
        superficie.fill((255, 0, 255)) # Rosa choque para erro
        return superficie

# --- DEFINIÇÃO DO MAPA ---
# Usamos strings para facilitar a visualização do design do nível
# 'P' = Parede/Árvore (Colisão), '.' = Chão (Livre)
DESIGN_MAPA = [
    "PPPPPPPPPPPPPPPPPPPPPPPPP",
    "P..........P............P",
    "P..........P............P",
    "P....P.....P.....PPPP...P",
    "P....P.....P........P...P",
    "P....PPPPPPP........P...P",
    "P...................P...P",
    "P.......................P",
    "P........PPPPPPPP.......P",
    "P.......................P",
    "P.......................P",
    "PPPPPPPPPPPPPPPPPPPPPPPPP",
]

# --- CLASSES DO JOGO ---

class Spritesheet:
    """Carrega todas as imagens necessárias de uma vez."""
    def __init__(self):
        self.chao = carregar_imagem('chao.png', (TILE_SIZE, TILE_SIZE))
        self.parede = carregar_imagem('parede.png', (TILE_SIZE, TILE_SIZE))
        self.player = carregar_imagem('player.png', (TILE_SIZE, TILE_SIZE))

class Bloco(pygame.sprite.Sprite):
    """Representa um bloco estático do cenário (Chão ou Parede)."""
    def __init__(self, x, y, imagem, eh_parede):
        super().__init__()
        self.image = imagem
        self.rect = self.image.get_rect()
        self.rect.x = x * TILE_SIZE
        self.rect.y = y * TILE_SIZE
        self.eh_parede = eh_parede

class Jogador(pygame.sprite.Sprite):
    """O personagem controlável."""
    def __init__(self, x, y, imagem):
        super().__init__()
        self.image = imagem
        self.rect = self.image.get_rect()
        # Posiciona o jogador no centro do tile
        self.rect.x = x * TILE_SIZE
        self.rect.y = y * TILE_SIZE
        self.velocidade = 4

    def update(self, paredes):
        # Captura as teclas pressionadas
        teclas = pygame.key.get_pressed()
        
        # Vetor de movimento
        dx = 0
        dy = 0
        
        if teclas[pygame.K_LEFT] or teclas[pygame.K_a]: dx = -self.velocidade
        if teclas[pygame.K_RIGHT] or teclas[pygame.K_d]: dx = self.velocidade
        if teclas[pygame.K_UP] or teclas[pygame.K_w]: dy = -self.velocidade
        if teclas[pygame.K_DOWN] or teclas[pygame.K_s]: dy = self.velocidade

        # Movimento e colisão horizontal
        self.rect.x += dx
        lista_colisao = pygame.sprite.spritecollide(self, paredes, False)
        for bloco in lista_colisao:
            if dx > 0: self.rect.right = bloco.rect.left
            if dx < 0: self.rect.left = bloco.rect.right

        # Movimento e colisão vertical
        self.rect.y += dy
        lista_colisao = pygame.sprite.spritecollide(self, paredes, False)
        for bloco in lista_colisao:
            if dy > 0: self.rect.bottom = bloco.rect.top
            if dy < 0: self.rect.top = bloco.rect.bottom

class InterfaceUsuario:
    """Desenha elementos da UI como barras de vida."""
    def __init__(self, tela):
        self.tela = tela
        self.fonte = pygame.font.SysFont('Arial', 20, bold=True)

    def desenhar(self):
        # Barra de Vida (simulada)
        margem = 10
        largura_barra = 200
        altura_barra = 25
        
        # Fundo da barra (cinza escuro)
        pygame.draw.rect(self.tela, (50, 50, 50), (margem, margem, largura_barra, altura_barra))
        
        # Vida atual (vermelho) - simulando 80% de vida
        vida_atual_largura = int(largura_barra * 0.8)
        pygame.draw.rect(self.tela, (200, 0, 0), (margem, margem, vida_atual_largura, altura_barra))
        
        # Texto da Vida
        texto = self.fonte.render("HP: 80 / 100", True, BRANCO)
        self.tela.blit(texto, (margem + 5, margem + 2))

# --- MOTOR PRINCIPAL DO JOGO ---

class Jogo:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Python RPG Profissional - Estrutura Pronta")
        self.tela = pygame.display.set_mode((LARGURA, ALTURA))
        self.relogio = pygame.time.Clock()
        
        # Carrega a arte primeiro
        self.assets = Spritesheet()
        
        # Grupos de Sprites (para gerenciamento eficiente)
        self.todos_sprites = pygame.sprite.Group()
        self.paredes = pygame.sprite.Group()
        
        self.inicializar_mundo()
        self.ui = InterfaceUsuario(self.tela)

    def inicializar_mundo(self):
        """Lê a matriz do mapa e cria os objetos correspondentes."""
        for y, linha in enumerate(DESIGN_MAPA):
            for x, tile in enumerate(linha):
                if tile == 'P':
                    # Cria uma parede
                    bloco = Bloco(x, y, self.assets.parede, eh_parede=True)
                    self.todos_sprites.add(bloco)
                    self.paredes.add(bloco)
                elif tile == '.':
                    # Cria o chão
                    bloco = Bloco(x, y, self.assets.chao, eh_parede=False)
                    self.todos_sprites.add(bloco)
                    # O chão não vai para o grupo 'paredes', então não tem colisão

        # Cria o jogador em uma posição válida (ex: tile 2, 2)
        self.jogador = Jogador(2, 2, self.assets.player)
        self.todos_sprites.add(self.jogador)

    def rodar(self):
        executando = True
        while executando:
            self.relogio.tick(FPS)
            
            # 1. Processar Eventos
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    executando = False
            
            # 2. Atualizar Lógica
            # Passamos o grupo 'paredes' para o jogador verificar colisão
            self.jogador.update(self.paredes)
            
            # 3. Desenhar tudo
            self.tela.fill(PRETO) # Limpa a tela com preto
            
            # Desenha todos os sprites na ordem correta
            self.todos_sprites.draw(self.tela)
            
            # Desenha a UI por cima de tudo
            self.ui.desenhar()
            
            # Atualiza o display
            pygame.display.flip()

        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    meu_jogo = Jogo()
    meu_jogo.rodar()