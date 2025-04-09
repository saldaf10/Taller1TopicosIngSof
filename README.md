# Quicker Ticket Assistant (QTA)
## Description
QTA is a help desk management system designed for companies working with medical devices. The application's goal is to establish order in the flow of calls received by companies. Additionally, it aims to automate the way companies handle their tickets.

## Usage Instructions
To run the project, make sure you have the following installed:

* **Python**
* **Django**

Follow these steps:

### 1. Clone the project from GitHub:
```bash
git clone https://github.com/jmmunozg1/QTAProject.git
```
### 2. Navigate to the project directory:
```bash
cd QTAProject
```
### 3. Start the server:
```bash
python manage.py runserver
```
### 4. Open your browser and go to http://localhost:8000 to access the application.


## How to Contribute
If you would like to contribute to this project, follow these steps:

1. Fork the repository.
2. Create a new branch for your contribution.
3. Make the changes and be sure to follow the project's style guidelines.
4. Submit a pull request.

## Contact
For any inquiries or suggestions, please contact us at camazog1@eafit.edu.co, jdzapatam@eafit.edu.co,  jmmunozg1@eafit.edu.co or open an issue on GitHub.

# Revisión Autocritica:

## 1. Usabilidad:
### Aspectos positivos:

La página web una vez se entra en ella es muy agradable a la vista y bastante intuitiva, una vez se entra a la plataforma como usuario las funcionalidades están claras y bien diseñandas. Especialmente la parte de creación de tickets.

### Áreas de mejora:

Mala consistencia a la hora de escribir los textos, se mezcla inglés con español y casi todas las letras empiezan con mayúscula.

Diseño responsivo: El diseño de la página web no es responsive, así que solo se podría usar comodamente desde un computador.

Veo que no tiene la función para crear un usuario, entonces en caso de no tener uno se debe crear mediante la terminal lo que no lo hace compatible con usuarios finales.

Algunas imágenes no cargan en el apartado de statistics.

About y More, muestrane exactamente la misma pestaña.

## 2. Compatibilidad:
### Aspectos positivos:

Basado en tecnologías estándar: El uso de Python y Django garantiza compatibilidad con múltiples sistemas operativos.​

### Áreas de mejora:

No se proporciona un archivo requirements.txt detallando las dependencias del proyecto. Incluirlo facilitaría la instalación y configuración en diferentes entornos.​

Todo el código esta creadon desde la misma aplicación lo cual hace más complicado hacer CRUD y encontrar alguna función o template en caso de seguir creciendo la página web.

No hay una carpeta de static donde se tengan todas las imágenes y el css, están todas sueltas.

## 3. Rendimiento:
### Aspectos positivos:

La página realmente es bastante rápida en la mayoría de las ventanas.

### Áreas de mejora:

Hay una pestaña en especifico un poco demorada en cargar incluso con pocos tickets que es statistics, esto se debe a que en la vista se recorren los tickets muchas veces, no hay paginación, lazy loading o tareas en segundo plano.

No se hicieron pruebas de rendimiento. Implementarlas ayudaría a identificar y corregir cuellos de botella.​

## 4. Seguridad:
### Aspectos positivos:

Framework seguro: Django ofrece características de seguridad integradas, como protección contra inyecciones SQL y CSRF.​

### Áreas de mejora:

Gestión de credenciales: Se observa la inclusión del archivo db.sqlite3 en el repositorio, lo que puede exponer datos sensibles. Ya que el proyectoe estuvo en la web siendo usado esto puede ser muy sensible.

Al conocer las urls se pueden saltar algunos pasos como el inicio de sesión y para algunas funciones no es necesario estar ingresado pero la idea era que así fuera.


# Inversion de dependencias:


## ✅ ¿Qué se hizo?

Se refactorizó la vista `ticket(request)` para aplicar el **principio de Inversión de Dependencias (Dependency Inversion Principle - DIP)**, parte de los principios SOLID.

El objetivo fue **desacoplar la lógica de creación de tickets** del modelo Ticket, mejorando la escalabilidad, mantenibilidad y testabilidad del código.

---

##  ¿Cómo se implementó?

### 🔧 1. Creación de una interfaz de abstracción

qta/interfaces/ticket_repository_interface.py


###  2. Implementación concreta de la interfaz usando Django ORM

qta/repositories/django_ticket_repository.pY

### 3. Servicio de creación desacoplado del modelo

qta/services/ticket_creator_service.py

### 4. Refactorización de la vista ticket(request)

qta/views.py

##¿Para qué se hizo?

✅ Desacoplar la lógica de negocio del modelo concreto Ticket.

✅ Facilitar pruebas unitarias mediante mocks del repositorio.

✅ Mejorar la mantenibilidad y extensibilidad del código.

✅ Cumplir con el principio SOLID (DIP).

✅ Permitir cambiar la fuente de datos en el futuro sin reescribir lógica de negocio.

# Implementación del Patrón Singleton

## ✅ ¿Qué se hizo?

Se implementó el **patrón de diseño Singleton** en la funcionalidad de escritura de archivos CSV. Esto asegura que solo exista una única instancia de la clase encargada de manejar la escritura de archivos CSV en todo el proyecto.

---

## 🔧 ¿Cómo se implementó?

1. **Creación de la clase `CSVWriter`**:
   - Se creó una clase en `qta/utils/csv_writer.py` que implementa el patrón Singleton.
   - Esta clase centraliza la lógica de escritura de archivos CSV.

2. **Refactorización de la vista `mainscreen`**:
   - Se reemplazó la lógica de escritura de archivos CSV en la vista `mainscreen` para utilizar la clase `CSVWriter`.

---

## 🛠️ ¿Por qué se eligió el patrón Singleton?

El patrón Singleton fue elegido porque:
- **Centralización**: Permite centralizar la lógica de escritura de archivos CSV en una única clase.
- **Reutilización**: Evita la duplicación de código en diferentes vistas.
- **Control de instancias**: Garantiza que solo exista una instancia de la clase `CSVWriter`, lo que mejora el control y la consistencia en la escritura de archivos.

---

## 🚀 ¿Cómo mejora la implementación?

1. **Mantenibilidad**:
   - Si se necesita cambiar la forma en que se escriben los archivos CSV, solo es necesario modificar la clase `CSVWriter`.

2. **Reutilización**:
   - La clase `CSVWriter` puede ser utilizada en cualquier parte del proyecto sin necesidad de duplicar código.

3. **Escalabilidad**:
   - Facilita la extensión de la funcionalidad de escritura de archivos CSV en el futuro.

---

## 📂 Cambios realizados en el repositorio:

1. **Archivo creado**:
   - `qta/utils/csv_writer.py`: Contiene la implementación del patrón Singleton.

2. **Cambios en `views.py`**:
   - Se refactorizó la vista `mainscreen` para utilizar la clase `CSVWriter`.


