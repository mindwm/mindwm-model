from neo4j import GraphDatabase
from neomodel import config

class Neo4j:
    __init__(self, url, username, password):
        config.DRIVER = GraphDatabase().driver(url, auth=(username, password))
        self.driver = config.DRIVER
