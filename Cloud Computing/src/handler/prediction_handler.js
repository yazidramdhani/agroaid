const axios = require('axios');
const FormData = require('form-data');
const { v4: uuidv4 } = require('uuid');
const { Prediction } = require("../models");
const { uploadImageToStorage } = require('../service/storage_service');

const machineLearningUrl = "http://34.128.87.160:5000"

const predictImage = async (request, h) => {
    const { image } = request.payload;
    const { type } = request.query;
    const { userId } = request.auth.credentials;
  
    const form = new FormData();
    form.append('image', image, {...image.hapi});

    try {
        const responseMl = await axios.post(`${machineLearningUrl}/predict-${type}`, form, {
            headers: {
                ...form.getHeaders(),
            },
        });
    
        let filePath = 'prediction/' + uuidv4() + '-' + image.hapi.filename
        await uploadImageToStorage(image, filePath)

        const prediction = await Prediction.create({
            ...responseMl.data,
            photoUrl : `https://storage.googleapis.com/agroaid_bucket/${filePath.replaceAll(" ", "%20")}`,
            userId: userId
        });

        const response = h.response({
            status: 'success',
            message: 'Disease predicted successfully',
            data: prediction
        });
        response.code(201);
  
        return response;

    } catch (error) {
        console.error(error);
        return h.response('Error occurred').code(500);
    }
};

const getAllPredictions = async (request, h) => {
    const { userId } = request.auth.credentials;
    const predictions = await Prediction.findAll({where: { userId : userId}})

    const response = h.response({
        status: 'success',
        message: 'Predictions retrieved successfully',
        data: predictions
    });
    response.code(200);

    return response;
}

module.exports = {
    predictImage,
    getAllPredictions,
};