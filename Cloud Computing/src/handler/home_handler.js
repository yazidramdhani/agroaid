const homeHandler = (request, h) => {
    const response = h.response({
        status: 'success',
        message: 'Success to connect'
    });
    response.code(200);
    return response;
};

module.exports = {
    homeHandler
};
