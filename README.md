Para correr el programa usamos

```
python3 main.py
```

Para clonar el proyecto, pueden usar [Github Desktop](https://desktop.github.com/).

Si gustan, les recomiendo ver este [video](https://www.youtube.com/watch?v=8Dd7KRpKeaE) para conocer mejor como trabajar con git y github.
 
Si es que alguien va a importar alguna librería externa (que no venga con python) como pandas, numpy, etc sigan las instrucciones siguientes
para que todos tengamos acceso automático a ella.

Si es que van a añadir por primera vez la dependencia, escribanla en el archivo `requirements.txt` así: 

```
numpy
```

Cuando abran el proyecto con su editor ingresen en la terminal el siguiente comando:

```
python3 -m venv proj-venv
```

Después en Windows :

```
proj-venv\Scripts\activate
```

En mac :

```
source proj-venv/bin/activate
```

Finalmente, para descargar las librerías:

```
pip install -r requirements.txt
```

Formato intermedio:
```
materia,profesor,clave,lunes,martes,jueves,viernes,sabado,domingo,creditos
calculo,annabella,01,11:30-13:00,NULL,15:30-17:00,NULL,NULL,NULL,NULL,5
```
