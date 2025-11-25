const express = require('express');
const { query } = require('../config/database');
const { authenticate, authorize } = require('../middleware/auth');

const router = express.Router();

// Get user activities
router.get('/activities', authenticate, async (req, res) => {
  try {
    const { limit = 50 } = req.query;
    const userId = req.user.role === 'admin' ? null : req.user.id;

    let sql = 'SELECT * FROM user_activities WHERE 1=1';
    const params = [];
    
    if (userId) {
      sql += ' AND user_id = $1';
      params.push(userId);
    }

    sql += ' ORDER BY created_at DESC LIMIT $' + (params.length + 1);
    params.push(parseInt(limit));

    const result = await query(sql, params);
    res.json({ activities: result.rows });
  } catch (error) {
    console.error('Get activities error:', error);
    res.status(500).json({ error: 'Failed to fetch activities' });
  }
});

// Record analytics metric
router.post('/metrics', authenticate, authorize('admin', 'moderator'), async (req, res) => {
  try {
    const { metric_name, metric_value, metric_data } = req.body;

    const result = await query(
      'INSERT INTO analytics (metric_name, metric_value, metric_data) VALUES ($1, $2, $3) RETURNING *',
      [metric_name, metric_value, JSON.stringify(metric_data || {})]
    );

    res.status(201).json({ metric: result.rows[0] });
  } catch (error) {
    console.error('Record metric error:', error);
    res.status(500).json({ error: 'Failed to record metric' });
  }
});

module.exports = router;

