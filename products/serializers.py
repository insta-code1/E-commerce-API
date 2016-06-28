from rest_framework import serializers


from .models import Category, Product, Variation

class VariationSerializer(serializers.ModelSerializer):
	class Meta:
		model = Variation
		fields = [
			'title',
			'price',
		]



class ProductDetailSerializer(serializers.ModelSerializer):
	variation_set = VariationSerializer(many=True) # (many=True,read_only=True)
	image = serializers.SerializerMethodField()
	class Meta:
		model = Product
		fields = [
			'id',
			'title',
			'image',
			'variation_set',
		]


	def get_image(self, obj):
		return obj.productimage_set.first().image.url  
		# getting the instance of image obj.productimage_set.first() 
		#then method chaining the .image.url


class ProductsSerializer(serializers.ModelSerializer):
	url = serializers.HyperlinkedIdentityField(view_name='products_detail_api')
	variation_set = VariationSerializer(many=True) # (many=True,read_only=True)
	image = serializers.SerializerMethodField()
	class Meta:
		model = Product
		fields = [
			'url',
			'id',
			'title',
			'image',
			'variation_set',
		]

	def get_image(self, obj):
		return obj.productimage_set.first().image.url  
		# getting the instance of image obj.productimage_set.first() 
		#then method chaining the .image.url
		

class CategorySerializer(serializers.ModelSerializer):
	url = serializers.HyperlinkedIdentityField(view_name='category_detail_api')
	product_set = ProductsSerializer(many=True)
	class Meta:
		model = Category
		fields = [
			'url',
			'id',
			'title',
			'description',
			'product_set', 
			#obj.project_set.all()
			#'default_category',
		]
