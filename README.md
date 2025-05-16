### Odoo-Test

# Instalación y Configuración de Odoo 18 con Docker Compose para el Módulo Retail Promotions

Este documento describe los pasos necesarios para instalar Odoo 18 utilizando Docker Compose y configurar el módulo "Retail Promotions".

### Requisitos

* **Docker:** Asegúrate de tener Docker Engine instalado en tu sistema. Puedes encontrar las instrucciones de instalación en la [documentación oficial de Docker](https://docs.docker.com/engine/install/).
* **Docker Compose:** Docker Compose también es necesario. Generalmente se instala junto con Docker Desktop, o puedes seguir las instrucciones en la [documentación oficial de Docker Compose](https://docs.docker.com/compose/install/).

### Pasos

1.  **Clonar el Repositorio:**
    Clona el repositorio que contiene la estructura de carpetas y el archivo `docker-compose.yaml`. **Importante:** No modifiques la estructura de carpetas ni los archivos dentro del repositorio, ya que están configurados para funcionar correctamente.

    ```bash
    git clone <URL_DEL_REPOSITORIO>
    cd <NOMBRE_DEL_REPOSITORIO>
    ```

    Depues de clonar el repositorio, crear una carpeta vacia en la raiz del proyecto llamada "postgresql"

3.  **Ejecución con Docker Compose:**
    Desde la raíz del proyecto, donde se encuentra el archivo `docker-compose.yaml`, ejecuta el siguiente comando:

    ```bash
    docker-compose up -d
    ```

    * La primera vez que ejecutes este comando, Docker Compose descargará las imágenes necesarias de Odoo y PostgreSQL. Este proceso puede llevar varios minutos dependiendo de tu conexión a internet.
    * En ejecuciones posteriores, Docker Compose solo iniciará los contenedores existentes, lo que debería tomar solo unos segundos.

4.  **Acceder a Odoo:**
    Una vez que los contenedores estén en funcionamiento, abre tu navegador web e ingresa a la siguiente dirección:

    ```
    http://localhost:8069
    ```

    * Si es la primera vez que accedes a Odoo, se mostrará un formulario para crear una nueva base de datos.
    * La **contraseña maestra** (master password) está configurada en el archivo `odoo.conf` y es `admin123`.
    * **Selecciona la casilla "Demo data"** para incluir datos de ejemplo que facilitarán la exploración del sistema y el módulo de promociones.

5.  **Configuración de Odoo:**

    * **Activar el Modo de Desarrollador:**
        1.  Ve a la sección **Ajustes**.
        2.  Desplázate hasta el final de la página, donde encontrarás la sección **Herramientas de desarrollador**.
        3.  Selecciona la opción **Activar modo de desarrollador (con activos de prueba)**. Esto te permitirá acceder a funcionalidades avanzadas y personalizar Odoo.

    * **Actualizar la Lista de Aplicaciones:**
        1.  Dirígete a la sección **Aplicaciones**.
        2.  Haz clic en el botón **Actualizar lista de aplicaciones**. Esto asegurará que Odoo reconozca los nuevos módulos en el sistema.

    * **Instalar el Módulo Retail Promotions:**
        1.  En el buscador de aplicaciones, ingresa **Retail Promotions**.
        2.  Localiza el widget del módulo "Retail Promotions".
        3.  Haz clic en el menú de los **tres puntos** (ubicado en el widget del módulo).
        4.  Selecciona la opción **Instalar**. Esto instalará el módulo de promociones en tu instancia de Odoo.

    * **Habilitar Descuentos en Ventas:**
        1.  Dirígete a la sección **Ajustes**.
        2.  Selecciona la pestaña **Ventas**.
        3.  Dentro de la sub-sección **Precios**, asegúrate de que la casilla **Descuentos** esté habilitada. Esto permitirá que los descuentos aplicados a través del módulo de promociones se muestren en las órdenes de venta.

6.  **Creación y Aplicación de Promociones:**

    * **Acceder a la Gestión de Promociones:**
        1.  Dirígete al módulo de **Ventas**.
        2.  En el menú superior, navega a **Órdenes** y luego selecciona **Promociones**. Esta sección te permitirá visualizar y crear nuevas promociones.

    * **Crear una Nueva Promoción:**
        1.  Haz clic en el botón **Crear** para abrir el formulario de nueva promoción.
        2.  **Completa los Datos Requeridos:**
            * **Nombre de la Promoción:** Introduce un nombre descriptivo para identificar fácilmente la promoción (ej: "Descuento de Verano", 
            * **Valor del Descuento:** Ingresa el valor del descuento.
            * **Fecha de Inicio:** Define la fecha en la que la promoción comenzará a ser válida.
            * **Fecha de Fin:** Establece la fecha en la que la promoción dejará de aplicarse.

        3.  **Seleccionar Productos a los que se Aplica el Descuento:**
            * En la sección designada (generalmente una pestaña o un campo llamado "Productos" o similar), selecciona los productos específicos a los que se aplicará esta promoción. Puedes buscar y añadir múltiples productos a la lista.

        4.  Haz clic en el botón **Guardar** para crear la promoción.

    * **Aplicación Automática del Descuento en Órdenes de Venta:**
        1.  Dirígete a la sección de **Órdenes de Venta**.
        2.  Selecciona una orden de venta existente o crea una nueva.
        3.  **Agregar una Nueva Línea de Producto:** Añade una nueva línea a la orden de venta seleccionando un producto.
        4.  **Detección Automática del Descuento:** Si el producto añadido a la línea de la orden de venta coincide con uno de los productos configurados en una promoción activa (dentro del rango de fechas de inicio y fin), el descuento se aplicará automáticamente al precio de ese producto en la línea de la orden. Podrás observar el descuento reflejado en el cálculo del importe de la línea y en el total de la orden.

    * **Consideraciones Importantes sobre las Líneas de Órdenes:**
        Es fundamental tener en cuenta que las líneas de las órdenes de venta se almacenan en la base de datos en el momento de su creación. Por lo tanto, **Odoo no modificará automáticamente las líneas de órdenes de venta existentes** si se crea o modifica una promoción después de que esas líneas fueron guardadas. El descuento solo se aplicará automáticamente a las **nuevas líneas de producto** que se agreguen a las órdenes de venta después de que la promoción esté activa y dentro de su período de validez.


## Parte 1: Respuestas a Preguntas Teóricas (30%)

**1. Conceptos Básicos de Odoo**

* **¿Cuáles son los componentes principales de un módulo en Odoo?**
    * **Modelos (models/):** Clases Python que definen la estructura de datos.
    * **Vistas (views/):** XML que define interfaces de usuario (formularios, listas, kanban).
    * **Datos de seguridad (security/):** Archivos CSV/XML para permisos y grupos.
    * **Manifiesto (__manifest__.py):** Metadata del módulo (nombre, versión, dependencias).
    * **Datos demo (demo/):** Datos de prueba.
    * **Controladores (controllers/):** Lógica para endpoints web.
    * **Informes (reports/):** Plantillas QWeb para PDF/Excel.
    * **Assets (static/):** CSS/JS/imágenes.

* **Explica la diferencia entre `fields.Char` y `fields.Text`.**
    * **`fields.Char`:** Cadena corta (ej: nombre) con longitud máxima especificada (`size`).
    * **`fields.Text`:** Texto largo multilínea (ej: descripción).

* **¿Para qué sirve el archivo `__manifest__.py`?**
    El archivo `__manifest__.py` es como la tarjeta de presentación de un módulo en Odoo. Define información esencial sobre el módulo, como su nombre, versión, autor, sitio web y una breve descripción. Lo más importante es que especifica las dependencias de otros módulos, los archivos de datos XML a cargar (vistas, datos iniciales, reportes, seguridad), los archivos Python que contienen el código del modelo y la lógica, e indica si el módulo es instalable y si es una aplicación en sí mismo.

**2. Conocimientos Retail**

* **¿Cómo manejarías el control de inventario en Odoo para una tienda retail?**
    Para una tienda retail, el control de inventario en Odoo se manejaría utilizando el módulo de Inventario. Se configurarían las diferentes ubicaciones de la tienda (estanterías, almacén, etc.) y se definirían reglas de stock para asegurar que siempre haya suficiente mercancía disponible y evitar el sobrestock. Se utilizarían las funcionalidades de gestión de entradas (compras a proveedores) y salidas (ventas a clientes), así como los métodos de valoración de inventario (FIFO, LIFO, etc.). También se configurarían alertas para notificar cuando los niveles de stock de ciertos productos estén bajos, permitiendo realizar pedidos a tiempo.

* **¿Qué módulos de Odoo consideras esenciales para una tienda retail?**
    Considero esenciales los siguientes módulos:
    * **Ventas (Sales):** Para gestionar las órdenes de venta a clientes.
    * **Punto de Venta (Point of Sale):** Específico para las operaciones de venta directa en la tienda física.
    * **Inventario (Inventory):** Para el control y la gestión de las existencias.
    * **Compras (Purchase):** Para gestionar los pedidos a los proveedores.
    * **Contabilidad (Accounting):** Para llevar el registro financiero de la tienda.
    * **Contactos (Contacts):** Para gestionar la información de clientes y proveedores.
    * **Marketing (Email Marketing, SMS Marketing):** Para la comunicación y promoción con los clientes.

**3. Seguridad y Accesos**

* **¿Cómo defines grupos de usuarios y permisos en Odoo?**
    En Odoo, los permisos y accesos se definen principalmente a través de grupos de usuarios. Primero, se crean grupos específicos (por ejemplo, "Vendedores", "Administradores de Inventario"). Luego, se asignan usuarios a estos grupos. Los permisos se configuran a nivel de modelo de datos, indicando qué operaciones (crear, leer, actualizar, eliminar) pueden realizar los usuarios pertenecientes a cada grupo en esos modelos. Esto se gestiona a través de los derechos de acceso.

* **¿Cuál es la diferencia entre una regla de registro (record rule) y una lista de control de acceso (ACL)?**
    Las Listas de Control de Acceso (ACL) definen los permisos de acceso a los modelos de datos en general. Por ejemplo, una ACL puede especificar que solo los usuarios del grupo "Administradores de Ventas" pueden crear nuevas órdenes de venta. En cambio, las reglas de registro (record rules) son más específicas y definen qué *registros individuales* de un modelo pueden ver o modificar los usuarios de un grupo, basándose en ciertas condiciones. Por ejemplo, una regla de registro podría permitir que un vendedor solo vea las órdenes de venta que ha creado él mismo o las de sus clientes asignados. Las ACL controlan el acceso a nivel del modelo, mientras que las reglas de registro controlan el acceso a nivel de los datos dentro de ese modelo.
