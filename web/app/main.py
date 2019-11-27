from flask import Flask, render_template

app = Flask( __name__ )

@app.route( '/' )
def index( ):
	return render_template( 'index.html' )
		#weather.html',
		#data = [ 
		#	{ 'name' : 'Toronto' },
		#	{ 'name' : 'Montreal' },
		#	{ 'name' : 'Calgary' },
		#	{ 'name' : 'Ottawa' },
		#	{ 'name' : 'Edmonton' },
		#	{ 'name' : 'Mississauga' },
		#	{ 'name' : 'Winnipeg' },
		#	{ 'name' : 'Vancouver' },
		#	{ 'name' : 'Brampton' },
		#	{ 'name' : 'Quebec' }
		#]
	#)

@app.route( '/example' )
def example( ):
	return render_template( 'example.html' )

@app.route( '/extend' )
def extend( ):
	return render_template( 'extend.html' )

if __name__ == '__main__':
  app.run( debug = True, host = '0.0.0.0.' )
