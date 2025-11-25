import { Component, OnInit, AfterViewInit, ViewChild, ElementRef } from '@angular/core';
import { DashboardService, DashboardData, AnalyticsData } from '../../services/dashboard.service';
import { gsap } from 'gsap';

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.scss']
})
export class DashboardComponent implements OnInit, AfterViewInit {
  @ViewChild('dashboardContainer', { static: false }) dashboardContainer!: ElementRef;

  dashboardData: DashboardData | null = null;
  analyticsData: AnalyticsData | null = null;
  loading: boolean = true;
  selectedPeriod: '7d' | '30d' | '1y' = '7d';
  periods: ('7d' | '30d' | '1y')[] = ['7d', '30d', '1y'];

  constructor(private dashboardService: DashboardService) {}

  ngOnInit(): void {
    this.loadDashboardData();
    this.loadAnalytics();
  }

  ngAfterViewInit(): void {
    setTimeout(() => this.initAnimations(), 100);
  }

  loadDashboardData(): void {
    this.dashboardService.getStats().subscribe({
      next: (data) => {
        this.dashboardData = data;
        this.loading = false;
      },
      error: (err) => {
        console.error('Error loading dashboard:', err);
        this.loading = false;
      }
    });
  }

  loadAnalytics(): void {
    this.dashboardService.getAnalytics(this.selectedPeriod).subscribe({
      next: (data) => {
        this.analyticsData = data;
        this.updateCharts();
      },
      error: (err) => {
        console.error('Error loading analytics:', err);
      }
    });
  }

  onPeriodChange(period: '7d' | '30d' | '1y'): void {
    this.selectedPeriod = period;
    this.loadAnalytics();
  }

  private initAnimations(): void {
    const container = this.dashboardContainer?.nativeElement;
    if (container) {
      const cards = container.querySelectorAll('.stat-card');
      gsap.from(cards, {
        opacity: 0,
        y: 30,
        duration: 0.6,
        stagger: 0.1,
        ease: 'power3.out'
      });
    }
  }

  private updateCharts(): void {
    // Chart.js integration will be added here
    // For now, we'll use the data structure ready for charts
    if (this.analyticsData) {
      console.log('Analytics data ready for charts:', this.analyticsData);
    }
  }

  getCategoryColor(category: string): string {
    const colors: { [key: string]: string } = {
      'RPG de acción': '#c0392b',
      'Rol multijugador masivo': '#f39c12',
      'Shooter de acción': '#3498db',
      'Acción por equipos': '#e74c3c',
      'Juego de cartas estratégico': '#9b59b6',
      'Estrategia en tiempo real': '#16a085'
    };
    return colors[category] || '#00f0ff';
  }

  formatDate(dateString: string): string {
    const date = new Date(dateString);
    return date.toLocaleDateString('es-ES', { day: '2-digit', month: 'short' });
  }

  getMaxValue(data: Array<{ count: number }>): number {
    return Math.max(...data.map(d => d.count), 1);
  }

  formatRating(rating: number): string {
    return rating ? rating.toFixed(1) : '0.0';
  }

  getGameDownloads(game: any): number {
    if (!game) return 0;
    return game.downloads || 0;
  }

  getGameRating(game: any): string {
    if (!game || !game.rating) return '0.0';
    const rating = game.rating;
    return rating.toFixed ? rating.toFixed(1) : '0.0';
  }

  getBadge(game: any): string {
    return game?.badge || 'NEW';
  }

  formatRevenue(revenue: number): string {
    return revenue ? revenue.toFixed(2) : '0.00';
  }

  getPeriodLabel(period: '7d' | '30d' | '1y'): string {
    if (period === '7d') return '7 Días';
    if (period === '30d') return '30 Días';
    return '1 Año';
  }

  getCategoryWidth(count: number): number {
    if (!this.dashboardData || !this.dashboardData.stats.totalGames) return 0;
    return (count / this.dashboardData.stats.totalGames) * 100;
  }

  getBarHeight(count: number): number {
    if (!this.analyticsData || !this.analyticsData.gamesOverTime.length) return 0;
    const maxValue = this.getMaxValue(this.analyticsData.gamesOverTime);
    return (count / maxValue) * 100;
  }

  getGameImageUrl(imageUrl: string | undefined): string {
    if (!imageUrl) return '';
    return 'url(' + imageUrl + ')';
  }
}

