// ---------- server.js ----------
require('dotenv').config();           // ① loads DATABASE_URL, PORT, etc.
const express = require('express');
const mysql   = require('mysql2/promise'); // use promise API for async / await
const cors    = require('cors');
const path    = require('path');

const app  = express();
const port = 5500;           // ignore process.env.PORT for now


/* ───────────────  middleware  ─────────────── */
app.use(cors());            // allow front-end to call API from same origin or elsewhere
app.use(express.json());    // built-in JSON body-parser
app.use(express.static(path.join(__dirname, 'public')));

/* ───────────────  database pool  ───────────────
   DATABASE_URL looks like:
   mysql://user:password@host:port/database
*/
const pool = mysql.createPool({
  uri: process.env.DATABASE_URL,
  waitForConnections: true,
  connectionLimit   : 8,
  ssl               : { rejectUnauthorized: true },
});

/* helper so we can simply write await query(sql, params) */
const query = (sql, params = []) => pool.execute(sql, params).then(([rows]) => rows);

/* ───────────────  routes  ─────────────── */

// GET /startups          – all rows, newest first
app.get('/startups', async (_req, res) => {
  try {
    const rows = await query('SELECT * FROM startup ORDER BY id DESC');
    res.json(rows);
  } catch (err) {
    console.error(err);
    res.status(500).json({ error: 'Database error' });
  }
});

// GET /startups/:id      – single row by primary key
app.get('/startups/:id', async (req, res) => {
  try {
    const rows = await query('SELECT * FROM startup WHERE id = ?', [req.params.id]);
    if (!rows.length) return res.status(404).json({ error: 'Not found' });
    res.json(rows[0]);
  } catch (err) {
    console.error(err);
    res.status(500).json({ error: 'Database error' });
  }
});

// POST /startups         – insert a new record
app.post('/startups', async (req, res) => {
  const { startup_name, author, description, prediction = null } = req.body;
  if (!startup_name || !author || !description) {
    return res.status(400).json({ error: 'Missing required fields' });
  }

  try {
    const result = await query(
      'INSERT INTO startup (startup_name, author, description, prediction) VALUES (?, ?, ?, ?)',
      [startup_name, author, description, prediction]
    );
    res.status(201).json({ id: result.insertId, message: 'Startup inserted' });
  } catch (err) {
    console.error(err);
    res.status(500).json({ error: 'Insert failed' });
  }
});


/* ───────────────  start server  ─────────────── */
app.listen(port, () =>
  console.log(`🚀  API & static files running on http://localhost:${port}`)
);
