package com.bangkit.agroaid.data.remote.response

import android.os.Parcelable
import com.google.gson.annotations.SerializedName
import kotlinx.parcelize.Parcelize

data class PredictResponse(
	@field:SerializedName("data")
	val data: PredictResult,

	@field:SerializedName("message")
	val message: String,

	@field:SerializedName("status")
	val status: String
)

@Parcelize
data class PredictResult(
	@field:SerializedName("photoUrl")
	val photoUrl: String,

	@field:SerializedName("createdAt")
	val createdAt: String,

	@field:SerializedName("symptom")
	val symptom: String,

	@field:SerializedName("disease")
	val disease: String,

	@field:SerializedName("solution")
	val solution: String,

	@field:SerializedName("prediction")
	val prediction: String,

	@field:SerializedName("cause")
	val cause: String,

	@field:SerializedName("medicine")
	val medicine: String,

	@field:SerializedName("predictionId")
	val predictionId: String,

	@field:SerializedName("userId")
	val userId: String
): Parcelable
