import json

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware


def load_products():
    with open("../data/productos.json", "r") as archivo:
        productos = json.load(archivo)
    return productos["subcategorias"]


def load_categories():
    with open("../data/productos.json", "r") as archivo:
        productos = json.load(archivo)
    return productos["categorias"]


def load_departments():
    with open("../data/productos.json", "r") as archivo:
        productos = json.load(archivo)
    return productos["departamentos"]


def load_sizes():
    with open("../data/productos_sizes.json", "r") as archivo:
        productos = json.load(archivo)
    return productos


products = load_products()
categories = load_categories()
departamentos = load_departments()
sizes = load_sizes()
app = FastAPI()

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Devolver todos los productos de la comuna
@app.get("/products/")
def get_products():
    return {"productos": products}


# Devolver las categorias de productos de la comuna (y departamentos)
@app.get("/categories/")
def get_categories():
    return {"departamentos": departamentos, "categorias": categories}


# Devolver los productos de una categoria
@app.get("/category_products/")
def get_products_from_category(category_id: int):
    resultado = []

    for producto in products:
        if producto['id_categoria'] == category_id:
            resultado.append(producto)

    return resultado


# Devolver los tamaños de un producto
@app.get("/product_sizes/")
def get_product_sizes(product_id: int):
    print(sizes)
    return {"tamanos": sizes[str(product_id)]}


# Agregar un producto a la cesta
@app.post("/add_product/")
def add_product(data: Request):
    return

# Devolver el listado de supermercados, de menor a mayor precio, dada la cesta actual, con su precio correspondiente





