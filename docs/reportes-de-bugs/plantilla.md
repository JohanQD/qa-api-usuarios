# [BUG-001] Título corto y específico del defecto

> Ejemplo de título: "POST /users responde 201 al crear un usuario con email sin dominio"

| Campo | Detalle |
| --- | --- |
| ID en Jira | [CLAVE-123] |
| Caso de prueba relacionado | [CP-000] |
| Endpoint y método | [POST /public/v2/users] |
| Entorno | GoRest API v2 – https://gorest.co.in |
| Fecha | [FECHA] |
| Reportado por | Johan Felipe Quiñones Díaz |
| Severidad | [Crítica / Alta / Media / Baja] |
| Prioridad | [Alta / Media / Baja] |
| Estado | [Abierto / En revisión / Cerrado] |

## Descripción

[Qué falla, en una o dos frases, y por qué importa para el negocio.]

## Precondiciones

- [Ej.: tener un token válido configurado en el header Authorization.]

## Pasos para reproducir

1. [Enviar una petición POST a `/public/v2/users`...]
2. [Con el siguiente cuerpo:]

```json
{
  "name": "QA Tester",
  "email": "ejemplo",
  "gender": "male",
  "status": "active"
}
```

3. [Revisar el código de estado y el cuerpo de la respuesta.]

## Resultado esperado

[Ej.: 422 con un error en el campo `email` indicando que el formato no es válido.]

## Resultado obtenido

[Ej.: 201 y el usuario queda creado con un email inválido.]

## Evidencia

- [Captura de Postman o del reporte HTML]
- [Respuesta completa de la API]

## Notas

[Frecuencia (siempre / a veces), impacto, posible causa o sugerencia.]

---

**Guía de severidad**

| Severidad | Cuándo usarla |
| --- | --- |
| Crítica | Bloquea una función principal o compromete la seguridad de los datos |
| Alta | Una función importante falla y no hay una alternativa razonable |
| Media | La función falla parcialmente o hay una alternativa |
| Baja | Problema menor: mensajes, formato o detalles sin impacto funcional |
