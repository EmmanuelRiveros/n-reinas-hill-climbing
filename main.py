# Last Updated: 28 October 2025
# Author: emreozdincer
# Fork: EmmanuelRiveros

# Opciones de configuración
use_colors = True # Si se instalo termcolor, marcar como True para usar colores en la salida
board_size = 10 # Tamaño de la tabla (N)
num_restarts = 1 # Numero de reinicios
print_iterations = False # Imprimir los estados de la tabla y la puntuacion en cada iteracion

if __name__ == "__main__":
    if use_colors:
        import n_queens

    successes = 0
    failures = 0
    for _ in range(num_restarts):
        game = n_queens.Game(board_size)

        # Los diferentes algoritmos de búsqueda pueden ser probados comentando/descomentando las siguientes lineas
        # En nuestro caso solo utilizaremos Hill Climbing
        is_successful = game.hill_climb_random_restart(max_restarts=1000, verbose=print_iterations)
        #is_successful = game.hill_climb(print_iterations)
        # is_successful = game.first_best_hill_climb(print_iterations)

        # Temperature = Temperature - Cooling Factor
        # is_successful = game.simulated_annealing(temperature=10000, cooling_factor=1, verbose=print_iterations)

        #if is_successful:
            #successes += 1
        #else:
            #failures += 1

    #print ("Successes: " + str(successes) + "\nFailures: " + str(failures))
