import sys
import pygame

vermelho = (255, 0, 0)
verde = (0, 255, 0)
azul = (0, 0, 255)
imagem = 'nerd_blue2.bmp'


class MeNerd():
    def __init__(self, screen):
        """[Inicializa a imagem de Nerd]
        """
        self.screen = screen

        # Carrega a imagem do Nerd e obtém seu rect
        self.image = pygame.image.load(imagem)
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Inicia a imagem na parte inferior central da tela
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        """[Desenha a imagem em sua posição atual]
        """
        self.screen.blit(self.image, self.rect)


def run_tela():
    # Inicializa e cria um objeto para a tela
    pygame.init()
    screen = pygame.display.set_mode((600, 400))
    pygame.display.set_caption('<< TELA AZUL >>')

    # Cria um Nerd
    me_nerd = MeNerd(screen)

    # Define a cor de fundo
    bg_color = azul

    # Inicia o laço principal da aplicação
    while True:

        # Observa eventos de teclado e mouse
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Redesenha a tela a cada passagem pelo laço
        screen.fill(bg_color)
        me_nerd.blitme()

        # Deixa a tela mais recente visível
        pygame.display.flip()


run_tela()
