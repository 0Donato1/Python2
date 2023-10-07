from builderror import BuildError

class Validator:

    def Check(self, amount:int, limit:int):

            if(limit < amount):

                raise BuildError(amount, limit)

            return True


