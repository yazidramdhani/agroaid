const jwt = require('jsonwebtoken');
const bcrypt = require('bcryptjs');
const { User } = require("../models");
require('dotenv').config();

const JWT_SECRET = process.env.JWT_SECRET;

const signupHandler = async (request, h) => {
    try {
        const { username, fullname,  email, password } = request.payload;

        const existingUser = await User.findOne({ where: { email } });
        if (existingUser) {
            return h.response({ message: 'Email already exists' }).code(400);
        }

        const hashedPassword = await bcrypt.hash(password, 10);

        const newUser = await User.create({ username, fullname, email, password: hashedPassword });

        const token = generateToken(newUser.userId, JWT_SECRET, '1d')

        delete newUser.dataValues.password

        newUser.dataValues.token = token

        return h.response({ message: 'Signup successful', token, user: newUser }).code(201);
    } catch (error) {
        console.error(error);
        return h.response({ message: 'Internal server error' }).code(500);
    }
};

const loginHandler = async (request, h) => {
    const { email, password } = request.payload;

    const user = await User.findOne({where: { email }});
    
    if (!user) {
      return h.response({ message: 'User not found' }).code(401);
    }
  
    const isPasswordValid = await bcrypt.compare(password, user.password);
  
    if (!isPasswordValid) {
      return h.response({ message: 'Invalid credentials' }).code(401);
    }
  
    const token = generateToken(user.userId, JWT_SECRET, '1d')
  
    delete user.dataValues.password

    user.dataValues.token = token

    return h.response({ message: 'Login successful', token: token, user: user }).code(200);
};

// TODO: gaperlu server side, cukup hapus token di client side
const logoutHandler = (request, h) => {
    const response = h.response({
        status: 'success',
        message: 'berhasil terconnect'
    });
    response.code(200);
    return response;
};

const generateToken = (userId, JWT_SECRET, expiresIn) => {
    token = jwt.sign({ userId: userId }, JWT_SECRET, { expiresIn: expiresIn });
    return token;
}

module.exports = {
    signupHandler,
    loginHandler,
    logoutHandler
};
  