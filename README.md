
# Cmd
# buscar la carpeta
cd "C:\Users\jose\Documents\GitHub\proyectoFullStack\FullStackPython"  
# activar ambiente virtual
.\.venv\Scripts\activate
# instalar el framework
pip install -U Flask
# actualizar python
python -m pip install --upgrade pip
# setuptools actualizar
pip install --upgrade setuptools
#   instalando driver especifico para esta version de python y windows ---bajar driver de esta direccion https://www.lfd.uci.edu/~gohlke/pythonlibs/#mysqlclient
pip install mysqlclient-1.4.6-cp38-cp38-win32.whl
# para instalar base de datos
pip install flask-mysqldb
# iniciar el servidor
python.exe -m flask run
