# Flask CI/CD Project

## Сипаттамасы
Бұл жоба Python Flask негізіндегі қарапайым веб-қосымша.
Жоба GitHub-қа орналастырылып, GitHub Actions арқылы тәуелділіктерді автоматты орнату және тестілерді автоматты іске қосу бапталған.

## Қолданылатын технологиялар
- Python
- Flask
- pytest
- Git
- GitHub
- GitHub Actions

## Орнату

Python орнатылғаннан кейін:

```bash
pip install -r requirements.txt
```

## Іске қосу

```bash
python app.py
```

Браузерде:

```text
http://127.0.0.1:5000/
```

## Тестілеу

```bash
pytest -v
```

## CI/CD

GitHub Actions pipeline келесі кезеңдерден тұрады:

1. Checkout repository
2. Python ортасын дайындау
3. Dependencies орнату
4. Build
5. pytest арқылы Test

Жобаға push жасалған кезде pipeline автоматты түрде іске қосылады.
