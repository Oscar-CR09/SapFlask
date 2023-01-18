from app import db


class Persona(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    nombre = db.Column(db.String(250))
    apelido = db.Column(db.String(250))
    email = db.Column(db.String(250))

    def __str__(self):
        return (
            f'Id: {self.id},'
            f'Nombre: {self.nombre},'
            f'Apellido: {self.apelido}'
            f'Email: {self.email} '
        )