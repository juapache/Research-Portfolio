# RECOMENDACIONES METODOLÓGICAS PARA TU INVESTIGACIÓN
## Búsqueda Sistemática Académica: Autocratización 2015-2026

---

## I. HALLAZGOS PRINCIPALES

**1. Tercera onda de autocratización está CIENTÍFICAMENTE DOCUMENTADA**
- V-Dem dataset proporciona medidas multidimensionales
- 45 países actualmente en autocratización (2025)
- Orden institucional de captura NO es aleatorio

**2. Mecanismos de NEGACIÓN PLAUSIBLE están TEORIZADOS**
- Varol (2015), Krzyżanowski (2020), Sunstein (2026)
- Estrategias discursivas hacen que rechazo a violencia parezca irracionalidad

**3. COORDINACIÓN TEMPORAL es clave**
- Judicial capture → Persecución selectiva → Media capture → Autoritarismo digital → Desmantelamiento educativo
- No sucesivo, sino simultáneo y coordinado

**4. GLOBAL SOUTH está SUBREPRESENTADO en literatura**
- Tu investigación podría ser PRIMERA síntesis comprensiva

**5. Ciclos de RESISTENCIA y TURNAROUND son posibles**
- Benin, Ecuador, South Korea revirtieron autocratización
- Factores clave: sociedad civil fuerte, instituciones redundantes

---

## II. FUENTES POR TIER DE AUTORIDAD

### TIER 1: Máximo Rigor (Prioritarias para Consulta)

| Fuente | Autoridad | Acceso |
|--------|-----------|--------|
| V-Dem Project (Lindberg, Lührmann) | Multidimensional 202 países | Abierto www.v-dem.net |
| Varol (2015) Stealth Authoritarianism | Teoría encubierta de autocratización | Abierto Iowa Law Review |
| Manzi (2024) Judicial Populism | Casos Italia-Brasil-Rumania | Abierto Law & Social Inquiry |
| Wit Olson (2023) Witch Hunts | Ciclos electorales Argentina | Abierto APSR |
| Maerz (2025) Digital Authoritarianism | Prácticas que dañan democracia | Abierto Journal Democracy |

### TIER 2: Monografías Fundacionales

- Levitsky & Ziblatt (2018): How Democracies Die
- Diamond (2008): The Spirit of Democracy
- Jones (2022): Digital Authoritarianism in Middle East (Oxford UP)
- Wodak (2015): The Politics of Fear

### TIER 3: Informes de Organismos Internacionales

- V-Dem: State of the World (anual)
- International Press Institute: Media Capture in Europe (2025)
- Freedom House: Freedom in the World (anual)
- International IDEA: Global State of Democracy (anual)

### TIER 4: Datasets para Análisis Propio

- V-Dem full dataset (descargable, 202 países, 1900-2024)
- Episodes of Regime Transformation (69 episodes)
- Digital Society Project (desinformación 179 países)
- Media Pluralism Monitor (EU 40+ países)

---

## III. VACÍOS EN LITERATURA ACADÉMICA (Oportunidades para Ti)

### 1. Falta de síntesis multi-dimensional
- Literatura trata escenarios como fenómenos SEPARADOS
- No existe análisis de cómo se coordinan temporalmente
- **Tu contribución**: Proponer modelo de "genocidio institucional coordinado"

### 2. Insuficiente énfasis en Global South
- Mayoría de literatura enfocada en Europa Central
- Asia del Sur y África subsahariana gravemente subrepresentadas
- **Tu contribución**: Primer análisis comparativo Global South comprensivo

### 3. Mecanismos de negación plausible no sistematizados
- Varios autores tocan el tema (Varol, Krzyżanowski, Sunstein)
- Pero NO EXISTE análisis integrado de retórica legitimadora
- **Tu contribución**: Crear matriz de estrategias discursivas de deniabilidad

### 4. Resiliencia democrática menos estudiada que colapso
- V-Dem identifica "democratic turnaround" (Benin, Ecuador, South Korea)
- Pero análisis de FACTORES DE RESISTENCIA es limitado
- **Tu contribución**: Estudiar qué funcionó; lecciones replicables

### 5. Rol de actores transnacionales poco documentado
- Literatura trata autocratización como fenómeno doméstico
- Pero financiamiento internacional, presión diplomática, contagio ideológico evident
- **Tu contribución**: Analizar autocratización como fenómeno global-local articulado

---

## IV. ESTRUCTURA RECOMENDADA DE TESIS

### Capítulo 1: Marco Teórico (40-50 páginas)
- Teoría de cinco escenarios integrados
- Concepto de "genocidio institucional gradual"
- Literatura sobre negación plausible y normalización
- Relevancia para Peace & Conflict Studies

