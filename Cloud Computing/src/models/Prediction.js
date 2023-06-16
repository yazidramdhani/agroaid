module.exports = (sequelize, DataTypes) => {
    const Prediction = sequelize.define("Prediction", {
        predictionId: {
            type: DataTypes.UUID,
            defaultValue: DataTypes.UUIDV4,
            primaryKey: true    
        },
        prediction: {
            type: DataTypes.TEXT,
            allowNull: true
        },
        disease: {
            type: DataTypes.TEXT,
            allowNull: true
        },
        cause: {
            type: DataTypes.TEXT,
            allowNull: true
        },
        symptom: {
            type: DataTypes.TEXT,
            allowNull: true
        },
        solution: {
            type: DataTypes.TEXT,
            allowNull: true
        },
        medicine: {
            type: DataTypes.TEXT,
            allowNull: true
        },
        photoUrl: {
            type: DataTypes.TEXT,
            allowNull: true
        },
    });
 
    Prediction.associate = (models) => {
        Prediction.belongsTo(models.User, { foreignKey: 'userId' });
    };

    return Prediction;
}