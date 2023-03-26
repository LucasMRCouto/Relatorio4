from database import Database

db = Database(database="loja_de_roupas", collection="vendas")
db.resetDatabase()

def totalB():
    result = db.collection.aggregate ([
        {"$unwind": "$produtos"},
        {"$match": {"cliente_id": "B"}},
        {"$group": {"_id": "$cliente_id", "total": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}},
    ])

    return result

def menosVendido():
    result = db.collection.aggregate([
        {"$unwind": "$produtos"},
        {"$group": {"_id": "$produtos.nome", "qntVendida": {"$sum": "$produtos.quantidade"}}},
        {"$sort": {"qntVendida": 1}},
        {"$limit": 1}
    ])

    return result

def clienteMenosGastou():
    result = db.collection.aggregate([
        {"$unwind": "$produtos"},
        {"$group": {"_id": "$cliente_id", "total": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}},
        {"$sort": {"total": 1}},
        {"$limit": 1}
    ])

    return result

def produtosVendidosMaisQue2():
    result = db.collection.aggregate([
        {"$unwind": "$produtos"},
        {"$match": {"produtos.quantidade": {"$gt": 2}}},
        {"$group": {"_id": "$produtos.nome"}}
    ])

    return result