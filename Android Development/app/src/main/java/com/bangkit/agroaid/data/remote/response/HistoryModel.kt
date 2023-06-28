package com.bangkit.agroaid.data.remote.response

import android.os.Parcelable
import kotlinx.parcelize.Parcelize

@Parcelize
data class PredictionHistory(
    val photoUrl: String,
    val symptom: String,
    val disease: String,
    val solution: String,
    val prediction : String,
    val cause : String,
    val medicine : String,
    val predictionId : String,
    val userId : String
) : Parcelable

data class HistoryResponse(
    val error: Boolean,
    val message: String,
    val listHistory: List<PredictionHistory>?
)