from flask import Flask, render_template, request
from pyspark import SparkContext
from pyspark.sql import SparkSession
from testpkg import testpkg

#initialize global variables
app = Flask( __name__ )
sc = SparkContext( )
spark = SparkSession( sc )
funspark = testpkg( spark )

#website main hub
@app.route( '/' )
def index( ):
	return render_template( 'index.html' )

#details of all books
@app.route( '/details' )
def details( ):
	return render_template( 'data_analysis.html' )

#detail of one book
@app.route( '/book', methods = [ "POST", "GET" ] )
def book( ):
	bookobj = request.args
	print( bookobj )
	return render_template( 'book_summary.html', book = bookobj )


#searching links
@app.route( '/search'  )
def search( ):
	return render_template( 'search.html' )

@app.route( '/search_results', methods = [ "POST" ] )
def search_results( ):
	filters = request.form.getlist( 'filter' )
	return render_template( 'search_results.html', results = funspark.getFilterResults( filters ) )


#recommendation links
@app.route( '/recom' )
def recom( ):
	return render_template( 'recom.html' )

@app.route( '/recom_reviews' )
def recom_reviews( ):
	return render_template( 'recom_reviews.html', selection = funspark.getNRanBooks( 5 ) )

@app.route( '/recom_results', methods = [ "POST" ] )
def recom_results( ):
	ratings = request.form.getlist( 'rating' )
	titles = request.form.getlist( 'title' )
	return render_template( 'recom_results.html', results = funspark.getRecommendations( titles, ratings ) )
	

if __name__ == '__main__':
	app.run( host = "0.0.0.0", port = 8080, debug = True )
