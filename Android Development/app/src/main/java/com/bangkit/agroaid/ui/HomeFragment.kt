package com.bangkit.agroaid.ui

import android.content.Intent
import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.Toast
import androidx.fragment.app.Fragment
import androidx.lifecycle.ViewModelProvider
import androidx.recyclerview.widget.LinearLayoutManager
import com.bangkit.agroaid.R
import com.bangkit.agroaid.data.remote.response.PredictionHistory
import com.bangkit.agroaid.databinding.HomeFragmentBinding
import com.bangkit.agroaid.helper.HistoryViewModelFactory
import com.bangkit.agroaid.helper.Status
import com.bangkit.agroaid.ui.adapter.HistoriesAdapter
import com.bangkit.agroaid.ui.auth.LoginActivity
import kotlinx.coroutines.CoroutineScope
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.launch
import android.util.Log


class HomeFragment : Fragment(R.layout.home_fragment) {
    private var _binding: HomeFragmentBinding? = null
    private val binding get() = _binding!!
    private lateinit var historyViewModel: HistoryViewModel
    private val historiesAdapter = HistoriesAdapter()

    override fun onCreateView(inflater: LayoutInflater, container: ViewGroup?, savedInstanceState: Bundle?): View? {
        _binding = HomeFragmentBinding.inflate(inflater, container, false)
        return binding.root
    }

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)

        binding.rvHistory.layoutManager = LinearLayoutManager(requireContext())
        binding.rvHistory.adapter = historiesAdapter
        observerView()
    }

    private fun observerView() {
        historyViewModel = ViewModelProvider(
            this,
            HistoryViewModelFactory.getInstanceHistory(requireContext())
        )[HistoryViewModel::class.java]
        
        historyViewModel.getSessionUser().observe(this) { data ->
            if (data.userToken != "") {
                binding.tvGreetings.text = buildString {
                    append("Hi, ")
                    append(data.fullName)
                }
                binding.btnLogout.setOnClickListener {
                    CoroutineScope(Dispatchers.Main).launch {
                        historyViewModel.clearSessionUser()
                        Toast.makeText(requireContext(), "Logged out", Toast.LENGTH_SHORT).show()
                        val intentToLoginActivity = Intent(requireContext(), LoginActivity::class.java)
                        intentToLoginActivity.flags = Intent.FLAG_ACTIVITY_CLEAR_TASK or Intent.FLAG_ACTIVITY_NEW_TASK
                        startActivity(intentToLoginActivity)
                        requireActivity().finish()
                    }
                }
                historyViewModel.getHistoryData("Bearer ${data.userToken}").observe(this) { history ->
                    if (history != null) {
                        when (history) {
                            is Status.LoadingStatus -> {
                                binding.pbRvHistory.visibility = View.VISIBLE
                            }
                            is Status.SuccessStatus -> {
                                binding.pbRvHistory.visibility = View.GONE
                                val listHistoryUser = ArrayList<PredictionHistory>()
                                for (history in history.dataresponse) {
                                    val histories =
                                        PredictionHistory(
                                            history.photoUrl,
                                            history.symptom,
                                            history.disease,
                                            history.solution,
                                            history.prediction,
                                            history.cause,
                                            history.medicine,
                                            history.predictionId,
                                            history.userId
                                        )
                                    listHistoryUser.add(histories)
                                }
                                historiesAdapter.submitList(listHistoryUser)
                                historiesAdapter.setOnItemClickListener { detailHistory ->
                                    Intent(requireContext(), PredictionDetailActivity::class.java).also {
                                        it.putExtra(PredictionDetailActivity.HISTORY_DETAIL, detailHistory)
                                        startActivity(it)
                                    }
                                }
                            }
                            is Status.ErrorStatus -> {
                                binding.pbRvHistory.visibility = View.GONE
                                Toast.makeText(
                                    requireContext(),
                                    history.messageerror,
                                    Toast.LENGTH_SHORT
                                ).show()
                                Log.d("masalahhomefragment", history.messageerror)
                            }
                        }
                    }
                }
            } else {
                val auth = Intent(requireContext(), LoginActivity::class.java)
                startActivity(auth)
                requireActivity().finish()
            }
        }
    }

    override fun onDestroyView() {
        super.onDestroyView()
        _binding = null
    }
}
