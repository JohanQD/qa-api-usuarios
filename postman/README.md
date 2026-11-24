# Colección de Postman

Aquí va la colección exportada con la ejecución manual de los casos de prueba.

## Cómo armarla

1. Crea en Postman una colección llamada **API de usuarios – GoRest**.
2. Crea un *environment* con dos variables:
   - `base_url` = `https://gorest.co.in/public/v2`
   - `token` = tu token de GoRest (marcado como *secret*, y nunca lo subas al repositorio)
3. En la pestaña **Authorization** de la colección, elige *Bearer Token* con el valor `{{token}}`.
4. Crea una carpeta por grupo (Funcionales, Validación de datos, Actualización y eliminación, Seguridad) y una petición por caso, nombrada con su ID (por ejemplo, `CP-008 Email duplicado`).
5. En la pestaña **Tests** de cada petición, agrega validaciones del código de estado y del cuerpo, por ejemplo:

```javascript
pm.test("CP-008: responde 422", () => {
    pm.response.to.have.status(422);
});
pm.test("CP-008: el error es en el campo email", () => {
    const errores = pm.response.json();
    pm.expect(errores.map(e => e.field)).to.include("email");
});
```

6. Ejecuta toda la colección con el **Collection Runner** y guarda una captura del resultado para el README.
7. Exporta la colección (formato v2.1) y guárdala en esta carpeta como `api-usuarios-gorest.postman_collection.json`.

> Antes de exportar, revisa que el token no quede escrito en ninguna petición: debe vivir solo en el environment, que no se sube.
