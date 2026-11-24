"""Creación de usuarios y validación de datos (CP-002, CP-005 a CP-011)."""

import pytest
import requests

from conftest import TIMEOUT, campos_con_error, eliminar_si_se_creo


@pytest.mark.smoke
def test_cp002_crear_usuario_con_datos_validos(usuario_creado, datos_usuario):
    """CP-002: con datos válidos, la API crea el usuario y devuelve lo enviado."""
    assert isinstance(usuario_creado["id"], int)
    for campo, valor in datos_usuario.items():
        assert usuario_creado[campo] == valor, f"El campo {campo} no coincide"


@pytest.mark.regression
@pytest.mark.parametrize(
    "campo_faltante",
    [
        pytest.param("name", id="CP-005 sin name"),
        pytest.param("email", id="CP-006 sin email"),
    ],
)
def test_crear_usuario_sin_campo_obligatorio(base_url, auth_headers, datos_usuario, campo_faltante):
    """CP-005 y CP-006: si falta un campo obligatorio, responde 422 con el error en ese campo."""
    datos_usuario.pop(campo_faltante)

    respuesta = requests.post(
        f"{base_url}/users", json=datos_usuario, headers=auth_headers, timeout=TIMEOUT
    )
    eliminar_si_se_creo(respuesta, auth_headers)

    assert respuesta.status_code == 422
    assert campo_faltante in campos_con_error(respuesta)


@pytest.mark.regression
@pytest.mark.parametrize(
    "campo, valor_invalido",
    [
        pytest.param("email", "correo.com", id="CP-007 email sin formato"),
        pytest.param("gender", "otro", id="CP-009 gender fuera del catalogo"),
        pytest.param("status", "pendiente", id="CP-010 status fuera del catalogo"),
    ],
)
def test_crear_usuario_con_valor_invalido(base_url, auth_headers, datos_usuario, campo, valor_invalido):
    """CP-007, CP-009 y CP-010: un valor inválido se rechaza con 422 en el campo correspondiente."""
    datos_usuario[campo] = valor_invalido

    respuesta = requests.post(
        f"{base_url}/users", json=datos_usuario, headers=auth_headers, timeout=TIMEOUT
    )
    eliminar_si_se_creo(respuesta, auth_headers)

    assert respuesta.status_code == 422
    assert campo in campos_con_error(respuesta)


@pytest.mark.regression
def test_cp008_crear_usuario_con_email_duplicado(base_url, auth_headers, usuario_creado):
    """CP-008: no se puede registrar dos veces el mismo email."""
    duplicado = {
        "name": "Usuario Duplicado",
        "email": usuario_creado["email"],
        "gender": "female",
        "status": "active",
    }

    respuesta = requests.post(
        f"{base_url}/users", json=duplicado, headers=auth_headers, timeout=TIMEOUT
    )
    eliminar_si_se_creo(respuesta, auth_headers)

    assert respuesta.status_code == 422
    assert "email" in campos_con_error(respuesta)


@pytest.mark.regression
def test_cp011_crear_usuario_con_cuerpo_vacio(base_url, auth_headers):
    """CP-011: un cuerpo vacío devuelve errores en los cuatro campos obligatorios."""
    respuesta = requests.post(f"{base_url}/users", json={}, headers=auth_headers, timeout=TIMEOUT)
    eliminar_si_se_creo(respuesta, auth_headers)

    assert respuesta.status_code == 422
    assert {"name", "email", "gender", "status"} <= campos_con_error(respuesta)
