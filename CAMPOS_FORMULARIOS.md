# Documentación de Campos de Formularios

## index.html - Login y Registro

### Login
- **Email**: tipo email, formato válido de correo electrónico, requerido
- **Contraseña**: tipo password, texto libre, requerido

### Registro
- **Cédula**: tipo text, máximo 10 caracteres, requerido
- **Nombre**: tipo text, máximo 100 caracteres, requerido
- **Email**: tipo email, formato válido de correo electrónico, requerido
- **Contraseña**: tipo password, texto libre, requerido

## agregar-finca.html

- **Nombre de la Finca**: tipo text, máximo 100 caracteres, requerido
- **Ubicación**: tipo text, máximo 200 caracteres, requerido
- **Tipo de Suelo**: tipo text, máximo 50 caracteres, requerido
- **Fecha de Registro**: tipo datetime-local, formato fecha y hora, opcional (se asigna automáticamente si no se especifica)

## agregar-cultivo.html

- **Tipo de Cultivo**: select, opciones: Maíz, Arroz, Frijol, Yuca, Plátano, Café, Cacao, Papa, Tomate, Lechuga, requerido
- **Área de Cultivo**: tipo number, mínimo 0.01 hectáreas, paso 0.01, requerido
- **Fecha de Siembra**: tipo date, formato YYYY-MM-DD, requerido
- **Fecha de Cosecha**: tipo date, formato YYYY-MM-DD, requerido
- **Estado del Cultivo**: select, opciones: Siembra, Crecimiento, Maduración, Cosecha, Finalizado, requerido

## agregar-maquinaria.html

- **Tipo de Maquinaria**: select, opciones: Tractor, Cosechadora, Sembradora, Pulverizadora, Arado, Rastra, Aspersor, Motoazada, Bomba de Agua, Otro, requerido
- **Marca**: tipo text, máximo 50 caracteres, requerido
- **Modelo**: tipo text, máximo 50 caracteres, requerido
- **Año de Fabricación**: tipo number, rango 1900-2030, requerido
- **Estado**: select, opciones: Excelente, Bueno, Regular, Malo, En Reparación, requerido
- **Descripción**: tipo textarea, máximo 500 caracteres, opcional
- **Fecha de Adquisición**: tipo date, formato YYYY-MM-DD, requerido

## agregar-notificacion.html

- **Tipo de Notificación**: select, opciones: Recordatorio, Alerta, Información, Urgente, Mantenimiento, Cosecha, Siembra, Riego, Fertilización, Plagas, requerido
- **Título**: tipo text, máximo 100 caracteres, requerido
- **Mensaje**: tipo textarea, máximo 500 caracteres, requerido
- **Fecha de Notificación**: tipo datetime-local, formato fecha y hora, requerido
- **Prioridad**: select, opciones: Baja, Media, Alta, Crítica, requerido

## terrenos.html - Formularios de Parcelas

### Agregar Parcela
- **Nombre de la Finca**: tipo text, debe existir en el sistema, requerido
- **ID de Parcela**: tipo text, máximo 20 caracteres, requerido
- **Superficie**: tipo number, rango 0-10000 hectáreas, paso 0.01, requerido

### Eliminar Parcela
- **Nombre de la Finca**: tipo text, debe existir en el sistema, requerido
- **ID de Parcela**: tipo text, debe existir en el sistema, requerido

### Eliminar Finca
- **Nombre de la Finca**: tipo text, debe existir en el sistema, requerido

## maquinaria.html - Formularios de Ventas y Servicios

### Crear Venta
- **ID de Maquinaria**: tipo text, debe existir en el sistema, requerido
- **Precio**: tipo number, rango 0-1000000, paso 0.01, requerido
- **Fecha de Venta**: tipo date, formato YYYY-MM-DD, opcional

### Crear Servicio/Reserva
- **ID de Maquinaria**: tipo text, debe existir en el sistema, requerido
- **Fecha de Inicio**: tipo date, formato YYYY-MM-DD, requerido
- **Fecha de Fin**: tipo date, formato YYYY-MM-DD, requerido

## Notas Importantes

### Validaciones del Frontend
- Todos los campos marcados como "requerido" deben completarse antes de enviar el formulario
- Los campos de tipo email validan el formato de correo electrónico
- Los campos numéricos tienen rangos mínimos y máximos definidos
- Los campos de texto tienen límites de caracteres específicos
- Los campos de fecha y datetime-local usan el formato estándar HTML5

### Validaciones del Backend
- El backend valida todos los campos nuevamente para seguridad
- Los campos de fecha se validan para asegurar que sean fechas válidas
- Los campos numéricos se validan para asegurar que estén dentro de los rangos permitidos
- Los campos de texto se sanitizan para prevenir inyección de código
- Se verifica que las referencias a otros registros (fincas, maquinaria) existan en la base de datos

### Formatos de Fecha
- **tipo date**: YYYY-MM-DD (ejemplo: 2024-06-22)
- **tipo datetime-local**: YYYY-MM-DDTHH:MM (ejemplo: 2024-06-22T14:30)

### Campos de Selección
- Todos los campos select tienen opciones predefinidas para mantener consistencia en los datos
- Los usuarios no pueden ingresar valores personalizados en estos campos
- Las opciones están diseñadas para cubrir los casos de uso más comunes en gestión agrícola 