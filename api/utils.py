import json
import requests


def request_min_list(nfo):
    URL = "https://api.observatorio.sernac.cl/api/v1/carro/calculo/minimo"
    req = {
        "id_comuna": 336,
        "productos": nfo
    }
    respuesta = json.loads(requests.post(URL, json = req).content)

    print(respuesta)
    resultado = []
    for supermercado in respuesta:
        resultado.append({
            "nombre": supermercado["proveedor_nombre"],
            "direccion": supermercado["direccion"],
            "precio": supermercado["precio"],
            "precio_f": supermercado["precio_format"]
        })
    return resultado


if __name__ == "__main__":
    print(request_min_list(
        [
            {
                "id_subcategoria": 321,
                "id_rango": 164
            },
            {
                "id_subcategoria": 606,
                "id_rango": 388
            },
            {
                "id_subcategoria": 716,
                "id_rango": 153
            },
            {
                "id_subcategoria": 735,
                "id_rango": 200
            },
            {
                "id_subcategoria": 323,
                "id_rango": 168
            }
        ]
    ))