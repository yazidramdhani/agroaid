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
   getAllPosts
} = require('./handler/post_handler');
const { addComment, getAllCommentsByPost } = require('./handler/comment_handler');
const { addReply, getAllRepliesByComment } = require('./handler/reply_handler');

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
      path: '/posts/{postId}/comments',
      handler: addComment,
   },
   {
      method: 'GET',
      path: '/posts/{postId}/comments',
      handler: getAllCommentsByPost,
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
];

module.exports = routes;
