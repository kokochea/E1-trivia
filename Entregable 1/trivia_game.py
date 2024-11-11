import pandas as pd
from functools import reduce
from itertools import chain
#Decorador que muestra un menu para empezar el juego
def menu(func, *args, **kwargs) -> callable:
    def wrapper(*args, **kwargs):
        print("Bienvenido al juego Preguntas y Respuestas\n¿Quieres comenzar? (Y/N)")
        player_answer = input().upper()
        if (player_answer=="Y"):
            print(f"\nJuego finalizado! \nTu puntuacion final es:", func(*args, **kwargs))
        elif(player_answer=="N"):
            print("Saliendo del juego...")
            quit()
        else:
            print("Has seleccionado una opcion incompatible, saliendo del juego...")
    return wrapper

#Quita los espacios y comillas innecesarios
def clean(list_of_questions):
    no_quotes = list(map(lambda x: x.replace('"', '').strip(), list_of_questions))
    return no_quotes

#Selecciona una cantidad especificada de preguntas de la base de preguntas
def get_random_questions(database, amount):
    return database.sample(n=amount).values.tolist()

#Realiza una pregunta, y compara el resultado correcto con la respuesta del usuario
def ask_question(next_question):
    question = (next_question[0])
    possible_answers = clean(next_question[1:4])
    correct_answer = next_question[4].replace('"', '').strip()

    print("\n", question, "\n")

    list(map(lambda x: print(f"{x+1}: {possible_answers[x]}"), range(len(possible_answers))))
    player_answer = input("Tu respuesta: ")

    if (player_answer == correct_answer):
        print("Correcto!")
        return 10
    else:
        print("Incorrecto!")
        print(f"La opcion correcta es", correct_answer)
        return 0

@menu
def trivia():
    db1 = pd.read_csv(r'c:\Users\Agust\OneDrive - Universidad de Montevideo\3er Año\Segundo Semestre\Programacion Avanzada\Entregable 1\trivia_questions.csv')
    # db2 = pd.read_csv(r'c:\ruta\a\otra_trivia_questions.csv')
    # all_db = list(chain(db1, db2))
    questions = iter(get_random_questions(db1, 5))
    scores = list(map(lambda x: ask_question(x), questions))
    final_score = reduce(lambda x,y: x+y, scores)
    return(final_score) 
        
if __name__ == '__main__':
    trivia()