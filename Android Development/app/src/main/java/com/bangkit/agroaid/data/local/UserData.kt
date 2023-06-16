package com.bangkit.agroaid.data.local

import android.os.Parcelable
import kotlinx.parcelize.Parcelize

@Parcelize
data class UserData(
    val fullName: String,
    val userId: String,
    val userName: String,
    val userToken: String
): Parcelable