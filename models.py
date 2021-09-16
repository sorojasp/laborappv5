# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Ciudades(models.Model):
    codigociudad = models.IntegerField(db_column='codigoCiudad', primary_key=True)  # Field name made lowercase.
    nombreciudad = models.CharField(db_column='nombreCiudad', max_length=100)  # Field name made lowercase.
    codigodepartamento = models.ForeignKey('Departamentos', models.DO_NOTHING, db_column='codigoDepartamento')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ciudades'


class Conflictocesantias(models.Model):
    idconflictocesantias = models.AutoField(db_column='idConflictoCesantias', primary_key=True)  # Field name made lowercase.
    idcontrato = models.ForeignKey('Contratolaboral', models.DO_NOTHING, db_column='idContrato')  # Field name made lowercase.
    fechaultimascesantiaspagadas = models.DateField(db_column='fechaUltimasCesantiasPagadas', blank=True, null=True)  # Field name made lowercase.
    fechafinalnopagocesantias = models.DateField(db_column='fechaFinalNoPagoCesantias', blank=True, null=True)  # Field name made lowercase.
    montodinero_cesantias = models.IntegerField(db_column='montoDinero_Cesantias', blank=True, null=True)  # Field name made lowercase.
    montodinero_interesescesantias = models.IntegerField(db_column='montoDinero_InteresesCesantias', blank=True, null=True)  # Field name made lowercase.
    iddemandapersonanatural = models.ForeignKey('Demandapersonanatural', models.DO_NOTHING, db_column='idDemandaPersonaNatural', blank=True, null=True)  # Field name made lowercase.
    iddemandaempresa = models.ForeignKey('Demandaempresa', models.DO_NOTHING, db_column='idDemandaEmpresa', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'conflictocesantias'


class Conflictodespidosjc(models.Model):
    idconflictodespidosjc = models.AutoField(db_column='idConflictoDespidoSJC', primary_key=True)  # Field name made lowercase.
    iddemandapersonanatural = models.ForeignKey('Demandapersonanatural', models.DO_NOTHING, db_column='idDemandaPersonaNatural', blank=True, null=True)  # Field name made lowercase.
    iddemandaempresa = models.ForeignKey('Demandaempresa', models.DO_NOTHING, db_column='idDemandaEmpresa', blank=True, null=True)  # Field name made lowercase.
    fechainiciocontrato = models.DateField(db_column='fechaInicioContrato')  # Field name made lowercase.
    tipocontrato = models.CharField(db_column='tipoContrato', max_length=100)  # Field name made lowercase.
    idcontrato = models.ForeignKey('Contratolaboral', models.DO_NOTHING, db_column='idContrato')  # Field name made lowercase.
    fechadespido = models.DateField(db_column='fechaDespido', blank=True, null=True)  # Field name made lowercase.
    montodinero_dsjc = models.IntegerField(db_column='montoDinero_DSJC', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'conflictodespidosjc'


class Conflictopagosalario(models.Model):
    idconflictopagosalario = models.AutoField(db_column='idConflictoPagoSalario', primary_key=True)  # Field name made lowercase.
    idcontrato = models.ForeignKey('Contratolaboral', models.DO_NOTHING, db_column='idContrato')  # Field name made lowercase.
    fechainicionopago = models.DateField(db_column='fechaInicioNoPago')  # Field name made lowercase.
    fechafinalnopagosalario = models.DateField(db_column='fechaFinalNoPagoSalario', blank=True, null=True)  # Field name made lowercase.
    montodinero_pagosalario = models.IntegerField(db_column='montoDinero_PagoSalario', blank=True, null=True)  # Field name made lowercase.
    iddemandapersonanatural = models.ForeignKey('Demandapersonanatural', models.DO_NOTHING, db_column='idDemandaPersonaNatural', blank=True, null=True)  # Field name made lowercase.
    iddemandaempresa = models.ForeignKey('Demandaempresa', models.DO_NOTHING, db_column='idDemandaEmpresa', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'conflictopagosalario'


class Conflictoprimas(models.Model):
    idconflictoprima = models.AutoField(db_column='idConflictoPrima', primary_key=True)  # Field name made lowercase.
    idcontrato = models.ForeignKey('Contratolaboral', models.DO_NOTHING, db_column='idContrato')  # Field name made lowercase.
    fechaultimaprimapagada = models.DateField(db_column='fechaUltimaPrimaPagada', blank=True, null=True)  # Field name made lowercase.
    fechafinalnopagoprima = models.DateField(db_column='fechaFinalNoPagoPrima', blank=True, null=True)  # Field name made lowercase.
    montodinero_prima = models.IntegerField(db_column='montoDinero_Prima', blank=True, null=True)  # Field name made lowercase.
    iddemandapersonanatural = models.ForeignKey('Demandapersonanatural', models.DO_NOTHING, db_column='idDemandaPersonaNatural', blank=True, null=True)  # Field name made lowercase.
    iddemandaempresa = models.ForeignKey('Demandaempresa', models.DO_NOTHING, db_column='idDemandaEmpresa', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'conflictoprimas'


class Conflictoscontactaabogado(models.Model):
    idconflictocontactaabogado = models.AutoField(db_column='idConflictoContactaAbogado', primary_key=True)  # Field name made lowercase.
    conflictoarl = models.TextField(db_column='conflictoARL', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    conflictopensiones = models.TextField(db_column='conflictoPensiones', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    conflictohorasextras = models.TextField(db_column='conflictoHorasExtras', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    conflictodominicalesfestivos = models.TextField(db_column='conflictoDominicalesFestivos', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    iddemandapersonanatural = models.ForeignKey('Demandapersonanatural', models.DO_NOTHING, db_column='idDemandaPersonaNatural', blank=True, null=True)  # Field name made lowercase.
    iddemandaempresa = models.ForeignKey('Demandaempresa', models.DO_NOTHING, db_column='idDemandaEmpresa', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'conflictoscontactaabogado'


class Conflictovacaciones(models.Model):
    idconflictovacaciones = models.AutoField(db_column='idConflictoVacaciones', primary_key=True)  # Field name made lowercase.
    idcontrato = models.ForeignKey('Contratolaboral', models.DO_NOTHING, db_column='idContrato')  # Field name made lowercase.
    fechaultimasvacaciones = models.DateField(db_column='fechaUltimasVacaciones')  # Field name made lowercase.
    fechafinalnopagovacaciones = models.DateField(db_column='fechaFinalNoPagoVacaciones', blank=True, null=True)  # Field name made lowercase.
    montodinero_vacaciones = models.IntegerField(db_column='montoDinero_Vacaciones', blank=True, null=True)  # Field name made lowercase.
    iddemandapersonanatural = models.ForeignKey('Demandapersonanatural', models.DO_NOTHING, db_column='idDemandaPersonaNatural', blank=True, null=True)  # Field name made lowercase.
    iddemandaempresa = models.ForeignKey('Demandaempresa', models.DO_NOTHING, db_column='idDemandaEmpresa', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'conflictovacaciones'


class Consultoriojuridico(models.Model):
    idconsultoriojuridico = models.AutoField(db_column='IdconsultorioJuridico', primary_key=True)  # Field name made lowercase.
    tipoconsultoriojuridico = models.CharField(db_column='tipoConsultorioJuridico', max_length=100, blank=True, null=True)  # Field name made lowercase.
    nombreconsultoriojuridico = models.CharField(db_column='nombreConsultorioJuridico', max_length=300)  # Field name made lowercase.
    telefonoconsultoriojuridico = models.IntegerField(db_column='telefonoConsultorioJuridico')  # Field name made lowercase.
    emailconsultoriojuridico = models.CharField(db_column='emailConsultorioJuridico', max_length=100, blank=True, null=True)  # Field name made lowercase.
    direccionconsultoriojuridico = models.CharField(db_column='direccionConsultorioJuridico', max_length=200, blank=True, null=True)  # Field name made lowercase.
    tipodocumentopersona = models.ForeignKey('Personas', models.DO_NOTHING, db_column='tipoDocumentoPersona')  # Field name made lowercase.
    numerodocumentopersona = models.ForeignKey('Personas', models.DO_NOTHING, db_column='numeroDocumentoPersona')  # Field name made lowercase.
    codigociudad = models.ForeignKey(Ciudades, models.DO_NOTHING, db_column='codigoCiudad')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'consultoriojuridico'


class Contratolaboral(models.Model):
    idcontrato = models.AutoField(db_column='idContrato', primary_key=True)  # Field name made lowercase.
    tipocontrato = models.CharField(db_column='tipoContrato', max_length=100)  # Field name made lowercase.
    fechainiciocontrato = models.DateField(db_column='fechaInicioContrato')  # Field name made lowercase.
    fechafinalcontrato = models.DateField(db_column='fechaFinalContrato', blank=True, null=True)  # Field name made lowercase.
    ultimosalario = models.IntegerField(db_column='ultimoSalario')  # Field name made lowercase.
    descripcionfunciones = models.TextField(db_column='descripcionFunciones')  # Field name made lowercase.
    tipodocumentopersona = models.ForeignKey('Personas', models.DO_NOTHING, db_column='tipoDocumentoPersona')  # Field name made lowercase.
    numerodocumentopersona = models.ForeignKey('Personas', models.DO_NOTHING, db_column='numeroDocumentoPersona')  # Field name made lowercase.
    idpersonanatural = models.ForeignKey('Personanatural', models.DO_NOTHING, db_column='IdPersonaNatural', blank=True, null=True)  # Field name made lowercase.
    nitempresa = models.ForeignKey('Empresa', models.DO_NOTHING, db_column='NItEmpresa', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'contratolaboral'


class Correopersonas(models.Model):
    correopersona = models.CharField(db_column='correoPersona', primary_key=True, max_length=70)  # Field name made lowercase.
    tipodocumentopersona = models.ForeignKey('Personas', models.DO_NOTHING, db_column='tipoDocumentoPersona')  # Field name made lowercase.
    numerodocumentopersona = models.ForeignKey('Personas', models.DO_NOTHING, db_column='numeroDocumentoPersona')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'correopersonas'


class Demandaempresa(models.Model):
    iddemandaempresa = models.AutoField(db_column='idDemandaEmpresa', primary_key=True)  # Field name made lowercase.
    fechademandaempresa = models.DateField(db_column='fechaDemandaEmpresa')  # Field name made lowercase.
    codigociudad = models.ForeignKey(Ciudades, models.DO_NOTHING, db_column='codigoCiudad')  # Field name made lowercase.
    tipodocumentopersona = models.ForeignKey('Personas', models.DO_NOTHING, db_column='tipoDocumentoPersona')  # Field name made lowercase.
    numerodocumentopersona = models.ForeignKey('Personas', models.DO_NOTHING, db_column='numeroDocumentoPersona')  # Field name made lowercase.
    nitempresa = models.ForeignKey('Empresa', models.DO_NOTHING, db_column='NItEmpresa')  # Field name made lowercase.
    idcontrato = models.ForeignKey(Contratolaboral, models.DO_NOTHING, db_column='idContrato')  # Field name made lowercase.
    fechapropuestaradicaciondemandaempresa = models.DateField(db_column='fechaPropuestaRadicacionDemandaEmpresa', blank=True, null=True)  # Field name made lowercase.
    fecharrealradicaciondemandaempresa = models.DateField(db_column='fecharRealRadicacionDemandaEmpresa', blank=True, null=True)  # Field name made lowercase.
    fechapropuestaradicacionderechopetiempresa = models.DateField(db_column='fechaPropuestaRadicacionDerechoPetiEmpresa', blank=True, null=True)  # Field name made lowercase.
    fecharrealradicacionderechopetiempresa = models.DateField(db_column='fecharRealRadicacionDerechoPetiEmpresa', blank=True, null=True)  # Field name made lowercase.
    informedesicionfinaldemandaempresa = models.TextField(db_column='informeDesicionFinalDemandaEmpresa', blank=True, null=True)  # Field name made lowercase.
    respuestafinaldemandaempresa = models.TextField(db_column='respuestaFinalDemandaEmpresa', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    montototaldemandapersjuri = models.FloatField(db_column='montoTotalDemandaPersJuri', blank=True, null=True)  # Field name made lowercase.
    superaminimacuantiapersjuri = models.TextField(db_column='superaMinimaCuantiaPersJuri', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'demandaempresa'


class Demandapersonanatural(models.Model):
    iddemandapersonanatural = models.AutoField(db_column='idDemandaPersonaNatural', primary_key=True)  # Field name made lowercase.
    fechademandapersonanatural = models.DateField(db_column='fechaDemandaPersonaNatural')  # Field name made lowercase.
    codigociudad = models.ForeignKey(Ciudades, models.DO_NOTHING, db_column='codigoCiudad')  # Field name made lowercase.
    tipodocumentopersona = models.ForeignKey('Personas', models.DO_NOTHING, db_column='tipoDocumentoPersona')  # Field name made lowercase.
    numerodocumentopersona = models.ForeignKey('Personas', models.DO_NOTHING, db_column='numeroDocumentoPersona')  # Field name made lowercase.
    idpersonanatural = models.ForeignKey('Personanatural', models.DO_NOTHING, db_column='IdPersonaNatural')  # Field name made lowercase.
    idcontrato = models.ForeignKey(Contratolaboral, models.DO_NOTHING, db_column='idContrato')  # Field name made lowercase.
    fechapropuestaradicaciondemandapersonan = models.DateField(db_column='fechaPropuestaRadicacionDemandaPersonaN', blank=True, null=True)  # Field name made lowercase.
    fecharrealradicaciondemandapersonan = models.DateField(db_column='fecharRealRadicacionDemandaPersonaN', blank=True, null=True)  # Field name made lowercase.
    fechapropuestaradicacionderechopetipersonan = models.DateField(db_column='fechaPropuestaRadicacionDerechoPetiPersonaN', blank=True, null=True)  # Field name made lowercase.
    fecharrealradicacionderechopetipersonan = models.DateField(db_column='fecharRealRadicacionDerechoPetiPersonaN', blank=True, null=True)  # Field name made lowercase.
    informedesicionfinaldemandapersonan = models.TextField(db_column='informeDesicionFinalDemandaPersonaN', blank=True, null=True)  # Field name made lowercase.
    respuestafinaldemandaersonan = models.TextField(db_column='respuestaFinalDemandaersonaN', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    montototaldemandapersnat = models.FloatField(db_column='montoTotalDemandaPersNat', blank=True, null=True)  # Field name made lowercase.
    superaminimacuantiapersnat = models.TextField(db_column='superaMinimaCuantiaPersNat', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'demandapersonanatural'


class Departamentos(models.Model):
    codigodepartamento = models.IntegerField(db_column='codigoDepartamento', primary_key=True)  # Field name made lowercase.
    nombredepartamento = models.CharField(db_column='nombreDepartamento', max_length=100)  # Field name made lowercase.
    codigopais = models.ForeignKey('Paises', models.DO_NOTHING, db_column='codigoPais')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'departamentos'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Empresa(models.Model):
    nitempresa = models.IntegerField(db_column='NItEmpresa', primary_key=True)  # Field name made lowercase.
    nombreempresars = models.CharField(db_column='nombreEmpresaRS', max_length=300)  # Field name made lowercase.
    direccionempresa = models.CharField(db_column='direccionEmpresa', max_length=200)  # Field name made lowercase.
    telefonoempresa = models.IntegerField(db_column='telefonoEmpresa', blank=True, null=True)  # Field name made lowercase.
    emailempresa = models.CharField(db_column='emailEmpresa', max_length=100, blank=True, null=True)  # Field name made lowercase.
    codigociudad = models.ForeignKey(Ciudades, models.DO_NOTHING, db_column='codigoCiudad')  # Field name made lowercase.
    tipodocumentopersona = models.ForeignKey('Personas', models.DO_NOTHING, db_column='tipoDocumentoPersona', blank=True, null=True)  # Field name made lowercase.
    numerodocumentopersona = models.ForeignKey('Personas', models.DO_NOTHING, db_column='numeroDocumentoPersona', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'empresa'


class Paises(models.Model):
    codigopais = models.IntegerField(db_column='codigoPais', primary_key=True)  # Field name made lowercase.
    nombrepais = models.CharField(db_column='nombrePais', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'paises'


class Personanatural(models.Model):
    idpersonanatural = models.IntegerField(db_column='IdPersonaNatural', primary_key=True)  # Field name made lowercase.
    tipodocumentopersona = models.ForeignKey('Personas', models.DO_NOTHING, db_column='tipoDocumentoPersona')  # Field name made lowercase.
    numerodocumentopersona = models.ForeignKey('Personas', models.DO_NOTHING, db_column='numeroDocumentoPersona')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'personanatural'


class Personas(models.Model):
    tipodocumentopersona = models.CharField(db_column='tipoDocumentoPersona', primary_key=True, max_length=70)  # Field name made lowercase.
    numerodocumentopersona = models.IntegerField(db_column='numeroDocumentoPersona')  # Field name made lowercase.
    nombrespersona = models.CharField(db_column='nombresPersona', max_length=70)  # Field name made lowercase.
    apellidospersona = models.CharField(db_column='apellidosPersona', max_length=70)  # Field name made lowercase.
    fechanacimientopersona = models.DateField(db_column='fechaNacimientoPersona', blank=True, null=True)  # Field name made lowercase.
    direccionpersona = models.CharField(db_column='direccionPersona', max_length=70, blank=True, null=True)  # Field name made lowercase.
    generopersona = models.CharField(db_column='generoPersona', max_length=70, blank=True, null=True)  # Field name made lowercase.
    lugarexpedicioncedulapersona = models.IntegerField(db_column='lugarExpedicionCedulaPersona', blank=True, null=True)  # Field name made lowercase.
    contrasenapersona = models.CharField(db_column='contrasenaPersona', max_length=70, blank=True, null=True)  # Field name made lowercase.
    codigociudad = models.ForeignKey(Ciudades, models.DO_NOTHING, db_column='codigoCiudad')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'personas'
        unique_together = (('tipodocumentopersona', 'numerodocumentopersona'),)
