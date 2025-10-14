from perplexity import Perplexity
from dotenv import load_dotenv
import json

load_dotenv()

client = Perplexity()


print("Witaj w piłkarskim quizie o FC Barcelona. Przed tobą 10 pytań.")
print("Chatbot AI generuje pytanie: ")

quiz_schema = {
    "type": "object",
    "properties": {
        "question": {"type": "string"},
        "options": {
            "type": "array",
            "items": {"type": "string"},
            "minItems": 4,
            "maxItems": 4,
        },
        "correct_answer_index": {"type": "integer"},
    },
    "required": ["question", "options", "correct_answer_index"],
    "additionalProperties": False,
}


def get_quiz_question(asked_questions=None):
    """
    asked_questions: lista stringów z treściami już zadanych pytań
    """
    if asked_questions is None:
        asked_questions = []

    base_prompt = """
Jesteś generatorem quizów dotyczących klubu piłkarskiego FC Barcelona. Wygeneruj dokładnie 
JEDNO pytanie quizowe z 4 opcjami odpowiedzi.

KRYTYCZNE: NIE POWTARZAJ pytań z poniższej listy!
"""


    if asked_questions:
        base_prompt += "\n\nJUŻ ZADANE PYTANIA (NIE POWTARZAJ):\n"
        for i, q in enumerate(asked_questions, 1):
            base_prompt += f"{i}. {q}\n"

    base_prompt += """
    
WAŻNE: Zwróć JSON dokładnie w tym formacie:
{
  "question": "Treść pytania",
  "options": ["opcja a", "opcja b", "opcja c", "opcja d"],
  "correct_answer_index": 0
}

Gdzie "correct_answer_index" to liczba 0-3 (0=a, 1=b, 2=c, 3=d).
Pytanie musi być RÓŻNE od wszystkich wyżej wymienionych!
"""

    response = client.chat.completions.create(
        model="sonar",
        messages=[
            {
                "role": "system",
                "content": "Jesteś pomocnym asystentem tworzenia unikalnych quizów sportowych.",
            },
            {"role": "user", "content": base_prompt},
        ],
        response_format={"type": "json_schema", "json_schema": {"schema": quiz_schema}},
        temperature=0.8,  
    )
    content = response.choices[0].message.content

    return json.loads(content)


def quiz(total_questions):
    points = 0
    letters = ["a", "b", "c", "d"]
    asked_questions = []  

    for i in range(total_questions):
        
        question_data = get_quiz_question(asked_questions)
        current_question = question_data["question"]

        asked_questions.append(current_question)

        print(f"\nPytanie {i+1}/{total_questions}: {current_question}")

        for idx, option in enumerate(question_data["options"]):
            print(f" {letters[idx]}. {option}")

        while True:
            answer = input("Twoja odpowiedź (a-d): ").lower()
            if answer in letters:
                break
            print("Podaj literę od a do d!")

        answer_index = letters.index(answer)
        correct_index = question_data["correct_answer_index"]

        if answer_index == correct_index:
            print("✓ Poprawna odpowiedź!")
            points += 1
        else:
            correct_letter = letters[correct_index]
            correct_option = question_data["options"][correct_index]
            print(
                f"✗ Błędna odpowiedź. Poprawna to: {correct_letter}. {correct_option}"
            )

    print(f"\n{'='*50}")
    print(
        f"Koniec quizu! Wynik: {points}/{total_questions} ({points/total_questions*100:.0f}%)"
    )
    print(f"{'='*50}")


if __name__ == "__main__":
    quiz(total_questions=10)
