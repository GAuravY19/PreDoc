from predoc_app.routes import app

if __name__ == "__main__":
    # app.run(debug = False, host='0.0.0.0')
    # app.run(debug=True)
    app.run(host='0.0.0.0', port=5000, debug=True)

