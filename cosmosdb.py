from azure.cosmos import exceptions, CosmosClient, PartitionKey

# Configuração do Cosmos DB
url = "https://<seu_endpoint>.documents.azure.com:443/"
key = "xxxx " #sua chave
client = CosmosClient(url, credential=key)

# Banco de dados e contêiner
database_name = 'CatalogoNetflix'
container_name = 'FilmesSéries'

# Criação do banco e do contêiner (caso ainda não existam)
def create_database_and_container():
    database = client.create_database_if_not_exists(id=database_name)
    container = database.create_container_if_not_exists(
        id=container_name,
        partition_key=PartitionKey(path="/id"),
        offer_throughput=400
    )
    return container
