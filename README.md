# Sistema de Chat en Tiempo Real con Salas Seguras

**Universidad de las Fuerzas Armadas ESPE**  
**Aplicaciones Distribuidas - Parcial I**  
**Docente:** Geovanny Cudco  
**Fecha:** 03 de noviembre de 2025

---

## Descripción

Chat en tiempo real con:
- Salas seguras por PIN
- Dos tipos: **texto** y **multimedia**
- Autenticación de administrador
- Sesión única por IP
- Subida de archivos (≤10MB)
- WebSockets + hilos para concurrencia
- Frontend responsivo en React
- Backend en Python (Flask + SocketIO)

---

## Requisitos Previos

- Python 3.9+
- Node.js 18+
- Redis (opcional, para sesiones)
- Docker (opcional)

---

## Instalación

```bash
# Backend
cd backend
pip install -r requirements.txt
python app.py

# Frontend
cd frontend
npm install
npm run dev