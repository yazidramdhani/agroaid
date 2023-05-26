const {User} = require("../models")

const homeHandler = async (request, h) => {
  const userCreated = await User.create({ name:"farrel-test"})
  const user = await User.findAll({where : { uuid: userCreated.dataValues.uuid}})
  const response = h.response({
    status: 'success',
    message: user
  });
  response.code(200);
  return response;
};

module.exports = {
  homeHandler
};
