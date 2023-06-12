const Hapi = require('@hapi/hapi');
const routes = require('./routes');
const db = require("./models")
const {User} = require("./models");

const JWT_SECRET = process.env.JWT_SECRET;

const init = async () => {
  const server = Hapi.server({
    port: 9000,
    host: process.env.NODE_ENV !== 'production' ? 'localhost' : '0.0.0.0',
    routes: {
      cors: {
        origin: ['*'],
      },
    },
  });

  server.register(require('hapi-auth-jwt2'));

  await server.auth.strategy('jwt', 'jwt', {
    key: JWT_SECRET,
    verifyOptions: { algorithms: ['HS256'] },
    validate: async (decoded, request) => {
      const userId = decoded.userId
      const existingUser = await User.findOne({ where: { userId } });
      if (!existingUser) {
          return { isValid: false };
      }
      return { isValid: true, credentials: decoded };
    },
  });

  server.auth.default('jwt');

  server.route(routes);

  await server.start();
  console.log(`Server berjalan pada ${server.info.uri}`);
};

db.sequelize
  .sync({ force: true })
  .then(() => {
    init();
  })
