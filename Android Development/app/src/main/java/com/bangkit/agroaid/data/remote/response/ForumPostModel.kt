package com.bangkit.agroaid.data.remote.response

import android.os.Parcelable
import com.google.gson.annotations.SerializedName
import kotlinx.parcelize.Parcelize

data class ForumResponse(
    @field:SerializedName("data")
	val data: List<ForumPosts>,

    @field:SerializedName("message")
	val message: String,

    @field:SerializedName("status")
	val status: String
)

@Parcelize
data class UserPost(
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
): Parcelable

@Parcelize
data class ForumPosts(
    @field:SerializedName("createdAt")
	val createdAt: String,

    @field:SerializedName("User")
	val user: UserPost,

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
): Parcelable
