const homeHandler = (request, h) => {

  const response = h.response({
    status: 'success',
    message: 'berhasil terconnect'
  });
  response.code(200);
  return response;
};

module.exports = {
  homeHandler
};