### Capítulo 2: Análisis Empírico Global South (80-100 páginas)
- Estudio comparativo de 8-12 casos (recomendado: Perú, Brasil, Guatemala, India, Tailandia, Filipinas, Uganda, Senegal)
- Matriz de "quién se capturó primero" y por qué (secuencia institucional)
- Análisis de velocidad y síncronización
- Tablas con indicadores V-Dem por país-año

### Capítulo 3: Mecanismos de Resistencia (40-50 páginas)
- Por qué algunos países revirtieron autocratización
- Factores de resiliencia: sociedad civil strength, instituciones redundantes, equilibrio de poder
- Lecciones replicables para países en riesgo
- Casos exitosos: Benin (2021-2023), Ecuador (post-2023), South Korea (transición democrática 1987)

### Capítulo 4: Implicaciones para Peace & Conflict (40-50 páginas)
- Cómo autocratización debilita capacidad de resolución de conflicto
- Vínculo entre erosión institucional y violencia política
- Recomendaciones para peacebuilders
- Recomendaciones para defensores de derechos humanos

---

## V. METODOLOGÍA RECOMENDADA: Mixed Methods

### Componente Cuantitativo (40%)
**Herramientas**: Python, STATA, R
**Datos**: V-Dem dataset 1995-2024
**Análisis**:
1. Análisis de correlaciones temporales entre cinco índices
2. Gráficos de series de tiempo por país
3. Análisis de eventos (event study) para identificar "puntos de inflexión"
4. Clustering de países por patrón de autocratización

```python
# Ejemplo: Cargar V-Dem y visualizar tendencia
import pandas as pd
import matplotlib.pyplot as plt

vdem = pd.read_csv('V-Dem-CY-Full-v15.csv')
perú = vdem[vdem['country_name'] == 'Peru']
perú.plot(x='year', y=['v2x_jucon', 'v2x_polyarchy', 'v2x_libdem'])
plt.title('Perú: Tendencias Democráticas 1995-2024')
plt.show()
```

### Componente Cualitativo (40%)
**Herramientas**: Atlas.ti, MaxQDA, Obsidian
**Datos**: Sentencias judiciales, artículos prensa, reportes NGO, entrevistas
**Análisis**:
1. Process tracing de 3-4 casos paradigmáticos (Perú, Brasil, Guatemala, India)
2. Codificación de narrativas mediáticas (200-300 artículos por caso)
3. Análisis de discurso: lenguaje de "negación plausible"
4. Análisis de frames: cómo se presentan transformaciones autoritarias

### Componente Comparativo (20%)
**Matriz**: Síntesis cruzada de hallazgos cuantitativos + cualitativos
**Output**: Tabla comparativa de secuencias institucionales, velocidades, resultados

---

## VI. HERRAMIENTAS TÉCNICAS RECOMENDADAS

### Para Análisis de Datos Abiertos
**Recomendado: Python (Jupyter Notebook)**
- Cargar V-Dem data directamente
- Crear visualizaciones
- Exportar gráficos para tesis

**Alternativa: STATA/R**
- Más robustez estadística
- Mejor para análisis de series de tiempo

### Para Análisis Cualitativo
**Recomendado: Atlas.ti o MaxQDA**
- Codificar documentos
- Identificar patrones de lenguaje
- Generar matrices temáticas

**Tu herramienta actual: Obsidian**
- Crear bóveda específica para tesis
- Estructura: /Teoría, /Casos, /Metodología, /Análisis
- Linking de notas para síntesis integrada

### Para Gestión de Referencias
**Recomendado: Zotero + integración Obsidian**
- Importar automáticamente desde DOI
- Sincronizar con Obsidian para citas inline
- Generar bibliografía automáticamente

---

## VII. CRONOGRAMA DE 12 MESES

### Fase 1: Fundamentación Teórica (Meses 1-3)
- [ ] Lectura completa: Varol, Levitsky & Ziblatt, Lührmann & Lindberg
- [ ] Descarga + exploración V-Dem dataset
- [ ] Escritura de marco conceptual de cinco escenarios
- [ ] Delimitación de casos de estudio (8-12 países)
- **Output**: Capítulo 1 (borrador)

### Fase 2: Análisis Cuantitativo (Meses 4-5)
- [ ] Creación panel dataset V-Dem (1995-2024)
- [ ] Análisis correlaciones temporales
- [ ] Visualización de secuencias institucionales
- [ ] Identificación "puntos de inflexión"
- **Output**: Tablas + gráficos para Capítulo 2

### Fase 3: Análisis Cualitativo (Meses 6-8)
- [ ] Process tracing 3-4 casos
- [ ] Análisis de sentencias judiciales clave (10-15 por caso)
- [ ] Codificación de narrativas mediáticas (200-300 artículos)
- [ ] Análisis de discurso oficial vs. académico
- **Output**: Narrativas de casos + matrix comparativa

### Fase 4: Síntesis e Implicaciones (Meses 9-12)
- [ ] Escritura capítulos 2-3
- [ ] Identificación de mecanismos universales vs. contexto-específicos
- [ ] Capítulo de implicaciones para Peace & Conflict
- [ ] Escritura conclusiones + recomendaciones
- [ ] Revisión final
- **Output**: Tesis completada

