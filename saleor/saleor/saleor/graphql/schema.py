
import graphene
from saleor.graphql.product.schema import ProductMutations

class Mutation(ProductMutations, graphene.ObjectType):
    # Combine ProductMutations with other mutation classes here as needed
    pass

schema = graphene.Schema(mutation=Mutation)
