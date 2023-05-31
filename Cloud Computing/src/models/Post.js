module.exports = (sequelize, DataTypes) => {
    const Post = sequelize.define("Post", {
        postId: {
            type: DataTypes.UUID,
            defaultValue: DataTypes.UUIDV4,
            primaryKey: true    
        },
        title: {
            type: DataTypes.STRING,
            allowNull: false
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

    Post.associate = (models) => {
        Post.belongsTo(models.User, { foreignKey: 'userId' });
    }

    return Post;
}