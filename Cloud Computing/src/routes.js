const {
  homeHandler
} = require('./handler/home_handler');

const {
  loginHandler,
  logoutHandler
} = require('./handler/authentication_handler');

const routes = [
  {
    method: 'GET',
    path: '/',
    handler: homeHandler,
  },
  {
    method: 'POST',
    path: '/login',
    handler: loginHandler,
  },
  {
    method: 'GET',
    path: '/logout',
    handler: logoutHandler,
  }
];

module.exports = routes;
