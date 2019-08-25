import os
from disco import app

if __name__ == "__main__":
    app.run(
        host=app.config["HOST"],
        debug=app.config["DEBUG"],
        port=app.config["PORT"]
    )

