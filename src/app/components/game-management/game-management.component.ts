import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { GameService, Game, GameFilters } from '../../services/game.service';
import { AuthService } from '../../services/auth.service';

@Component({
  selector: 'app-game-management',
  templateUrl: './game-management.component.html',
  styleUrls: ['./game-management.component.scss']
})
export class GameManagementComponent implements OnInit {
  games: Game[] = [];
  filteredGames: Game[] = [];
  loading: boolean = false;
  showForm: boolean = false;
  editingGame: Game | null = null;
  
  gameForm!: FormGroup;
  filters: GameFilters = {
    page: 1,
    limit: 20,
    sort: 'created_at',
    order: 'desc'
  };

  categories: string[] = [];
  searchTerm: string = '';
  selectedCategory: string = '';

  constructor(
    private gameService: GameService,
    private authService: AuthService,
    private fb: FormBuilder
  ) {}

  ngOnInit(): void {
    this.initForm();
    this.loadGames();
  }

  initForm(): void {
    this.gameForm = this.fb.group({
      title: ['', Validators.required],
      subtitle: [''],
      description: ['', Validators.required],
      image_url: [''],
      category: ['', Validators.required],
      color: ['#00f0ff'],
      price: [0],
      original_price: [0],
      discount: [0],
      badge: ['NEW'],
      logo: [''],
      is_free: [false]
    });
  }

  loadGames(): void {
    this.loading = true;
    this.gameService.getGames(this.filters).subscribe({
      next: (response) => {
        this.games = response.games;
        this.applyFilters();
        this.extractCategories();
        this.loading = false;
      },
      error: (err) => {
        console.error('Error loading games:', err);
        this.loading = false;
      }
    });
  }

  extractCategories(): void {
    const uniqueCategories = new Set(this.games.map(g => g.category));
    this.categories = Array.from(uniqueCategories).sort();
  }

  applyFilters(): void {
    let filtered = [...this.games];

    if (this.searchTerm) {
      const search = this.searchTerm.toLowerCase();
      filtered = filtered.filter(g =>
        g.title.toLowerCase().includes(search) ||
        g.description.toLowerCase().includes(search)
      );
    }

    if (this.selectedCategory) {
      filtered = filtered.filter(g => g.category === this.selectedCategory);
    }

    this.filteredGames = filtered;
  }

  onSearchChange(): void {
    this.applyFilters();
  }

  onCategoryChange(): void {
    this.applyFilters();
  }

  openCreateForm(): void {
    this.editingGame = null;
    this.gameForm.reset();
    this.showForm = true;
  }

  openEditForm(game: Game): void {
    this.editingGame = game;
    this.gameForm.patchValue(game);
    this.showForm = true;
  }

  closeForm(): void {
    this.showForm = false;
    this.editingGame = null;
    this.gameForm.reset();
  }

  saveGame(): void {
    if (this.gameForm.valid) {
      const gameData = this.gameForm.value;
      
      if (this.editingGame) {
        this.gameService.updateGame(this.editingGame.id!, gameData).subscribe({
          next: () => {
            this.loadGames();
            this.closeForm();
          },
          error: (err) => console.error('Error updating game:', err)
        });
      } else {
        this.gameService.createGame(gameData).subscribe({
          next: () => {
            this.loadGames();
            this.closeForm();
          },
          error: (err) => console.error('Error creating game:', err)
        });
      }
    }
  }

  deleteGame(id: number): void {
    if (confirm('¿Estás seguro de eliminar este juego?')) {
      this.gameService.deleteGame(id).subscribe({
        next: () => {
          this.loadGames();
        },
        error: (err) => console.error('Error deleting game:', err)
      });
    }
  }

  canEdit(): boolean {
    return this.authService.isModerator();
  }

  canDelete(): boolean {
    return this.authService.isAdmin();
  }
}

