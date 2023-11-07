erDiagram
  Cliente {
    id: int [pk]
    nombre: string
    dirección: string
    correo_electrónico: string
  }

  Producto {
    id: int [pk]
    nombre: string
    precio: float
    descripción: string
    categoría_id: int [fk]
    proveedor_id: int [fk]
  }

  Orden {
    id: int [pk]
    fecha_de_orden: date
    cliente_id: int [fk]
  }

  Categoría {
    id: int [pk]
    nombre: string
  }

  Proveedor {
    id: int [pk]
    nombre: string
    dirección: string
    correo_electrónico: string
  }

  Reseña {
    id: int [pk]
    cliente_id: int [fk]
    producto_id: int [fk]
    puntuación: int
    comentario: string
  }

  Cliente --> Orden
  Producto --> Categoría
  Producto --> Proveedor
  Cliente --> Reseña [arrowhead=open]
