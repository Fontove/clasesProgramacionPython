import math
import turtle

# Configurar la ventana
pantalla = turtle.Screen()
pantalla.title("Hoja cayendo")
pantalla.bgcolor("lightblue")
pantalla.setup(width=600, height=600)
pantalla.tracer(0)  # Desactivar animación automática para controlarla nosotros

SUELO_Y = -250   # Altura del borde superior del suelo
LARGO = 70       # Largo de la hoja (sin el tallo)
ANCHO = 16       # Medio ancho máximo de la hoja


def a_forma(puntos):
    """Convierte puntos (x, y) de la hoja, con la hoja apuntando a la derecha,
    al sistema de coordenadas que usa turtle para las formas."""
    return tuple((-y, x) for (x, y) in puntos)


def medio_ancho(t):
    """Medio ancho de la hoja en la posición t (0 = base, 1 = punta)."""
    ancho = ANCHO * math.sin(math.pi * t ** 0.75)   # Base redonda, punta afilada
    ancho *= 1 + 0.03 * math.sin(t * 60)            # Borde ligeramente dentado
    return ancho


def punto_en(t, lado):
    """Punto en el borde de la hoja. lado = 1 arriba, -1 abajo."""
    x = -LARGO / 2 + t * LARGO
    curva = 3 * math.sin(math.pi * t)               # La hoja está un poco curvada
    return (x, curva + lado * medio_ancho(t))


def linea_gruesa(x1, y1, x2, y2, grosor1, grosor2):
    """Polígono delgado entre dos puntos, más grueso al inicio (para venas y tallo)."""
    largo = math.hypot(x2 - x1, y2 - y1)
    nx, ny = -(y2 - y1) / largo, (x2 - x1) / largo  # Dirección perpendicular
    return [
        (x1 + nx * grosor1 / 2, y1 + ny * grosor1 / 2),
        (x2 + nx * grosor2 / 2, y2 + ny * grosor2 / 2),
        (x2 - nx * grosor2 / 2, y2 - ny * grosor2 / 2),
        (x1 - nx * grosor1 / 2, y1 - ny * grosor1 / 2),
    ]


# Construir la forma de la hoja a partir de varias piezas
hoja_forma = turtle.Shape("compound")

# Tallo
base_x = -LARGO / 2
hoja_forma.addcomponent(
    a_forma(linea_gruesa(base_x - 14, -3, base_x + 2, 0, 1.5, 2.5)), "#5c3317", "#5c3317"
)

# Lámina de la hoja
pasos = 40
borde = [punto_en(i / pasos, 1) for i in range(pasos + 1)]
borde += [punto_en(i / pasos, -1) for i in range(pasos, -1, -1)]
hoja_forma.addcomponent(a_forma(borde), "#e0661b", "#8b3a0f")

# Vena central
centro = [punto_en(i / pasos, 0) for i in range(int(pasos * 0.95) + 1)]
for (x1, y1), (x2, y2) in zip(centro, centro[1:]):
    hoja_forma.addcomponent(a_forma(linea_gruesa(x1, y1, x2, y2, 1.6, 1.6)), "#8b3a0f", "#8b3a0f")

# Venas laterales: salen de la vena central hacia la punta
for t in (0.15, 0.3, 0.45, 0.6, 0.75):
    x0, y0 = punto_en(t, 0)
    for lado in (1, -1):
        largo_vena = medio_ancho(t) * 0.85
        x1 = x0 + largo_vena * 0.8
        y1 = y0 + lado * largo_vena * 0.75
        hoja_forma.addcomponent(
            a_forma(linea_gruesa(x0, y0, x1, y1, 1.2, 0.3)), "#a3471a", "#a3471a"
        )

pantalla.register_shape("hoja", hoja_forma)

# Dibujar el suelo
suelo = turtle.Turtle()
suelo.hideturtle()
suelo.penup()
suelo.goto(-310, SUELO_Y)
suelo.color("forestgreen")
suelo.begin_fill()
for _ in range(2):
    suelo.forward(620)
    suelo.right(90)
    suelo.forward(100)
    suelo.right(90)
suelo.end_fill()

# Crear la hoja
hoja = turtle.Turtle()
hoja.shape("hoja")
hoja.penup()

x_inicial = 0
y = 300
tiempo = 0
ALTURA_REPOSO = SUELO_Y + ANCHO * 0.6  # Hoja acostada sobre el pasto


def caer():
    global y, tiempo
    tiempo += 0.04
    y -= 1.5                                       # Baja poco a poco
    x = x_inicial + math.sin(tiempo) * 110         # Se balancea de lado a lado
    giro = math.cos(tiempo) * 35                   # Se inclina al balancearse

    if y > ALTURA_REPOSO:
        hoja.goto(x, y)
        hoja.setheading(giro)
        pantalla.update()
        pantalla.ontimer(caer, 20)
    else:
        # Llegó al suelo: se queda acostada
        hoja.goto(x, ALTURA_REPOSO)
        hoja.setheading(0)
        pantalla.update()


hoja.goto(x_inicial, y)
caer()
pantalla.mainloop()
