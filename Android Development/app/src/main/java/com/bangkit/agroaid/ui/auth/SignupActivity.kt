package com.bangkit.agroaid.ui.auth

import android.content.Intent
import android.os.Build
import android.os.Bundle
import android.view.View
import android.view.WindowInsets
import android.view.WindowManager
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity
import androidx.lifecycle.ViewModelProvider
import com.bangkit.agroaid.data.remote.response.SignupResponse
import com.bangkit.agroaid.databinding.ActivitySignupBinding
import com.bangkit.agroaid.helper.AuthViewModelFactory


class SignupActivity : AppCompatActivity() {

    private lateinit var activitySignupBinding: ActivitySignupBinding
    private lateinit var signupViewModel : SignupViewModel

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        activitySignupBinding = ActivitySignupBinding.inflate(layoutInflater)
        setContentView(activitySignupBinding.root)

        viewSetUp()
        observerView()
        actionView()
    }

    private fun viewSetUp() {
        @Suppress("DEPRECATION")
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.R) {
            window.insetsController?.hide(WindowInsets.Type.statusBars())
        } else {
            window.setFlags(
                WindowManager.LayoutParams.FLAG_FULLSCREEN,
                WindowManager.LayoutParams.FLAG_FULLSCREEN
            )
        }
        supportActionBar?.hide()
    }


    private fun errorView(msgError: String?) {
        Toast.makeText(this, msgError, Toast.LENGTH_SHORT).show()
    }

    private fun intentMove(signupResponse: SignupResponse?) {
        if (signupResponse != null && (signupResponse.message === "Signup successful")) {
            Toast.makeText(this, signupResponse.message, Toast.LENGTH_SHORT).show()
            startActivity(Intent(this@SignupActivity, LoginActivity::class.java))
        }
    }

    private fun loadingView(isLoading: Boolean?) {
        if (isLoading == true){
            activitySignupBinding.pbSignup.visibility = View.VISIBLE
        } else {
            activitySignupBinding.pbSignup.visibility = View.GONE
        }
    }

    private fun observerView() {
        signupViewModel = ViewModelProvider(this, AuthViewModelFactory.getAuthenticationInstance(this))[SignupViewModel::class.java]

        signupViewModel.loadingValidation.observe(this) {
            loadingView(it)
        }

        signupViewModel.msgError.observe(this) {
            errorView(it)
        }

        signupViewModel.signupResult.observe(this) {
            intentMove(it)
        }
    }

    private fun actionView() {

        activitySignupBinding.footerTwo.setOnClickListener {
            val intentToUserLogin = Intent(this@SignupActivity, LoginActivity::class.java)
            startActivity(intentToUserLogin)
        }

        activitySignupBinding.sendButton.setOnClickListener {
            val fullname = activitySignupBinding.nameSignup.text.toString()
            val username = activitySignupBinding.unameSignup.text.toString()
            val userEmail = activitySignupBinding.emailSignup.text.toString()
            val userPassword = activitySignupBinding.passSignup.text.toString()

            when {
                fullname.isEmpty() -> {
                    activitySignupBinding.nameSignup.error = "Name can't empty"
                }

                username.isEmpty() -> {
                    activitySignupBinding.unameSignup.error = "Name can't empty"
                }

                userEmail.isEmpty() -> {
                    activitySignupBinding.emailSignup.error = "Email can't empty"
                }

                userPassword.isEmpty() -> {
                    activitySignupBinding.passSignup.error = "Password can't empty"
                }

                activitySignupBinding.emailSignup.error != null -> {
                    return@setOnClickListener
                }

                activitySignupBinding.passSignup.error != null -> {
                    return@setOnClickListener
                }

                else -> {
                    signupViewModel.userSignup(fullname, username, userEmail, userPassword)
                }
            }
        }
    }
}