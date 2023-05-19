const {
  homeHandler
} = require('./handler/home_handler');

const routes = [
  {
    method: 'GET',
    path: '/',
    handler: homeHandler,
  }
];

module.exports = routes;
