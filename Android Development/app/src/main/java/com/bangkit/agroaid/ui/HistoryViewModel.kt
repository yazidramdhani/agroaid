package com.bangkit.agroaid.ui

import androidx.lifecycle.LiveData
import androidx.lifecycle.ViewModel
import com.bangkit.agroaid.data.local.UserData
import com.bangkit.agroaid.data.remote.response.PredictionHistory
import com.bangkit.agroaid.helper.Status
import com.bangkit.agroaid.repository.AuthRepository
import com.bangkit.agroaid.repository.DataRepository

class HistoryViewModel(private val dataRepository: DataRepository, private val authRepo: AuthRepository) : ViewModel() {
    fun getSessionUser(): LiveData<UserData> {
        return authRepo.getUser()
    }

    suspend fun clearSessionUser() {
        dataRepository.deleteUser()
    }

    fun getHistoryData(userToken : String): LiveData<Status<List<PredictionHistory>>> {
        return dataRepository.getHistory(userToken)
    }
}