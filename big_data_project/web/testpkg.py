import pyspark.sql.functions as fun

class testpkg( ):

	def __init__( self, spark ):
		self.spark = spark
		self.books = self.spark.read.parquet( "static/data/metaClean.parquet" );
		self.totalBooks = self.books.count( )
		self.reviews = self.spark.read.parquet( "static/data/reviClean.parquet" );
		self.totalReviews = self.reviews.count( )

	#get the top n books from books
	def getNBooks( self, n ):
		return self.books.head( n )

	#get the top n reviews from reviews
	def getNReviews( self, n ):
		return self.reviews.head( n )



	#get n random books from books, by saying that n^2 of all is needed,
	#we actually significantly improve the chances there are atleast n books
	def getNRanBooks( self, n ):
		#return self.books.rdd.takeSample( False, 5 )
		return self.books.sample( False, ( 1.0 * n ** 2 ) / self.totalBooks ).head( 5 )

	#get search results after applying filters
	# 0:title, 1:description, 2:lower than, 3:greater than, 4:better sales rank
	def getFilterResults( self, filters ):
		print( self.books.columns )
		proba = self.books
		if filters[ 0 ] != '':
			filters[ 0 ].lower( )
			parts = filters[ 0 ].split( ',' )
			for part in parts:
				proba = proba.filter( fun.lower( proba.title ).contains( part ) )
		if filters[ 1 ] != '':
			filters[ 1 ].lower( )
			parts = filters[ 1 ].split( ',' )
			for part in parts:
				proba = proba.filter( fun.lower( proba.title ).contains( part ) )
		if filters[ 2 ] != '':
			proba = proba.filter( proba.price < filters[ 2 ] )
		if filters[ 3 ] != '':
			proba = proba.filter( proba.price > filters[ 3 ] )
		if filters[ 4 ] != '':
			proba = proba.filter( proba.bookSalesRank < filters[ 4 ] )
		print( filters )
		return proba.head( 5 )

	#get recommendation based on ratings
	def getRecommendations( self, names, ratings ):
		self.reviewerid = {}
		self.asinNum = {}
		self.split = self.reviews.select('reviewerID','asin','overall')
		r1,r2,r3,r4,r5,r6,r7,r8,r9,r10 = self.split.randomSplit([0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1])
		self.splits = [r1,r2,r3,r4,r5,r6,r7,r8,r9,r10]
		self.k = 1
		self.reviews2 = []
		for i in self.splits:
    			for x in i.head(i.count()):
        			self.reviewerid[x[0]] = self.k
        			self.asinNum[x[1]] = self.k
        			self.k+=1
		self.reviews2 = []
		self.id = list(self.reviewerid.items())
		for i in self.splits:
    			for x in i.head(i.count()):
        			self.reviews2.append((self.reviewerid[x[0]],self.asinNum[x[1]],x[2]))
		for i in range(len(names)):
    			self.reviews2.append((self.id[-1][1] + 1,self.books.filter(self.books.title==names[i]).head()[0],ratings[i]))
		self.reviewsF = spark.createDataFrame(reviews2,('reviewerID','asin','overall'))
		self.model = ALS.train(self.reviewsF,rank=5,numIterations=5)
		for i in names:
    			self.books.filter(self.books.title==i).head()[0]
			self.results = model.recommendProducts(self.id[-1][1] + 1,5)
			self.recommendations = []
		for i in range(len(results)):
   			for key, value in asinNum.items(): 
        			if results[i][1] == value: 
           				 self.recommendations.append(key)
		return self.recommendations

















