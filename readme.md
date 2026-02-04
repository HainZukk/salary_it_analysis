# Análisis de Salarios en el Sector IT / Data Science

## Introducción

El sector de Tecnología de la Información (IT), y en particular el área de Data Science, presenta grandes diferencias salariales a nivel global. Factores como el país de residencia, el nivel de experiencia, el rol desempeñado y la modalidad de trabajo (presencial o remoto) influyen significativamente en los ingresos de los profesionales.

El objetivo de este trabajo es analizar un dataset de salarios del sector IT/Data con el fin de identificar patrones, comparar países y comprender qué variables tienen mayor impacto en la remuneración anual medida en dólares estadounidenses.

---

## Objetivo del análisis

El análisis busca responder preguntas clave relacionadas con:

* Las diferencias salariales entre países.
* La influencia del nivel de experiencia.
* El impacto del trabajo remoto.
* La distribución de roles dentro del sector Data.

Para evitar distorsiones causadas por valores extremos, en la mayoría de los casos se utiliza la **mediana salarial** en lugar del promedio.

---

## Preguntas de análisis

A partir del dataset analizado, se intentó responder las siguientes preguntas:

1.  ¿Existe una diferencia salarial entre Estados Unidos y Argentina?
2.  ¿La brecha salarial entre US y AR es significativa?
3.  ¿Cómo influye el país de residencia en el salario?
4.  ¿Qué rol gana más?
5.  ¿Cómo se distribuyen los sueldos?
6.  ¿Hay más juniors o seniors?
7.  ¿Cuánto influye la experiencia?
8.  ¿El trabajo remoto paga más?

---

## Metodología

El análisis se realizó utilizando **Python** y las siguientes bibliotecas:

* `pandas`: para la manipulación y análisis de datos.
* `matplotlib` y `seaborn`: para la visualización de la información.

Se aplicaron técnicas de filtrado, agrupamiento y agregación de datos (`groupby`, `value_counts`, `median`) para obtener métricas representativas. Las visualizaciones incluyen gráficos de barras, boxplots y countplots, priorizando la claridad y la correcta interpretación de los resultados.

---

## Principales análisis realizados

### Comparación salarial por país
Se comparó la mediana salarial anual en dólares entre Estados Unidos y Argentina. El análisis muestra una diferencia marcada a favor de Estados Unidos, evidenciando una brecha salarial significativa asociada al país de residencia.

### Distribución de roles en el sector Data
Se analizó la frecuencia de los distintos roles (*Data Scientist, Data Analyst, Data Engineer*, entre otros) en Argentina, identificando cuáles son los puestos más comunes dentro del sector.

### Impacto del nivel de experiencia
Se evaluó cómo varía el salario según el nivel de experiencia (*Entry, Mid, Senior, Executive*), observándose un incremento progresivo de la mediana salarial a medida que aumenta la experiencia.

### Trabajo remoto y salario
Se estudió la relación entre la modalidad de trabajo (presencial, híbrido y remoto) y el salario percibido, analizando si el trabajo remoto presenta una ventaja salarial.

---

## Conclusiones

A partir del análisis realizado, se concluye que:

* El **país de residencia** es uno de los factores más determinantes del salario.
* Existe una **brecha salarial significativa** entre Estados Unidos y Argentina.
* El **nivel de experiencia** impacta directamente en la remuneración.
* El **trabajo remoto** puede representar una oportunidad de mejora salarial, especialmente para profesionales en países con salarios locales más bajos que trabajan para el exterior.
* Algunos roles especializados dentro del sector Data presentan salarios considerablemente superiores al promedio.

---

## Limitaciones y trabajo futuro

Este análisis se basa en un dataset específico y puede contener sesgos relacionados con la muestra de datos. Como trabajo futuro, se propone profundizar el análisis incorporando:

* Comparaciones por tamaño de empresa.
* Análisis temporal de la evolución salarial.
* Segmentación más detallada por tecnologías específicas.

## Estructura del proyecto

Salary_analysis/
├── data/
│   ├── salaries.csv          # Datos crudos
│   └── salaries.json         # Formato alternativo
├── notebooks/
│   ├── data_cleaning.ipynb   # Proceso de limpieza
│   └── visualization.ipynb   # Análisis visual y EDA
├── src/
│   └── cleaning_function.py  # Funciones auxiliares de Python
└── README.md                 # Documentación del proyecto

```