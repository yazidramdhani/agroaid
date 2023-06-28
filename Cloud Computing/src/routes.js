const {
   homeHandler
} = require('./handler/home_handler');

const {
   signupHandler,
   loginHandler,
   logoutHandler
} = require('./handler/authentication_handler');

const {
   addPost,
   getAllPosts,
   likePost,
   unlikePost
} = require('./handler/post_handler');
const { addComment, getAllCommentsByPost, likeComment, unlikeComment  } = require('./handler/comment_handler');
const { addReply, getAllRepliesByComment, likeReply, unlikeReply } = require('./handler/reply_handler');
const { predictImage, getAllPredictions } = require('./handler/prediction_handler');

const routes = [
   {
      method: 'GET',
      path: '/',
      options: {
         auth: false,
         handler: homeHandler,
      }
   },
   {
      method: 'POST',
      path: '/signup',
      options: {
         auth: false,
         handler: signupHandler,
      }
   },
   {
      method: 'POST',
      path: '/login',
      options: {
         auth: false,
         handler: loginHandler,
      }
   },
   {
      method: 'GET',
      path: '/logout',
      handler: logoutHandler,
   },
   {
      method: 'POST',
      path: '/posts',
      handler: addPost,
   },
   {
      method: 'GET',
      path: '/posts',
      handler: getAllPosts,
   },
   {
      method: 'POST',
      path: '/posts/{postId}/like',
      handler: likePost,
   },
   {
      method: 'POST',
      path: '/posts/{postId}/unlike',
      handler: unlikePost,
   },
   {
      method: 'POST',
      path: '/posts/{postId}/comments',
      handler: addComment,
   },
   {
      method: 'GET',
      path: '/posts/{postId}/comments',
      handler: getAllCommentsByPost,
   },
   {
      method: "POST",
      path: "/comments/{commentId}/like",
      handler: likeComment,
   },
   {
      method: "POST",
      path: "/comments/{commentId}/unlike",
      handler: unlikeComment,
   },
   {
      method: 'POST',
      path: '/comments/{commentId}/replies',
      handler: addReply,
   },
   {
      method: 'GET',
      path: '/comments/{commentId}/replies',
      handler: getAllRepliesByComment,
   },
   {
      method: "POST",
      path: "/replies/{replyId}/like",
      handler: likeReply,
   },
   {
      method: "POST",
      path: "/replies/{replyId}/unlike",
      handler: unlikeReply,
   },
   {
      method: 'POST',
      path: '/predict',
      handler: predictImage,
      options: {
          payload: {
              output: 'stream',
              parse: true,
              allow: 'multipart/form-data',
              multipart: true
          }
      }
   },
   {
      method: 'GET',
      path: '/predictions',
      handler: getAllPredictions,
   },
];

module.exports = routes;
