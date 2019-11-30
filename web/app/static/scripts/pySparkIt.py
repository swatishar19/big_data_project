from pyspark import SparkContext

class GiveMe( ):

	def __init__( self ):
		self.three = 3

	def pySparkIt( self ):
		sc = SparkContext( "local", "five" )
		return sc.version
