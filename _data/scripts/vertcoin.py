from coinscrapper import CoinScrapper

class Vertcoin(CoinScrapper):

    def __init__ (self, driver):
        self.name = 'vertcoin'
        self.driver = driver
        self.symbol = 'vtc'

    def get_public_nodes(self):
        return self.cryptoid_api_nodes()
        
    def get_wealth_distribution(self):
        return self.cryptoid_api_wealth_distribution()

    def get_client_codebases(self):
        return self.cryptoid_api_node_types() 

    def get_consensus_distribution(self):
        return self.chains_consensus_scrape()
