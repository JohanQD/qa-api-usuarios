"""Consulta, actualización y eliminación de usuarios (CP-001, CP-003, CP-004, CP-012 a CP-015)."""

import pytest
import requests

from conftest import TIMEOUT, campos_con_error, email_unico


@pytest.mark.smoke
def test_cp001_listar_usuarios(base_url):
    """CP-001: el listado de usuarios responde 200 con una lista JSON."""
    respuesta = requests.get(f"{base_url}/users", timeout=TIMEOUT)

    assert respuesta.status_code == 200
    assert isinstance(respuesta.json(), list)


@pytest.mark.smoke
def test_cp003_consultar_usuario_creado(base_url, auth_headers, usuario_creado):
    """CP-003: el usuario recién creado se puede consultar con los mismos datos."""
    respuesta = requests.get(
        f"{base_url}/users/{usuario_creado['id']}", headers=auth_headers, timeout=TIMEOUT
    )

    assert respuesta.status_code == 200
    assert respuesta.json() == usuario_creado


@pytest.mark.regression
def test_cp004_consultar_usuario_inexistente(base_url, auth_headers):
    """CP-004: un id que no existe responde 404."""
    respuesta = requests.get(f"{base_url}/users/999999999", headers=auth_headers, timeout=TIMEOUT)

    assert respuesta.status_code == 404


@pytest.mark.regression
def test_cp012_actualizar_todos_los_campos_con_put(base_url, auth_headers, usuario_creado):
    """CP-012: PUT actualiza todos los campos del usuario."""
    nuevos_datos = {
        "name": "QA Tester Actualizado",
        "email": email_unico(),
        "gender": "female",
        "status": "inactive",
    }

    respuesta = requests.put(
        f"{base_url}/users/{usuario_creado['id']}",
        json=nuevos_datos,
        headers=auth_headers,
        timeout=TIMEOUT,
    )

    assert respuesta.status_code == 200
    for campo, valor in nuevos_datos.items():
        assert respuesta.json()[campo] == valor, f"El campo {campo} no se actualizó"


@pytest.mark.regression
def test_cp013_actualizar_solo_status_con_patch(base_url, auth_headers, usuario_creado):
    """CP-013: PATCH cambia solo el campo enviado y conserva los demás."""
    respuesta = requests.patch(
        f"{base_url}/users/{usuario_creado['id']}",
        json={"status": "inactive"},
        headers=auth_headers,
        timeout=TIMEOUT,
    )

    assert respuesta.status_code == 200
    actualizado = respuesta.json()
    assert actualizado["status"] == "inactive"
    for campo in ("name", "email", "gender"):
        assert actualizado[campo] == usuario_creado[campo], f"El campo {campo} cambió sin pedirlo"


@pytest.mark.regression
def test_cp014_actualizar_con_email_invalido(base_url, auth_headers, usuario_creado):
    """CP-014: la actualización también valida el formato del email."""
    respuesta = requests.patch(
        f"{base_url}/users/{usuario_creado['id']}",
        json={"email": "correo.com"},
        headers=auth_headers,
        timeout=TIMEOUT,
    )

    assert respuesta.status_code == 422
    assert "email" in campos_con_error(respuesta)


@pytest.mark.smoke
def test_cp015_eliminar_usuario(base_url, auth_headers, usuario_creado):
    """CP-015: al eliminar un usuario responde 204 y después ya no se encuentra."""
    url_usuario = f"{base_url}/users/{usuario_creado['id']}"

    eliminacion = requests.delete(url_usuario, headers=auth_headers, timeout=TIMEOUT)
    consulta = requests.get(url_usuario, headers=auth_headers, timeout=TIMEOUT)

    assert eliminacion.status_code == 204
    assert consulta.status_code == 404
