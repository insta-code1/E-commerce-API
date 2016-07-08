from rest_framework import serializers

from carts.mixins import TokenMixin

from .models import Order, UserAddress

class FinalizedOrderSerializer(serializers.Serializer):
	order_token = serializers.CharField()
	payment_method_nonce = serializers.CharField()
	order_id = serializers.IntegerField(required=False)
	user_checkout_id = serializers.IntegerField(required=False)

	def validate(self, data):
		order_token = data.get("order_token")
		order_data = self.parse_token(order_token)
		order_id = order_data.get(order_id)
		user_checkout_id = serializers.IntegerField(required=False)

		try:
			order_obj = Order.objects.get(id=order_, user__id=user_checkout_id)
			data["order_id"] = order_id
			data["user_checkout_id"] = user_checkout_id
		except:
			raise serializers.ValidationError("This is not a valid order for this user.")

		payment_method_nonce = data.get("payment_method_nonce")
		if payment_method_nonce == None:
			raise serializers.ValidationError("This is not a valid payment method nonce.")
		return data
	

class OrderDetailSerializer(serializers.ModelSerializer):
	url = serializers.HyperlinkedIdentityField(view_name="order_detial_api")
	subtotal = serializers.SerializerMethodField()
	class Meta:
		model = Order
		fields = [
			'url',
			'order_id'
			'user',
			'shipping_address',
			'billing_address',
			'shipping_total_price',
			'subtotal',
			'order_total',
		]

	def get_subtotal(self, obj):
		return obj.cart.subtotal


class UserAddressSerializer(serializers.ModelSerializer):
	class Meta:
		model = UserAddress
		fields = [
			'id',
			'user',
			'type',
			'street',
			'city',
			'state',
			'zipcode',
		]