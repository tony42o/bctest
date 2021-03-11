def confirm_validity(block, previous_block):

        if previous_block.index + 1 != block.index:

            return False

        elif previous_block.compute_hash != block.previous_hash:

            return False

        elif block.timestamp <= previous_block.timestamp:

            return False

        return True
