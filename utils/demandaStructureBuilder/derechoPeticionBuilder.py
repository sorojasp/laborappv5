from .demandaBuilderDemanda import DemanadaBuilderDemanda


class DerechoPeticionBuilder(DemanadaBuilderDemanda):

    nombre_demandante:str
    apellido_demandante:str
    tipo_documento_demandante:str
    lugar_expedicion_documento_demandante:str
    documento_demandante:str
    nombre_empresa:str
    tipo_documento_empresa:str
    documento_empresa:str
    ciudad_empresa:str
    lugar_resisdencia_demandante:str
    header:str
    summary:str
    allText:str

    def __init__(self,nombre_demandante:str,
                 apellido_demandante:str,
                 tipo_documento_demandante:str,
                 lugar_expedicion_documento_demandante:str,
                 documento_demandante:str,
                 nombre_empresa:str,
                 tipo_documento_empresa:str,
                 documento_empresa:str,
                 ciudad_empresa:str,
                 lugar_resisdencia_demandante):
        DemanadaBuilderDemanda.__init__(self, nombre_demandante,
                                        apellido_demandante,
                                        tipo_documento_demandante,
                                        lugar_expedicion_documento_demandante,
                                        documento_demandante,
                                        nombre_empresa,
                                        tipo_documento_empresa,
                                        documento_empresa,
                                        ciudad_empresa,
                                        lugar_resisdencia_demandante )
    def build_header(self)->str:
        self.header = f"""\



        Señores.
        {self.nombre_empresa}
        {self.lugar_resisdencia_demandante}



"""
        return self.header


derechoBuilder=DerechoPeticionBuilder("Stiven Orlando", "Rojas P", "CC", "Bogotá", "80.865.137","Uniempresarial", "NIT","7897HGJHG","Bogotá","Bogotá")
print(derechoBuilder.build_header())
