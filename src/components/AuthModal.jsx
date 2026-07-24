import React, { useState } from 'react';
import { motion, AnimatePresence } from 'framer-motion';

const AuthModal = ({ isOpen, onClose, initialTab = 'login' }) => {
    const [tab, setTab] = useState(initialTab);
    const [loginData, setLoginData] = useState({ email: '', password: '', remember: false });
    const [signupData, setSignupData] = useState({ name: '', email: '', password: '', role: 'professional', agree: false });
    const [showPass, setShowPass] = useState(false);
    const [loading, setLoading] = useState(false);
    const [success, setSuccess] = useState('');

    // Sync tab when modal opens with a specific tab
    React.useEffect(() => { if (isOpen) setTab(initialTab); }, [isOpen, initialTab]);

    const handleLogin = (e) => {
        e.preventDefault();
        setLoading(true);
        setTimeout(() => { setLoading(false); setSuccess('Logged in successfully! Redirecting…'); }, 1500);
    };

    const handleSignup = (e) => {
        e.preventDefault();
        setLoading(true);
        setTimeout(() => { setLoading(false); setSuccess('Account created! Please verify your email.'); }, 1500);
    };

    if (!isOpen) return null;

    return (
        <AnimatePresence>
            {isOpen && (
                <>
                    {/* Backdrop */}
                    <motion.div
                        key="backdrop"
                        initial={{ opacity: 0 }}
                        animate={{ opacity: 1 }}
                        exit={{ opacity: 0 }}
                        className="fixed inset-0 bg-slate-900/60 backdrop-blur-sm z-[100]"
                        onClick={onClose}
                        aria-hidden="true"
                    />

                    {/* Modal */}
                    <motion.div
                        key="modal"
                        initial={{ opacity: 0, scale: 0.92, y: 20 }}
                        animate={{ opacity: 1, scale: 1, y: 0 }}
                        exit={{ opacity: 0, scale: 0.92, y: 20 }}
                        transition={{ duration: 0.3, ease: 'easeOut' }}
                        className="fixed inset-0 z-[101] flex items-center justify-center p-4"
                        role="dialog"
                        aria-modal="true"
                        aria-label={tab === 'login' ? 'Login dialog' : 'Sign up dialog'}
                    >
                        <div className="bg-white rounded-3xl shadow-2xl w-full max-w-md overflow-hidden" onClick={(e) => e.stopPropagation()}>

                            {/* Header gradient strip */}
                            <div className="h-1.5 bg-gradient-to-r from-sky-500 via-teal-400 to-indigo-500" />

                            <div className="p-8">
                                {/* Logo */}
                                <div className="flex items-center gap-2 mb-6">
                                    <div className="w-8 h-8 rounded-lg bg-gradient-to-br from-sky-500 to-teal-400 flex items-center justify-center">
                                        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" aria-hidden="true">
                                            <path d="M12 2L12 22M2 12L22 12" stroke="white" strokeWidth="3.5" strokeLinecap="round" />
                                        </svg>
                                    </div>
                                    <span className="font-bold text-slate-900">HealthCareer <span className="gradient-text">Pro</span></span>
                                </div>

                                {/* Success State */}
                                {success ? (
                                    <div className="text-center py-6">
                                        <div className="w-16 h-16 rounded-full bg-green-100 flex items-center justify-center mx-auto mb-4">
                                            <svg width="32" height="32" viewBox="0 0 24 24" fill="none">
                                                <path d="M9 12L11 14L15 10M21 12C21 16.97 16.97 21 12 21C7.03 21 3 16.97 3 12C3 7.03 7.03 3 12 3C16.97 3 21 7.03 21 12Z" stroke="#22C55E" strokeWidth="2.5" strokeLinecap="round" strokeLinejoin="round" />
                                            </svg>
                                        </div>
                                        <p className="font-semibold text-slate-900 text-lg mb-1">Success!</p>
                                        <p className="text-slate-500 text-sm">{success}</p>
                                        <button onClick={onClose} className="mt-6 px-6 py-2.5 bg-gradient-to-r from-sky-500 to-teal-400 text-white rounded-xl font-semibold text-sm hover:-translate-y-0.5 transition-all">
                                            Close
                                        </button>
                                    </div>
                                ) : (
                                    <>
                                        {/* Tabs */}
                                        <div className="flex bg-slate-100 rounded-2xl p-1 mb-6">
                                            {['login', 'signup'].map((t) => (
                                                <button
                                                    key={t}
                                                    onClick={() => setTab(t)}
                                                    className={`flex-1 py-2.5 rounded-xl text-sm font-semibold transition-all duration-200 ${tab === t
                                                            ? 'bg-white text-sky-600 shadow-sm'
                                                            : 'text-slate-500 hover:text-slate-700'
                                                        }`}
                                                    aria-selected={tab === t}
                                                >
                                                    {t === 'login' ? 'Login' : 'Sign Up'}
                                                </button>
                                            ))}
                                        </div>

                                        {/* LOGIN FORM */}
                                        {tab === 'login' && (
                                            <form onSubmit={handleLogin} className="flex flex-col gap-4" noValidate>
                                                <div>
                                                    <h2 className="text-2xl font-bold text-slate-900">Welcome back</h2>
                                                    <p className="text-slate-500 text-sm mt-1">Sign in to your account</p>
                                                </div>

                                                <div className="flex flex-col gap-1.5">
                                                    <label className="text-xs font-semibold text-slate-600 uppercase tracking-wide" htmlFor="login-email">Email Address</label>
                                                    <div className="relative">
                                                        <svg className="absolute left-3.5 top-1/2 -translate-y-1/2 text-slate-400 pointer-events-none" width="16" height="16" viewBox="0 0 24 24" fill="none">
                                                            <path d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" stroke="currentColor" strokeWidth="2" />
                                                        </svg>
                                                        <input
                                                            id="login-email"
                                                            type="email"
                                                            required
                                                            placeholder="you@example.com"
                                                            value={loginData.email}
                                                            onChange={(e) => setLoginData({ ...loginData, email: e.target.value })}
                                                            className="w-full h-11 pl-10 pr-4 rounded-xl border border-slate-200 focus:border-sky-400 focus:ring-2 focus:ring-sky-100 outline-none text-sm text-slate-700 bg-slate-50 focus:bg-white transition-all"
                                                        />
                                                    </div>
                                                </div>

                                                <div className="flex flex-col gap-1.5">
                                                    <div className="flex items-center justify-between">
                                                        <label className="text-xs font-semibold text-slate-600 uppercase tracking-wide" htmlFor="login-password">Password</label>
                                                        <button type="button" className="text-xs text-sky-500 hover:text-sky-600 font-medium">Forgot password?</button>
                                                    </div>
                                                    <div className="relative">
                                                        <svg className="absolute left-3.5 top-1/2 -translate-y-1/2 text-slate-400 pointer-events-none" width="16" height="16" viewBox="0 0 24 24" fill="none">
                                                            <rect x="3" y="11" width="18" height="11" rx="2" stroke="currentColor" strokeWidth="2" />
                                                            <path d="M7 11V7a5 5 0 0110 0v4" stroke="currentColor" strokeWidth="2" />
                                                        </svg>
                                                        <input
                                                            id="login-password"
                                                            type={showPass ? 'text' : 'password'}
                                                            required
                                                            placeholder="••••••••"
                                                            value={loginData.password}
                                                            onChange={(e) => setLoginData({ ...loginData, password: e.target.value })}
                                                            className="w-full h-11 pl-10 pr-10 rounded-xl border border-slate-200 focus:border-sky-400 focus:ring-2 focus:ring-sky-100 outline-none text-sm text-slate-700 bg-slate-50 focus:bg-white transition-all"
                                                        />
                                                        <button type="button" onClick={() => setShowPass(!showPass)} className="absolute right-3 top-1/2 -translate-y-1/2 text-slate-400 hover:text-slate-600" aria-label={showPass ? 'Hide password' : 'Show password'}>
                                                            <svg width="16" height="16" viewBox="0 0 24 24" fill="none">
                                                                {showPass ? <path d="M17.94 17.94A10.07 10.07 0 0112 20c-7 0-11-8-11-8a18.45 18.45 0 015.06-5.94M9.9 4.24A9.12 9.12 0 0112 4c7 0 11 8 11 8a18.5 18.5 0 01-2.16 3.19M1 1l22 22" stroke="currentColor" strokeWidth="2" strokeLinecap="round" /> : <path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z" stroke="currentColor" strokeWidth="2" /><circle cx="12" cy="12" r="3" stroke="currentColor" strokeWidth="2" />}
                                                            </svg>
                                                        </button>
                                                    </div>
                                                </div>

                                                <label className="flex items-center gap-2 cursor-pointer">
                                                    <input type="checkbox" checked={loginData.remember} onChange={(e) => setLoginData({ ...loginData, remember: e.target.checked })} className="w-4 h-4 accent-sky-500 rounded" />
                                                    <span className="text-sm text-slate-600">Remember me for 30 days</span>
                                                </label>

                                                <button
                                                    type="submit"
                                                    disabled={loading}
                                                    className="btn-ripple w-full h-11 bg-gradient-to-r from-sky-500 to-teal-500 text-white font-bold rounded-xl hover:shadow-lg hover:shadow-sky-200 hover:-translate-y-0.5 transition-all duration-300 flex items-center justify-center gap-2 text-sm disabled:opacity-70 disabled:cursor-not-allowed"
                                                >
                                                    {loading ? (
                                                        <svg className="animate-spin" width="18" height="18" viewBox="0 0 24 24" fill="none"><circle cx="12" cy="12" r="10" stroke="white" strokeWidth="3" strokeDasharray="40" strokeDashoffset="10" /></svg>
                                                    ) : 'Login to Account'}
                                                </button>

                                                <p className="text-center text-sm text-slate-500">
                                                    Don't have an account?{' '}
                                                    <button type="button" onClick={() => setTab('signup')} className="text-sky-500 font-semibold hover:underline">Sign up free</button>
                                                </p>
                                            </form>
                                        )}

                                        {/* SIGNUP FORM */}
                                        {tab === 'signup' && (
                                            <form onSubmit={handleSignup} className="flex flex-col gap-4" noValidate>
                                                <div>
                                                    <h2 className="text-2xl font-bold text-slate-900">Create account</h2>
                                                    <p className="text-slate-500 text-sm mt-1">Join 50,000+ healthcare professionals</p>
                                                </div>

                                                {/* Role Toggle */}
                                                <div className="flex bg-slate-100 rounded-xl p-1">
                                                    {[{ val: 'professional', label: '👨‍⚕️ Professional' }, { val: 'hospital', label: '🏥 Hospital' }].map((r) => (
                                                        <button
                                                            key={r.val}
                                                            type="button"
                                                            onClick={() => setSignupData({ ...signupData, role: r.val })}
                                                            className={`flex-1 py-2 rounded-lg text-xs font-semibold transition-all ${signupData.role === r.val ? 'bg-white text-sky-600 shadow-sm' : 'text-slate-500'}`}
                                                        >
                                                            {r.label}
                                                        </button>
                                                    ))}
                                                </div>

                                                <div className="flex flex-col gap-1.5">
                                                    <label className="text-xs font-semibold text-slate-600 uppercase tracking-wide" htmlFor="signup-name">
                                                        {signupData.role === 'hospital' ? 'Hospital / Organisation Name' : 'Full Name'}
                                                    </label>
                                                    <div className="relative">
                                                        <svg className="absolute left-3.5 top-1/2 -translate-y-1/2 text-slate-400 pointer-events-none" width="16" height="16" viewBox="0 0 24 24" fill="none">
                                                            <circle cx="12" cy="7" r="4" stroke="currentColor" strokeWidth="2" /><path d="M5 21C5 17.134 8.134 14 12 14C15.866 14 19 17.134 19 21" stroke="currentColor" strokeWidth="2" strokeLinecap="round" />
                                                        </svg>
                                                        <input
                                                            id="signup-name"
                                                            type="text"
                                                            required
                                                            placeholder={signupData.role === 'hospital' ? 'Apollo Hospitals' : 'Dr. Priya Sharma'}
                                                            value={signupData.name}
                                                            onChange={(e) => setSignupData({ ...signupData, name: e.target.value })}
                                                            className="w-full h-11 pl-10 pr-4 rounded-xl border border-slate-200 focus:border-sky-400 focus:ring-2 focus:ring-sky-100 outline-none text-sm text-slate-700 bg-slate-50 focus:bg-white transition-all"
                                                        />
                                                    </div>
                                                </div>

                                                <div className="flex flex-col gap-1.5">
                                                    <label className="text-xs font-semibold text-slate-600 uppercase tracking-wide" htmlFor="signup-email">Email Address</label>
                                                    <div className="relative">
                                                        <svg className="absolute left-3.5 top-1/2 -translate-y-1/2 text-slate-400 pointer-events-none" width="16" height="16" viewBox="0 0 24 24" fill="none">
                                                            <path d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" stroke="currentColor" strokeWidth="2" />
                                                        </svg>
                                                        <input
                                                            id="signup-email"
                                                            type="email"
                                                            required
                                                            placeholder="you@example.com"
                                                            value={signupData.email}
                                                            onChange={(e) => setSignupData({ ...signupData, email: e.target.value })}
                                                            className="w-full h-11 pl-10 pr-4 rounded-xl border border-slate-200 focus:border-sky-400 focus:ring-2 focus:ring-sky-100 outline-none text-sm text-slate-700 bg-slate-50 focus:bg-white transition-all"
                                                        />
                                                    </div>
                                                </div>

                                                <div className="flex flex-col gap-1.5">
                                                    <label className="text-xs font-semibold text-slate-600 uppercase tracking-wide" htmlFor="signup-password">Password</label>
                                                    <div className="relative">
                                                        <svg className="absolute left-3.5 top-1/2 -translate-y-1/2 text-slate-400 pointer-events-none" width="16" height="16" viewBox="0 0 24 24" fill="none">
                                                            <rect x="3" y="11" width="18" height="11" rx="2" stroke="currentColor" strokeWidth="2" /><path d="M7 11V7a5 5 0 0110 0v4" stroke="currentColor" strokeWidth="2" />
                                                        </svg>
                                                        <input
                                                            id="signup-password"
                                                            type={showPass ? 'text' : 'password'}
                                                            required
                                                            placeholder="Min. 8 characters"
                                                            value={signupData.password}
                                                            onChange={(e) => setSignupData({ ...signupData, password: e.target.value })}
                                                            className="w-full h-11 pl-10 pr-10 rounded-xl border border-slate-200 focus:border-sky-400 focus:ring-2 focus:ring-sky-100 outline-none text-sm text-slate-700 bg-slate-50 focus:bg-white transition-all"
                                                        />
                                                        <button type="button" onClick={() => setShowPass(!showPass)} className="absolute right-3 top-1/2 -translate-y-1/2 text-slate-400 hover:text-slate-600" aria-label="Toggle password">
                                                            <svg width="16" height="16" viewBox="0 0 24 24" fill="none">
                                                                <path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z" stroke="currentColor" strokeWidth="2" /><circle cx="12" cy="12" r="3" stroke="currentColor" strokeWidth="2" />
                                                            </svg>
                                                        </button>
                                                    </div>
                                                </div>

                                                <label className="flex items-start gap-2 cursor-pointer">
                                                    <input
                                                        type="checkbox"
                                                        required
                                                        checked={signupData.agree}
                                                        onChange={(e) => setSignupData({ ...signupData, agree: e.target.checked })}
                                                        className="w-4 h-4 accent-sky-500 mt-0.5 flex-shrink-0"
                                                    />
                                                    <span className="text-xs text-slate-600 leading-relaxed">
                                                        I agree to the{' '}
                                                        <a href="#" className="text-sky-500 font-semibold hover:underline">Terms of Service</a>{' '}and{' '}
                                                        <a href="#" className="text-sky-500 font-semibold hover:underline">Privacy Policy</a>
                                                    </span>
                                                </label>

                                                <button
                                                    type="submit"
                                                    disabled={loading || !signupData.agree}
                                                    className="btn-ripple w-full h-11 bg-gradient-to-r from-sky-500 to-teal-500 text-white font-bold rounded-xl hover:shadow-lg hover:shadow-sky-200 hover:-translate-y-0.5 transition-all duration-300 flex items-center justify-center gap-2 text-sm disabled:opacity-70 disabled:cursor-not-allowed"
                                                >
                                                    {loading ? (
                                                        <svg className="animate-spin" width="18" height="18" viewBox="0 0 24 24" fill="none"><circle cx="12" cy="12" r="10" stroke="white" strokeWidth="3" strokeDasharray="40" strokeDashoffset="10" /></svg>
                                                    ) : 'Create Free Account'}
                                                </button>

                                                <p className="text-center text-sm text-slate-500">
                                                    Already have an account?{' '}
                                                    <button type="button" onClick={() => setTab('login')} className="text-sky-500 font-semibold hover:underline">Login</button>
                                                </p>
                                            </form>
                                        )}
                                    </>
                                )}
                            </div>

                            {/* Close button */}
                            <button
                                onClick={onClose}
                                className="absolute top-5 right-5 w-8 h-8 rounded-full bg-slate-100 hover:bg-slate-200 flex items-center justify-center transition-colors duration-200"
                                aria-label="Close dialog"
                            >
                                <svg width="14" height="14" viewBox="0 0 24 24" fill="none">
                                    <path d="M18 6L6 18M6 6l12 12" stroke="#64748B" strokeWidth="2.5" strokeLinecap="round" />
                                </svg>
                            </button>
                        </div>
                    </motion.div>
                </>
            )}
        </AnimatePresence>
    );
};

export default AuthModal;
