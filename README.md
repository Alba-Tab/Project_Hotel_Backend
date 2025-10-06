# 🏨 Backend Hotelería Multi-Tenant

Proyecto: **Sistema de Gestión Hotelera SaaS**  
Tecnología: Django + PostgreSQL + django-tenants  
Objetivo: Sistema multi-tenant donde cada hotel tiene su propia base de datos aislada.

---

## 📋 Descripción del Proyecto

Este sistema permite gestionar múltiples hoteles de forma independiente, donde cada hotel (tenant) tiene:

- ✅ **Datos completamente aislados** (esquemas separados en PostgreSQL)
- ✅ **Sistema de usuarios propio** por hotel
- ✅ **Gestión de habitaciones, reservas y finanzas** independiente
- ✅ **API REST** completa por tenant
- ✅ **Administración** centralizada de hoteles

---

## 🏗️ Arquitectura Multi-Tenant

```
┌─────────────────────────────────────────────┐
│              ESQUEMA PUBLIC                 │
│  - customers_client (hoteles/tenants)       │
│  - customers_domain (dominios)              │
│  - Configuración global compartida          │
└─────────────────────────────────────────────┘

┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐
│  HOTEL_SOL      │  │  HOTEL_MAR      │  │  HOTEL_LUNA     │
│  - usuarios     │  │  - usuarios     │  │  - usuarios     │
│  - habitaciones │  │  - habitaciones │  │  - habitaciones │
│  - reservas     │  │  - reservas     │  │  - reservas     │
│  - finanzas     │  │  - finanzas     │  │  - finanzas     │
└─────────────────┘  └─────────────────┘  └─────────────────┘
```

---

## ⚙️ Configuración e Instalación

### 1. **Prerequisitos**

```bash
# PostgreSQL debe estar instalado y corriendo
# Python 3.11+ recomendado
```

### 2. **Clonar y configurar entorno**

```bash
git clone https://github.com/Alba-Tab/Project_Hotel_Backend.git
cd Project_Hotel_Backend

# Crear y activar entorno virtual
python -m venv .venv
.venv\Scripts\Activate.ps1  # Windows
# source .venv/bin/activate  # Linux/Mac

# Instalar dependencias
pip install -r requirements.txt
```

### 3. **Configurar Base de Datos**

```sql
-- En PostgreSQL crear la base de datos
CREATE DATABASE hotel_db;
```

### 4. **Configurar variables de entorno**

```bash
# Crear archivo .env (opcional)
DATABASE_NAME=hotel_db
DATABASE_USER=postgres
DATABASE_PASSWORD=tu_password
DATABASE_HOST=127.0.0.1
DATABASE_PORT=5432
```

---

## 🚀 Inicialización del Proyecto

### **Paso 1: Verificar configuración**

```bash
python manage.py check
```

### **Paso 2: Crear migraciones para SHARED_APPS**

```bash
python manage.py makemigrations customers
```

### **Paso 3: Migrar esquema público**

```bash
python manage.py migrate_schemas --shared
```

### **Paso 4: Crear migraciones para TENANT_APPS**

```bash
python manage.py makemigrations usuarios
python manage.py makemigrations --empty core habitaciones reservas finanzas
```

### **Paso 5: Migrar todos los esquemas**

```bash
python manage.py migrate_schemas
```

### **Paso 6: Crear tenant de prueba**

```python
python manage.py shell

from customers.models import Client, Domain

# Crear tenant
tenant = Client(
    schema_name="hotel_sol",
    name="Hotel Sol",
    paid_until="2025-12-31",
    on_trial=False
)
tenant.save()

# Crear dominio
domain = Domain(
    domain="hotelsol.localhost",
    tenant=tenant,
    is_primary=True
)
domain.save()
exit()
```

### **Paso 7: Ejecutar servidor**

```bash
python manage.py runserver
```

---

## 🔧 Comandos Útiles

### **Gestión de Migraciones**

