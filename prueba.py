from couchdb.mapping import Document, TextField, IntegerField, Mapping
from couchdb.mapping import DictField, ViewField, BooleanField, ListField
from couchdb import Server
import couchdb


#La direccion del servidor
couch = couchdb.Server("http://127.0.0.1:5984/")

#Hace la coneccion local automaticamente 
#server = Server()

#Referirse a una base de datos ya existente
db = couch['test']

#Crear una database
#db = server.create("test")

#Eliminar una database 
#db = server.delete("test")


#Crear un documento 

#doc = {
#    '_id': '1',
#    #'_rev': '1-0000000001',
#    'content': {
#        'nombre': 'jean',
#        'apellido': 'soto',
#        'edad': '19'
#    }
#}

#db.save(doc)

#Eliminar un documento 

#doc= db['1']
#db.delete(doc)


print 'Programa finalizado con exito'
