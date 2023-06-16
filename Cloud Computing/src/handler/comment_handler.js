const {Comment, User} = require("../models")

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
    const comments = await Comment.findAll({where: { postId : postId}, 
      include: {
        model: User,
        attributes: { exclude: ['password'] }
      }
    })
    
    const response = h.response({
        status: 'success',
        message: 'Comments retrieved successfully',
        data: comments
    });
    response.code(200);

    return response;
};

const likeComment = async (request, h) => {
  const { commentId } = request.params;
  const comment = await Comment.findByPk(commentId);

  if (!comment) {
    return h
      .response({
        status: "error",
        message: "Comment not found",
      })
      .code(404);
  }

  comment.likes += 1;
  await comment.save();

  return h
    .response({
      status: "success",
      message: "Comment liked successfully",
      data: comment,
    })
    .code(200);
};

const unlikeComment = async (request, h) => {
  const { commentId } = request.params;
  const comment = await Comment.findByPk(commentId);

  if (!comment) {
    return h
      .response({
        status: "error",
        message: "Comment not found",
      })
      .code(404);
  }

  comment.likes -= 1;
  await comment.save();

  return h
    .response({
      status: "success",
      message: "Comment unliked successfully",
      data: comment,
    })
    .code(200);
};

module.exports = {
  addComment,
  getAllCommentsByPost,
  likeComment,
  unlikeComment,
};
