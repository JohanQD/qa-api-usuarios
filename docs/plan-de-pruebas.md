# Plan de pruebas – API de gestión de usuarios

| Campo | Detalle |
| --- | --- |
| Proyecto | Validación de la API de registro y gestión de usuarios |
| Sistema bajo prueba | GoRest API v2 – recurso `/public/v2/users` |
| URL base | `https://gorest.co.in/public/v2` |
| Responsable | Johan Felipe Quiñones Díaz |
| Versión del plan | 1.0 |
| Fecha | [FECHA] |

## 1. Objetivo

Verificar que la API registra, consulta, actualiza y elimina usuarios de forma correcta, segura y consistente, y que rechaza con mensajes claros los datos inválidos y los accesos no autorizados.

## 2. Alcance

### Dentro del alcance

| Endpoint | Método | Funcionalidad |
| --- | --- | --- |
| `/users` | GET | Listar usuarios |
| `/users` | POST | Crear usuario (requiere token) |
| `/users/{id}` | GET | Consultar un usuario |
| `/users/{id}` | PUT / PATCH | Actualizar un usuario (requiere token) |
| `/users/{id}` | DELETE | Eliminar un usuario (requiere token) |

Tipos de prueba: funcionales (positivas y negativas), validación de datos, autenticación, seguridad básica y tiempo de respuesta.

### Fuera del alcance

- Otros recursos de GoRest (posts, comments, todos).
- Pruebas de carga y estrés.
- Pruebas de interfaz gráfica.

## 3. Reglas de negocio validadas

| Campo | Regla |
| --- | --- |
| `name` | Obligatorio |
| `email` | Obligatorio, formato válido y único |
| `gender` | Obligatorio, solo `male` o `female` |
| `status` | Obligatorio, solo `active` o `inactive` |
| Autenticación | Crear, actualizar y eliminar requieren token Bearer válido |

## 4. Riesgos y prioridad

| Riesgo | Impacto en el negocio | Prioridad | Cómo se cubre |
| --- | --- | --- | --- |
| La API acepta datos inválidos o incompletos | Clientes mal registrados y reprocesos | Alta | Casos negativos por campo (CP-005 a CP-011) |
| Se crean usuarios duplicados | Pérdida de trazabilidad | Alta | CP-008 |
| Se permite crear o modificar sin autenticación | Exposición o alteración de datos de terceros | Alta | CP-016 a CP-019 |
| La respuesta expone campos que no debería | Fuga de información | Media | CP-020 |
| Entradas maliciosas generan errores no controlados | Caídas y mala experiencia | Media | CP-021 |
| Tiempos de respuesta altos | Mala experiencia de usuario | Baja | CP-022 |

## 5. Enfoque

1. **Diseño:** partición de equivalencia (valores válidos e inválidos por campo) y análisis de valores límite (campos vacíos, valores fuera del catálogo).
2. **Ejecución manual:** todos los casos en Postman, guardando la colección y las evidencias.
3. **Gestión de defectos:** cada hallazgo se registra en Jira con pasos, resultado esperado contra el obtenido, severidad y prioridad, enlazado a su caso de prueba.
4. **Automatización:** los casos de mayor riesgo se automatizan con Pytest y se agrupan con marcadores (`smoke`, `regression`, `security`, `performance`).
5. **Integración continua:** GitHub Actions ejecuta la suite en cada push y guarda el reporte HTML.

## 6. Entorno y herramientas

| Elemento | Detalle |
| --- | --- |
| Entorno | API pública de GoRest (datos compartidos con otros usuarios) |
| Herramientas | Postman, Jira, Python, Pytest, requests, pytest-html, GitHub Actions |
| Datos de prueba | Correos únicos generados en cada ejecución; los usuarios creados se eliminan al terminar |

## 7. Criterios

- **Entrada:** acceso a la API, token válido y casos de prueba revisados.
- **Salida:** 100% de los casos ejecutados, 100% de los casos de prioridad alta aprobados o con su defecto documentado, y suite automatizada en verde en GitHub Actions.
- **Suspensión:** la API no responde o el token deja de funcionar.

## 8. Entregables

- Este plan de pruebas.
- Casos de prueba con su estado ([casos-de-prueba.md](casos-de-prueba.md)).
- Colección de Postman ([../postman/](../postman/)).
- Reportes de defectos ([reportes-de-bugs/](reportes-de-bugs/)).
- Suite automatizada y reporte HTML.
