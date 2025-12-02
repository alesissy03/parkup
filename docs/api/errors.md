# ParkUPB – Format erori API

Toate erorile REST vor avea următorul format JSON:

```json
{
  "error": "COD_SIMPLU",
  "message": "Descriere prietenoasă pentru utilizator / developer."
}

exemple:
{
  "error": "INVALID_DATA",
  "message": "Câmpul 'email' este obligatoriu."
}

{
  "error": "EMAIL_TAKEN",
  "message": "Adresa de email este deja folosită."
}

{
  "error": "INVALID_CREDENTIALS",
  "message": "Email sau parolă incorectă."
}
