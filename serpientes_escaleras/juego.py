import pygame
import random
import sys
import os

os.chdir(r"C:\Users\Usuario\Documents\scidata\25_fun_py\serpientes y escaleras")

'''Inicializar Pygame'''
pygame.init()

'''crear ventana del juego'''
VENTANA_ANCHO = 1200
VENTANA_ALTO = 600
ventana = pygame.display.set_mode((VENTANA_ANCHO, VENTANA_ALTO))
pygame.display.set_caption("Serpientes y Escaleras de SciData")

'''Configurar frames por segundo'''
reloj = pygame.time.Clock()
FPS = 60

'''Cargar el escenario'''
escenario_imagen = pygame.image.load("tablero.jpg")

'''Sistema de casillas'''
prev_casillas = [[(200+95*k, 520-47*j) for k in range(10)] for j in range(10)]
prev_casillas[1].reverse()
prev_casillas[3].reverse()
prev_casillas[5].reverse()
prev_casillas[7].reverse()
prev_casillas[9].reverse()
CASILLAS = sum(prev_casillas, [])


'''serpientes y escaleras'''
preserpientes = {37:18,65:36,70:54,81:77}
preescaleras = {9:30,25:44,41:62,74:95}

serpientes= {k-1: v-1 for k, v in preserpientes.items()}
escaleras= {k-1: v-1 for k, v in preescaleras.items()}


'''Variables del juego'''
posicion_jugador = 0
dado_valor = None  # Sin valor inicial
juego_activo = True
font = pygame.font.SysFont('Arial', 72)

def dibujar_escenario():
    escenario_escalado = pygame.transform.scale(escenario_imagen, (VENTANA_ANCHO, VENTANA_ALTO))
    ventana.blit(escenario_escalado, (0, 0))

def dibujar_jugador():
    if 0 <= posicion_jugador < len(CASILLAS):
        x, y = CASILLAS[posicion_jugador]
        pygame.draw.circle(ventana, (0, 0, 255), (x, y), 20)

def dibujar_dado():
    if dado_valor is not None:  # Solo dibujar si hay valor
        # Fondo del dado
        pygame.draw.rect(ventana, (255, 255, 255), (50, 50, 100, 100))
        pygame.draw.rect(ventana, (0, 0, 0), (50, 50, 100, 100), 2)
        
        # Puntos del dado
        puntos = {
            1: [(100, 100)],
            2: [(75, 75), (125, 125)],
            3: [(75, 75), (100, 100), (125, 125)],
            4: [(75, 75), (125, 75), (75, 125), (125, 125)],
            5: [(75, 75), (125, 75), (100, 100), (75, 125), (125, 125)],
            6: [(75, 75), (125, 75), (75, 100), (125, 100), (75, 125), (125, 125)]
        }
        for punto in puntos[dado_valor]:
            pygame.draw.circle(ventana, (0, 0, 0), punto, 8)

def dibujar_mensaje_ganador():
    texto = font.render("¡GANASTE!", True, (255, 0, 0))
    ventana.blit(texto, (VENTANA_ANCHO//2 - texto.get_width()//2, 
                         6))

'''Bucle principal'''
running = True
while running:
    reloj.tick(FPS)
    
    # Procesar eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and juego_activo:
            if event.key == pygame.K_SPACE and dado_valor is None:
                dado_valor = random.randint(1, 6)  # Lanzar dado
            elif event.key == pygame.K_RETURN and dado_valor is not None:
                # Mover ficha
                posicion_jugador += dado_valor
                if posicion_jugador in serpientes.keys():
                    posicion_jugador = serpientes[posicion_jugador]
                elif posicion_jugador in escaleras.keys():
                    posicion_jugador = escaleras[posicion_jugador]
                else:
                    posicion_jugador = posicion_jugador
                    
                if posicion_jugador >= 99:
                    if posicion_jugador == 99: 
                        juego_activo = False
                    else:
                        posicion_jugador = 198 - posicion_jugador
                dado_valor = None  # Resetear dado

    # Dibujado
    dibujar_escenario()
    dibujar_jugador()
    dibujar_dado()
    
    if not juego_activo:
        dibujar_mensaje_ganador()
    
    pygame.display.update()

pygame.quit()
sys.exit()