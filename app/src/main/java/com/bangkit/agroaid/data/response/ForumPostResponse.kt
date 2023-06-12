package com.bangkit.agroaid.data.response

import com.google.gson.annotations.SerializedName

data class ForumPostResponse(

	@field:SerializedName("data")
	val data: List<DataItem>,

	@field:SerializedName("message")
	val message: String,

	@field:SerializedName("status")
	val status: String
)

data class User(

	@field:SerializedName("createdAt")
	val createdAt: String,

	@field:SerializedName("userId")
	val userId: String,

	@field:SerializedName("email")
	val email: String,

	@field:SerializedName("username")
	val username: String,

	@field:SerializedName("updatedAt")
	val updatedAt: String
)

data class DataItem(

	@field:SerializedName("createdAt")
	val createdAt: String,

	@field:SerializedName("User")
	val user: User,

	@field:SerializedName("postId")
	val postId: String,

	@field:SerializedName("title")
	val title: String,

	@field:SerializedName("userId")
	val userId: String,

	@field:SerializedName("content")
	val content: String,

	@field:SerializedName("likes")
	val likes: Int,

	@field:SerializedName("updatedAt")
	val updatedAt: String
)
