# Infografías - Unidad 1: Marco Contextual del Desarrollo Gerencial

A continuación se presentan los diagramas visuales (infografías) para la Unidad 1, basados en los apuntes detallados.

## 1. Infografía Integradora de la Unidad 1

Este diagrama muestra cómo se enlazan los textos principales de la unidad en torno al concepto central del Desarrollo Gerencial.

```mermaid
graph TD
    A[Unidad 1: Marco Contextual] --> B(Las Organizaciones y su Anatomía)
    A --> C(El Aprendizaje y la Educación)
    A --> D(El Entorno Público y la Innovación)

    %% Lazatti
    B --> B1[Santiago Lazatti]
    B1 --> B2[Funciones Gerenciales]
    B1 --> B3[Sistema Técnico vs Sistema Social]
    
    %% Gore
    C --> C1[Ernesto Gore]
    C1 --> C2[La educación en la empresa]
    C1 --> C3[De la capacitación técnica al desarrollo de criterios]
    
    %% CLAD
    D --> D1[CLAD]
    D1 --> D2[Carta Iberoamericana de Innovación]
    D1 --> D3[Inteligencia Colectiva y Era Digital]

    %% Enlaces cruzados
    B2 -. Requiere .-> C2
    C3 -. Fomenta .-> D2
    B3 -. Se impacta por .-> D3
```

---

## 2. Infografía Particular: Santiago Lazatti (Funciones Gerenciales)

Este mapa mental desglosa la anatomía de las organizaciones y el rol del gerente según Lazatti.

```mermaid
mindmap
  root((Lazatti:
  Funciones
  Gerenciales))
    Anatomía de la Organización
      Sistema Técnico
        Operación
        Información
        Arquitectura Organizativa
        Resultados
      Sistema Social
        Individuos
        Grupos
        Clima Organizacional
        Cultura
    Rol del Gerente
      No hace tareas operativas
      Conduce el comportamiento de otros
      Opera en el límite entre subsistemas
    Las Fuerzas Vitales
      Conducción Management
      El Trabajo Humano
      Poder y Cultura
```

---

## 3. Infografía Particular: Ernesto Gore (La educación en la empresa)

Diagrama de flujo que explica la transición del aprendizaje instrumental al desarrollo de criterios según Gore.

```mermaid
graph LR
    subgraph Dominio Instrumental
    A1(Saber cómo hacer tareas físicas) --> A2(Adiestramiento)
    A2 --> A3(Conocimiento estructurado)
    end
    
    subgraph Transición al Liderazgo
    B1(Ascenso de técnico a jefe) --> B2(Pérdida de certezas)
    B2 --> B3(Necesidad de nuevas habilidades sociales)
    end
    
    subgraph Desarrollo Gerencial
    C1(Dominio Tecnológico/Simbólico) --> C2(Entender el contexto)
    C2 --> C3(Uso de Criterios y Valores)
    end

    A3 -->|Promoción| B1
    B3 -->|Capacitación estratégica| C1
```

---

## 4. Infografía Particular: CLAD (Carta Iberoamericana de Innovación)

Mapa que detalla los pilares de la innovación pública y la inteligencia colectiva.

```mermaid
graph TD
    A{Innovación Pública CLAD}
    
    A --> B(Inteligencia Colectiva)
    A --> C(Digitalización y Tecnologías)
    A --> D(Nuevo Perfil Directivo)
    
    B --> B1[Co-creación ciudadana]
    B --> B2[Aprovechamiento de datos]
    
    C --> C1[Teletrabajo y Smartificación]
    C --> C2[Uso ético de IA]
    
    D --> D1[Flexibilidad e Innovación]
    D --> D2[Gestión del Cambio]
```
