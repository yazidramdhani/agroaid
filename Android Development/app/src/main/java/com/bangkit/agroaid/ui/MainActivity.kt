package com.bangkit.agroaid.ui

import android.content.Intent
import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import androidx.navigation.NavController
import androidx.navigation.Navigation
import androidx.navigation.ui.NavigationUI.setupWithNavController
import com.bangkit.agroaid.R
import com.bangkit.agroaid.databinding.ActivityMainBinding
import com.bangkit.agroaid.helper.HistoryViewModelFactory

class MainActivity : AppCompatActivity() {

    private lateinit var binding: ActivityMainBinding
    private lateinit var navController: NavController

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        binding = ActivityMainBinding.inflate(layoutInflater)
        setContentView(binding.root)

        navController=Navigation.findNavController(this, R.id.nav_host_fragment_main)
        setupWithNavController(binding.bottomNavbar,navController)

        binding.bottomNavbar.background = null
        binding.bottomNavbar.menu.getItem(1).isEnabled = false

        binding.fabCamera.setOnClickListener {
            val predict = Intent(this@MainActivity, PredictActivity::class.java)
            startActivity(predict)
        }
    }
}