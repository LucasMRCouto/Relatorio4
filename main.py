from save_json import writeAJson
from ProductAnalyser import *

result1 = totalB()
writeAJson(result1, "Total cliente B")

result2 = menosVendido()
writeAJson(result2, "Produto menos vendido")

result3 = clienteMenosGastou()
writeAJson(result3, "Cliente menos gastou")

result4 = produtosVendidosMaisQue2()
writeAJson(result4, "Produtos vendidos mais que 2")