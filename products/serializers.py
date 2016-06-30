from rest_framework import serializers


from .models import Category, Product, Variation

class VariationSerializer(serializers.ModelSerializer):
	class Meta:
		model = Variation
		fields = [
			'id',
			'title',
			'price',
		]


class ProductDetailUpdateSerializer(serializers.ModelSerializer):
	variation_set = VariationSerializer(many=True, read_only=True) # (many=True,read_only=True)
	image = serializers.SerializerMethodField()
	class Meta:
		model = Product
		fields = [
			'id',
			'title',
			'image',
			'price',
			'description',
			'variation_set',
		]


	def get_image(self, obj):
		try:
			return obj.productimage_set.first().image.url
		except:
			return None  

 	def create(self, validated_data):
	 	title = validated_data["title"]
	 	Product.objects.get(title=title)
	 	product = Product.objects.create(**validated_data)
	 	return product

 	def update(self, instance, validated_data):
	 	title = validated_data["title"]
	 	Product.objects.get(title=title)
	 	instance.title = validated_data["title"]
	 	instance.save()
	 	return instance

# put this in the views to use
# class ProductCreateAPIView(generics.CreateAPIView):
# 	queryset = Product.objects.all()
# 	serializer_class = ProductDetailUpdateSerializer

# and this in the urls
#include in the imports ProductCreateAPIView
#url(r'^api/products/create/$', ProductCreateAPIView.as_view(), name='products_create_api'),



class ProductDetailSerializer(serializers.ModelSerializer):
	variation_set = VariationSerializer(many=True, read_only=True) # (many=True,read_only=True)
	image = serializers.SerializerMethodField()
	class Meta:
		model = Product
		fields = [
			'id',
			'title',
			'image',
			'price',
			'description',
			'variation_set',
		]


	def get_image(self, obj):
		try:
			return obj.productimage_set.first().image.url  
		except:
			return None
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
		try:
			return obj.productimage_set.first().image.url  
		except:
			return None

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
