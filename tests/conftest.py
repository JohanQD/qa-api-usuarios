"""Configuración compartida y datos de prueba para la suite de la API de usuarios."""

import os
import uuid

import pytest
import requests

BASE_URL = os.getenv("GOREST_BASE_URL", "https://gorest.co.in/public/v2")
TIMEOUT = 15  # segundos máximos de espera por petición


def email_unico() -> str:
    """Genera un correo distinto en cada ejecución para no chocar con datos existentes."""
    return f"qa.tester.{uuid.uuid4().hex[:10]}@pruebasqa.com"


def campos_con_error(respuesta: requests.Response) -> set:
    """Devuelve los nombres de los campos que la API reporta con error (respuestas 422)."""
    cuerpo = respuesta.json()
    if isinstance(cuerpo, list):
        return {error.get("field") for error in cuerpo}
    return set()


def eliminar_si_se_creo(respuesta: requests.Response, headers: dict) -> None:
    """Si una prueba negativa creó un usuario por error, lo elimina para no dejar basura."""
    if respuesta.status_code == 201:
        usuario_id = respuesta.json().get("id")
        requests.delete(f"{BASE_URL}/users/{usuario_id}", headers=headers, timeout=TIMEOUT)


@pytest.fixture(scope="session")
def base_url() -> str:
    return BASE_URL


@pytest.fixture(scope="session")
def token() -> str:
    valor = os.getenv("GOREST_TOKEN")
    if not valor:
        pytest.skip("Falta la variable de entorno GOREST_TOKEN")
    return valor


@pytest.fixture(scope="session")
def auth_headers(token) -> dict:
    return {
        "Authorization": f"Bearer {token}",
        "Accept": "application/json",
        "Content-Type": "application/json",
    }


@pytest.fixture
def datos_usuario() -> dict:
    """Datos válidos para crear un usuario nuevo."""
    return {
        "name": "QA Tester",
        "email": email_unico(),
        "gender": "male",
        "status": "active",
    }


@pytest.fixture
def usuario_creado(base_url, auth_headers, datos_usuario):
    """Crea un usuario antes de la prueba y lo elimina al terminar."""
    respuesta = requests.post(
        f"{base_url}/users", json=datos_usuario, headers=auth_headers, timeout=TIMEOUT
    )
    assert respuesta.status_code == 201, (
        f"No se pudo crear el usuario de prueba: {respuesta.status_code} {respuesta.text}"
    )
    usuario = respuesta.json()

    yield usuario

    # Limpieza: si la prueba ya lo eliminó, la API responde 404 y no pasa nada.
    requests.delete(f"{base_url}/users/{usuario['id']}", headers=auth_headers, timeout=TIMEOUT)
