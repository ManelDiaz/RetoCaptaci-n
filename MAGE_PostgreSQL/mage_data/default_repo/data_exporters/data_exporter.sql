INSERT INTO public.tabla_destino (nombre, apellido, edad, salario, activo)
SELECT nombre, apellido, edad, salario, activo FROM {{ df_1 }};