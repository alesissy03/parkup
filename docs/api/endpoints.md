# ParkUPB API – Endpoints

## Autentificare

### POST /api/auth/register  (Task 5)
- Creează un utilizator nou.
- Vezi docstring în app/routes/auth.py::register

### POST /api/auth/login  (Task 5)
- Autentificare utilizator.
- Vezi docstring în app/routes/auth.py::login

---

## Parcări & locuri

### GET /api/parking/lots  (Task 6, 7, 8)
- Listează parcările (parking lots).

### GET /api/parking/spots  (Task 6, 7, 8)
- Listează locurile de parcare (parking spots), opțional filtrate.

---

## Rezervări

### POST /api/reservations/  (Task 9)
- Creează o rezervare nouă.

### DELETE /api/reservations/{id}  (Task 9)
- Anulează o rezervare.

### GET /api/reservations/my  (Task 10)
- Istoricul rezervărilor user-ului curent.

---

## Admin

### POST /api/admin/polygons  (Task 6)
- Salvează poligoanele desenate (GeoJSON).

### GET /api/admin/stats  (Task 11)
- Returnează statistici globale.
