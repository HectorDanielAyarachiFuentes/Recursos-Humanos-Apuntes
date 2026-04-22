# Infografías - Unidad 3: Desarrollo Gerencial

A continuación se presentan los diagramas visuales para la Unidad 3, en base a los resúmenes de Dessler y Lazatti.

## 1. Infografía Integradora de la Unidad 3

Este diagrama muestra cómo se conectan las etapas del desarrollo (Lazatti) con las técnicas específicas de entrenamiento (Dessler).

```mermaid
graph TD
    A[Unidad 3: Desarrollo Gerencial] --> B(Etapas del Desarrollo)
    A --> C(Técnicas de Entrenamiento)

    %% Lazatti
    B --> B1[S. Lazatti]
    B1 --> B2[Detectar potencial]
    B1 --> B3[Desarrollar y Promover]
    
    %% Dessler
    C --> C1[G. Dessler]
    C1 --> C2[Dentro del puesto]
    C1 --> C3[Fuera del puesto]

    %% Enlaces
    B3 -. Se ejecuta mediante .-> C2
    B3 -. Se ejecuta mediante .-> C3
```

---

## 2. Infografía Particular: Gary Dessler (Desarrollo de Gerentes)

Mapa mental sobre los métodos de entrenamiento gerencial según Dessler.

```mermaid
mindmap
  root((Dessler:
  Desarrollo
  Gerencial))
    Proceso General
      Proyección de necesidades
      Evaluación del desempeño
      Desarrollo del candidato
    Dentro del Puesto
      Rotación de puestos
      Método de asesoramiento (Coaching)
      Aprendizaje de acción
    Fuera del Puesto
      Estudio de casos
      Juegos gerenciales
      Seminarios externos
      Programas universitarios
      Modelado de comportamiento
```

---

## 3. Infografía Particular: Santiago Lazatti (Etapas del Desarrollo)

Diagrama de flujo del ciclo de vida del desarrollo del talento interno.

```mermaid
graph LR
    A(1. Ingreso) --> B(2. Desempeño Actual)
    B --> C(3. Detección de Potencial)
    C --> D(4. Desarrollo)
    D --> E(5. Promoción)
    
    B -. Feedback constante .-> B
    C -. Evaluación psicológica .-> C
    D -. Capacitación continua .-> D
    
    E --> F(Nuevo Rol)
    F -. Reinicia ciclo .-> B
```
