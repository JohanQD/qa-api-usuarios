"""Autenticación al crear usuarios (CP-016 y CP-017)."""

import pytest
import requests

from conftest import TIMEOUT, email_unico

DATOS_VALIDOS = {"name": "QA Tester", "gender": "male", "status": "active"}


@pytest.mark.security
@pytest.mark.smoke
def test_cp016_crear_usuario_sin_token(base_url):
    """CP-016: sin token, la API rechaza la creación con 401."""
    datos = {**DATOS_VALIDOS, "email": email_unico()}

    respuesta = requests.post(f"{base_url}/users", json=datos, timeout=TIMEOUT)

    assert respuesta.status_code == 401


@pytest.mark.security
def test_cp017_crear_usuario_con_token_invalido(base_url):
    """CP-017: con un token inválido, la API rechaza la creación con 401."""
    datos = {**DATOS_VALIDOS, "email": email_unico()}
    headers = {"Authorization": "Bearer token_invalido_de_prueba"}

    respuesta = requests.post(f"{base_url}/users", json=datos, headers=headers, timeout=TIMEOUT)

    assert respuesta.status_code == 401