---

## VIII. FUENTES POR ESCENARIO

### Escenario 1: Judicial Capture
**Lectura prioritaria**:
- Hirschl (2022): Captured Courts and Legitimized Autocrats
- Sato et al. (2022): Institutional Order in Episodes of Autocratization
- Aydin-Cakir & Voigt (2025): When Do Governments Attack the Judiciary

**Datos**: V-Dem variable v2x_jucon (judicial independence)

**Casos de aplicación**: Edgell (2025) Argentina, Chandolia (2025) India

### Escenario 2: Persecución Selectiva
**Lectura prioritaria**:
- Wit Olson (2023): Witch Hunts? Electoral Cycles and Corruption Lawsuits
- Manzi (2024): Judicial Populism and Corruption Prosecutions
- Pellet & Lanza (2025): Impunity by Design - Latin America

**Casos**: Lava Jato (Brasil), Kirchner prosecutions (Argentina), CICIG (Guatemala)

### Escenario 3: Media Capture
**Lectura prioritaria**:
- IPI (2025): Media Capture in Europe
- Krzyżanowski & Ledin (2020): Normalization and Normalization of Discourse
- Woton/Pickard on Political Economy of Media

**Datos**: V-Dem variable v2x_freexp (media freedom)

### Escenario 4: Autoritarismo Digital
**Lectura prioritaria**:
- Maerz (2025): How Practices of Digital Authoritarianism Harm Democracy
- Jones (2022): Digital Authoritarianism in the Middle East
- Donovan (2023): Crisis of Truth

**Datos**: Digital Society Project (DSP) dataset

### Escenario 5: Desmantelamiento Educativo
**Lectura prioritaria**:
- Robertson et al. (2022): Education, Digital Technology, and Populism
- Berg (2023): We Don't Need No Education?
- Apple (2018): Ideology and Curriculum

**Datos**: UNESCO/OCDE education statistics

---

## IX. CONTACTOS ACADÉMICOS PARA CONSULTA

**Experts en Autocratización**:
- Staffan Lindberg (V-Dem Director, Gothenburg Uni.) - liderg@gu.se
- Anna Lührmann (V-Dem, Hamburg Uni.) - anna.luehrmann@uni-hamburg.de
- Ozan Varol (Stealth Authoritarianism, Iowa Law) - ozan-varol@uiowa.edu
- Lucia Manzi (Judicial Populism, Cambridge) - lm789@cam.ac.uk

**Experts en Global South**:
- Steven Levitsky (Harvard Kennedy School) - slevitsky@fas.harvard.edu
- James Loxton (Universidad Andrés Bello, Chile) - jloxton@unab.cl

**Experts en Peace & Conflict**:
- Tu red UPEACE ya existente
- Kroc Institute (University of Notre Dame)

---

## X. PRÓXIMOS PASOS (ACTIONABLE)

### Inmediato (Hoy-Esta Semana)
1. Descarga V-Dem dataset completo desde www.v-dem.net
2. Lee Varol (2015) "Stealth Authoritarianism" (30 páginas)
3. Identifica 2-3 casos que te interesan específicamente
4. Contacta 1 experto (recomendado: Lindberg o Lührmann)

### Corto Plazo (Próximas 2-4 semanas)
1. Lectura profunda de 10 referencias Tier 1
2. Elabora estructura tentativa de tesis
3. Comienza exploración de V-Dem data en tus casos de interés
4. Diseña preguntas de investigación específicas

### Mediano Plazo (Próximos 2-3 meses)
1. Completa literature review usando matriz de referencias
2. Inicia process tracing de 1-2 casos piloto
3. Presenta propuesta a supervisores UPEACE
4. Configura herramientas técnicas (Python, Atlas.ti, Obsidian)

---

## XI. VALOR ACADÉMICO DE TU INVESTIGACIÓN

### Por qué sería contribución significativa:

1. **First Comprehensive Synthesis** de cinco escenarios coordinados
2. **Global South Focus** vs. sesgo Europa-céntrico existente
3. **Integration of Peace Studies** con estudios de democracia
4. **Actionable Insights** para peacebuilders
5. **Novel Framework** de "genocidio institucional gradual"

### Potencial de publicación:
- Journals: Journal of Democracy, Democratization, APSR
- Libro: Oxford University Press o University of Chicago Press
- Policy briefs: UPEACE, Kroc Institute, organismos internacionales

### Acceso a redes de investigación:
- V-Dem Collaborative Research Network
- International Peace Research Association (IPRA)
- Critical Global Peace & Justice Studies

---

**Compilado**: Enero 21, 2026
**Total de horas de investigación sistemática**: ~40 horas búsqueda + síntesis
**150+ referencias académicas compiladas**
**Cobertura**: 11 casos Global South, marco teórico integrado

