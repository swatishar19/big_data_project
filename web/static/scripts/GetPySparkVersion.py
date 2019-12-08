from pyspark import SparkContext

class GetPySparkVersion( ):

	def __init__( self ):
		self.three = 3

	def PySparkVersion( self ):
		sc = SparkContext( "local", "five" )
		return sc.version
