import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { AuthService } from '../../../services/auth.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})
export class LoginComponent implements OnInit {
  loginForm!: FormGroup;
  registerForm!: FormGroup;
  error: string = '';
  loading: boolean = false;
  showRegister: boolean = false;

  constructor(
    private fb: FormBuilder,
    private authService: AuthService,
    private router: Router
  ) {}

  ngOnInit(): void {
    // Check route to determine which form to show
    const currentRoute = this.router.url;
    this.showRegister = currentRoute.includes('/register');

    // Login Form
    this.loginForm = this.fb.group({
      email: ['', [Validators.required, Validators.email]],
      password: ['', [Validators.required, Validators.minLength(6)]]
    });

    // Register Form
    this.registerForm = this.fb.group({
      username: ['', [Validators.required, Validators.minLength(3)]],
      email: ['', [Validators.required, Validators.email]],
      password: ['', [Validators.required, Validators.minLength(6)]],
      confirmPassword: ['', [Validators.required]],
      full_name: ['']
    }, { validators: this.passwordMatchValidator });

    // Redirect if already logged in
    if (this.authService.isAuthenticated()) {
      this.router.navigate(['/dashboard']);
    }
  }

  passwordMatchValidator(form: FormGroup) {
    const password = form.get('password');
    const confirmPassword = form.get('confirmPassword');
    return password && confirmPassword && password.value === confirmPassword.value
      ? null : { mismatch: true };
  }

  toggleForm(): void {
    this.showRegister = !this.showRegister;
    this.error = '';
    // Reset forms
    this.loginForm.reset();
    this.registerForm.reset();
  }

  onSubmit(): void {
    if (this.loginForm.valid) {
      this.loading = true;
      this.error = '';

      const email = this.loginForm.value.email;
      const password = this.loginForm.value.password;

      console.log('🔐 Intentando login para:', email);

      this.authService.login(email, password).subscribe({
        next: (response) => {
          console.log('✅ Login exitoso:', response.user);
          this.router.navigate(['/dashboard']);
        },
        error: (err) => {
          console.error('❌ Error en login:', err);
          this.error = err.error?.error || err.error?.message || 'Credenciales inválidas. Intenta nuevamente.';
          this.loading = false;
        },
        complete: () => {
          this.loading = false;
        }
      });
    } else {
      // Marcar todos los campos como touched para mostrar errores
      Object.keys(this.loginForm.controls).forEach(key => {
        this.loginForm.get(key)?.markAsTouched();
      });
    }
  }

  onRegister(): void {
    if (this.registerForm.valid) {
      this.loading = true;
      this.error = '';

      const formData = {
        username: this.registerForm.value.username,
        email: this.registerForm.value.email,
        password: this.registerForm.value.password,
        full_name: this.registerForm.value.full_name || null
      };

      console.log('📝 Registrando usuario:', { ...formData, password: '***' });

      this.authService.register(
        formData.username,
        formData.email,
        formData.password,
        formData.full_name
      ).subscribe({
        next: (response) => {
          console.log('✅ Usuario registrado exitosamente:', response.user);
          this.router.navigate(['/dashboard']);
        },
        error: (err) => {
          console.error('❌ Error en registro:', err);
          this.error = err.error?.error || err.error?.message || 'Error al registrar. Intenta nuevamente.';
          this.loading = false;
        },
        complete: () => {
          this.loading = false;
        }
      });
    } else {
      // Marcar todos los campos como touched para mostrar errores
      Object.keys(this.registerForm.controls).forEach(key => {
        this.registerForm.get(key)?.markAsTouched();
      });
    }
  }
}

