import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { AuthService } from '../../services/auth.service';

interface User {
  id: number;
  username: string;
  email: string;
  role: string;
  full_name?: string;
  is_active: boolean;
  created_at: string;
}

@Component({
  selector: 'app-user-list',
  templateUrl: './user-list.component.html',
  styleUrls: ['./user-list.component.scss']
})
export class UserListComponent implements OnInit {
  users: User[] = [];
  loading: boolean = false;
  error: string = '';
  currentUser: any = null;

  constructor(
    private http: HttpClient,
    private authService: AuthService
  ) {}

  ngOnInit(): void {
    this.currentUser = this.authService.getCurrentUser();
    this.loadUsers();
  }

  loadUsers(): void {
    this.loading = true;
    this.error = '';

    const token = this.authService.getToken();
    if (!token) {
      this.error = 'No estás autenticado';
      this.loading = false;
      return;
    }

    this.http.get<{users: User[]}>('http://localhost:3000/api/users', {
      headers: {
        'Authorization': `Bearer ${token}`
      }
    }).subscribe({
      next: (response) => {
        this.users = response.users || response as any; // Handle both formats
        this.loading = false;
        console.log('✅ Usuarios cargados:', this.users);
      },
      error: (err) => {
        console.error('❌ Error cargando usuarios:', err);
        this.error = err.error?.error || 'Error al cargar usuarios';
        this.loading = false;
      }
    });
  }

  refresh(): void {
    this.loadUsers();
  }

  getRoleIcon(role: string): string {
    switch(role) {
      case 'admin': return '👑';
      case 'moderator': return '👤';
      default: return '👥';
    }
  }

  getRoleColor(role: string): string {
    switch(role) {
      case 'admin': return '#ffd700';
      case 'moderator': return '#00f0ff';
      default: return '#ffffff';
    }
  }
}

