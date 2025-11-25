import { Component, OnInit } from '@angular/core';
import { ApiService } from '../../services/api.service';
import { AuthService } from '../../services/auth.service';

export interface User {
  id: number;
  username: string;
  email: string;
  role: 'admin' | 'moderator' | 'user';
  full_name?: string;
  avatar_url?: string;
  is_active: boolean;
  created_at: string;
}

@Component({
  selector: 'app-user-management',
  templateUrl: './user-management.component.html',
  styleUrls: ['./user-management.component.scss']
})
export class UserManagementComponent implements OnInit {
  users: User[] = [];
  filteredUsers: User[] = [];
  loading: boolean = false;
  searchTerm: string = '';
  selectedRole: string = '';

  constructor(
    private api: ApiService,
    private authService: AuthService
  ) {}

  ngOnInit(): void {
    if (this.authService.isAdmin()) {
      this.loadUsers();
    }
  }

  loadUsers(): void {
    this.loading = true;
    this.api.get<{ users: User[], pagination: any }>('/users', {
      page: 1,
      limit: 100
    }).subscribe({
      next: (response) => {
        this.users = response.users;
        this.applyFilters();
        this.loading = false;
      },
      error: (err) => {
        console.error('Error loading users:', err);
        this.loading = false;
      }
    });
  }

  applyFilters(): void {
    let filtered = [...this.users];

    if (this.searchTerm) {
      const search = this.searchTerm.toLowerCase();
      filtered = filtered.filter(u =>
        u.username.toLowerCase().includes(search) ||
        u.email.toLowerCase().includes(search) ||
        (u.full_name && u.full_name.toLowerCase().includes(search))
      );
    }

    if (this.selectedRole) {
      filtered = filtered.filter(u => u.role === this.selectedRole);
    }

    this.filteredUsers = filtered;
  }

  updateUserRole(userId: number, newRole: 'admin' | 'moderator' | 'user'): void {
    this.api.put(`/users/${userId}/role`, { role: newRole }).subscribe({
      next: () => {
        this.loadUsers();
      },
      error: (err) => {
        console.error('Error updating role:', err);
        alert('Error al actualizar el rol');
      }
    });
  }

  getRoleColor(role: string): string {
    const colors: { [key: string]: string } = {
      'admin': '#ff4444',
      'moderator': '#ffaa00',
      'user': '#00f0ff'
    };
    return colors[role] || '#ffffff';
  }

  formatDate(dateString: string): string {
    const date = new Date(dateString);
    return date.toLocaleDateString('es-ES', { 
      day: '2-digit', 
      month: 'short', 
      year: 'numeric' 
    });
  }
}

