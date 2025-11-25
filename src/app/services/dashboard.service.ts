import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { ApiService } from './api.service';

export interface DashboardStats {
  totalGames: number;
  totalUsers: number;
  totalRevenue: number;
  freeGames: number;
  paidGames: number;
}

export interface DashboardData {
  stats: DashboardStats;
  categories: Array<{ category: string; count: number }>;
  recentGames: any[];
  recentUsers: any[];
  activities: Array<{ activity_type: string; count: number }>;
}

export interface AnalyticsData {
  gamesOverTime: Array<{ date: string; count: number }>;
  usersOverTime: Array<{ date: string; count: number }>;
  topGames: Array<{ title: string; downloads: number; rating: number }>;
  revenueOverTime: Array<{ date: string; revenue: number }>;
}

@Injectable({
  providedIn: 'root'
})
export class DashboardService {
  constructor(private api: ApiService) {}

  getStats(): Observable<DashboardData> {
    return this.api.get<DashboardData>('/dashboard/stats');
  }

  getAnalytics(period: '7d' | '30d' | '1y' = '7d'): Observable<AnalyticsData> {
    return this.api.get<AnalyticsData>('/dashboard/analytics', { period });
  }
}