```bash
# Ver estado de migraciones
python manage.py showmigrations

# Crear nuevas migraciones
python manage.py makemigrations

# Aplicar migraciones a todos los tenants
python manage.py migrate_schemas

# Migrar tenant específico
python manage.py migrate_schemas --schema=hotel_sol
```

### **Gestión de Tenants**

```bash
# Listar todos los tenants
python manage.py shell -c "from customers.models import Client; print([c.name for c in Client.objects.all()])"

# Verificar esquemas en BD
python manage.py shell -c "from django.db import connection; cursor = connection.cursor(); cursor.execute('SELECT schema_name FROM information_schema.schemata;'); print([row[0] for row in cursor.fetchall()])"
```

### **Crear Superusuarios**

```bash
# Crear superusuario para tenant específico
python manage.py create_tenant_superuser --schema=hotel_sol
```

---

## 📁 Estructura del Proyecto

```
├── cadena_hoteleria/          # Configuración principal
│   ├── settings.py           # Configuración Django + django-tenants
│   ├── urls.py              # URLs principales
│   ├── urls_public.py       # URLs esquema público
│   └── urls_tenant.py       # URLs para cada tenant
├── customers/               # App para gestión de tenants
│   └── models.py           # Client y Domain models
├── apps/
│   ├── usuarios/           # Sistema de usuarios por tenant
│   ├── habitaciones/       # Gestión de habitaciones
│   ├── reservas/          # Sistema de reservas
│   └── finanzas/          # Contabilidad y pagos
├── core/                  # Funcionalidades compartidas
└── requirements.txt       # Dependencias del proyecto
```

---

## 🌐 Acceso al Sistema

### **URLs de Acceso:**

- **Esquema Público**: `http://127.0.0.1:8000/`
- **Tenant Hotel Sol**: `http://hotelsol.localhost:8000/`
- **Admin Panel**: `http://127.0.0.1:8000/admin/` (público)
- **Admin Tenant**: `http://hotelsol.localhost:8000/admin/`

### **APIs Disponibles:**

- `GET /api/core/` - APIs centrales
- `GET /api/usuarios/` - Gestión de usuarios del hotel
- `GET /api/habitaciones/` - Gestión de habitaciones
- `GET /api/reservas/` - Sistema de reservas
- `GET /api/finanzas/` - Gestión financiera

---

## �️ Desarrollo

### **Agregar Nuevos Modelos**

1. Crear modelo en la app correspondiente
2. Ejecutar `python manage.py makemigrations`
3. Aplicar con `python manage.py migrate_schemas`

### **Crear Nuevo Tenant**

```python
from customers.models import Client, Domain

tenant = Client(
    schema_name="nuevo_hotel",
    name="Hotel Nuevo",
    paid_until="2025-12-31"
)
tenant.save()

Domain.objects.create(
    domain="nuevohotel.localhost",
    tenant=tenant,
    is_primary=True
)
```

### **Acceder a Datos de Tenant Específico**

```python
from django_tenants.utils import schema_context

with schema_context('hotel_sol'):
    from apps.usuarios.models import Usuario
    usuarios = Usuario.objects.all()
    print(f"Hotel Sol tiene {usuarios.count()} usuarios")
```

---

## ✅ Estado Actual

- ✅ **Configuración Multi-tenant**: Funcionando
- ✅ **Base de Datos**: PostgreSQL configurada
- ✅ **Migraciones**: Aplicadas correctamente
- ✅ **Tenant de Prueba**: Hotel Sol creado
- ✅ **Servidor**: Funcionando en puerto 8000
- ✅ **APIs**: Estructura básica lista
- ⏳ **Modelos de Negocio**: Por implementar
- ⏳ **Autenticación**: Por configurar
- ⏳ **Frontend**: Por desarrollar

---

## 📝 Notas Importantes

- **Activar entorno virtual** antes de ejecutar comandos
- **PostgreSQL debe estar corriendo** para operaciones de BD
- **Cada tenant tiene datos completamente aislados**
- **Solo el esquema público puede gestionar tenants**
- **Los dominios determinan qué tenant se activa**

---
