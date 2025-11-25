const express = require('express');
const { query } = require('../config/database');
const { authenticate } = require('../middleware/auth');
const axios = require('axios');

const router = express.Router();

// Python service URL
const PYTHON_SERVICE = process.env.PYTHON_SERVICE_URL || 'http://localhost:5000';

// Get dashboard stats
router.get('/stats', authenticate, async (req, res) => {
  try {
    // Total games
    const gamesResult = await query('SELECT COUNT(*) as total FROM games', []);
    const totalGames = parseInt(gamesResult.rows[0].total);

    // Total users
    const usersResult = await query('SELECT COUNT(*) as total FROM users', []);
    const totalUsers = parseInt(usersResult.rows[0].total);

    // Total revenue (sum of prices)
    const revenueResult = await query(
      'SELECT COALESCE(SUM(price), 0) as total FROM games WHERE is_free = false',
      []
    );
    const totalRevenue = parseFloat(revenueResult.rows[0].total);

    // Games by category
    const categoryResult = await query(
      'SELECT category, COUNT(*) as count FROM games GROUP BY category ORDER BY count DESC',
      []
    );

    // Recent games
    const recentGamesResult = await query(
      'SELECT * FROM games ORDER BY created_at DESC LIMIT 5',
      []
    );

    // Recent users
    const recentUsersResult = await query(
      'SELECT id, username, email, role, created_at FROM users ORDER BY created_at DESC LIMIT 5',
      []
    );

    // User activities (last 24 hours)
    const activitiesResult = await query(
      `SELECT activity_type, COUNT(*) as count 
       FROM user_activities 
       WHERE created_at >= NOW() - INTERVAL '24 hours'
       GROUP BY activity_type`,
      []
    );

    res.json({
      stats: {
        totalGames,
        totalUsers,
        totalRevenue,
        freeGames: await query('SELECT COUNT(*) as total FROM games WHERE is_free = true', []).then(r => parseInt(r.rows[0].total)),
        paidGames: await query('SELECT COUNT(*) as total FROM games WHERE is_free = false', []).then(r => parseInt(r.rows[0].total))
      },
      categories: categoryResult.rows,
      recentGames: recentGamesResult.rows,
      recentUsers: recentUsersResult.rows,
      activities: activitiesResult.rows
    });
  } catch (error) {
    console.error('Dashboard stats error:', error);
    res.status(500).json({ error: 'Failed to fetch dashboard stats' });
  }
});

// Get analytics data for charts
router.get('/analytics', authenticate, async (req, res) => {
  try {
    const { period = '7d' } = req.query;
    
    let dateFilter = "NOW() - INTERVAL '7 days'";
    if (period === '30d') dateFilter = "NOW() - INTERVAL '30 days'";
    if (period === '1y') dateFilter = "NOW() - INTERVAL '1 year'";

    // Games created over time
    const gamesOverTime = await query(
      `SELECT DATE(created_at) as date, COUNT(*) as count 
       FROM games 
       WHERE created_at >= ${dateFilter}
       GROUP BY DATE(created_at) 
       ORDER BY date ASC`,
      []
    );

    // Users registered over time
    const usersOverTime = await query(
      `SELECT DATE(created_at) as date, COUNT(*) as count 
       FROM users 
       WHERE created_at >= ${dateFilter}
       GROUP BY DATE(created_at) 
       ORDER BY date ASC`,
      []
    );

    // Top games by downloads
    const topGames = await query(
      'SELECT title, downloads, rating FROM games ORDER BY downloads DESC LIMIT 10',
      []
    );

    // Revenue over time
    const revenueOverTime = await query(
      `SELECT DATE(created_at) as date, COALESCE(SUM(price), 0) as revenue 
       FROM games 
       WHERE created_at >= ${dateFilter} AND is_free = false
       GROUP BY DATE(created_at) 
       ORDER BY date ASC`,
      []
    );

    res.json({
      gamesOverTime: gamesOverTime.rows,
      usersOverTime: usersOverTime.rows,
      topGames: topGames.rows,
      revenueOverTime: revenueOverTime.rows
    });
  } catch (error) {
    console.error('Analytics error:', error);
    res.status(500).json({ error: 'Failed to fetch analytics' });
  }
});

// Get advanced analytics from Python service
router.get('/analytics/advanced', authenticate, async (req, res) => {
  try {
    const response = await axios.get(`${PYTHON_SERVICE}/api/analytics/advanced`);
    res.json(response.data);
  } catch (error) {
    console.error('Advanced analytics error:', error.message);
    // Fallback to basic analytics if Python service is unavailable
    res.status(500).json({ 
      error: 'Python analytics service unavailable',
      message: 'Falling back to basic analytics'
    });
  }
});

// Get predictions from Python service
router.get('/analytics/predictions', authenticate, async (req, res) => {
  try {
    const response = await axios.get(`${PYTHON_SERVICE}/api/analytics/predictions`);
    res.json(response.data);
  } catch (error) {
    console.error('Predictions error:', error.message);
    res.status(500).json({ error: 'Predictions service unavailable' });
  }
});

module.exports = router;

