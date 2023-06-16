const {Reply, User} = require("../models")

const addReply = async (request, h) => {
    const { content } = request.payload;
    const { commentId } = request.params;
    const { userId } = request.auth.credentials;
    const reply = await Reply.create({content: content, userId: userId, commentId: commentId})
  
    const response = h.response({
        status: 'success',
        message: 'Reply created successfully',
        data: reply
    });
    response.code(201);

    return response;
};

const getAllRepliesByComment = async (request, h) => {
    const { commentId } = request.params;
    const replies = await Reply.findAll({where: { commentId : commentId}, 
        include: {
            model: User,
            attributes: { exclude: ['password'] }
        }
    })
    
    const response = h.response({
        status: 'success',
        message: 'Replies retrieved successfully',
        data: replies
    });
    response.code(200);

    return response;
};

const likeReply = async (request, h) => {
  const { replyId } = request.params;
  const reply = await Reply.findByPk(replyId);

  if (!reply) {
    return h
      .response({
        status: "error",
        message: "Reply not found",
      })
      .code(404);
  }

  reply.likes += 1;
  await reply.save();

  return h
    .response({
      status: "success",
      message: "Reply liked successfully",
      data: reply,
    })
    .code(200);
};

const unlikeReply = async (request, h) => {
  const { replyId } = request.params;
  const reply = await Reply.findByPk(replyId);

  if (!reply) {
    return h
      .response({
        status: "error",
        message: "Reply not found",
      })
      .code(404);
  }

  reply.likes -= 1;
  await reply.save();

  return h
    .response({
      status: "success",
      message: "Reply unliked successfully",
      data: reply,
    })
    .code(200);
};

module.exports = {
  addReply,
  getAllRepliesByComment,
  likeReply,
  unlikeReply,
};
