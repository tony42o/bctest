def build_genesis(self):

        self.build_block(proof_number=0, previous_hash=0)

 def build_block(self, proof_number, previous_hash):

        block = Block(

            index=len(self.chain),

            proof_number=proof_number,

            previous_hash=previous_hash,

            data=self.current_data

        )

        self.current_data = []  

        self.chain.append(block)

        return block
