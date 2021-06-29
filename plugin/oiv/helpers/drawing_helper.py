"""Constants settings for bouwlaag and repressief object drawing"""
import oiv.helpers.constants as PC
#repressief object constants

ROSNAPSYMBOLS = ['32', '47', '148', '150', '152', '301',
                 'Algemeen', 'Voorzichtig', 'Waarschuwing', 'Gevaar']
ROSNAPLAYERS = ["Object terrein", "Isolijnen", "Bereikbaarheid", "Sectoren"]
OBJECTTYPES = ['Evenement', 'Gebouw', 'Natuur', 'Waterongeval']

#bouwlaag constants
BLSNAPLAYERS = [PC.PAND["bouwlaaglayername"], "Bouwkundige veiligheidsvoorzieningen", "Ruimten"]
BLSNAPSYMBOLS = ['1', '10', '32', '47', '148', '149', '150', '151', '152', '701', '702', '703', '704',
                 '1011', 'Algemeen', 'Voorzichtig', 'Waarschuwing', 'Gevaar']
