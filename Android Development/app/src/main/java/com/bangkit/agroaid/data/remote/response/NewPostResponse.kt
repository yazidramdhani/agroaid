package com.bangkit.agroaid.data.remote.response

import com.google.gson.annotations.SerializedName

data class NewPostResponse(

    @field:SerializedName("data")
	val data: Data,

    @field:SerializedName("message")
	val message: String,

    @field:SerializedName("status")
	val status: String
)

data class Data(

	@field:SerializedName("createdAt")
	val createdAt: String,

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
