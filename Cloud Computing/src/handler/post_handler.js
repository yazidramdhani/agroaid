const {Post} = require("../models")

const addPost = async (request, h) => {
    const { title, content } = request.payload;
    const { userId } = request.auth.credentials;
    const post = await Post.create({title:title, content: content, userId: userId})
    // const data = { post:post.dataValues , test: {test1:"aa", test2:"bb"}}

    const response = h.response({
        status: 'success',
        message: 'Post created successfully',
        data: post
    });
    response.code(201);

    return response;
};

const getAllPosts = async (request, h) => {
    posts = await Post.findAll()

    const response = h.response({
        status: 'success',
        message: 'Posts retrieved successfully',
        data: posts
    });
    response.code(200);

    return response;
};

module.exports = {
    addPost,
    getAllPosts
};