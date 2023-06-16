package com.bangkit.agroaid.ui.adapter

import android.view.LayoutInflater
import android.view.ViewGroup
import androidx.recyclerview.widget.DiffUtil
import androidx.recyclerview.widget.ListAdapter
import androidx.recyclerview.widget.RecyclerView
import coil.load
import com.bangkit.agroaid.data.remote.response.PredictionHistory
import com.bangkit.agroaid.databinding.HistoryItemsBinding

class HistoriesAdapter :
    ListAdapter<PredictionHistory, HistoriesAdapter.MyViewHolder>(CALLBACK) {

    private var clickListener: ((PredictionHistory) -> Unit)? = null


    fun setOnItemClickListener(onClickListener: (PredictionHistory) -> Unit) {
        clickListener = onClickListener
    }

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): MyViewHolder {
        val historyItemsBinding = HistoryItemsBinding.inflate(LayoutInflater.from(parent.context), parent, false)
        return MyViewHolder(historyItemsBinding)
    }

    override fun onBindViewHolder(myViewHolder: MyViewHolder, position: Int) {
        val history = getItem(position)
        if (history != null) {
            myViewHolder.bind(history)
            myViewHolder.itemView.setOnClickListener { clickListener?.invoke(history) }
        }
    }

    class MyViewHolder(private val historyItemsBinding: HistoryItemsBinding) :
        RecyclerView.ViewHolder(historyItemsBinding.root) {
        fun bind(predictionHistory: PredictionHistory) {
            historyItemsBinding.ivHistoryItem.load(predictionHistory.photoUrl){
                crossfade(true)
            }
        }
    }

    companion object {
        private val CALLBACK = object : DiffUtil.ItemCallback<PredictionHistory>() {
            override fun areItemsTheSame(itemOld: PredictionHistory, itemNew: PredictionHistory): Boolean {
                return itemOld == itemNew
            }

            override fun areContentsTheSame(itemOld: PredictionHistory, itemNew: PredictionHistory): Boolean {
                return itemOld.predictionId == itemNew.predictionId
            }
        }
    }
}