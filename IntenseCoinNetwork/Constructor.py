class BlockChain(object):

    def __init__(self):

        self.chain = []

        self.current_data = []

        self.nodes = set()

        self.build_genesis()
