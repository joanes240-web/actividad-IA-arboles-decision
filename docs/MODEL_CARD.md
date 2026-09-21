# Model Card · Simulador what-if v1.0.0

## Propósito
Comparar alternativas de intervención formativa bajo supuestos explícitos y reproducibles.

## Tipo
Modelo determinístico basado en una función saturante. No utiliza machine learning.

## Entradas
`c`, `r`, `p` en el intervalo [0,1].

## Salidas
- `G`: reducción relativa simulada.
- `T_s`: tiempo medio simulado.
- `E_s`: índice relativo `T0/Ts`.

## Caso base
`T0 = 42.0 h` para la versión académica.

## Calibración
Los parámetros reproducen cuatro objetivos de reducción del piloto: 11.0%, 14.5%, 17.6% y 24.3%.

## Validación incluida
- reproducción de escenarios;
- caso base;
- límites numéricos;
- monotonicidad;
- sensibilidad conjunta de beta ±10%.

## Límites
- no estima causalidad;
- no calcula intervalos de confianza ni significancia;
- no debe utilizarse para ranking individual;
- T0 debe recalcularse por población/periodo en una implantación productiva;
- la escala 0–1 depende de una definición operacional documentada.

## Evolución recomendada
Datos longitudinales o experimentales para estimar parámetros, incorporar incertidumbre y evaluar diseños causales.
