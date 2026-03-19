# Mock project board

Básicamente es un sistema de gestión académica donde se puede ver todo el ciclo de vida del software: desde los requisitos hasta el despliegue. Está hecho con Python en el backend y HTML/CSS/JS en el frontend de manera individual.

---

## ¿Qué hace el sistema?

Gestiona estudiantes, cursos y matrículas de una institución educativa. Tiene autenticación con roles, generación de reportes y notificaciones por correo. Todo el flujo del proyecto (sprints, tareas, bugs, pruebas) se puede ver desde la misma app.

---

## Requisitos Funcionales

Estos son los que sí o sí tiene que hacer el sistema:

1. **Autenticación con roles** — los usuarios pueden iniciar sesión como estudiante, docente o administrador, cada uno con permisos distintos.
2. **CRUD de estudiantes** — los administradores pueden crear, ver, editar y eliminar registros de estudiantes.
3. **Reportes de notas** — el sistema genera reportes en PDF y Excel por curso y semestre.
4. **Matrícula en cursos** — los estudiantes pueden inscribirse en cursos siempre que haya cupos y cumplan los prerrequisitos.
5. **Notificaciones por correo** — se mandan correos automáticos cuando hay cambios en notas o inscripciones.

---

## Requisitos No Funcionales

Estos son los que definen *cómo* debe funcionar, no *qué* hace:

1. **Rendimiento** — cualquier endpoint tiene que responder en menos de 2 segundos bajo carga normal.
2. **Disponibilidad** — el sistema debe estar disponible el 99.9% del tiempo al mes.
3. **Seguridad** — todas las comunicaciones van por HTTPS con certificado TLS válido.
4. **Accesibilidad** — la interfaz cumple el estándar WCAG 2.1 nivel AA para que sea usable por todos.

---

## Stack Tecnológico

### Backend
- **Python 3.11** — el lenguaje base del proyecto
- **FastAPI** — framework para construir la API REST, muy rápido y moderno
- **Pydantic** — para validar los datos que entran y salen
- **Uvicorn** — el servidor que corre la app

### Frontend
- **Jinja2** — motor de plantillas para renderizar el HTML desde el servidor
- **HTML5 + CSS3 + JavaScript** — lo clásico
- **Tailwind CSS** — para los estilos sin escribir tanto CSS a mano

### DevOps / Herramientas
- **Git + GitHub** — control de versiones y repositorio
- **Pytest + Postman** — para las pruebas unitarias e integración
- **Figma** — diseño de prototipos
- **Render** — despliegue en la nube (gratis)
- **Scrum** — metodología ágil con 4 sprints

---

## Equipo Mock (equipo falso)

| Nombre           | Rol            | Herramientas     |
|------------------|----------------|------------------|
| Laura Gómez      | Product Owner  | Jira / Notion    |
| Carlos Herrera   | Analista       | Figma / Draw.io  |
| Valentina Ríos   | Programador    | Python / FastAPI |
| Andrés Mora      | Tester QA      | Pytest / Postman |
| Sofía Castro     | Usuario Final  | Chrome / Figma   |

---

## Cómo correrlo local

```bash
# Activar el entorno virtual
source venv/bin/activate

# Correr el servidor
uvicorn main:app --reload
```

La app queda en `http://localhost:8000`.

---

## Páginas de la app

| Ruta            | Qué muestra                              |
|-----------------|------------------------------------------|
| `/`             | Inicio, métricas, equipo, stack          |
| `/backlog`      | Requisitos funcionales y no funcionales  |
| `/design`       | Arquitectura, modelo de datos, sprints   |
| `/development`  | Código, Git, pipeline CI/CD              |
| `/testing`      | Pruebas, cobertura, bugs                 |
| `/deployment`   | Estado del despliegue y conclusiones     |

---

## Métricas del proyecto

- 2,847 líneas de código
- 63 commits
- 12 endpoints en la API
- 96% de cobertura de pruebas
- 4 sprints completados
- 3 bugs encontrados y resueltos
