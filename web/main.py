from flask import Flask, render_template, request
from static.scripts.GetThree import GetThree
from static.scripts.GetPySparkVersion import GetPySparkVersion


app = Flask( __name__ )

@app.route( '/' )
def index( ):
	return render_template( 'index.html' )

@app.route( '/search'  )
def search( ):
	return render_template( 'search.html' )

@app.route( '/search_results', methods = [ "POST" ] )
def search_results( ):
	filter = request.form[ 'filter' ]
	return render_template( 'search_results.html', filter = filter )

@app.route( '/recom' )
def recom( ):
	return render_template( 'recom.html' )

@app.route( '/recom_results' )
def recom_results( ):
	results = [ 'a', 'b', 'c', 'd', 'e' ]
	return render_template( 'recom_results.html', results = results )

@app.route( '/three' )
def three( ):
	Get = GetThree( )
	return str( Get.Three( ) )

@app.route( '/version' )
def version( ):
	Get = GetPySparkVersion( )
	return str( Get.PySparkVersion( ) )
	

if __name__ == '__main__':
  app.run( host = '127.0.0.1', port = 8080, debug = True )
