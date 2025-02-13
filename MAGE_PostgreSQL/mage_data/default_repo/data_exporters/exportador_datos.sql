INSERT INTO public.tabla_destino (id, nombre, apellido, edad, fecha_nacimiento, salario, activo)
VALUES
    ({{ id }}, '{{ nombre }}', '{{ apellido }}', {{ edad }}, '{{ fecha_nacimiento }}', {{ salario }}, {{ activo }});