package com.bangkit.agroaid.ui.auth

import android.animation.AnimatorSet
import android.animation.ObjectAnimator
import android.content.Intent
import android.os.Build
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.text.Editable
import android.text.TextWatcher
import android.view.View
import android.view.WindowInsets
import android.view.WindowManager
import android.widget.Toast
import androidx.core.content.ContextCompat
import androidx.lifecycle.ViewModelProvider
import com.bangkit.agroaid.R
import com.bangkit.agroaid.data.local.UserData
import com.bangkit.agroaid.data.remote.response.LoginResponse
import com.bangkit.agroaid.databinding.ActivityLoginBinding
import com.bangkit.agroaid.helper.AuthViewModelFactory
import com.bangkit.agroaid.ui.HomeFragment
import com.bangkit.agroaid.ui.MainActivity


class LoginActivity : AppCompatActivity() {
    private lateinit var activityLoginBinding: ActivityLoginBinding
    private lateinit var loginViewModel: LoginViewModel

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        activityLoginBinding = ActivityLoginBinding.inflate(layoutInflater)
        setContentView(activityLoginBinding.root)
        observeLiveData()
        viewSetUp()
        actionView()
        customButton()
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


    private fun observeLiveData() {
        loginViewModel = ViewModelProvider(this, AuthViewModelFactory.getAuthenticationInstance(this))[LoginViewModel::class.java]

        loginViewModel.loadingValidation.observe(this) {
            loadingView(it)
        }
        loginViewModel.msgError.observe(this) {
            errorView(it)
        }
    }

    private fun customButton() {
        val userPassword  = activityLoginBinding.passLogin.text.toString()
        activityLoginBinding.loginButton.isEnabled = userPassword.length > 7
        if (activityLoginBinding.loginButton.isEnabled == true){
            activityLoginBinding.loginButton.background = ContextCompat.getDrawable(this, R.drawable.button_round)
        } else {
            activityLoginBinding.loginButton.background = ContextCompat.getDrawable(this, R.drawable.button_round_disabled)
        }
    }

    private fun errorView(msgError: String?) {
        Toast.makeText(this, "Email or Password not valid and correct", Toast.LENGTH_SHORT).show()
        Toast.makeText(this, msgError, Toast.LENGTH_SHORT).show()
    }

    private fun loadingView(isLoad: Boolean?) {
        if (isLoad == true) {
            activityLoginBinding.pbLogin.visibility = View.VISIBLE
        } else {
            activityLoginBinding.pbLogin.visibility = View.GONE
        }
    }

    private fun actionView() {

        activityLoginBinding.loginButton.setOnClickListener {
            val userEmail = activityLoginBinding.emailLogin.text.toString()
            val userPassword = activityLoginBinding.passLogin.text.toString()
            when {
                userEmail.isEmpty() -> {
                    activityLoginBinding.emailLogin.error = "Email can't empty"
                }

                userPassword.isEmpty() -> {
                    activityLoginBinding.passLogin.error = "Password can't empty"
                }
                else -> {
                    loginViewModel.loginSession(userEmail, userPassword)
                    loginViewModel.loginResult.observe(this) {
                        loginViewModel.userSave(
                            UserData(fullName = it.fullName, userId = it.userId, userName = it.userName, userToken = it.token)
                        )
                        if (it != null) {
                            val intentToMainActivity = Intent(this@LoginActivity, MainActivity::class.java)
                            intentToMainActivity.flags = Intent.FLAG_ACTIVITY_CLEAR_TASK or Intent.FLAG_ACTIVITY_NEW_TASK
                            startActivity(intentToMainActivity)
                            finish()
                        }
                    }
                }
            }
        }

        activityLoginBinding.footerTwo.setOnClickListener {
            startActivity(Intent(this@LoginActivity, SignupActivity::class.java))
        }

        activityLoginBinding.passLogin.addTextChangedListener(object: TextWatcher {
            override fun beforeTextChanged(s: CharSequence?, srt: Int, cnt: Int, aft: Int) {
                //nothing to do
            }

            override fun onTextChanged(s: CharSequence?, srt: Int, bfr: Int, cnt: Int) {
                customButton()
            }

            override fun afterTextChanged(s: Editable?) {
                //nothing to do
            }

        })
    }
}