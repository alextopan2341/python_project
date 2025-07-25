# Calculator Microservice

Un microserviciu RESTful construit cu **FastAPI**, **SQLite** și **Pydantic**, care expune operații matematice:

* **pow**: ridicarea la putere
* **fibonacci**: al n-lea număr Fibonacci
* **factorial**: factorialul unui număr

Toate cererile către API sunt persistate într-o bază de date SQLite.

---

## Caracteristici

* Endpoints HTTP JSON
* Validare și serializare cu Pydantic
* Persistență a cererilor în SQLite
* Autentificare simplă cu **API Key**
* Monitorizare prin **Prometheus**
* Caching local cu **lru\_cache**
* Containerizare cu **Docker**
* Testare automată cu **pytest**

---

## Structura proiectului

```
calculator-sqlite/
├── app/
│   ├── config.py        # Setări și variabile de mediu
│   ├── db.py            # Configurare SQLAlchemy + inițializare DB
│   ├── models.py        # Modele ORM SQLAlchemy
│   ├── schemas.py       # Modele Pydantic
│   ├── crud.py          # Operații de acces la date
│   ├── utils.py         # Funcții de calcul (pow, fib, fact)
│   ├── dependencies.py  # Dependențe FastAPI (DB, auth)
│   └── main.py          # Definirea API-ului și rutelor
├── tests/
│   └── test_endpoints.py # Teste cu pytest
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .flake8
└── README.md
```

---

## Cerințe

* Python 3.11+
* SQLite (implicit, nu necesită instalare separată)
* Docker (opțional, pentru containerizare)

Instalare dependențe:

```bash
python -m venv .venv
. .venv/bin/activate   # Linux/macOS
. .venv\Scripts\activate.ps1  # Windows PowerShell
pip install --upgrade pip
pip install -r requirements.txt
```

---

## Variabile de mediu

Folosește un fișier `.env` în rădăcină cu:

```env
API_KEY=supersecretkey
DATABASE_URL=sqlite:///./requests.db
KAFKA_BOOTSTRAP=localhost:9092
```

---

## Pornire locală

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

* Documentație Swagger UI: `http://127.0.0.1:8000/docs`
* Documentație ReDoc:       `http://127.0.0.1:8000/redoc`
* Metrice Prometheus:      `http://127.0.0.1:8000/metrics`

---

## Endpoints API

| Metodă | Endpoint         | Descriere                            |
| ------ | ---------------- | ------------------------------------ |
| POST   | `/pow`           | Ridică `x` la puterea `y`.           |
| POST   | `/fibonacci/{n}` | Returnează al n-lea număr Fibonacci. |
| POST   | `/factorial/{n}` | Returnează `n!`.                     |

### Exemple

#### Ridicare la putere

```bash
curl -X POST http://127.0.0.1:8000/pow \
  -H "Content-Type: application/json" \
  -H "x-api-key: supersecretkey" \
  -d '{"x":2,"y":3}'
```

#### Fibonacci

```bash
curl -X POST http://127.0.0.1:8000/fibonacci/10 \
  -H "x-api-key: supersecretkey"
```

#### Factorial

```bash
curl -X POST http://127.0.0.1:8000/factorial/5 \
  -H "x-api-key: supersecretkey"
```

---

## Testare

```bash
pytest --maxfail=1 -q
```

---

## Docker

### Build image

```bash
docker build -t calculator-ms .
```

### Rulează container

```bash
docker run -d -p 8000:80 \
  -e API_KEY=supersecretkey \
  -e DATABASE_URL=sqlite:///./requests.db \
  calculator-ms
```

---

## Extensii

* Caching distribuit cu **Redis** (prin aiocache)
* Logging distribuit cu **Kafka**
* Autorizare OAuth2/JWT
* CI/CD: integrare cu GitHub Actions/GitLab CI pentru lint și teste

---

## Licență

Acest proiect este licențiat sub MIT License.
