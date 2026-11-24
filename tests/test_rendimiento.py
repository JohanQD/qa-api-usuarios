"""Prueba no funcional de tiempo de respuesta (CP-022)."""

import os

import pytest
import requests

from conftest import TIMEOUT

LIMITE_SEGUNDOS = float(os.getenv("MAX_RESPONSE_SECONDS", "2"))


@pytest.mark.performance
def test_cp022_tiempo_de_respuesta_al_listar_usuarios(base_url):
    """CP-022: el listado de usuarios responde en menos del límite definido (2 s por defecto)."""
    respuesta = requests.get(f"{base_url}/users", timeout=TIMEOUT)
    segundos = respuesta.elapsed.total_seconds()

    assert respuesta.status_code == 200
    assert segundos < LIMITE_SEGUNDOS, f"Tardó {segundos:.2f} s (límite: {LIMITE_SEGUNDOS} s)"
