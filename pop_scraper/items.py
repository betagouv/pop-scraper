# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ItemPalissy(scrapy.Item):
  ACQU = scrapy.Field()
  ADRS = scrapy.Field()
  AFIG = scrapy.Field()
  AIRE = scrapy.Field()
  APPL = scrapy.Field()
  ATEL = scrapy.Field()
  AUTP = scrapy.Field()
  AUTR = scrapy.Field()
  BASE = scrapy.Field()
  BIBL = scrapy.Field()
  CANT = scrapy.Field()
  CATE = scrapy.Field()
  COM = scrapy.Field()
  CONTACT = scrapy.Field()
  CONTIENT_IMAGE = scrapy.Field()
  COOR = scrapy.Field()
  COORM = scrapy.Field()
  COPY = scrapy.Field()
  DATE = scrapy.Field()
  DBOR = scrapy.Field()
  DENO = scrapy.Field()
  DENQ = scrapy.Field()
  DEPL = scrapy.Field()
  DESC = scrapy.Field()
  DIMS = scrapy.Field()
  DMAJ = scrapy.Field()
  DMIS = scrapy.Field()
  DOMN = scrapy.Field()
  DOSADRS = scrapy.Field()
  DOSS = scrapy.Field()
  DOSURL = scrapy.Field()
  DOSURLP = scrapy.Field()
  DOSURLPDF = scrapy.Field()
  DPRO = scrapy.Field()
  DPT = scrapy.Field()
  DPT_LETTRE = scrapy.Field()
  EDIF = scrapy.Field()
  EMPL = scrapy.Field()
  ETAT = scrapy.Field()
  ETUD = scrapy.Field()
  EXEC = scrapy.Field()
  EXPO = scrapy.Field()
  HIST = scrapy.Field()
  # HISTORIQUE = scrapy.Field()
  IDAGR = scrapy.Field()
  IMAGE = scrapy.Field()
  IMG = scrapy.Field()
  IMPL = scrapy.Field()
  INSC = scrapy.Field()
  INSEE = scrapy.Field()
  INTE = scrapy.Field()
  JDAT = scrapy.Field()
  LARC = scrapy.Field()
  LIENS = scrapy.Field()
  LIEU = scrapy.Field()
  LINHA = scrapy.Field()
  LMDP = scrapy.Field()
  LOCA = scrapy.Field()
  LREG = scrapy.Field()
  MANQUANT = scrapy.Field()
  MATR = scrapy.Field()
  MEMOIRE_REFS = scrapy.Field()
  MEMOIRE_URLS = scrapy.Field()
  MFICH = scrapy.Field()
  MICR = scrapy.Field()
  MOSA = scrapy.Field()
  NART = scrapy.Field()
  NINV = scrapy.Field()
  NOMS = scrapy.Field()
  NUMA = scrapy.Field()
  NUMP = scrapy.Field()
  OBS = scrapy.Field()
  ORIG = scrapy.Field()
  PAPP = scrapy.Field()
  PARN = scrapy.Field()
  PART = scrapy.Field()
  PDEN = scrapy.Field()
  PDIM = scrapy.Field()
  PERS = scrapy.Field()
  PETA = scrapy.Field()
  PHOTO = scrapy.Field()
  PINS = scrapy.Field()
  PINT = scrapy.Field()
  PLOC = scrapy.Field()
  POP_ARRETE_PROTECTION = scrapy.Field()
  POP_COMMENTAIRES = scrapy.Field()
  POP_CONTIENT_GEOLOCALISATION = scrapy.Field()
  POP_COORDINATES_POLYGON = scrapy.Field()
  POP_COORDONNEES = scrapy.Field()
  POP_DOSSIER_PROTECTION = scrapy.Field()
  POP_DOSSIER_VERT = scrapy.Field()
  POP_FLAGS = scrapy.Field()
  POP_IMPORT = scrapy.Field()
  PPRO = scrapy.Field()
  PRECISION_JURIDIQUE = scrapy.Field()
  PREP = scrapy.Field()
  PRODUCTEUR = scrapy.Field()
  PROT = scrapy.Field()
  REF = scrapy.Field()
  REFA = scrapy.Field()
  REFE = scrapy.Field()
  REFJOC = scrapy.Field()
  REFM = scrapy.Field()
  REFMUS = scrapy.Field()
  REFP = scrapy.Field()
  REG = scrapy.Field()
  RENP = scrapy.Field()
  RENV = scrapy.Field()
  REPR = scrapy.Field()
  SCLD = scrapy.Field()
  SCLE = scrapy.Field()
  SCLX = scrapy.Field()
  SOUR = scrapy.Field()
  STAD = scrapy.Field()
  STAT = scrapy.Field()
  STRU = scrapy.Field()
  THEM = scrapy.Field()
  TICO = scrapy.Field()
  TITR = scrapy.Field()
  TOUT = scrapy.Field()
  VIDEO = scrapy.Field()
  VOLS = scrapy.Field()
  WADRS = scrapy.Field()
  WCOM = scrapy.Field()
  WEB = scrapy.Field()
  WRENV = scrapy.Field()
  ZONE = scrapy.Field()

class ItemMemoire(scrapy.Item):
  ref = scrapy.Field()
  ref_palissy = scrapy.Field()
  name = scrapy.Field()
  copy = scrapy.Field()
  url = scrapy.Field()
  position = scrapy.Field(serializer=int)
