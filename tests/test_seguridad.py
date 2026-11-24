"""Pruebas básicas de seguridad (CP-018 a CP-021)."""

import pytest
import requests

from conftest import TIMEOUT, email_unico, eliminar_si_se_creo

CAMPOS_ESPERADOS = {"id", "name", "email", "gender", "status"}


def es_exitosa(respuesta: requests.Response) -> bool:
    return 200 <= respuesta.status_code < 300


@pytest.mark.security
def test_cp018_actualizar_usuario_sin_token(base_url, auth_headers, usuario_creado):
    """CP-018: sin token no se puede modificar un usuario, y sus datos no cambian."""
    url_usuario = f"{base_url}/users/{usuario_creado['id']}"

    intento = requests.patch(url_usuario, json={"name": "Modificado sin permiso"}, timeout=TIMEOUT)
    verificacion = requests.get(url_usuario, headers=auth_headers, timeout=TIMEOUT)

    assert not es_exitosa(intento), f"La API permitió el cambio sin token: {intento.status_code}"
    assert verificacion.json()["name"] == usuario_creado["name"]


@pytest.mark.security
def test_cp019_eliminar_usuario_sin_token(base_url, auth_headers, usuario_creado):
    """CP-019: sin token no se puede eliminar un usuario, y sigue existiendo."""
    url_usuario = f"{base_url}/users/{usuario_creado['id']}"

    intento = requests.delete(url_usuario, timeout=TIMEOUT)
    verificacion = requests.get(url_usuario, headers=auth_headers, timeout=TIMEOUT)

    assert not es_exitosa(intento), f"La API permitió eliminar sin token: {intento.status_code}"
    assert verificacion.status_code == 200


@pytest.mark.security
def test_cp020_respuesta_solo_expone_campos_esperados(usuario_creado):
    """CP-020: la respuesta no incluye campos adicionales (por ejemplo, tokens o datos internos)."""
    assert set(usuario_creado.keys()) == CAMPOS_ESPERADOS


@pytest.mark.security
@pytest.mark.parametrize(
    "texto_malicioso",
    [
        pytest.param("<script>alert('qa')</script>", id="CP-021 script"),
        pytest.param("' OR '1'='1", id="CP-021 inyeccion SQL"),
    ],
)
def test_cp021_entrada_maliciosa_en_name(base_url, auth_headers, texto_malicioso):
    """CP-021: un texto malicioso no provoca errores del servidor y, si se acepta, se guarda tal cual."""
    datos = {"name": texto_malicioso, "email": email_unico(), "gender": "male", "status": "active"}

    respuesta = requests.post(f"{base_url}/users", json=datos, headers=auth_headers, timeout=TIMEOUT)
    eliminar_si_se_creo(respuesta, auth_headers)

    assert respuesta.status_code < 500, "La entrada maliciosa provocó un error del servidor"
    if respuesta.status_code == 201:
        assert respuesta.json()["name"] == texto_malicioso
