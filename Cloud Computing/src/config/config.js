require('dotenv').config();

module.exports = {
    "development": {
        "username": "root",
        "password": null,
        "database": "agroaid_db",
        "host": "localhost",
        "dialect": "mysql"
    },
    "test": {
        "username": "",
        "password": null,
        "database": "",
        "host": "",
        "dialect": "mysql"
    },
    "production": {
        "username": process.env.MYSQL_USER,
        "password": process.env.MYSQL_PASSWORD,
        "database": process.env.MYSQL_DATABASE,
        "host": process.env.DB_HOST,
        "dialect": "mysql"
    }
}
  