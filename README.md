# Validación de la API de registro y gestión de usuarios

Proyecto de QA de extremo a extremo sobre una API REST de usuarios: plan de pruebas, diseño de casos, ejecución manual en Postman, gestión de defectos en Jira y una suite automatizada con Python y Pytest que se ejecuta sola en GitHub Actions.

![Estado de las pruebas](https://github.com/JohanQD/qa-api-usuarios/actions/workflows/api-tests.yml/badge.svg)

> **Autor:** Johan Felipe Quiñones Díaz · QA Tester · Bogotá, Colombia
> [LinkedIn](https://www.linkedin.com/in/johanquinonesqa) · [GitHub](https://github.com/JohanQD)

---

## 1. Problema identificado

En una fintech, un e-commerce o cualquier plataforma digital, el registro y la gestión de usuarios es la puerta de entrada del cliente. Si la API que lo soporta falla, el impacto llega directo al negocio:

- **Datos inválidos o incompletos** que generan clientes mal registrados y reprocesos.
- **Usuarios duplicados** que afectan la trazabilidad y los reportes.
- **Accesos sin autenticación** que exponen o modifican información de terceros.
- **Errores no controlados** que se convierten en casos de soporte y en mala experiencia.

**Pregunta de negocio:** ¿la API registra, consulta, actualiza y elimina usuarios de forma correcta, segura y consistente, y rechaza con claridad los datos inválidos?

## 2. Solución desarrollada

Apliqué un ciclo completo de QA sobre la API pública [GoRest](https://gorest.co.in) (recurso `/public/v2/users`), que usa autenticación con token Bearer y responde con errores de validación por campo, igual que muchas APIs reales.

1. **Plan de pruebas:** alcance, riesgos, enfoque y criterios de aceptación. → [docs/plan-de-pruebas.md](docs/plan-de-pruebas.md)
2. **Diseño de casos de prueba** con partición de equivalencia y análisis de valores límite. → [docs/casos-de-prueba.md](docs/casos-de-prueba.md)
3. **Ejecución manual en Postman** de todos los casos, con la colección exportada. → [postman/](postman/)
4. **Gestión de defectos y hallazgos en Jira**, enlazados a los casos de prueba. → [docs/reportes-de-bugs/](docs/reportes-de-bugs/)
5. **Automatización con Pytest** de los casos de mayor riesgo, organizados por tipo (`smoke`, `regression`, `security`, `performance`). → [tests/](tests/)
6. **Integración continua con GitHub Actions:** la suite corre en cada cambio y genera un reporte HTML descargable. → [.github/workflows/api-tests.yml](.github/workflows/api-tests.yml)

## 3. Herramientas utilizadas

| Área | Herramientas |
| --- | --- |
| Pruebas manuales de API | Postman |
| Gestión de casos y defectos | Jira (plan gratuito) |
| Automatización | Python, Pytest, requests |
| Reportes | pytest-html |
| Control de versiones e integración continua | Git, GitHub, GitHub Actions |
| Técnicas de diseño | Partición de equivalencia, valores límite, pruebas negativas, pruebas de seguridad básicas |

## 4. Resultados

> Completa esta tabla con tus cifras reales al terminar el proyecto.

| Indicador | Resultado |
| --- | --- |
| Casos de prueba diseñados | [NÚMERO] |
| Casos ejecutados manualmente en Postman | [NÚMERO] |
| Casos automatizados con Pytest | [NÚMERO] |
| Hallazgos documentados en Jira | [NÚMERO] |
| Tiempo de ejecución de la suite automatizada | [SEGUNDOS] |
| Ejecución en CI | En cada push, con reporte HTML como artefacto |

**Hallazgos principales:** [Resume aquí los 2 o 3 hallazgos más relevantes, con enlace a su reporte.]

**Valor para una empresa:**

- Una regresión automática que se ejecuta en cada cambio y detecta fallos antes de que lleguen al cliente.
- Casos de prueba trazables a los riesgos del negocio (datos inválidos, duplicados, accesos no autorizados).
- Documentación lista para que cualquier persona del equipo entienda qué se probó, qué se encontró y cómo reproducirlo.

**Evidencias:**

- [CAPTURA DEL REPORTE HTML]
- [CAPTURA DEL TABLERO DE JIRA]
- [CAPTURA DE LA EJECUCIÓN EN GITHUB ACTIONS]

## 5. Cómo ejecutar el proyecto

### Requisitos

- Python 3.10 o superior
- Un token gratuito de GoRest: inicia sesión en [gorest.co.in](https://gorest.co.in/consumer/login) y copia tu token de acceso.

### Ejecución local

```bash
# 1. Clonar el repositorio
git clone https://github.com/JohanQD/qa-api-usuarios.git
cd qa-api-usuarios

# 2. Crear un entorno virtual e instalar dependencias
python -m venv venv
source venv/bin/activate        # En Windows: venv\Scripts\activate
pip install -r requirements.txt

# 3. Configurar el token (nunca lo subas al repositorio)
export GOREST_TOKEN="tu_token"  # En Windows (PowerShell): $env:GOREST_TOKEN="tu_token"

# 4. Ejecutar todas las pruebas con reporte HTML
pytest

# Ejecutar solo un grupo
pytest -m smoke
pytest -m security
```

El reporte queda en `reports/reporte.html`.

### Ejecución en GitHub Actions

1. En el repositorio, ve a **Settings → Secrets and variables → Actions → New repository secret**.
2. Crea el secreto `GOREST_TOKEN` con tu token.
3. Cada push a `main` ejecuta la suite. El reporte se descarga desde la pestaña **Actions**, en la sección *Artifacts* de cada ejecución.

## Estructura del repositorio

```
qa-api-usuarios/
├── .github/workflows/api-tests.yml   # Integración continua
├── docs/
│   ├── plan-de-pruebas.md            # Alcance, riesgos y criterios
│   ├── casos-de-prueba.md            # Casos diseñados y su estado
│   └── reportes-de-bugs/             # Hallazgos documentados
├── postman/                          # Colección exportada de Postman
├── tests/
│   ├── conftest.py                   # Configuración y datos de prueba
│   ├── test_autenticacion.py
│   ├── test_crear_usuario.py
│   ├── test_gestion_usuarios.py
│   ├── test_seguridad.py
│   └── test_rendimiento.py
├── pytest.ini
└── requirements.txt
```
