# 🤖 Chatbot Quiz — opis projektu

# Chatbot Quiz — opis projektu

## PL — Opis (Polski)

Krótki opis
- Prosty projekt z kursu READY 4AI pokazujący generowanie pytań quizowych przy użyciu API Perplexity.
- Główny skrypt: `chatbot_quiz_app_with_Perplexity.py`.

Co robi program
- Wysyła prośbę do modelu Perplexity (model `sonar`) z prośbą o wygenerowanie dokładnie jednego pytania dotyczącego FC Barcelona w formacie JSON.
- Parsuje odpowiedź i uruchamia prosty interaktywny quiz w konsoli (wybór odpowiedzi: a–d).
- Na końcu wyświetla wynik użytkownika.

Wymagania
- Python 3.10+ zalecane.
- Zmienna środowiskowa: `PERPLEXITY_API_KEY` (w pliku `.env`).

Instalacja
1. Stwórz środowisko wirtualne (zalecane):
   ```
   python -m venv .venv
   .venv\Scripts\activate
   ```
2. Zainstaluj zależności:
   ```
   pip install -r requirements.txt
   ```
3. Utwórz plik `.env` z wpisem:
   ```
   PERPLEXITY_API_KEY=twój_klucz
   ```

Uruchomienie
```
python chatbot_quiz_app_with_Perplexity.py
```
- Domyślnie uruchamiany jest quiz z 10 pytaniami (zmień parametr `total_questions` w kodzie, jeśli chcesz).

Najważniejsze pliki
- `chatbot_quiz_app_with_Perplexity.py` — generator pytań i logika quizu.
- `requirements.txt` — lista zależności (pip).
- (opcjonalnie) `backend_api.py`, `frontend/chatbot-react/` — przykładowe komponenty backend/frontend.

Uwagi
- Skrypt oczekuje poprawnego, czystego JSON-a od modelu — warto rozważyć dodatkowe walidacje/parsing i retry.

---

## EN — Description (English)

Short description
- Simple project demonstrating quiz question generation using the Perplexity API.
- Main script: `chatbot_quiz_app_with_Perplexity.py`.

What the program does
- Requests exactly one quiz question (topic: FC Barcelona) from the Perplexity model (`sonar`) in JSON format.
- Parses the response and runs a console-based interactive quiz (answer choices a–d).
- Shows the final score.

Requirements
- Python 3.10+ recommended.
- Environment variable: `PERPLEXITY_API_KEY` (e.g., in a `.env` file).

Installation
1. Create a virtual environment (recommended):
   ```
   python -m venv .venv
   .venv\Scripts\activate
   ```
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Create a `.env` file with:
   ```
   PERPLEXITY_API_KEY=your_key
   ```

Run
```
python chatbot_quiz_app_with_Perplexity.py
```
- The quiz runs with 10 questions by default (change `total_questions` in the script to adjust).

Key files
- `chatbot_quiz_app_with_Perplexity.py` — question generator and quiz logic.
- `requirements.txt` — pip dependencies.
- Optional: `backend_api.py`, `frontend/chatbot-react/` — example backend/frontend components.

Notes
- The script assumes the model returns valid JSON; add validation and retries for robustness.
- Add a LICENSE file before publishing the repository.





