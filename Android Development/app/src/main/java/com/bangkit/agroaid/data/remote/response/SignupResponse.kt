package com.bangkit.agroaid.data.remote.response

import com.google.gson.annotations.SerializedName

data class SignupResponse(

	@field:SerializedName("message")
	val message: String,

	@field:SerializedName("token")
	val token: String
)
