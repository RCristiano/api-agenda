# API Agenda

Api de agendamento veterinário

```mermaid
erDiagram
    Owner {
        int id PK "Primary Key"
        string name "Owner name"
        string email "Owner email"
        string phone "Owner phone"
        string address "Owner address"
        string city "Owner city"
    }
    Pet {
        int id PK "Primary Key"
        int owner_id FK "Foreign Key"
        string name "Pet name"
    }
    Veterinarian {
    int id PK "Primary Key"
        string name "Veterinarian name"
    }
    Chart {
        int id PK "Primary Key"
        int pet_id FK "Foreign Key"
        int vet_id FK "Foreign Key"
        string date "chart date"
        string time "chart time"
        string description "chart description"
    }
    Owner ||--|{ Pet : has
    Chart }|--|| Pet : includes
    Chart }|--|| Veterinarian : includes
```

```mermaid
classDiagram
    class Application{
        Int id
        Int owner_id
        Int pet_id
        Enum status
        String Description
        +insert_application(pet_id, status, Description)
        +get_application(id)
        +update_application(id, status, Description)
        +status_update(id, status)
    }
    class Owner{
        Int id
        int cpf
        String password
        String Name
        String Email
        String Phone
        String Address
        String City
        +get_owner(id)
        +get_pets(id)
        +add_owner(name, email, phone, address, city)
        +update_owner(id, name, email, phone, address, city)
    }
    class Pet{
        Int id
        Int owner_id
        String Name
        DateTime birth
        Enum species
        +getPet(id)
        +add_pet(owner_id, name)
        +update_pet(id, owner_id, name)
        +get_charts(id)
    }
    class Chart{
        Int id
        Int pet_id
        +get_chart(id)
        +add_chart(pet_id, vet_id, date, time, description)
        +update_chart(id, pet_id, vet_id, date, time, description)
    }
    class Exam{
        Int id
        Int chart_id
        String Doctor
        DateTime execution_date
        String type
        String file_link
        +insert(chart_id, Doctor, execution_date, type, file_link)
    }
    class Pathology{
        Int id
        Int chart_id
        String Description
        +insert(chart_id, Description)
    }
    Application "N" --> "1" Pet
    Owner "1" --> "*" Pet : has
    Chart "1" --> "1" Pet : includes
    Chart "1" --> "*" Exam
    Chart "1" --> "*" Pathology
```

## Tech Stack

### Development

- [Git](https://git-scm.com/)
- [Python](https://www.python.org/) >= 3.10
- [Poetry](https://python-poetry.org/)

### Backend

- [FastAPI](https://fastapi.tiangolo.com/)

### Security

- [JWT](https://jwt.io/)

## Run Locally

Clone the project

```bash
git clone https://github.com/RCristiano/agente-agenda
```

Go to the project directory

```bash
cd agente-agenda
```

Install dependencies

```bash
poetry install
```

Start the server

```bash
poetry run uvicorn main:app --reload
```

### Live server

Open your browser at <http://127.0.0.1:8000>.

### Interactive API docs

Go to <http://127.0.0.1:8000/docs>.

### Alternative API docs

And now, go to <http://127.0.0.1:8000/redoc>.

## Authors

- Alexandre Junio dos Santos Vieira, RA 2010464
- Fábio Borges Dias, RA 2007056
- [Fabio Rogerio Lins Pereira de Souza](https://github.com/frlps), RA 2003660
- Gustavo Guerreiro Martinho da Cunha Sales, RA 2001642
- Marcio M. Marcelli, RA 2002829
- [Rodrigo Cristiano Ferreira Vieira](https://www.github.com/RCristiano), RA 2015474
- Vanderlei Claudio, RA 1827341
