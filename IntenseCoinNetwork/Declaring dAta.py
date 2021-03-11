def get_data(self, sender, receiver, amount):

        self.current_data.append({

            'sender': sender,

            'receiver': receiver,

            'amount': amount

        })

        return True
