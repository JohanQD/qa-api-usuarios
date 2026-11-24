# Casos de prueba – API de gestión de usuarios

Casos diseñados con partición de equivalencia y análisis de valores límite. Actualiza la columna **Estado** después de ejecutar cada caso en Postman (Aprobado, Fallido o Bloqueado) y enlaza el reporte de Jira cuando haya un hallazgo.

**Datos válidos de referencia:** `name`: "QA Tester", `email`: correo único, `gender`: "male" o "female", `status`: "active" o "inactive".

## Funcionales – flujo principal

| ID | Caso | Técnica | Resultado esperado | Prioridad | Automatizado | Estado |
| --- | --- | --- | --- | --- | --- | --- |
| CP-001 | Listar usuarios | Positiva | 200 y una lista en formato JSON | Alta | Sí | Pendiente |
| CP-002 | Crear usuario con datos válidos | Positiva | 201, id generado y datos iguales a los enviados | Alta | Sí | Pendiente |
| CP-003 | Consultar el usuario recién creado | Positiva | 200 y datos iguales a los registrados | Alta | Sí | Pendiente |
| CP-004 | Consultar un usuario que no existe | Negativa | 404 y mensaje de recurso no encontrado | Media | Sí | Pendiente |

## Validación de datos al crear

| ID | Caso | Técnica | Resultado esperado | Prioridad | Automatizado | Estado |
| --- | --- | --- | --- | --- | --- | --- |
| CP-005 | Crear sin `name` | Partición de equivalencia (campo vacío) | 422 con error en `name` | Alta | Sí | Pendiente |
| CP-006 | Crear sin `email` | Partición de equivalencia (campo vacío) | 422 con error en `email` | Alta | Sí | Pendiente |
| CP-007 | Crear con `email` de formato inválido (`correo.com`) | Partición de equivalencia (formato inválido) | 422 con error en `email` | Alta | Sí | Pendiente |
| CP-008 | Crear con un `email` ya registrado | Regla de negocio (unicidad) | 422 con error en `email` | Alta | Sí | Pendiente |
| CP-009 | Crear con `gender` fuera del catálogo (`otro`) | Valores fuera del catálogo | 422 con error en `gender` | Media | Sí | Pendiente |
| CP-010 | Crear con `status` fuera del catálogo (`pendiente`) | Valores fuera del catálogo | 422 con error en `status` | Media | Sí | Pendiente |
| CP-011 | Crear con el cuerpo vacío | Valor límite (sin datos) | 422 con errores en los 4 campos | Media | Sí | Pendiente |

## Actualización y eliminación

| ID | Caso | Técnica | Resultado esperado | Prioridad | Automatizado | Estado |
| --- | --- | --- | --- | --- | --- | --- |
| CP-012 | Actualizar todos los campos con PUT | Positiva | 200 y datos actualizados | Media | Sí | Pendiente |
| CP-013 | Actualizar solo `status` con PATCH | Positiva | 200; cambia `status` y el resto se mantiene | Media | Sí | Pendiente |
| CP-014 | Actualizar con `email` de formato inválido | Negativa | 422 con error en `email` | Media | Sí | Pendiente |
| CP-015 | Eliminar un usuario y consultarlo después | Positiva | 204 al eliminar y 404 al consultar | Alta | Sí | Pendiente |

## Seguridad

| ID | Caso | Técnica | Resultado esperado | Prioridad | Automatizado | Estado |
| --- | --- | --- | --- | --- | --- | --- |
| CP-016 | Crear usuario sin token | Autenticación | 401; no se crea el usuario | Alta | Sí | Pendiente |
| CP-017 | Crear usuario con token inválido | Autenticación | 401; no se crea el usuario | Alta | Sí | Pendiente |
| CP-018 | Actualizar un usuario sin token | Autorización | La API no permite el cambio (sin respuesta 2xx) | Alta | Sí | Pendiente |
| CP-019 | Eliminar un usuario sin token | Autorización | La API no permite la eliminación (sin respuesta 2xx) | Alta | Sí | Pendiente |
| CP-020 | La respuesta solo expone los campos esperados | Exposición de datos | Solo `id`, `name`, `email`, `gender` y `status` | Media | Sí | Pendiente |
| CP-021 | Crear con texto malicioso en `name` (script o SQL) | Entradas maliciosas | Sin error 500; si se acepta, se guarda como texto literal | Media | Sí | Pendiente |

## No funcionales

| ID | Caso | Técnica | Resultado esperado | Prioridad | Automatizado | Estado |
| --- | --- | --- | --- | --- | --- | --- |
| CP-022 | Tiempo de respuesta al listar usuarios | Rendimiento básico | Menos de 2 segundos | Baja | Sí | Pendiente |

## Resumen de ejecución

| Total | Aprobados | Fallidos | Bloqueados | Pendientes |
| --- | --- | --- | --- | --- |
| 22 | [N] | [N] | [N] | [N] |
