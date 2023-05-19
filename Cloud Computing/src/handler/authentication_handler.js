const loginHandler = (request, h) => {
  const response = h.response({
      status: 'success',
      message: 'berhasil terconnect'
  });
  response.code(200);
  return response;
};

const logoutHandler = (request, h) => {
  const response = h.response({
      status: 'success',
      message: 'berhasil terconnect'
  });
  response.code(200);
  return response;
};

module.exports = {
  loginHandler,
  logoutHandler
};
  