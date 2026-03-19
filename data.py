from models import TeamMember, Requirement, Entity, Sprint, TestResult, Bug, Metric, Task, Activity

team = [
    TeamMember(name="Laura Gómez",    role="Product Owner",  technology="Jira / Notion",    email="lgomez@sistemagestor.dev"),
    TeamMember(name="Carlos Herrera", role="Analista",        technology="Figma / Draw.io",  email="cherrera@sistemagestor.dev"),
    TeamMember(name="Valentina Ríos", role="Programador",     technology="Python / FastAPI", email="vrios@sistemagestor.dev"),
    TeamMember(name="Andrés Mora",    role="Tester QA",       technology="Pytest / Postman", email="amora@sistemagestor.dev"),
    TeamMember(name="Sofía Castro",   role="Usuario Final",   technology="Chrome / Figma",   email="scastro@sistemagestor.dev"),
]

requirements = [
    Requirement(id=1,  description="El sistema debe permitir autenticación con roles diferenciados (estudiante, docente, administrador)", type="functional",     priority="alta",  validated=True),
    Requirement(id=2,  description="Los administradores pueden crear, editar, consultar y eliminar registros de estudiantes",            type="functional",     priority="alta",  validated=True),
    Requirement(id=3,  description="El sistema debe generar reportes de notas en formato PDF y Excel por curso y semestre",              type="functional",     priority="media", validated=True),
    Requirement(id=4,  description="Los estudiantes pueden matricularse en cursos verificando cupos disponibles y prerrequisitos",       type="functional",     priority="alta",  validated=True),
    Requirement(id=5,  description="El sistema debe enviar notificaciones por correo ante cambios de notas o inscripción de cursos",     type="functional",     priority="media", validated=True),
    Requirement(id=6,  description="El tiempo de respuesta de cualquier endpoint no debe superar los 2 segundos bajo carga normal",      type="non-functional", priority="alta",  validated=True),
    Requirement(id=7,  description="El sistema debe mantener una disponibilidad del 99.9% medida mensualmente",                         type="non-functional", priority="alta",  validated=True),
    Requirement(id=8,  description="Todas las comunicaciones deben realizarse sobre HTTPS con certificado TLS válido",                   type="non-functional", priority="alta",  validated=True),
    Requirement(id=9,  description="La interfaz debe cumplir el estándar de accesibilidad WCAG 2.1 nivel AA",                           type="non-functional", priority="media", validated=True),
]

entities = [
    Entity(name="Estudiante", fields=["id: UUID", "nombre: str", "email: str", "programa: str", "semestre: int"]),
    Entity(name="Curso",      fields=["id: UUID", "nombre: str", "creditos: int", "profesor: str", "cupos: int"]),
    Entity(name="Matricula",  fields=["id: UUID", "estudiante_id: UUID", "curso_id: UUID", "fecha: date", "nota: float"]),
]

sprints = [
    Sprint(number=1, name="Requisitos y planeación", status="completado", start_date="2025-01-13", end_date="2025-01-24"),
    Sprint(number=2, name="Diseño y arquitectura",   status="completado", start_date="2025-01-27", end_date="2025-02-07"),
    Sprint(number=3, name="Desarrollo core",         status="completado", start_date="2025-02-10", end_date="2025-02-28"),
    Sprint(number=4, name="Pruebas y despliegue",    status="completado", start_date="2025-03-03", end_date="2025-03-14"),
]

tests = [
    TestResult(type="Pruebas Unitarias",      total=24, passed=24, description="Validación de modelos Pydantic y lógica de negocio"),
    TestResult(type="Pruebas de Integración", total=10, passed=10, description="Endpoints FastAPI con datos reales"),
    TestResult(type="Pruebas de Aceptación",  total=5,  passed=5,  description="Flujos completos validados con usuario final"),
]

bugs = [
    Bug(id=1, description="Token JWT expiraba antes de lo esperado",        severity="alta",  status="resuelto", resolved_by="Valentina Ríos"),
    Bug(id=2, description="Formulario de matrícula no validaba cupos",      severity="media", status="resuelto", resolved_by="Andrés Mora"),
    Bug(id=3, description="Tabla de notas no renderizaba en Safari mobile", severity="baja",  status="resuelto", resolved_by="Valentina Ríos"),
]

metrics = [
    Metric(label="Líneas de código", value="2,847",  icon="💻"),
    Metric(label="Commits",          value="63",     icon="📦"),
    Metric(label="Endpoints API",    value="12",     icon="🔌"),
    Metric(label="Cobertura",        value="96%",    icon="🧪"),
    Metric(label="Sprints",          value="4 / 4",  icon="✅"),
    Metric(label="Bugs resueltos",   value="3 / 3",  icon="🐛"),
]

tools = [
    "Python 3.11", "FastAPI", "Pydantic", "Uvicorn", "Jinja2",
    "HTML5", "CSS3", "JavaScript", "Tailwind CSS", "Git", "GitHub",
    "Figma", "Postman", "Pytest", "Railway", "Scrum",
]

# ── Kanban tasks ──────────────────────────────────────────────────────────────

