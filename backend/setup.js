const bcrypt = require('bcryptjs');
const fs = require('fs');
const path = require('path');

// Generate password hash for admin
const adminPassword = 'admin123';
bcrypt.hash(adminPassword, 10, (err, hash) => {
  if (err) {
    console.error('Error generating hash:', err);
    return;
  }
  
  console.log('\n=== Battle.net Backend Setup ===\n');
  console.log('Admin credentials:');
  console.log('  Email: admin@battlenet.com');
  console.log('  Password: admin123');
  console.log('\nPassword hash (for database):');
  console.log(hash);
  console.log('\n=== Next Steps ===\n');
  console.log('1. Create .env file in backend/ directory with:');
  console.log('   PORT=3000');
  console.log('   NODE_ENV=development');
  console.log('   DB_HOST=localhost');
  console.log('   DB_PORT=5432');
  console.log('   DB_NAME=battlenet_db');
  console.log('   DB_USER=postgres');
  console.log('   DB_PASSWORD=your_postgres_password');
  console.log('   JWT_SECRET=your-secret-key-here');
  console.log('   JWT_EXPIRE=7d');
  console.log('\n2. Create PostgreSQL database:');
  console.log('   psql -U postgres');
  console.log('   CREATE DATABASE battlenet_db;');
  console.log('   \\q');
  console.log('\n3. Run database initialization:');
  console.log('   psql -U postgres -d battlenet_db -f scripts/init-db.sql');
  console.log('\n4. Update the admin password hash in init-db.sql with the hash above');
  console.log('\n5. Start the server:');
  console.log('   npm run dev\n');
});

