package com.bangkit.agroaid.ui.auth

import androidx.lifecycle.LiveData
import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import com.bangkit.agroaid.data.local.UserData
import com.bangkit.agroaid.data.remote.response.LoginResult
import com.bangkit.agroaid.repository.AuthRepository
import kotlinx.coroutines.launch

class LoginViewModel(private val authRepository: AuthRepository): ViewModel() {
    val loginResult: LiveData<LoginResult> = authRepository.loginResult
    val loadingValidation : LiveData<Boolean> = authRepository.loadingValidation
    val msgError: LiveData<String> = authRepository.msgError

    fun loginSession(userEmail: String, userPassword: String) {
        authRepository.userLogin(userEmail, userPassword)
    }

    fun userSave(userData: UserData) {
        viewModelScope.launch {
            authRepository.saveUser(userData)
        }
    }
}