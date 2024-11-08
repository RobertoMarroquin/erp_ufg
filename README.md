# erp_ufg

# Base de Datos
# Esquema de Base de Datos por Módulos
## Módulo: Inventario

### Tabla: Productos
| Campo         | Tipo         | Descripción                                      |
|---------------|--------------|--------------------------------------------------|
| product_id    | PK           | Identificador único del producto                |
| nombre        | VARCHAR      | Nombre del producto                              |
| descripción   | TEXT         | Descripción detallada del producto              |
| precio        | DECIMAL      | Precio de venta                                 |
| stock         | INT          | Cantidad disponible en inventario               |
| categoria_id  | FK           | Relación con la tabla Categorías                |

---

### Tabla: Categorías
| Campo         | Tipo         | Descripción                                      |
|---------------|--------------|--------------------------------------------------|
| categoria_id  | PK           | Identificador único de la categoría             |
| nombre        | VARCHAR      | Nombre de la categoría                          |

---

### Tabla: Proveedores
| Campo         | Tipo         | Descripción                                      |
|---------------|--------------|--------------------------------------------------|
| proveedor_id  | PK           | Identificador único del proveedor               |
| nombre        | VARCHAR      | Nombre del proveedor                            |
| contacto      | VARCHAR      | Información de contacto del proveedor           |

---

### Tabla: Compras
| Campo         | Tipo         | Descripción                                      |
|---------------|--------------|--------------------------------------------------|
| compra_id     | PK           | Identificador único de la compra                |
| fecha         | DATE         | Fecha de la compra                              |
| total         | DECIMAL      | Total de la compra                              |
| proveedor_id  | FK           | Relación con la tabla Proveedores               |

---

### Tabla: Detalles_Compra
| Campo            | Tipo         | Descripción                                   |
|------------------|--------------|-----------------------------------------------|
| detalle_compra_id| PK           | Identificador único del detalle de compra    |
| compra_id        | FK           | Relación con la tabla Compras                |
| product_id       | FK           | Relación con la tabla Productos              |
| cantidad         | INT          | Cantidad comprada                            |
| precio_compra    | DECIMAL      | Precio por unidad del producto               |

---

### Tabla: Movimientos de Inventario
| Campo              | Tipo         | Descripción                                  |
|--------------------|--------------|----------------------------------------------|
| movimiento_id      | PK           | Identificador único del movimiento          |
| product_id         | FK           | Relación con la tabla Productos             |
| tipo_movimiento    | ENUM         | Tipo de movimiento (entrada o salida)       |
| cantidad           | INT          | Cantidad del movimiento                     |
| fecha              | DATE         | Fecha del movimiento                        |
| referencia_id      | FK           | Relación con Compras, Ventas o Ajustes      |
| descripcion        | TEXT         | Descripción o detalle del movimiento        |

---

## Módulo: Ventas

### Tabla: Clientes
| Campo         | Tipo         | Descripción                                      |
|---------------|--------------|--------------------------------------------------|
| cliente_id    | PK           | Identificador único del cliente                 |
| nombre        | VARCHAR      | Nombre del cliente                              |
| email         | VARCHAR      | Correo electrónico del cliente                 |
| teléfono      | VARCHAR      | Número de teléfono del cliente                 |

---

### Tabla: Facturas
| Campo         | Tipo         | Descripción                                      |
|---------------|--------------|--------------------------------------------------|
| factura_id    | PK           | Identificador único de la factura               |
| fecha         | DATE         | Fecha de emisión                                |
| total         | DECIMAL      | Total de la factura                             |
| cliente_id    | FK           | Relación con la tabla Clientes                  |
| vendedor_id   | FK           | Relación con la tabla Vendedores                |

---

### Tabla: Detalles_Factura
| Campo             | Tipo         | Descripción                                  |
|-------------------|--------------|----------------------------------------------|
| detalle_factura_id| PK           | Identificador único del detalle de factura  |
| factura_id        | FK           | Relación con la tabla Facturas              |
| product_id        | FK           | Relación con la tabla Productos             |
| cantidad          | INT          | Cantidad vendida                            |
| precio_venta      | DECIMAL      | Precio de venta por unidad                  |

---

## Módulo: Personal

### Tabla: Vendedores
| Campo         | Tipo         | Descripción                                      |
|---------------|--------------|--------------------------------------------------|
| vendedor_id   | PK           | Identificador único del vendedor                |
| user_id       | FK           | Relación con la tabla Usuarios de Django        |
| numero_caja   | INT          | Número de la caja asignada                      |

---

### Tabla: Registros_Horarios
| Campo         | Tipo         | Descripción                                      |
|---------------|--------------|--------------------------------------------------|
| registro_id   | PK           | Identificador único del registro de horario     |
| vendedor_id   | FK           | Relación con la tabla Vendedores                |
| fecha         | DATE         | Fecha del registro                              |
| hora_entrada  | TIME         | Hora de entrada                                 |
| hora_salida   | TIME         | Hora de salida                                  |

---

### Tabla: Permisos_Laborales
| Campo         | Tipo         | Descripción                                      |
|---------------|--------------|--------------------------------------------------|
| permiso_id    | PK           | Identificador único del permiso                 |
| vendedor_id   | FK           | Relación con la tabla Vendedores                |
| fecha_permiso | DATE         | Fecha del permiso                               |
| motivo        | TEXT         | Motivo del permiso                              |
| duración_horas| INT          | Duración del permiso en horas                   |

---

## Módulo: Contabilidad

### Tabla: Movimientos
| Campo         | Tipo         | Descripción                                      |
|---------------|--------------|--------------------------------------------------|
| movimiento_id | PK           | Identificador único del movimiento              |
| tipo          | ENUM         | Tipo de movimiento (ingreso o egreso)           |
| fecha         | DATE         | Fecha del movimiento                            |
| monto         | DECIMAL      | Monto del movimiento                            |
| descripción   | TEXT         | Detalle del movimiento                          |
| factura_id    | FK (nullable)| Relación con la tabla Facturas (si aplica)      |
| compra_id     | FK (nullable)| Relación con la tabla Compras (si aplica)       |

---

Este esquema permite una organización modular de las tablas, facilitando su comprensión y administración. Si necesitas algún ajuste o detalle adicional, házmelo saber.