tasks = [
    # Sprint 1
    Task(id="SGP-01", title="Reunión inicial con cliente y stakeholders",      type="chore",   status="done", priority="alta",  assignee="Laura Gómez",    assignee_initials="LG", points=2, sprint=1),
    Task(id="SGP-02", title="Levantamiento de requisitos funcionales",          type="chore",   status="done", priority="alta",  assignee="Laura Gómez",    assignee_initials="LG", points=3, sprint=1),
    Task(id="SGP-03", title="Definición del stack tecnológico",                 type="chore",   status="done", priority="media", assignee="Carlos Herrera", assignee_initials="CH", points=1, sprint=1),
    Task(id="SGP-04", title="Configurar repositorio GitHub y ramas",            type="chore",   status="done", priority="media", assignee="Valentina Ríos", assignee_initials="VR", points=1, sprint=1),
    # Sprint 2
    Task(id="SGP-05", title="Diseñar modelo de datos entidad-relación",         type="design",  status="done", priority="alta",  assignee="Carlos Herrera", assignee_initials="CH", points=3, sprint=2),
    Task(id="SGP-06", title="Crear diagrama de arquitectura del sistema",        type="design",  status="done", priority="alta",  assignee="Carlos Herrera", assignee_initials="CH", points=2, sprint=2),
    Task(id="SGP-07", title="Prototipar pantallas principales en Figma",         type="design",  status="done", priority="media", assignee="Sofía Castro",   assignee_initials="SC", points=3, sprint=2),
    Task(id="SGP-08", title="Definir contratos de API (OpenAPI / Swagger)",      type="chore",   status="done", priority="media", assignee="Valentina Ríos", assignee_initials="VR", points=2, sprint=2),
    # Sprint 3
    Task(id="SGP-09", title="Implementar autenticación JWT con roles",           type="feature", status="done", priority="alta",  assignee="Valentina Ríos", assignee_initials="VR", points=5, sprint=3),
    Task(id="SGP-10", title="CRUD completo de estudiantes",                      type="feature", status="done", priority="alta",  assignee="Valentina Ríos", assignee_initials="VR", points=4, sprint=3),
    Task(id="SGP-11", title="CRUD completo de cursos",                           type="feature", status="done", priority="alta",  assignee="Valentina Ríos", assignee_initials="VR", points=3, sprint=3),
    Task(id="SGP-12", title="Sistema de matrícula con validación de cupos",      type="feature", status="done", priority="alta",  assignee="Valentina Ríos", assignee_initials="VR", points=5, sprint=3),
    Task(id="SGP-13", title="Generación de reportes de notas en PDF",            type="feature", status="done", priority="media", assignee="Valentina Ríos", assignee_initials="VR", points=3, sprint=3),
    Task(id="SGP-14", title="Notificaciones por correo (matrícula y notas)",     type="feature", status="done", priority="media", assignee="Valentina Ríos", assignee_initials="VR", points=3, sprint=3),
    # Sprint 4
    Task(id="SGP-15", title="Pruebas unitarias — modelos Pydantic",              type="chore",   status="done",        priority="alta",  assignee="Andrés Mora",    assignee_initials="AM", points=3, sprint=4),
    Task(id="SGP-16", title="Pruebas unitarias — lógica de negocio",             type="chore",   status="done",        priority="alta",  assignee="Andrés Mora",    assignee_initials="AM", points=3, sprint=4),
    Task(id="SGP-17", title="Pruebas de integración — endpoints API",            type="chore",   status="done",        priority="alta",  assignee="Andrés Mora",    assignee_initials="AM", points=2, sprint=4),
    Task(id="SGP-18", title="Bug: token JWT expiraba antes de lo esperado",      type="bug",     status="done",        priority="alta",  assignee="Valentina Ríos", assignee_initials="VR", points=2, sprint=4),
    Task(id="SGP-19", title="Bug: formulario matrícula sin validar cupos",       type="bug",     status="done",        priority="media", assignee="Andrés Mora",    assignee_initials="AM", points=1, sprint=4),
    Task(id="SGP-20", title="Bug: tabla notas no carga en Safari mobile",        type="bug",     status="done",        priority="baja",  assignee="Valentina Ríos", assignee_initials="VR", points=1, sprint=4),
    Task(id="SGP-21", title="Configurar pipeline GitHub Actions CI/CD",          type="chore",   status="done",        priority="alta",  assignee="Valentina Ríos", assignee_initials="VR", points=3, sprint=4),
    Task(id="SGP-22", title="Despliegue en Railway — entorno producción",        type="chore",   status="done",        priority="alta",  assignee="Valentina Ríos", assignee_initials="VR", points=2, sprint=4),
    Task(id="SGP-23", title="Pruebas de aceptación con usuario final",           type="chore",   status="done",        priority="alta",  assignee="Sofía Castro",   assignee_initials="SC", points=2, sprint=4),
    Task(id="SGP-24", title="Documentación técnica final del proyecto",          type="chore",   status="done",        priority="media", assignee="Carlos Herrera", assignee_initials="CH", points=2, sprint=4),
]

# ── Activity feed ─────────────────────────────────────────────────────────────

activity = [
    Activity(user="Valentina Ríos", initials="VR", action="cerró",     target="SGP-18 — Bug JWT token expiry",            time="hace 2 días",  type="close"),
    Activity(user="Andrés Mora",    initials="AM", action="completó",   target="Suite de pruebas de integración (10/10)",  time="hace 2 días",  type="close"),
    Activity(user="Valentina Ríos", initials="VR", action="desplegó",   target="v1.0.3 en Railway — producción",           time="hace 3 días",  type="deploy"),
    Activity(user="Andrés Mora",    initials="AM", action="abrió",      target="SGP-20 — Bug Safari mobile",               time="hace 4 días",  type="open"),
    Activity(user="Laura Gómez",    initials="LG", action="aprobó",     target="Sprint 4 — Pruebas y despliegue",          time="hace 4 días",  type="approve"),
    Activity(user="Valentina Ríos", initials="VR", action="mergeó",     target="feature/auth → develop",                   time="hace 6 días",  type="merge"),
    Activity(user="Carlos Herrera", initials="CH", action="actualizó",  target="Documentación de arquitectura v2",         time="hace 7 días",  type="comment"),
    Activity(user="Laura Gómez",    initials="LG", action="creó",       target="Sprint 4 — Pruebas y despliegue",          time="hace 12 días", type="approve"),
]
