module.exports = (sequelize, DataTypes) => {
    const User = sequelize.define("User", {
        uuid: {
            type: DataTypes.UUID,
            defaultValue: DataTypes.UUIDV4,
            primaryKey: true    
        },
        name: {
            type: DataTypes.STRING,
            allowNull: false
        }
    });

    return User;
}