import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { ApiService } from './api.service';

export interface Game {
  id?: number;
  title: string;
  subtitle?: string;
  description: string;
  image_url?: string;
  category: string;
  color?: string;
  price?: number;
  original_price?: number;
  discount?: number;
  badge?: string;
  logo?: string;
  is_free?: boolean;
  rating?: number;
  downloads?: number;
  created_at?: string;
  updated_at?: string;
}

export interface GamesResponse {
  games: Game[];
  pagination: {
    page: number;
    limit: number;
    total: number;
    pages: number;
  };
}

export interface GameFilters {
  page?: number;
  limit?: number;
  category?: string;
  search?: string;
  sort?: 'title' | 'price' | 'rating' | 'created_at';
  order?: 'asc' | 'desc';
}

@Injectable({
  providedIn: 'root'
})
export class GameService {
  constructor(private api: ApiService) {}

  getGames(filters?: GameFilters): Observable<GamesResponse> {
    return this.api.get<GamesResponse>('/games', filters);
  }

  getGame(id: number): Observable<{ game: Game }> {
    return this.api.get<{ game: Game }>(`/games/${id}`);
  }

  createGame(game: Game): Observable<{ game: Game }> {
    return this.api.post<{ game: Game }>('/games', game);
  }

  updateGame(id: number, game: Partial<Game>): Observable<{ game: Game }> {
    return this.api.put<{ game: Game }>(`/games/${id}`, game);
  }

  deleteGame(id: number): Observable<{ message: string }> {
    return this.api.delete<{ message: string }>(`/games/${id}`);
  }
}

