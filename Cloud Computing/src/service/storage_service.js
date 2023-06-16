const {Storage} = require('@google-cloud/storage');
const fs = require('fs');
const { Readable } = require('stream');

const storage = new Storage({
    projectId: 'agroaid',
    keyFilename: 'storage-admin-key.json',
});

const uploadImageToStorage = async (image, filePath) => {
    const bucket = storage.bucket("agroaid_bucket");
    const file = bucket.file(filePath);
    const stream = file.createWriteStream()

    stream
        .on('finish', () => {
            console.log(`${filePath} uploaded`)
            return filePath
        });
  
    Readable
        .from(image._data)
        .pipe(stream)
        
    // console.log(Readable.from(image._data))
    // console.log(image)
};

module.exports = {
    uploadImageToStorage
};