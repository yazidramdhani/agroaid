const {Post, User} = require("../models")

const addPost = async (request, h) => {
    const { title, content } = request.payload;
    const { userId } = request.auth.credentials;
    const post = await Post.create({title:title, content: content, userId: userId})

    const response = h.response({
        status: 'success',
        message: 'Post created successfully',
        data: post
    });
    response.code(201);

    return response;
};

const getAllPosts = async (request, h) => {
    const posts = await Post.findAll({ 
        include: {
            model: User,
            attributes: { exclude: ['password'] }
        } 
    })

    const response = h.response({
        status: 'success',
        message: 'Posts retrieved successfully',
        data: posts
    });
    response.code(200);

    return response;
};

const likePost = async (request, h) => {
  const { postId } = request.params;
  const post = await Post.findByPk(postId);
  
  if (!post) {
    return h.response({
      status: 'error',
      message: 'Post not found',
    }).code(404);
  }
  
  post.likes += 1;
  await post.save();
  
  return h.response({
    status: 'success',
    message: 'Post liked successfully',
    data: post,
  }).code(200);
};

module.exports = {
  addPost,
  getAllPosts,
  likePost,
};
