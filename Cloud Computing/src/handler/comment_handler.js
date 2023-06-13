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

const addReply = async (request, h) => {
    const { commentId, content } = request.payload;
    const { userId } = request.auth.credentials;

    const comment = await Comment.findByPk(commentId);
    if (!comment) {
        return h.response({
            status: 'error',
            message: 'Comment not found'
        }).code(404);
    }

    // Create the reply
    const reply = await Comment.create({ postId: comment.postId, userId: userId, content: content, parentId: commentId });

    const response = h.response({
        status: 'success',
        message: 'Reply added successfully',
        data: reply
    });
    response.code(201);

    return response;
};

const getAllRepliesByComment = async (request, h) => {
    const { commentId } = request.params;

    const comment = await Comment.findByPk(commentId, { include: 'comments' });
    if (!comment) {
        return h.response({
            status: 'error',
            message: 'Comment not found'
        }).code(404);
    }

    const replies = comment.comments;

    const response = h.response({
        status: 'success',
        message: 'Replies retrieved successfully',
        data: replies
    });
    response.code(200);

    return response;
};

module.exports = {
  addComment,
  getAllCommentsByPost,
  addReplyToComment,
  getAllRepliesByComment
};
