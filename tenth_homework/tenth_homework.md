# Домашнє завдання

## Технічне завдання: Бронювання авіаквитків з Pydantic

## Мета

Попрактикуватися у створенні власних моделей даних на основі `BaseModel` та їх валідації:

- `@field_validator` — перевірка одного поля;
- `@model_validator` — перевірка кількох полів разом;
- `@property` — обчислювані значення на основі полів моделі.

> **Встановлення бібліотеки:**
>
> ```bash
> pip install pydantic
> ```

---

## Основні завдання

## 1. Модель `Passenger`

Поля:

- `first_name: str`;
- `last_name: str`;
- `age: int`.

Вимоги:

- `age` — має бути в межах від **0 до 120** (`@field_validator`).

Додай `@property full_name`, яка повертає `"{first_name} {last_name}"`.

---

## 2. Модель `Flight`

Поля:

- `flight_number: str`;
- `origin: str`;
- `destination: str`;
- `price: float`.

Вимоги:

- `price` — має бути **більшою за 0** (`@field_validator`);
- `origin` не повинен дорівнювати `destination` (`@model_validator(mode="after")`).

Додай `@property route`, яка повертає рядок `"{origin} -> {destination}"`.

---

## 3. Модель `Ticket`

Поля:

- `passenger: Passenger` (вкладена модель);
- `flight: Flight` (вкладена модель);
- `seat_number: int`;
- `has_baggage: bool = False`.

Вимоги:

- `seat_number` — має бути в межах від **1 до 200** (`@field_validator`).

Додай `@property total_price`, яка повертає ціну квитка (`flight.price`) і додає `50`, якщо `has_baggage == True`.

---

## Приклад використання

```python
ticket = Ticket(
    passenger={"first_name": "John", "last_name": "Doe", "age": 25},
    flight={"flight_number": "PS101", "origin": "KBP", "destination": "WAW", "price": 2500},
    seat_number=14,
    has_baggage=True,
)

print(ticket.passenger.full_name)  # John Doe
print(ticket.flight.route)         # KBP -> WAW
print(ticket.total_price)          # 2550.0
```

Спробуй також створити квиток з некоректними даними (наприклад, `age=200` або `origin == destination`) і подивись на `ValidationError`, яку поверне `pydantic`.

---

## Додаткове завдання

Додай до `Passenger` поле `is_child: bool = False`. У `@model_validator` для `Ticket` перевір, що дитина (`is_child=True`) не сидить на аварійному ряду — місця з `seat_number` від `13` до `14`.

---

## Інструкція для студентів

- Весь текст у коді (змінні, функції, повідомлення) — англійською мовою.
- Оформіть рішення у вигляді Pull Request (PR) і надайте мені посилання в особисті повідомлення.
- Не забуваємо про гарні commit messages при використанні команди:

```bash
git commit -m "..."
```
