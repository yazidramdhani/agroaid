module.exports = (sequelize, DataTypes) => {
    const Comment = sequelize.define("Comment", {
        commentId: {
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

    Comment.associate = (models) => {
        Comment.belongsTo(models.User, { foreignKey: 'userId' });
        Comment.belongsTo(models.Post, { foreignKey: 'postId' });
    };

    return Comment;
}