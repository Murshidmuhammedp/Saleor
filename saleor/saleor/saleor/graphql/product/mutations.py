import graphene
from graphql_jwt.decorators import login_required
from .models import CustomerProductPrice, Product
from saleor.account.models import User

class SetCustomPrice(graphene.Mutation):
    class Arguments:
        product_id = graphene.ID(required=True)
        customer_id = graphene.ID(required=True)
        custom_price = graphene.Decimal(required=True)

    success = graphene.Boolean()
    message = graphene.String()

    @login_required
    def mutate(self, info, product_id, customer_id, custom_price):
        user = info.context.user
        if not user.has_perm("product.manage_products"):  # Permission check
            return SetCustomPrice(success=False, message="Permission denied.")

        product = Product.objects.get(id=product_id)
        customer = User.objects.get(id=customer_id)

        customer_price, created = CustomerProductPrice.objects.update_or_create(
            product=product, customer=customer, defaults={"custom_price": custom_price}
        )

        return SetCustomPrice(success=True, message="Custom price set successfully.")

# Add this mutation to the list of available mutations in the `mutations.py` file
class Mutation(graphene.ObjectType):
    set_custom_price = SetCustomPrice.Field()
