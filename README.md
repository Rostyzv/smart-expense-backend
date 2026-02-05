# Smart Expense Backend (Python)

Este es el servidor central (API) que gestiona los datos de la aplicación de gastos. Está construido con FastAPI.

Características
API REST: Endpoints para leer y guardar gastos.
Base de Datos: SQLite integrado (no requiere configuración externa).
Compatibilidad: Diseñado para conectar con la app móvil: 
[Smart Expense Tracker](https://github.com/Rostyzv/smart-expense-tracker)

Cómo ejecutar
- Instalar dependencias: `pip install fastapi uvicorn`
- Ejecutar: `python -m uvicorn main:app --reload --host 0.0.0.0`
