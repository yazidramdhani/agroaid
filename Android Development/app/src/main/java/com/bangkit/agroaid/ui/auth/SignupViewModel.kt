package com.bangkit.agroaid.ui.auth

import androidx.lifecycle.LiveData
import androidx.lifecycle.ViewModel
import com.bangkit.agroaid.data.remote.response.SignupResponse
import com.bangkit.agroaid.repository.AuthRepository

class SignupViewModel(private val authRepository: AuthRepository) : ViewModel() {
    val signupResult: LiveData<SignupResponse> = authRepository.signupResponse
    val loadingValidation: LiveData<Boolean> = authRepository.loadingValidation
    val msgError: LiveData<String> = authRepository.msgError
    fun userSignup(fullname: String, username: String, userEmail: String, userPassword: String) {
        authRepository.userSignup(fullname, username, userEmail, userPassword)
    }
}