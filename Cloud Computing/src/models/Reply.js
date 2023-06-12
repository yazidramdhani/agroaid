module.exports = (sequelize, DataTypes) => {
    const Reply = sequelize.define("Reply", {
        replyId: {
            type: DataTypes.UUID,
            defaultValue: DataTypes.UUIDV4,
            primaryKey: true    
        },
        content: {
            type: DataTypes.TEXT,
            allowNull: false
        },
        likes: {
            type: DataTypes.INTEGER,
            defaultValue: 0
        },
    });
 
    Reply.associate = (models) => {
        Reply.belongsTo(models.User, { foreignKey: 'userId' });
        Reply.belongsTo(models.Comment, { foreignKey: 'commentId' });
    };

    return Reply;
}