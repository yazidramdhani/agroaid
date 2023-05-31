const {Comment} = require("../models")

const addComment = async (request, h) => {
  const { content } = request.payload;
  const { postId } = request.params;
  const { userId } = request.auth.credentials;
  const comment = await Comment.create({content: content, userId: userId, postId: postId})

  const response = h.response({
      status: 'success',
      message: 'Comment created successfully',
      data: comment
  });
  response.code(201);

  return response;
};

const getAllCommentsByPost = async (request, h) => {
    const { postId } = request.params;
    const comments = await Comment.findAll({where: { postId : postId}})
    
    const response = h.response({
        status: 'success',
        message: 'Comments retrieved successfully',
        data: comments
    });
    response.code(200);

    return response;
};

module.exports = {
  addComment,
  getAllCommentsByPost
};
