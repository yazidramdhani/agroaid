package com.bangkit.agroaid.data.remote.response

import com.google.gson.annotations.SerializedName

data class LoginResponse(
	@field:SerializedName("message")
	val message: String,

	@field:SerializedName("user")
	val user: LoginResult,
)

data class LoginResult(
	@field:SerializedName("fullname")
	val fullName: String,

	@field:SerializedName("userId")
	val userId: String,

	@field:SerializedName("email")
	val email: String,

	@field:SerializedName("username")
	val userName: String,

	@field:SerializedName("token")
	val token: String
)
