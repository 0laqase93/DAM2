package com.example.practica1

import android.content.Intent
import android.net.Uri
import android.os.Bundle
import android.widget.Button
import com.google.android.material.appbar.CollapsingToolbarLayout
import com.google.android.material.floatingactionbutton.FloatingActionButton
import com.google.android.material.snackbar.Snackbar
import androidx.appcompat.app.AppCompatActivity
import com.example.practica1.databinding.ActivityScrollingBinding

class ScrollingActivity : AppCompatActivity() {

    private lateinit var binding: ActivityScrollingBinding

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        binding = ActivityScrollingBinding.inflate(layoutInflater)
        setContentView(binding.root)


        val botonCristiano = findViewById<Button>(R.id.button1)
        val botonIllojuan = findViewById<Button>(R.id.button2)
        val botonFernando = findViewById<Button>(R.id.button3)
        val botonMessi = findViewById<Button>(R.id.button4)

        botonCristiano.setOnClickListener {
            val url = "https://es.wikipedia.org/wiki/Cristiano_Ronaldo"
            val i = Intent(Intent.ACTION_VIEW, Uri.parse(url))
            startActivity(i)
        }

        botonIllojuan.setOnClickListener {
            val url = "https://es.wikipedia.org/wiki/IlloJuan"
            val i = Intent(Intent.ACTION_VIEW, Uri.parse(url))
            startActivity(i)
        }

        botonFernando.setOnClickListener {
            val url = "https://es.wikipedia.org/wiki/Fernando_Alonso"
            val i = Intent(Intent.ACTION_VIEW, Uri.parse(url))
            startActivity(i)
        }

        botonMessi.setOnClickListener {
            val url = "https://es.wikipedia.org/wiki/Lionel_Messi"
            val i = Intent(Intent.ACTION_VIEW, Uri.parse(url))
            startActivity(i)
        }

        /**
         *
        setSupportActionBar(findViewById(R.id.toolbar))
        binding.toolbarLayout.title = title
        binding.fab.setOnClickListener { view ->
            Snackbar.make(view, "Replace with your own action", Snackbar.LENGTH_LONG)
                .setAction("Action", null)
                .setAnchorView(R.id.fab).show()
        }
         */
    }
}