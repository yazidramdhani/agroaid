module.exports = (sequelize, DataTypes) => {
    const User = sequelize.define("User", {
        uuid: {
            type: DataTypes.STRING,
            allowNull: false,
        },
        name: {
            type: DataTypes.STRING,
            allowNull: true,
        }
    });

    return User;
}